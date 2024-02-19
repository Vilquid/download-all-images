# download-all-images (en)

Download all imges from one (or more) url

## Description

This Python script automates the process of downloading all images from a webpage using Firefox, Selenium and the requests library. It navigates to a specified URL, scrolls through the webpage to ensure all images are loaded, and then downloads each image into a specified folder. The script is capable of handling multiple URLs sequentially and adjusts the scroll speed based on predefined connection speeds.

## Features

- Automated webpage navigation and image loading using Selenium.
- Dynamic scroll delay adjustment based on connection quality.
- Downloads all images found on a webpage.
- Organizes downloaded images into a folder named after the last segment of the URL.
- Clears the target folder before downloading, ensuring fresh downloads every time.

## Requirements

To run this script, you will need Python installed on your system along with the following packages:

- `selenium`
- `requests`

Additionally, you will need the appropriate WebDriver for Selenium, specifically geckodriver for Firefox, installed and accessible in your system's PATH.

## Installation

1. **Python and pip:**
   Ensure that Python and pip are installed on your system. You can download Python from the official website, which includes pip.

2. **Dependencies:**
   Install the required Python packages by running the following command in your terminal:

	```sh
	pip install requirements.txt
	python ~/script/main.py
	```

# download-all-images (fr)

Télécharger toutes les images depuis une (ou plusieurs) URL

## Description

Ce script Python automatise le processus de téléchargement de toutes les images d'une page Web en utilisant Firefox, Selenium et la bibliothèque requests. Il navigue vers une URL spécifiée, défile sur la page Web pour s'assurer que toutes les images sont chargées, puis télécharge chaque image dans un dossier spécifié. Le script est capable de gérer plusieurs URL de manière séquentielle et ajuste la vitesse de défilement en fonction des vitesses de connexion prédéfinies.

## Fonctionnalités

- Navigation automatique sur la page Web et chargement des images avec Selenium.
- Ajustement dynamique du délai de défilement en fonction de la qualité de la connexion.
- Télécharge toutes les images trouvées sur une page Web.
- Organise les images téléchargées dans un dossier nommé d'après le dernier segment de l'URL.
- Vide le dossier cible avant le téléchargement, assurant des téléchargements frais à chaque fois.

## Prérequis

Pour exécuter ce script, vous aurez besoin de Python installé sur votre système ainsi que des paquets suivants :

- `selenium`
- `requests`

De plus, vous aurez besoin du WebDriver approprié pour Selenium, spécifiquement geckodriver pour Firefox, installé et accessible dans le PATH de votre système.

## Installation

1. **Python et pip :**
   Assurez-vous que Python et pip sont installés sur votre système. Vous pouvez télécharger Python depuis le site officiel, qui inclut pip.

2. **Dépendances :**
   Installez les paquets Python requis en exécutant la commande suivante dans votre terminal :

   ```sh
   pip install requirements.txt
   ```

3. **WebDriver :**
   Téléchargez et installez geckodriver depuis sa [page GitHub officielle](https://github.com/mozilla/geckodriver/releases). Assurez-vous qu'il est ajouté au PATH de votre système.
