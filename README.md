# DeauthNet 🕷
Programme écrit en Python réalisé dans le cadre de la SAE304 pouvant déconnecter tous (ou presque) les appareils connectés à un point d'accès en utilisant le principe de l'attaque par déni de service dans la WI-FI.

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

Crée par Ulysse (sk0za) & Jean-Baptiste (-> https://github.com/champagnearden) 

