from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyBWhvN1X7K3QPi4Ve-yc8_Eub0Pt8LPDik"
my_cse_id = "009765940938512451287:h-q6wkpr9qi"


##funcao
def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def pesquisar_pdf(termo):
    results = google_search(
    termo+ ' filetype:pdf', my_api_key, my_cse_id, num=10)
    return results


"""
results = google_search(
    'titulo teste filetype:pdf', my_api_key, my_cse_id, num=10)
for result in results:
    #pprint.pprint(result)
    titulo=result['title']
    link=result['link']
    descricao=result['snippet']
    print(titulo+'-'+descricao)
    print(link)
    print('...')
"""