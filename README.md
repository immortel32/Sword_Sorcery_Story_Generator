# Sword and Sorcery  Story Generator
## But de cette application
Le but de cette application est de données une deuxième vie au jeu de société [Sword & Sorcery](https://www.sword-and-sorcery.com/).

À partir d'une banque de quête et de points de cheminement, l'application va construire une campagne unique.

Une même quête pourrait être différente en y incluant des points de cheminements au hasards.

# Que fait l'application présentement?
Présentement pas grand-chose. Elle peut lire différents points de cheminements et générer le livre de contes et le livre de secret.

# Requis
Il faut que vous ayez Python 3.7 (ou plus) d'installé.
L'application devrait fonctionner sur tous les systèmes d'opérations

# Comment démarrer l'application?
- [Télécharger](https://github.com/immortel32/Sword_Sorcery_Story_Generator/archive/refs/heads/main.zip) le contenu de github
- Aller dans le répertoire app: `cd app`
- Démarrer l'application avec la commande: `python3 main.py`
  
# Comment créer de nouveaux points de cheminement "indépendant"?
Pour créer un nouveau point de cheminement "indépendant", il vous faut:
- Un titre
- (Optionnel) Des instructions spéciales pour la mise en place
- (Optionnel) Auteur pour que je puise vous ajouter dans la liste des contributeurs
- L'histoire qui peut comprendre 1 ou plusieurs choix/paragraphes

Une fois votre histoire créée, il faut la mettre dans un fichier (.json) dans le répertoire data/waypoint
Voici un exemple du fichier boite_mystere_1.json
```json
{
  "title": "Boîte mystère",
  "instruction_setup": "Ce point de cheminement doit être prêt d'un mur.",
  "story": [
    {
      "index": 1,
      "text": "Alors que vous avancez prudemment, vous découvrez une boîte dissimulée dans un coin, celle-ci est fermée mais n'est pas verrouillée. Que voulez-vous faire:\n   - Prendre une action spéciale pour ouvrir la boîte, lire la section <<INDEX_2>>\n   - Vous décidez d'ignorer la boîte. Laissez le point de cheminement à cet endroit et poursuivez votre tour."
    },
    {
      "index": 2,
      "text": "Vous ouvrez la boîte prudemment, pour y découvrir un trésor. Retirez le point de cheminement de la quête."
    }
  ]
}
```

Vous avez votre histoire mais trop compliqué à mettre en JSON? Envoyez-la-moi et je le ferai.

# Aidez-moi
SVP envoyez-moi vos histoires, c'est cette banque d'histoires qui fera la richesse de cette application