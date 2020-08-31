this is where I keep the positive samples from the evaluation of the automatic origin detection methods.
you can see this examples as the 'clean' data that can be used on the classifier (Lux)

**'pos_samples.csv'** contain the positive examples from the first and second annotations processes. (evaluation steps)
It also includes 50 examples from emergent and no examples from factcheck.
size of pos_samples.csv: **371**

is the same file that is in the repo VeritasCorpus/goldDatav2.1 (probably done by me) (annotation)
**'results.csv'** is the result of the annotations performed by me in the third version of the dataset.
**'filter.py'** filters the good and bad examples from **'results.csv'** into **'good_a3.csv'** and **'bad_a3.csv'** respectively.
size of good_a3.csv: **125**

**veritas v3.0** contains the good results of the **FIRST** manual annotation, 168 examples that had at > 0  "yes" vote
size of veritas3.csv: **163**

**veritas v4.0** contains the good results of the **MAIN** manual annotation, examples that had at > 0  "yes" vote
