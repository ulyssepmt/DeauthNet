# DeauthNet
**FR**: Programme réalisé dans le cadre de la SAE304 pouvant déconnecter tous (ou presque) les appareils connectés à un point d'accès en utilisant le principe de l'attaque par déni de service dans la WI-FI.

**De quoi s'agit t-il ?**

L'attaque par Deauth fonctionne sur l'envoi de paquets de désauthentification à un point d'accès (AP) après avoir récupéré le nom et l'adresse MAC de l'AP (récupéré grâce aux trames beacon). Ces paquets de désauthentification contiennent une demande de désauthentification pour les machines connectées au point d'accès et ce dernier répond en coupant les connexions avec les appareils affectés (ces dernier devront se reconnecter afin de rétablir la connexion).

/!\ Il s'agit juste d'un programme crée dans le cadre d'un projet informatique et je précise que cette attaque nécessite un accès physique ou à distance à l'appareil pour envoyer des paquets de désauthentification.

*Pré-requis:* 

1. Les différents imports à installer (via pip, python ou apt-get install). 
2. Inssider afin de récupérer un channel à cibler. Lien: https://www.metageek.com/downloads/inssider-win/
3. L'image ("entete.php") doit se trouver dans le même répertoire que le script Python

*Comment l'utiliser:*

1. Choisissez avant tout une interface sur laquelle le mode monitor est activé. 
2. Saississez un channel dans lequel se trouve l'AP à cibler. 
3. Selectionnez votre AP (qui apparaîtra dans la ListBox). 
4. Lancez l'attaque. 

Vue de l'interface : 

![Capture](https://user-images.githubusercontent.com/89702597/215350488-c7d27fa7-a068-4ae3-85e9-6169eb7f8d2a.PNG)

Crée par Ulysse (zefyR) & Jean-Baptiste (https://github.com/champagnearden) 
**================================================================================**
**EN**: Program realized in the framework of SAE304 that can disconnect all (or almost all) devices connected to an access point by using the principle of denial of service attack in WI-FI.
**What is it ?**

The Deauth attack works by sending deauthentication packets to an access point (AP) after retrieving the name and MAC address of the AP (retrieved from beacon frames). These deauthentication packets contain a deauthentication request for the machines connected to the access point and the latter responds by cutting off the connections with the affected devices (the latter will have to reconnect in order to re-establish the connection).

/!\ This is just a program created as part of a computer project and I would like to point out that this attack requires physical or remote access to the device to send deauthentication packets.

*Required:* 

1. The different imports to install (via pip, python or apt-get install). 
2. Inssider to get a channel to target. Link: https://www.metageek.com/downloads/inssider-win/
3. The image ("entete.php") must be in the same directory as the Python script

*How to use it:*

1. First of all, choose an interface on which the monitor mode is activated. 
2. Select a channel where the AP to be targeted is located. 
3. Select your AP (which will appear in the ListBox). 
4. Launch the attack. 
