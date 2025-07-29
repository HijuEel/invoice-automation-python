import pandas as pd

# Charger le fichier Excel
fichier = "facture_input.xlsx"
df = pd.read_excel(fichier)

# Filtrer les factures non payées
non_payees = df[df["Statut"] == "Non payée"].copy()

# Calculs
non_payees.loc[:, "TVA (€)"] = non_payees["Montant HT"] * non_payees["TVA %"] / 100
non_payees.loc[:, "Montant TTC"] = non_payees["Montant HT"] + non_payees["TVA (€)"]

# Affichage
print("\n📄 Factures NON PAYÉES avec montants calculés :\n")
print(non_payees[["Numéro facture", "Client", "Montant HT", "TVA %", "TVA (€)", "Montant TTC"]])

# Exporter vers un nouveau fichier Excel
non_payees.to_excel("journal_output.xlsx", index=False)
print("\n✅ Le journal comptable a été exporté dans 'journal_output.xlsx' !")
