import requests
import json
from datetime import datetime

class RnaRequest:
  ### Make request on the RNA Api ### 
  # https://entreprise.data.gouv.fr/api_doc_rna
    def __init__(self):
        ### Initialization method ###
        self.created = datetime.now()
        self.updated = datetime.now()
        self.urlapi = 'https://entreprise.data.gouv.fr/api/rna/v1/'
        self.headers = ""
        self.response = ""

    def __repr__(self):
         return " mis à jour le " + str(self.updated)

    def searchby_fulltext(self,value):
        self.headers = {'Accept': 'application/json'}
        urlrequest = 'full_text/'
        url = self.urlapi + urlrequest + value
        return self.getresponse(url) 

    def getresponse(self,url):
        self.response = requests.get(url, headers = self.headers).json()
        return self.response

    def save(self):
        with open(self.resultfilename(), 'w') as outfile:
            json.dump(self.response, outfile)
        return 'ok'

    def resultfilename(self):
      ### update the name for the result file ###
        d = datetime.now()
        resultfilename = "./json/"+ "results_" + str(d.year) + "_" + str(d.month) + "_" + str(d.day) + "_" + str(d.hour) + "_" + str(d.minute) + "_" + str(d.second)+".json"
        return resultfilename


class SireneRequest:
  ### Make request on the Sirene Api ### 
  # https://api.insee.fr/catalogue/site/themes/wso2/subthemes/insee/pages/item-info.jag?name=Sirene&version=V3&provider=insee
    def __init__(self,token):
        ### Initialization method ###
        self.created = datetime.now()
        self.updated = datetime.now()
        self.urlapi = 'https://api.insee.fr/entreprises/sirene/V3/'
        self.headers = {'Accept': 'application/json','Authorization' : f'Bearer {API_KEY}'}

    def __repr__(self):
         return " mis à jour le " + str(self.updated)

    def searchby_siren(self,value=''):
        urlrequest = 'siren/'
        url = self.urlapi + urlrequest + str(value)
        print(url)
        return self.getresponse(url) 
                
    def searchby_cp(self,value=''):
        urlrequest = 'siren/'
        url = self.urlapi + urlrequest + str(value)
        print(url)
        return self.getresponse(url) 

    def getresponse(self,url):
        return requests.get( url, headers = self.headers).json()




class InfogreffeRequest:
  ### Make request on the *infogreffe API ### 
  # 
  # NOT  WORKING ! 
  # https://opendata.datainfogreffe.fr/api/v2/console
    def __init__(self):
        ### Initialization method ###
        self.created = datetime.now()
        self.updated = datetime.now()
        self.urlapi = 'https://opendata.datainfogreffe.fr/api/v2'
        self.headers = ""
        self.response = ""

    def __repr__(self):
         return " mis à jour le " + str(self.updated)

    def searchby_fulltext(self,value):
        self.headers = {'Accept': 'application/json'}
        urlrequest = 'full_text/'
        url = self.urlapi + urlrequest + value
        return self.getresponse(url) 

    def getresponse(self,url):
        self.response = requests.get(url, headers = self.headers).json()
        return self.response

    def save(self):
        with open(self.resultfilename(), 'w') as outfile:
            json.dump(self.response, outfile)
        return 'ok'

    def resultfilename(self):
      ### update the name for the result file ###
        d = datetime.now()
        resultfilename = "./json/"+ "results_" + str(d.year) + "_" + str(d.month) + "_" + str(d.day) + "_" + str(d.hour) + "_" + str(d.minute) + "_" + str(d.second)+".json"
        return resultfilename