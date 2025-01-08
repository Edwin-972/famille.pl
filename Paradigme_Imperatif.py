# Saisie des noms et des notes des étudiants
noms_etudiants = []
notes_etudiants = []

# Demande du nombre d'étudiants
nombre_etudiants = int(input("Combien d'étudiants voulez-vous saisir ? "))

# Saisie des données pour chaque étudiant
for i in range(nombre_etudiants):
    nom = input(f"Nom de l’étudiant {i + 1} : ")
    while True:
        try:
            note = float(input(f"Note de {nom} (sur 20) : "))
            if 0 <= note <= 20:  # La note doit être entre 0 et 20
                break
            else:
                print("La note doit être entre 0 et 20.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    noms_etudiants.append(nom)
    notes_etudiants.append(note)

# Affichage des noms et des notes
print("\nListe des étudiants et leurs notes :")
for i in range(nombre_etudiants):
    print(f"{noms_etudiants[i]} : {notes_etudiants[i]}/20")

# Fonction pour calculer la moyenne
def calculer_moyenne(notes):
    if len(notes) == 0:  # Si pas de notes, renvoyer 0
        return 0
    return sum(notes) / len(notes)

# Calcul de la moyenne de la classe
moyenne_classe = calculer_moyenne(notes_etudiants)
print(f"\nMoyenne de la classe : {moyenne_classe:.2f}")

# Fonction pour afficher les étudiants par réussite ou échec
def afficher_repartition(noms, notes):
    reussite = [noms[i] for i in range(len(notes)) if notes[i] >= 10]
    echec = [noms[i] for i in range(len(notes)) if notes[i] < 10]
    print("\nÉtudiants ayant réussi :", ", ".join(reussite) if reussite else "Aucun")
    print("Étudiants en échec :", ", ".join(echec) if echec else "Aucun")

# Affichage de la répartition des étudiants
afficher_repartition(noms_etudiants, notes_etudiants)

# Fonction pour trouver l'étudiant ayant la meilleure note
def meilleure_note(noms, notes):
    if len(notes) == 0:
        print("\nPas de notes pour déterminer la meilleure note.")
        return
    max_note = max(notes)
    index = notes.index(max_note)
    print(f"\nL’étudiant avec la meilleure note est {noms[index]} avec {max_note:.2f}.")

# Affichage de l'étudiant ayant la meilleure note
meilleure_note(noms_etudiants, notes_etudiants)