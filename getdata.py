from gouvapidata import *

mydata = GouvApiData()

mydata.search_active_by_cp('91790',0)

#my_json = {'etablissements': [{'id': 55419840, 'siren': '538516063', 'nic': '00012', 'siret': '53851606300012', 'statut_diffusion': 'O', 'date_creation': '2012-01-02', 'tranche_effectifs': None, 'annee_effectifs': None, 'activite_principale_registre_metiers': '4520AB', 'date_dernier_traitement': '2020-02-21T03:54:16', 'etablissement_siege': 't', 'nombre_periodes': '1', 'complement_adresse': None, 'numero_voie': '19', 'indice_repetition': None, 'type_voie': 'AV', 'libelle_voie': 'DE PARIS', 'code_postal': '91790', 'libelle_commune': 'BOISSY-SOUS-SAINT-YON', 'libelle_commune_etranger': None, 'distribution_speciale': None, 'code_commune': '91085', 'code_cedex': None, 'libelle_cedex': None, 'code_pays_etranger': None, 'libelle_pays_etranger': None, 'complement_adresse_2': None, 'numero_voie_2': None, 'indice_repetition_2': None, 'type_voie_2': None, 'libelle_voie_2': None, 'code_postal_2': None, 'libelle_commune_2': None, 'libelle_commune_etranger_2': None, 'distribution_speciale_2': None, 'code_commune_2': None, 'code_cedex_2': None, 'libelle_cedex_2': None, 'code_pays_etranger_2': None, 'libelle_pays_etranger_2': None, 'date_debut': '2012-01-02', 'etat_administratif': 'A', 'enseigne_1': None, 'enseigne_2': None, 'enseigne_3': None, 'denomination_usuelle': 'MCA AUTOS', 'activite_principale': '45.20A', 'nomenclature_activite_principale': 'NAFRev2', 'caractere_employeur': 'N', 'longitude': '2.217579', 'latitude': '48.549045', 'geo_score': '0.79', 'geo_type': 'housenumber', 'geo_adresse': '19 Avenue de Paris 91790 Boissy-sous-Saint-Yon', 'geo_id': 'ADRNIVX_0000000271541297', 'geo_ligne': 'G', 'geo_l4': '19 AVENUE DE PARIS', 'geo_l5': None, 'unite_legale_id': 14147134, 'created_at': '2020-02-02T03:58:26.139+01:00', 'updated_at': '2020-02-23T00:34:29.329+01:00', 'unite_legale': {'id': 14147134, 'siren': '538516063', 'statut_diffusion': 'O', 'unite_purgee': None, 'date_creation': '2012-01-02', 'sigle': None, 'sexe': None, 'prenom_1': None, 'prenom_2': None, 'prenom_3': None, 'prenom_4': None, 'prenom_usuel': None, 'pseudonyme': None, 'identifiant_association': None, 'tranche_effectifs': None, 'annee_effectifs': None, 'date_dernier_traitement': '2020-02-21T03:54:16', 'nombre_periodes': '2', 'categorie_entreprise': 'PME', 'annee_categorie_entreprise': '2017', 'date_fin': None, 'date_debut': '2019-12-02', 'etat_administratif': 'A', 'nom': None, 'nom_usage': None, 'denomination': 'MCA AUTOS', 'denomination_usuelle_1': None, 'denomination_usuelle_2': None, 'denomination_usuelle_3': None, 'categorie_juridique': '5499', 'activite_principale': '45.20A', 'nomenclature_activite_principale': 'NAFRev2', 'nic_siege': '00012', 'economie_sociale_solidaire': 'N', 'caractere_employeur': 'N', 'created_at': '2020-01-30T17:02:30.627+01:00', 'updated_at': '2020-02-22T00:28:26.908+01:00', 'etablissement_siege': None}}], 'meta': {'total_results': 522, 'per_page': 1, 'total_pages': 522, 'page': 1}}


#print(my_json['meta']['total_pages'])


#etabs = my_json['etablissements']
#for etab in etabs :
    #print(etab['id'])
#    for data in etab:
        #print(data + ":" + str(etab[data]) )
#        ""

    