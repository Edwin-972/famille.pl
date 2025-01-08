% Définition des individus
homme(pierre).
homme(jaques).
homme(marc).
homme(paul).
femme(marie).
femme(sophie).
femme(julie).

% Définition des relations parentales
parent(julie, marc).
parent(julie, jaques).
parent(pierre, jaques). 
parent(jaques, sophie).
parent(pierre, paul).
parent(marie, paul).

% Définition des règles

% Père et mère
père(X, Y) :- homme(X), parent(X, Y).
mère(X, Y) :- femme(X), parent(X, Y).

% Grand_parent
grand_parent(X, Y) :- parent(X, Z), parent(Z, Y).

% Frères et sœurs
frere_ou_soeur(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Longueur d_une liste
longueur([], 0).
longueur([_ | Queue], N) :- 
    longueur(Queue, M), 
    N is M + 1.

% Vérification d_un membre dans une liste
membre(X, [X | _]). % X est le premier élément de la liste
membre(X, [_ | Queue]) :- 
    membre(X, Queue). % Vérifier dans la queue de la liste

% Oncles et tantes
oncle(X, Y) :- homme(X), parent(Z, Y), frere_ou_soeur(X, Z).
tante(X, Y) :- femme(X), parent(Z, Y), frere_ou_soeur(X, Z).


% Cousins
cousin(X, Y) :- parent(Z, X), frere_ou_soeur(Z, W), parent(W, Y).
