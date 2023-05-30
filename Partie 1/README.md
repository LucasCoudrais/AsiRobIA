# TCP et UPD 
|   Facteur   |   TCP |   UDP 
|---    |:-:    |:-:    
|   Type de connexion  |   Connexion requise avant de transmettre des données   |  Aucune connexion requise pour démarrer et terminer un transfert de données
|   Séquence de données   |   Oui (ordre spécifique)  |   Non (pas d'ordre)
|   Retransmission des données  |   Possible, données récupérables   |   Pas possible, données irrécupérables
|   Livraison  |   Garantie   |   Pas garantie
|   Controle d'erreurs  |   Approfondie, arrivé dans l'état prévu garantit   |   Minimale, ne permet pas forcémment d'éviter toutes les erreurs
|   Radiodiffusion  |   Oui   |   Non
|   Rapidité  |   Transmission lente mais complète   |   Transmission rapide mais risque incomplète
 
## TCP idéal pour 
- Email ou SMS
- Tranfert de fichier
- Navigation Web

## UDP idéal pour 
- Streaming en direct
- Jeu vidéo en ligne
- Chat vidéo

## Comparaison
![Comparison](img/tcp-vs-udp-comparison-ipcisco.com_.png)

## Comparatif pour l'envoi de données
Pour des données classiques, les deux se valent, cela dépend juste de nos exigences et du contexte \

Cependant pour les envois de flux d'information en direct, il se trouve qu'UDP sera plus adapté que TCP. \
Notamment grâce au fait qu'UDP autrorise la perte de paquet ce qui peut arriver et n'est pas très dérangeant dans la transmission de flux. Le fait qu'il l'autorise est bien car la perte de paquet ne va pas perturber le reste de la communication

# Transmission informations controle
Ici simplement envoie start au lencement et stop au ctrl+C
## Transmision UDP
Voir les fichiers `client_UDP.py` et `server_UDP.py` dans le dossier `controle`
![Client server UDP](img/client_server_udp.png)
## Transmision TCP
Voir les fichiers `client_TCP.py` et `server_TCP.py` dans le dossier `controle`
![Client server TCP](img/client_server_tcp.png)

# Transmission informations sporadique
Ici simplement envoie un nombre aléatoire de données à des intervalles aléatoire (plutot court) toutes les X seconde ou X est lui aussi aléatoire
## Transmision UDP
Voir les fichiers `client_UDP.py` et `server_UDP.py` dans le dossier `sporadique`
![Client server UDP](img/client_server_UDP_sporadique.png)
## Transmision TCP
Voir les fichiers `client_TCP.py` et `server_TCP.py` dans le dossier `sporadique`
![Client server TCP](img/client_server_TCP_sporadique.png)

# Transmission flux d'information
Envoie de manière constante et rapidement des informations, le but étant que tout transite au mieux
## Transmision UDP
Voir les fichiers `client_UDP.py` et `server_UDP.py` dans le dossier `flux`
![Client server UDP](img/client_server_UDP_flux.png)
## Transmision TCP
Voir les fichiers `client_TCP.py` et `server_TCP.py` dans le dossier `flux`
![Client server TCP](img/client_server_TCP_flux.png)

# Transmission flux stream video
Envoie de manière constante les images d'une vidéo de manière à la diffuser en streaming du serveur vers le client.
## Transmision UDP
Voir les fichiers `client_UDP.py` et `server_UDP.py` dans le dossier `stream-video`
![Client server stream video](img/stream-video.png)

## Sources 
- Doc UPD TCP : 
- - https://www.avast.com/fr-fr/c-tcp-vs-udp-difference
- - https://ipcisco.com/lesson/tcp-versus-udp/
- Client Sever UDP python : https://pythontic.com/modules/socket/udp-client-server-example
- Client Server TCP python : https://realpython.com/python-sockets/#tcp-sockets
- Stream video : https://pyshine.com/Send-video-over-UDP-socket-in-Python/
