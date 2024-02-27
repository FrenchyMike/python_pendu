# Basic Hangman game in Python

## Context of development
*Commments in program are in french, sorry for english people :'(*

This programm was designed through a tutorial from [Openclassroom](https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python])
This is my real first program in Python, so I'm sure it could be improve a lot.
Thank for your interest. Hope you will enjoy it !

## How the program works

This program is composed of 3 python file an a txt file:
* main_v2.py
* liste_joueur_v2.py
* fonction_v2.py
* liste_joueur_v2.txt

### The fonction_v2.py program

This program is composed of all needed functions to provide the main program.
I commented it as much as i estimated it, but i'm sure it could be improve. If 
you have any idea or suggestion please let me know :)

Below some examples of designed functions:
* `afficherMainMenu()`: display the main menu of the programm
* `listeDonneesJoueurs()`: get the list of gamers
* `enregistrerJoueurs()`: allow users to register a gamer tag
* ...

### The main_v2.py program

This program consists of the main function which should be run to start playing.
It uses all functions from fonction_v2.py

### The donnees.py and liste_joueur_v2.txt

Both these file are used to store datas:
* donnees.py : store used word for the game (donnees means data)
* liste_joueur_v2.py : store gamer tag and score


## Improvment

* [ ] Throw data from donnees.py and liste_joueur_v2.txt into a data base
  * data base, I will use a noSQL database cause python use dictionnary 
which can be easily convert into json
  * MongoDB
  * ElasticSearch (too heavy for such a small database)
* [x] Design a [gitlab pipeline](https://gitlab.com/FrenchyMike/python_pendu/pipelines) to lint the code (with using sonarQube, or any 
py linter)
