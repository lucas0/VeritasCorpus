# Veritas

## Repo containing all versions of VERITAS dataset

The code used for the Crawling/Scrapping of each version can be found under the respective folders.

Entries of each Fact-Checking Agency are stored in separate csv files, ex: Snopes entries are found on snopes.csv files.

The structure of each version might vary slightly but generally contains these columns 

- **page/article_url**
: the url of the scrapped fact-checking article(FCA)  
- **claim**
: the main claim verified by the FCA
- **claim_label**
: the label assigned to the verified claim
- **tags**
: keywords used by the FCA author to categorize the FCA
- **claim_source_url**
: the url of the identified origin (or an origin candidate, depending of the version) for that claim 
- **claim_source_domain**
: the domain of the claim_source_url, e.g.: nytimes.com is the domain for https://www.nytimes.com/2020/08/26/world/covid-19-coronavirus.html
- **date**
: the FCA's publication date  

---

Published Articles related to this work:

Azevedo, Lucas, et al. "LUX (Linguistic aspects Under eXamination): Discourse Analysis for Automatic Fake News Classification." Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021. 2021.

@inproceedings{azevedo2021lux,
  title={LUX (Linguistic aspects Under eXamination): Discourse Analysis for Automatic Fake News Classification},
  author={Azevedo, Lucas and d’Aquin, Mathieu and Davis, Brian and Zarrouk, Manel},
  booktitle={Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021},
  pages={41--56},
  year={2021}
}

Azevedo, Lucas, and Mohamed Moustafa. "Veritas annotator: Discovering the origin of a rumour." Proceedings of the Second Workshop on Fact Extraction and VERification (FEVER). 2019.

@inproceedings{azevedo2019veritas,
  title={Veritas annotator: Discovering the origin of a rumour},
  author={Azevedo, Lucas and Moustafa, Mohamed},
  booktitle={Proceedings of the Second Workshop on Fact Extraction and VERification (FEVER)},
  pages={90--98},
  year={2019}
}

Azevedo, Lucas. "Truth or lie: Automatically fact checking news." Companion Proceedings of the The Web Conference 2018. 2018.

@inproceedings{azevedo2018truth,
  title={Truth or lie: Automatically fact checking news},
  author={Azevedo, Lucas},
  booktitle={Companion Proceedings of the The Web Conference 2018},
  pages={807--811},
  year={2018}
}
