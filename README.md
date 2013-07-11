A simple MapReduce framework from Coursera's [Introduction to Data Science](https://class.coursera.org/datasci-001/class/index) with examples   

While it implements the gist of the MapReduce model, this framework only executes on a single machine.   

Inside data/ is a bunch of test data, and inside solution/ is the expected output 

Run    

    python wordcount.py data/books.json    

to test the word count example.    

    python join.py data/records.json    

to execute the SQL relation join example. Expected output can be verified against ``join.json``    

... and so on