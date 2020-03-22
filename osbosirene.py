from obsoapigouv import *

import os
import dotenv

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


API_KEY = os.getenv("API_KEY")

## https://entreprise.data.gouv.fr/api/sirene/v3/etablissements/?etat_administratif=A&code_postal=91790



## - Requete RNA ##
#myrequestrna = RnaRequest()

# myrequestrna.searchby_fulltext('judo boissy')

# myrequestrna.save()


#print(myrequestrna.searchby_fulltext('judo boissy'))

## - Requete sirene ##
myrequestsirene = SireneRequest(f'Bearer {API_KEY}')

print(myrequestsirene.searchby_siren('353873953'))

# Requete Infogreffe
#myrequestrna = InfogreffeRequest()

#myrequestrna.searchby_fulltext('judo boissy')

#myrequestrna.save()
