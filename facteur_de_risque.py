# Programme pour calculer l'évaluation d'un facteur de risque
# Créé pour le livre électronique "Stratégies de Gestion des Risques"

# 1. Définir les variables
probabilite = 4  # Niveau de probabilité (ex. de 1 à 5)
impact = 5       # Niveau d'impact (ex. de 1 à 5)

# 2. Effectuer le calcul
evaluation_du_risque = probabilite * impact

# 3. Afficher le résultat à l'utilisateur
print("--- Calculateur de Risque ---")
print(f"Probabilité du risque : {probabilite}")
print(f"Impact du risque : {impact}")
print("----------------------------")
print(f"L'évaluation totale du risque est : {evaluation_du_risque}")

# 4. Interprétation du résultat
if evaluation_du_risque >= 15:
    print("\nC'est un risque de haute priorité. Il nécessite une attention immédiate.")
elif evaluation_du_risque >= 8:
    print("\nC'est un risque de priorité moyenne. Il doit être surveillé de près.")
else:
    print("\nC'est un risque de faible priorité. Il ne nécessite pas d'action immédiate.")