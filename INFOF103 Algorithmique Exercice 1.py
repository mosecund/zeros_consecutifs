# INFO-F103 - Algorithmique - Exercice côté 1
#
# Prénom : Ismael
# Nom : Secundar
# Matricule : 504107

# N'oubliez pas de modifier le nom du fichier ex1.py en VotreMatricule.py

def zeros_consecutifs(n, binaire_n=""):
    """
    Fonction récursive qui retourne le plus grand nombre de 0 consécutifs
    dans la représentation binaire de n

    Arguments :

    - n : un nombre entier positif
    - vous pouvez ajouter autant d’arguments optionnels que vous le souhaitez
    """

    assert (isinstance(n, int))

    if binaire_n == "":                                                         # verifie si binaire_n est vide et
                                                                                # n est en binaire ou pas
        binaire_n = f'{n:b}'

    if binaire_n != "":                                                         # n a deja ete convertie
        compteur = 0
        compteur_zero = 0

        while len(binaire_n[compteur:]) != 0 and binaire_n[compteur] != "1":    # on verifie binaire_n à partir de
            compteur_zero += 1
            compteur += 1

        binaire_n = binaire_n[compteur + 1:]

        if binaire_n != "":                                                     # verifie la condition de fin pour
                                                                                # arreter la récursion
            compteur_zero = max(compteur_zero, zeros_consecutifs(n, binaire_n))

    return compteur_zero
    # Insérer votre algorithme ici, vous pouvez supprimer cette ligne ;-)


# Tests non-exhaustifs de votre solution

assert (zeros_consecutifs(2) == 1)
assert (zeros_consecutifs(4) == 2)
assert (zeros_consecutifs(32) == 5)
assert (zeros_consecutifs(42) == 1)
assert (zeros_consecutifs(49) == 3)
assert (zeros_consecutifs(1258) == 2)
assert (zeros_consecutifs(42) == 1)
assert (zeros_consecutifs(2021) == 2)
assert (zeros_consecutifs(2050) == 9)
assert (zeros_consecutifs(1) == 0)
assert (zeros_consecutifs(0) == 1)

print("Tous les tests sont passés avec succès, félicitations ! \\o/")