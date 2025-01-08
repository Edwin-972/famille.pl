# famille.
Etudiant : Edwin 

Exercice 1

1. Qui est le père de Marc ?
 
   ?- père(X, marc).
   X = jaques.


3. Marc a-t-il des enfants ?
   
   ?- parent(marc, _).
   true.

Exercice 2

1. Qui est le grand-parent de Paul ?
   
   ?- grand_parent(X, paul).
   false.

3. Jacques est-il le grand-parent de Sophie ?
   
   ?- grand_parent(jaques, sophie).
   false.

Exercice 3

1. Paul a-t-il des frères ou des sœurs ?
   
   ?- frere_ou_soeur(paul, X).
   false.

Exercice 4

1. Trouvez tous les hommes dans la base de données :
   
   ?- findall(X, homme(X), Liste).
   Liste = [pierre, jaques, marc, paul].

3. Recherchez tous les parents de Sophie :
   
   ?- parent(X, sophie).
   X = jaques.

Exercice 7

1. Vérifiez si Marie est un élément de la liste `[pierre, marie, paul]` :
   
   ?- membre(marie, [pierre, marie, paul]).
   true.

Exercice 8

1. Marc est-il l'oncle de Paul ?
   
   ?- oncle(marc, paul).
   false.

3. Quels sont les oncles de Sophie ?
   
   ?- oncle(X, sophie).
X = marc ; 
X = paul ; 
   false.

Exercice 9

1. Trouvez les cousins de Paul :
   
   ?- cousin(X, paul).
   false.

3. Trouvez les cousins de Sophie :
   ?- cousin(X, sophie).
   false.
