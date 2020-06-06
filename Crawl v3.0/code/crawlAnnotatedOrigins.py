import os,sys
import pandas as pd
from newspaper import Article
from urllib.parse import urlparse

cwd = os.path.abspath(__file__+"/..")

print(cwd)

data_path = cwd+"/VeritasCorpus v3.0"
out_data_path = cwd+"/Crawledv3.0"

input_data = pd.read_csv(data_path, sep=",", encoding='utf8')
header = ['a_url','claim','verdict','a_tags','a_date', 'a_author', 'source_list', 'o_url', 'value', 'name', 'o_domain', 'o_body', 'o_title', 'o_date', 'o_author', 'o_keywords', 'o_summary']

complete_data = []

for i,e in input_data.iterrows():
    sys.stdout.buffer.write(e['claim'].encode('utf-8'))
    o_url = e['source_url']

    #get origin_domain
    parsed_uri = urlparse(o_url)
    o_domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

    #get o_body, o_title, o_summary, o_keywords, o_date, and o_author
    a = Article(o_url)
    try:
        a.download()
        a.parse()
    except Exception as e:
        print(e)
        continue

    o_body = a.text
    o_title = a.title
    o_date = a.publish_date
    o_author = a.authors

    a.nlp()
    o_keywords = a.keywords
    o_summary = a.summary

    n = list(e)+[o_domain, o_body, o_title, o_date, o_author, o_keywords, o_summary]
    complete_data.append(n)
    print(i,"\n\n")

data = pd.DataFrame(complete_data, columns=header)
data.to_csv(out_data_path, index=False)
