# Reconnaissance de chiffre
Ce projet à pour but de reconnaître des chiffres. Les chiffres sont dessinés sur une interface web, puis envoyés à un backend python pour essayer de reconnaître le chiffre en question. 

## Prérequis et Dépendences

### Prérequis
Pour utiliser ce programme, il faut avoir:
- **python3**
- **[poetry](https://github.com/python-poetry/poetry)**
- **[docker-compose](https://docs.docker.com/compose/)**


### Dépendences
Pour installer les dépendences, il faut se rendre dans le dossier du projet, puis utiliser les commandes suivantes pour lancer un shell poetry et installer les dépendences:
```
$ poetry shell
$ poetry install
```

## Utilisation du programme

### Les servers
Le projet nécessite d'avoir une instance de server web nginx **[nginx](https://www.nginx.com/)**, ainsi qu'un server **[fastapi](https://fastapi.tiangolo.com/)**.
Le server nginx tourne sur docker, et le server fastapi tourne avec uvicorn.

Pour lancer les serveur, il faut être dans le shell poetry.

Si on n'est pas dans le shell poetry, il faut d'abord faire:
```
$ poetry shell
```
Dès qu'on est dans le shell poetry on peut lancer le server nginx:
```
$ docker-compose up
```
Ou bien, si on ne veut pas utiliser un autre terminal:
```
$ docker-compose up -d
```

Pour lancer le server uvicorn, il faut se diriger vers le dossier app, puis lancer le server:
```
$ cd app
$ uvicorn main:app
```

### Utilisation
Pour pouvoir utiliser le programme, il faut utiliser l'interface web qu'on retrouve à l'adresse:

**[http://localhost:8095/](http://localhost:8095/)**

Ensuite, on peut dessiner et demander au programme de deviner, ou bien l'entrainer.

Le bouton train from file va aller prendre les fichiers *n.data* et entrainer le modèle avec.