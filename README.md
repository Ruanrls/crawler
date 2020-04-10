# crawler
A web crawler with email crawler

## How to use
**- on windows**
  - You need to install python and exec the program with the interpreter
  
**- on linux**
    
  you can use:
    
  ``` python full_crawler.py {-h} {-v} {-t TIME} {-r} host ```
  
  or:
  
  ``` ./full_crawler.py {-h} {-v} {-t TIME} {-r} host ```
  
    
  where:
  
    - h: the help command
    - v: increase the verbosity of program, showing errors and each links found
    - t: 'number': set the maximum of links that the script will crawl
    - r: randomize the choices of links that script will crawl
    - host: the url of host that you want to start the crawling (need to start with: 'http://' or 'https://')
