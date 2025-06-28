# dans cet exercise, certaines reponses seront mises en commentaire

import pandas as pd
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv(
    'STEG_BILLING_HISTORY.csv',
    sep=',',                
    encoding='utf-8',       
    low_memory=False
)

#affichez les dix premières lignes, stockez les résultats dans une variable appelée 'client_0_bills'.
client_0_bills = df.head(10)
print(client_0_bills)

#le type de données de la variable 'client_0_bills' ?
print(type(client_0_bills))

#Affichez les informations générales de l'ensemble de données et essayez de répondre aux questions suivantes 

print(df.info())
print(df.describe())

#reponses:
#nombre de ligne: dapres les infos , nous avons 4476749 lignes 
#nombre de colonnes: dapres les infos, nous avons 16 colonnes
#caractéristiques catégorielles: nous avons 3 caractéristiques catégorielles(float, int, object)
#espace mémoire: l'espace mémoire utilisé est de   546.5+ MB


#Inspectez l'ensemble de données pour détecter d'éventuelles valeurs manquantes.
print(df.isnull().sum())
# nous avons 48 valeurs manquantes dans la colonne 'counter_number' et  4531 valeur manquante dans la colonne 'reading_remarque'


#Choisissez votre stratégie pour traiter les valeurs manquantes et expliquez-nous pourquoi vous avez fait ce choix.

# Pour traiter les valeurs manquantes, nous allons supprimer les lignes contenant des valeurs manquantes.
# Cela est justifié car les valeurs manquantes dans 'counter_number' et 'reading_remarque' peuvent affecter l'analyse des données, et leur suppression permet de conserver la cohérence des données.
df_cleaned = df.dropna()

# Exécutez une analyse descriptive sur les caractéristiques numériques (colonnes).
print(df_cleaned.describe())

# Sélectionnez les enregistrements de factures pour le client avec un id = 'train_Client_0', en utilisant 2 méthodes.
# Méthode 1 : avec condition directe
client_0 = df[df['client_id'] == 'train_Client_0']

# Méthode 2 : avec query
client_0_alt = df.query("client_id == 'train_Client_0'")

# Transformez la caractéristique 'counter_type' en une variable numérique en utilisant l'encodeur de votre choix.
le = LabelEncoder()
df['counter_type_encoded'] = le.fit_transform(df['counter_type'])

print(df[['counter_type', 'counter_type_encoded']].head())

# Supprimez la caractéristique 'counter_statue' du Dataframe
df.drop(columns=['counter_statue'], inplace=True)

