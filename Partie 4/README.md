# Cractéristique de notre application

Nous avons là une application très légère qui ne demande pas une grande charge sans un grand besoin de scalabilité avec aucune base de données, simplement un système de stockage avec un système de fichier. Nous pouvons alors penser à une architecture simpliste.

## Comment gérer le déploiement en ligne et les choix d’architectures à faire sur une solution comme AWS

1. **Amazon S3 (Simple Storage Service)** : Système de stockage pour nos fichiers

2. **Amazon EC2 (Elastic Compute Cloud)** : Déploiement d'une instance EC2 pour exécuter notre application Python. 

3. **Amazon Route 53** : Gestion de notre domaine et configuration les enregistrements DNS nécessaires pour pointer vers notre instance EC2.

## Comment gérer le déploiement en ligne et les choix d’architectures à faire sur une solution comme PythonAnymhere

1. **PythonAnywhere Web App** : Déployer notre application Python.

2. **PythonAnywhere File Storage** : Utilisr le système de stockage de fichiers fourni par PythonAnywhere pour stocker nos fichiers statiques.

3. **Domain Configuration** : Configurer les enregistrements DNS appropriés pour lier notre domaine personnalisé à notre application déployée sur PythonAnywhere.

## Architecture Globale

Nous choisisson finalement 3 entité dans notre architecture qui permetra le déploiement en ligne sur un environnement de production pour notre application webservices python.
- Instance permettant l'exécution de l'application python
- Système de sotckage pour notre code et notre système de fichier
- Configuration du domaine pour reidiriger vers notre instance d'exécution.

Cette architecture convient aux applications légères ne nécessitant pas une grande infrastructure ni de base de données.

On pourrait élargir le sujet en posant la problématique de notre problème de performance avec un lours traitement d'image sur le flux vidéo qui nécéssite des capacités d'intelligence artificielle (cf Partie 2 ou DS)