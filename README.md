# **Décryptage de Cryptogramme en Substitution Monoalphabétique**
Ce programme Python aide à déchiffrer un texte chiffré en utilisant une **méthode de substitution monoalphabétique**. Il utilise l'analyse de la fréquence des lettres en langue française et une substitution guidée par des hypothèses sur les mots fréquents et les structures courantes du français pour casser le cryptogramme.

## Fonctionnalités
1. **Analyse de Fréquence des Lettres** : Le programme commence par analyser le texte chiffré en comptant la fréquence de chaque lettre, et les compare aux fréquences des lettres en français (E, A, S, I, N, T, etc.). Cela génère une substitution initiale basée sur les lettres les plus probables.
2. **Substitution Monoalphabétique** : Une substitution de base est appliquée, où chaque lettre du cryptogramme est associée à une lettre de l'alphabet français en fonction de sa fréquence. 
3. **Affinage Progressif des Hypothèses** :
   - Le programme propose une série de substitutions manuelles basées sur l'observation de mots et de digrammes partiellement déchiffrés dans le texte.
   - Des mots comme "LE", "UNE", "DES", et des digrammes comme "ES", "LE" et "DE" sont utilisés pour guider la substitution.
   - À chaque nouvelle substitution, le texte est mis à jour pour révéler davantage de mots et vérifier la cohérence.
4. **Fonction d'Affinage Interactif** : La fonction `refine_substitution` permet de tester des hypothèses en réattribuant des lettres dans le dictionnaire de substitution. Cette fonction peut être utilisée pour ajuster la substitution en fonction des résultats intermédiaires observés dans le texte déchiffré.
5. **Aperçu Progressif du Texte Déchiffré** : À chaque itération, le programme affiche le texte partiellement déchiffré, ce qui permet à l'utilisateur de confirmer ou de réviser les hypothèses de substitution.

## Structure du Code
- **Analyse de fréquence** : Compte les occurrences de chaque lettre dans le cryptogramme.
- **Initialisation de la substitution** : Création d'un dictionnaire de correspondances lettre à lettre basé sur la fréquence en français.
- **Fonction d'affinage de substitution** : `refine_substitution`, qui permet de tester de nouvelles correspondances pour chaque lettre.
- **Affichage interactif** : Le texte est progressivement affiché pour permettre une évaluation des correspondances lettre par lettre.

## Utilisation
Ce programme est conçu pour être exécuté dans un environnement Python. L'utilisateur peut modifier les hypothèses de substitution directement dans le code pour ajuster les correspondances en fonction des résultats partiels obtenus à chaque étape du déchiffrement.
### Exécution
1. Assurez-vous que le texte chiffré est bien inséré dans la variable `cipher_text`.
2. Exécutez le programme pour voir les résultats de la substitution initiale.
3. Modifiez les substitutions en fonction des hypothèses et affinez le texte jusqu'à ce qu'il soit complètement déchiffré.

## Exemple d'Utilisation
Un exemple de texte chiffré est inclus dans la variable `cipher_text`. L'utilisateur peut observer le texte partiellement déchiffré et appliquer des substitutions pour découvrir le message en clair.

Ce programme est particulièrement utile pour ceux qui veulent explorer les techniques de cryptanalyse classique et se familiariser avec les méthodes de décryptage monoalphabétiques.

## Exigences
- **Python 3.x** : Assurez-vous que Python 3 est installé sur votre machine.