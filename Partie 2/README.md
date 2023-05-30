# Approches à base de http/https
## Pourquoi ?
- **Sécurité** : HTTPS ajoute une couche de chiffrement SSL/TLS (Secure Sockets Layer/Transport Layer Security) aux communications HTTP.
- **Confidentialité des données**:  HTTPS chiffre les données en transit, ce qui rend extrêmement difficile pour les attaquants d'intercepter et de déchiffrer les informations confidentielles.
- **Authentification** : HTTPS utilise des certificats SSL/TLS pour authentifier les serveurs et garantir que les utilisateurs se connectent au bon site Web. Les certificats sont délivrés par des autorités de certification (CA) de confiance.
- **Norme de facto** : Au fil du temps, HTTPS est devenu une norme de facto pour de nombreux services et applications en ligne. Les navigateurs modernes marquent les sites Web non sécurisés (HTTP) comme « non sécurisés » pour sensibiliser les utilisateurs aux risques potentiels. 
- **SEO et référencement** : Les moteurs de recherche, tels que Google, donnent la priorité aux sites Web sécurisés en HTTPS dans leurs résultats de recherche.
## Exemple interaction navigateur <=> application python
- **Scraping web** : Utilisez BeautifulSoup pour extraire des données d'une page web via HTTP/HTTPS.
- **Envoi de requêtes** : Utilisez Requests pour envoyer des requêtes HTTP/HTTPS depuis Python vers un serveur web, pour interagir avec des API, récupérer des données ou envoyer des formulaires en ligne.
- **Création de serveur web** : Utilisez Flask ou Django pour créer une application web côté serveur. Le navigateur envoie des requêtes HTTP/HTTPS à votre application Python, qui les traite et renvoie des réponses.
## Exemple interaction entre code python
- **Communication entre deux applications Python** :
- - L'application A envoie une requête HTTP/HTTPS à l'application B 
- - L'application B reçoit la requête, et renvoie une réponse à l'application A.
- **Intégration de services tiers** :
- - Une application Python utilise des services tiers (par exemple, des services de messagerie ou de paiement) en effectuant des appels HTTP/HTTPS pour interagir avec ces services.
- - Les services tiers reçoivent les requêtes, effectuent les opérations demandées et renvoient les résultats à l'application Python.
- **Échange de données entre différents composants d'une application web** : 
- - Différents composants d'une application web Python communiquent entre eux via des requêtes HTTP/HTTPS.