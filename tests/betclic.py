import urllib.request, requests
import json
import csv

def matchs():

    url = "https://offer.cdn.begmedia.com/api/pub/v4/events?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=1000&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate&sportIds=1"
    reponse = requests.get(url)
    contenu = reponse.json()
    
    # print(json.dumps(contenu, sort_keys=True, indent=4))

    
    for i in contenu:
    

          print("Date :", i['date'])
          print("Match :", i['name'])

          eq1 = i['markets'][0]['selections'][0]['name']
          nul = i['markets'][0]['selections'][1]['name']
          eq2 = i['markets'][0]['selections'][2]['name']

          cote_eq1 = i['markets'][0]['selections'][0]['odds']
          cote_nul = i['markets'][0]['selections'][1]['odds']
          cote_eq2 = i['markets'][0]['selections'][2]['odds']

          print(eq1 , end="      ")
          print("Cote :", cote_eq1)
          print(nul , end="               ")
          print("Cote :", cote_nul)
          print(eq2 , end="      ")
          print("Cote :", cote_eq2)
          print()

          
          # with open('data.csv', 'w', encoding='UTF8') as f:
          #   writer = csv.writer(f)
        
          #   writer.writerow(eq1)
          #   writer.writerow(nul)
          #   writer.writerow(eq2)

        
          calcul_surebet = (1/cote_eq1)+(1/cote_nul)+(1/cote_eq2)
        
          if calcul_surebet < 1:
            print("Date :", i['date'])
            print("Match :", i['name'])
            print()
          else:
            pass
          
