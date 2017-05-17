# NLP-FOREX-PREDICT
Foreign exchange market prediction using natural language processing.

# Library
* gensim v1.0.1

# Datasets
* Historical forex data: http://www.histdata.com/download-free-forex-data/?/ascii/tick-data-quotes
* News - Reuters: https://github.com/philipperemy/Reuters-full-data-set
* News - Bloomberg + Reuters: https://github.com/philipperemy/financial-news-dataset

# Data exploration and preparation

## Reuters news data

* Primary observation
  * Data extracted by script "read.py" provided in the above repo, saved them into "reuters-all.txt", then choped it into separate filea, reuters-link.txt, reuters-timestamp.txt and reuters-title.txt using sed.
  * Total days: 3514
  * Total news: 8,551,441. 
  * Total lines in reuters-all.txt without preprocessing: 8551467. Now "read.py" is modified to remove this corruption.
  * Dates of news ranging from 20070101 - 20160816; 3516 days in total.
  * Timestamps are sorted by day but not necessarily by time.
  * Number of news per day: approx 300 - 1700
  * Holidays reduces the number of news, e.g. 25/Dec has 539 news 
 

## Bloomberg + Reuters news datased

* 450,341 news from Bloomberg and 109,110 news from Reuters, according to README, however I count 448395 Bloomberg files.
* Total size of news is 2.3 GB for Bloomberg and 555 MB for Reuters.
* After preprocessing and concatinating, the number of lines in the corpus file is 737222, which is much bigger than expected. I suspect extra new line charactors are increasing the number of lines. File size reduced to 1.3 GB (40% reduction? really?).
* Training on a 770 MB file consumes about 35 GB memory. 
* Some news include garbage in its original text, see the bottom of 2010-06-14/u-a-e-central-bank-head-sees-economy-growing-4-in-2010-after-contraction. The garbage starts from "Enlarge image"
* The preprocess script makes corruption of text?

### Basic text analysis on bloombregcorpus.txt
* word count: 205970873

#### Gensim training optimisation
* Multicore doesn't work on Cent OS7, as it can be seen from the CPU % of top command. Typically, the CPU % is at 100% per thread running the dox2vec training. On my home mac, the CPU % increases as more workeres are added (4 workers -> 250 CPU%)
* On linux, I tried Anaconda and vanila python both but the max CPU% was about 200% for both case.
* Hyper parameter tuning:

#### Reuters-Urgent
* Word count of 'h= http' on text output of original "read.py" -> 8551441. Thats 26 lines less than the initial naive line count.
* save result as non decorated text file. When I do this, entries with \n will have "" but not for those without. This can be used for testing the data cleaning.

### Reuters-Not Urgent
* It is better to do with lots of text for word embedding, use mixed source.
* Clean title.txt by removing duplicates etc.
* Unify timzones.
* Check all txt files can be loaded as pandas dataframe. currently timestamp doesn't load properly.
* Make histogram of number of news.
* Use Bloomberg dataset.

### Bloomberg
* See if I can split the input file into multiple ones.

# Training Doc2Vec model
* Training was successful on the server with the doc2vec-lee.
* Using script "doc2vec-reuters.ipnb". Original: doc2vec-lee.ipynb (available in gensim repo).
* model.train() takes very long. Use servers for this. 
* Check availability of BLAS on python which I installed on the server -> training takesw a few seconds, which means BLAS is available.
* Parameter tuning
    vocabulary (number, 名詞、動詞、形容詞)
    vector dimensionality
    Doc2vec only? Word2vec also?
    epoch
    model type? (DBOW, DM)
    window
    size of corpus

* Saving trained model: model.save("filename")
* Loading trained model: np.load("filename") # returns an iterable
