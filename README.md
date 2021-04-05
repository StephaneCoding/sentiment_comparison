# Sentiment-comparison-engine

## Descriptif
A partir de deux mots clefs entrés par l'utilisateur, le programme va déterminer lequel d'entre eux est le plus apprécié.
D'après la définition de twitter, les commentaires sont aussi considérés comme des tweets.

## Pour commencer
Il vous faut un compte développeur Twitter pour obtenir l'API Twitter et entrez les clefs ligne 17 et 18 dans le code

### Description du programme
Il faut entrer un entier qui représentera le nombre de tweets qui sera évaluée dans le "sondage". Plus le nombre de tweets sera élevée, plus le programme mettra du temps à se lancer. Par la suite, entrer également le langage des tweets (français ou anglais). 10 peut être un nombre idéal si l'on veut tester rapidement le programme. En revanche si l'utilisateur rentre autre chose que ce qui est demandé, un message d'erreur s'affichera et le programme s'arrêtera.
Par la suite, on va obtenir le score moyen des sentiments récoltés avec les tweets. On les nettoie, récolte le score total et en fait la moyenne pour comparer lequel des deux mots entrés possède le meilleur score à l'aide de TextBlob.sentiments.subjectivity qui retourne un float entre 0 et 1 qui détermine les tweets qui font référence à l'opinion personnelle, l'émotion ou jugement.

### Prérequis

Installez tous les modules pour pouvoir lancer le projet avec la commande qui suivra

```
pip install tweepy
pip install textblob
pip install statistics
php install preprocessor
pip install typing
```

### Lancer le projet

Pour lancer le projet, il faut utiliser la commande qui suit

```
python3 sentiment_engine.py
```
