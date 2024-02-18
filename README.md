# a wonderful tool

This is a wonderful tool, which allows you to input any r34.xxx link to scrape the images of it and use that data further or just to download the images :D

# How to use

## Depdendencies
> pip install scrapy numpy pandas seaborn matplotlib

## Actually using the thing

First you need to run the Spider to gather the data for that change this line in re34scraper/r34scraper/spider/crawling_spider.py

> start_urls = ["https://rule34.xxx/index.php?page=post&s=list&tags=dark_souls+"]

in the "" place any url from r34.xxx after you entered a seach term there, here another [example](https://rule34.xxx/index.php?page=post&s=list&tags=elden_ring+) of a url.

when you have done that simply enter the folling command

> scrapy crawl r34scraper r -o output.csv 


## Using the data

Copy the output.csv file into the download too and data stuff folder then you can simply run sort_data.csv, which saves the data as a new file called sorted.csv.

From there you can either just run the dowload or download_gui.py to download the images.

Or you can use either of the .ipynb files to genererate grahps with the count of chracters and their avg score, but feel free to write your own thing to use the data and send a pr to the repo with it.

But for that you need to install juyter notebook which you can download the vs code extension for or you for whatever editor you use get the required plugin.

Here a example of a graph:
![graph](example.png)
