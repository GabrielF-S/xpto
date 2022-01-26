import requests
import pandas as pd

casosCovid = requests.get("https://covid-api.mmediagroup.fr/v1/cases?country=Brazil")
casosCovid = casosCovid.json()

planilha = pd.DataFrame.from_dict([casosCovid['Sao Paulo']])
planilha.to_csv("Casos.csv", index=False)
