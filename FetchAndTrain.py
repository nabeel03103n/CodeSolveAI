import requests
from bs4 import BeautifulSoup
from googlesearch import search
import os
import wikipedia


class Fetch():

    title = ""
    answer = ""
    r = ""
    def FetchAndTrainStackOverFlow(query):
        global title
        global answer
        global r
        for j in search(query,tld="co.in", num=10, stop=10, pause=2):
            try:   
        
                if "stackoverflow.com" in j:
                    r = requests.get(j)
                    with open(f"Data/StackOverFlow/{query}.html",'w+')as f:
                        f.write(r.text)
                    with open(f"Data/StackOverFlow/{query}.html")as f:
                        html_doc = f.read()
                    soup = BeautifulSoup(html_doc, 'html.parser')
                    title = f"{j}\n\n{soup.title.text}"
                    answercell = soup.find_all(class_="answercell")
                    s_prose = answercell[0].find(class_="s-prose")

                    result = f"{title}\n\n{s_prose.text}--answer\n\n"
                    os.remove(f"{os.getcwd()}\Data\StackOverFlow\{query}.html")


                return result
            except:
                return False

    # def FetchAndTrainGeeksForGeeks(query):
    #     for j in search(query,tld="co.in", num=10, stop=10, pause=2):
    #         try:
    #             # query = f"{query}. geekforgeeks"

    #             if "geeksforgeeks.org" in j:
    #                 r = requests.get(j)
    #                 with open(f"Data/GeeksForGeeks/{query}.html",'w+')as f:
    #                     f.write(r.text)
    #                 with open(f"Data/GeeksForGeeks/{query}.html")as f:
    #                     html_doc = f.read()
    #                 soup = BeautifulSoup(html_doc, 'html.parser')
    #                 title = f"{j}\n\n{soup.title.text}"
    #                 answercell = soup.find(class_="code")
    #                 os.remove(f"{os.getcwd()}\Data\StackOverFlow\{query}.html")
    #                 result = f"{title}\n\n{answercell.text}\n\n"


    #                 return result
    #         except:
    #             return False
            
    def exceptions(query):
        query = str(query).replace("/","").replace("-","")
        result = wikipedia.summary(query,sentences=5)
        add = wikipedia.search(query)
        for i in range(len(add)):
            add[i] = "/"+add[i]
        add = str(add).replace(" ",'').replace("-",'').rstrip(' ').rsplit(',')
        results = f"{result}\n\n\n\n{add}"
        return results
