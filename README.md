# nlp-forex-predict
Foreign exchange market prediction using NLP.

## Datasets
* Historical forex data: http://www.histdata.com/download-free-forex-data/?/ascii/tick-data-quotes
* News - Reuters: https://github.com/philipperemy/Reuters-full-data-set
* News - Bloomberg + Reuters: https://github.com/philipperemy/financial-news-dataset

## Data exploration and preparation

### Reuters news data

* Data extracted by script "read.py" provided in the above repo, saved them into "reuters-all.txt", then choped it into separate filea, reuters-link.txt, reuters-timestamp.txt and reuters-title.txt using sed.
* Total days: 3514
* According to the dataset README, the total number of news is 8,551,441. However, total lines in reuters-all.txt: 8551467, due to corruption of data.
* Dates of news ranging from 20070101 - 20160816; 3516 days in total.
* Timestamps are sorted by day but not necessarily by time.

---

* Check number of lines in 

$ sh reuters-link | wc -l

 8551467

$ sh reuters-timestamp | wc -l

 8551467

$ cat reuters-all.txt | wc -l

 8551467

$ wc -l reuters-title.txt

 8551467 reuters-title.txt

They are consistent.

* Number of news per day: approx 300 - 1700
* Holidays reduces the number of news, for example 25/Dec has 539 news

### Bloomberg + Reuters news datased

* 450,341 news from Bloomberg and 109,110 news from Reuters, according to README, however I count 448395 Bloomberg files.
* Total size of news is 2.3 GB for Bloomberg and 555 MB for Reuters.

### To Do
#### Reuters-Urgent
Automate data cleaning
* Write script that extracts title only, do the following steps.
* load text as pandas dataframe and replace \n with white space and remove ". What will happen when loading entries with "? -> When loading from csv, it doesn' change lines even when the number of " is odd, but the position of " is kind of randomised. See how many lines the output have and compare it against the word count of 'h= http' for example.
-> 8551441. Thats 26 lines less than the initial naive line count.
Check titles that has " and see how it is loaded in when it is loaded to pandas.
* save result as non decorated text file. When I do this, entries with \n will have "" but not for those without. This can be used for testing the data cleaning.

#### Reuters-Not Urgent
* It is better to do with lots of text for word embedding, use mixed source.
* Clean title.txt be removing duplicates etc.
* Unify timzones.
* Check all txt files can be loaded as pandas dataframe. currently timestamp cannot.
* Make histogram of number of news.
* Use Bloomberg dataset.

## Training Doc2Vec model
* Using script "doc2vec-reuters.ipnb". Original: doc2vec-lee.ipynb (available in gensim repo).
* model.train() takes very long. Use servers for this. 
