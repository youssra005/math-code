#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pgcd_euclid.py
Calcul du PGCD (GCD) de deux entiers par l'algorithme d'Euclide.
Affiche toutes les étapes de la division :
    a = b * q + r
et affiche :
- le PGCD
- si les nombres sont premiers entre eux
- la vérification d’existence de solutions de a*u + b*v = c
- les solutions particulières et générales si elles existent
"""

def lire_entier(prompt):
    """Lire un entier depuis l'entrée utilisateur avec validation."""
    while True:
        try:
            s = input(prompt)
            if s.strip().lower() in ('q', 'quit', 'exit'):
                print("Sortie demandée. Au revoir.")
                raise SystemExit
            return int(s)
        except ValueError:
            print("Entrée invalide — veuillez saisir un entier (ou 'q' pour quitter).")

def euclide_avec_etapes(a, b):
    """Algorithme d’Euclide pour le PGCD, avec enregistrement des étapes."""
    etapes = []
    while b != 0:
        q = a // b
        r = a % b
        etapes.append((a, b, q, r))
        a, b = b, r
    return abs(a), etapes

def euclide_etendu(a, b):
    """Algorithme d’Euclide étendu : retourne (pgcd, u, v) tels que a*u + b*v = pgcd."""
    if b == 0:
        return (a, 1, 0)
    else:
        pgcd, u1, v1 = euclide_etendu(b, a % b)
        u = v1
        v = u1 - (a // b) * v1
        return (pgcd, u, v)

def afficher_etapes(etapes):
    """Affiche joliment les étapes enregistrées."""
    if not etapes:
        print("Aucune division effectuée (cas particulier).")
        return
    print("\nÉtapes de la division (format: a = b * q + r) :")
    print("-" * 48)
    print(f"{'n°':>2} | {'a':>10} | {'b':>10} | {'q':>6} | {'r':>8}")
    print("-" * 48)
    for i, (a, b, q, r) in enumerate(etapes, start=1):
        print(f"{i:2d} | {a:10d} | {b:10d} | {q:6d} | {r:8d}")
    print("-" * 48)

def main():
    print("Calcul du PGCD et résolution de l’équation a*u + b*v = c")
    print("Entrez deux entiers (appuyez sur Ctrl+C ou tapez 'q' pour quitter).")
    try:
        x = lire_entier("Entier a (premier nombre) : ")
        y = lire_entier("Entier b (deuxième nombre) : ")
    except SystemExit:
        return

    a0, b0 = x, y
    a, b = abs(x), abs(y)

    if a == 0 and b == 0:
        print("\nPGCD(0, 0) n'est pas défini.")
        return

    pgcd, etapes = euclide_avec_etapes(a, b)
    afficher_etapes(etapes)

    print(f"\nConclusion : PGCD({a0}, {b0}) = {pgcd}")

    # Vérification si les deux nombres sont premiers entre eux
    if pgcd == 1:
        print("✅ Les deux nombres sont premiers entre eux (PGCD = 1).")
    else:
        print("ℹ️ Les deux nombres ne sont pas premiers entre eux (PGCD ≠ 1).")

    # Vérification d’existence des solutions pour a*u + b*v = c
    print("\nVérification d’existence de solutions pour l’équation a*u + b*v = c :")
    c = lire_entier("Entrez la valeur de c : ")

    if c % pgcd == 0:
        print(f"✅ L’équation {a0}·u + {b0}·v = {c} admet au moins une solution entière, car {pgcd} | {c}.")

        # Trouver une solution particulière avec l’algorithme étendu
        _, u, v = euclide_etendu(a0, b0)
        # Ajustement pour que a*u + b*v = c
        u0 = u * (c // pgcd)
        v0 = v * (c // pgcd)

        print(f"\n👉 Solution particulière : u₀ = {u0}, v₀ = {v0}")
        print(f"Vérification : {a0}*{u0} + {b0}*{v0} = {a0*u0 + b0*v0}")

        # Formules de la solution générale
        print(f"\n🧮 Solution générale :")
        print(f"u = {u0} + ({b0}//{pgcd})·t = {u0} + {b0//pgcd}·t")
        print(f"v = {v0} - ({a0}//{pgcd})·t = {v0} - {a0//pgcd}·t  , t ∈ ℤ")

    else:
        print(f"❌ L’équation {a0}·u + {b0}·v = {c} n’admet pas de solution entière, car {pgcd} ne divise pas {c}.")


if __name__ == "__main__":
    main()
