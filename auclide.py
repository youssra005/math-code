#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pgcd_euclid.py
Calcul du PGCD (GCD) de deux entiers par l'algorithme d'Euclide.
Affiche toutes les étapes de la division :
    a = b * q + r
et affiche le PGCD, une conclusion et un message si les nombres sont premiers entre eux.

Usage: python pgcd_euclid.py
"""

def lire_entier(prompt):
    """Lire un entier depuis l'entrée utilisateur avec validation."""
    while True:
        try:
            s = input(prompt)
            # Permettre que l'utilisateur tape 'q' pour quitter
            if s.strip().lower() in ('q', 'quit', 'exit'):
                print("Sortie demandée. Au revoir.")
                raise SystemExit
            return int(s)
        except ValueError:
            print("Entrée invalide — veuillez saisir un entier (ou 'q' pour quitter).")

def euclide_avec_etapes(a, b):
    """
    Exécute l'algorithme d'Euclide pour a et b (entiers >= 0).
    Retourne (pgcd, etapes) où etapes est une liste de tuples:
      (dividende, diviseur, quotient, reste)
    """
    etapes = []
    while b != 0:
        q = a // b
        r = a % b
        etapes.append((a, b, q, r))
        a, b = b, r
    return abs(a), etapes

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
    print("Calcul du PGCD par l'algorithme d'Euclide")
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
    if a == 0:
        print(f"\nPGCD({a0}, {b0}) = {b} (car premier nombre = 0).")
        return
    if b == 0:
        print(f"\nPGCD({a0}, {b0}) = {a} (car deuxième nombre = 0).")
        return

    pgcd, etapes = euclide_avec_etapes(a, b)
    afficher_etapes(etapes)

    print(f"\nConclusion : PGCD({a0}, {b0}) = {pgcd}")

    # Nouveau : Vérification si les deux nombres sont premiers entre eux
    if pgcd == 1:
        print("✅ Les deux nombres sont premiers entre eux (PGCD = 1).")
    else:
        print("ℹ️ Les deux nombres ne sont pas premiers entre eux (PGCD ≠ 1).")

    print("\nRemarques :")
    print("- Le calcul s'est fait sur les valeurs absolues des entiers fournis.")
    print("- Si vous voulez aussi les coefficients de Bézout (ax + by = pgcd), demandez-le.")

if __name__ == "__main__":
    main()