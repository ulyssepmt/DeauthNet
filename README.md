# DeauthNet
Programme réalisé dans le cadre de la SAE304 pouvant déconnecté tous (ou presque) les appareils connectés à un point d'accès en utilisant le principe de l'attaque par déni de service dans la WI-FI.

**De quoi s'agit t-il ?**
L'attaque par Deauth ou attaque par déni de service WI-FI fonctionne sur l'envoi de paquets de désauthentification à un point d'accès (AP) après avoir récupéré le nom et l'adresse MAC de l'AP (récupéré grâce aux trames beacon). Ces paquets de désauthentification contiennent une demande de désauthentification pour les machines connectées au point d'accès. Lorsque le point d'accès reçoit ces paquets, il répond en coupant les connexions avec les appareils affectés (ces dernier devront se reconnecter afin de rétablir la connexion. Il est donc possible de déconnecter les appareils pendant un certain temps ou indéfiniment (suivant les conditions de la boucle while, for, qui envoi les paquets). 

/!\ Il s'agit juste d'un programme crée dans le cadre d'un projet informatique et je précise que cette attaque nécessite un accès physique ou à distance à l'appareil pour envoyer des paquets de désauthentification. Ellee ne permet donc pas de voler des informations ou de compromettre d'un quelqonque appareil connecté à l'AP. L'attaque Deauth peut simplement causer des perturbations pour les utilisateurs du réseau et même rendre le réseau inutilisable.

*Pré-requis:* 

1. Les différents imports à installés (via pip, python ou apt-get install). 
2. Inssider afin pour réupéré un channel à cibler. Lien: https://www.metageek.com/downloads/inssider-win/
3. L'image ("entete.php") dans le même répertoire que le script Python

*Comment l'utiliser:*

1. Choisissez avant tout une interface sur laquelle le mode monitor est activé. 
2. Saississez un channel dans lequel se trouve l'AP à cibler. 
3. Selectionner votre AP (qui apparaîtra dans la ListBox). 
4. Lancer l'attaque. 

Vu de l'interface : 

![d](https://user-images.githubusercontent.com/89702597/215349724-845c068d-22cb-4cad-ab43-42cb8996f048.PNG)
