for file in  $( for pair in *$( cat good-pair-year.txt ); do find . -name *$pair*.csv-date; done ); do python daily_volatility.py $file > $file-vol; done
