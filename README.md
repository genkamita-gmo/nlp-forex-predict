# nlp-forex-predict
Foreign exchange market prediction using NLP.

## Datasets
* Historical forex data: http://www.histdata.com/download-free-forex-data/?/ascii/tick-data-quotes
* News: https://github.com/philipperemy/Reuters-full-data-set

## Data exploration and preparation

### Reuters news data

* Data extracted by script "read.py" provided in the above repo, saved them into "reuters-all.txt", then choped it into separate filea, reuters-link.txt, reuters-timestamp.txt and reuters-title.txt using sed.
* Total days: 3514
* Total lines in reuters-all.txt : 8551467
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

it looks ok.

* Number of news per day: approx 300 - 1700
* Holidays make news halved (for example 25/Dec: 539)
* news

## To Do
