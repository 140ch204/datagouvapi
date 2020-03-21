from apigouv import *

## https://entreprise.data.gouv.fr/api/sirene/v3/etablissements/?etat_administratif=A&code_postal=91790



## - Requete RNA ##
#myrequestrna = RnaRequest()

# myrequestrna.searchby_fulltext('judo boissy')

# myrequestrna.save()


#print(myrequestrna.searchby_fulltext('judo boissy'))

## - Requete sirene ##
myrequestsirene = SireneRequest(f'Bearer {API_KEY}')

myrequestsirene.searchby_cp('91790')




# Requete Infogreffe
#myrequestrna = InfogreffeRequest()

#myrequestrna.searchby_fulltext('judo boissy')

#myrequestrna.save()
