from apigouv import *

# Requete RNA
myrequestrna = RnaRequest()

myrequestrna.searchby_fulltext('judo boissy')

myrequestrna.save()


#print(myrequestrna.searchby_fulltext('judo boissy'))

# Requete sirene
# myrequestsirene = SireneRequest('Bearer e39c63aa-d74e-34b7-8356-3557900b7c6b')

#print(myrequestsirene.searchby_siren('005520135'))

