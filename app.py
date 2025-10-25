import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')


#question 3A : chiffre d'affaires total
'''
données['ca'] = données['prix'] * données['qte']

ca_total_global = données['ca'].sum()

df_total = pd.DataFrame({'Catégorie': ['CA Total'], 'Montant': [ca_total_global]})

figure = px.bar(df_total , x= 'Catégorie', y='Montant', title='Chiffre d\'affaire total', labels={'Montant': 'Chiffre d\'affaire (en €)', 'Catégorie': ''} , text='Montant')
'''

#Question 3B : ventes par produit
#figure = px.pie(données, values='qte', names='produit', title='quantité vendue par produit')

#Question 3C : ventes par région
#figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

#Question 6A : ventes par produit
'''
qte_par_produit = données.groupby('produit')['qte'].sum().reset_index()
figure = px.bar(qte_par_produit, x='produit', y='qte', title='Quantité totale vendue par produit')
'''

#Question 6B : chiffre d'affaires par produit
données['chiffre_affaires'] = données['prix'] * données['qte']

ca_produit = données.groupby('produit')['chiffre_affaires'].sum().reset_index()
figure = px.bar(ca_produit, x='produit', y='chiffre_affaires', title='Chiffre d\'affaires par produit', labels={'chiffre_affaires': 'Chiffre d\'affaires (en €)', 'produit': 'Produit'}, text='chiffre_affaires')


figure.write_html('ventes_produit_barres.html')

print('fichier généré avec succès !')
