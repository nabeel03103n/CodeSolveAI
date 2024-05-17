import requests
from bs4 import BeautifulSoup
from googlesearch import search
import os
import wikipedia
import time

class Fetch():

    title = ""
    answer = ""
    r = ""
    def FetchAndTrainStackOverFlow(query):
        query = query.lower()
        if "stackoverflow" in query:pass
        else:query = f"{query} stackoverflow"
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
                    ptime = time.time()

                return result 
            except:
                return False

    
    def PythonOrg(query):
        query = query.lower()
        global title
        global answer
        global r
        if "python" in query:pass
        else:query = f"{query} python"
        for j in search(query,tld="co.in", num=10, stop=10, pause=2):
            try:
                if "pypi" in j:
                    r = requests.get(j)
                    with open(f"Data/PythonOrg/{query}.html",'w',encoding='utf-8')as f:
                        f.write(r.text)
                    with open(f"Data/PythonOrg/{query}.html",encoding='utf-8')as f:
                        html_doc = f.read()
                    soup = BeautifulSoup(html_doc, 'html.parser')
                    title = f"{j}\n\n{soup.title.text}"
                    answerscell = []
                    pre_tags = soup.find_all('pre')
                    for pre_tag in pre_tags:
                        answerscell.append(pre_tag.text)
                    # print(answercell)
                    answercell = "\n".join(answerscell)
                    return answercell

                    # try:
                    #     answercell = soup.find_all(class_="code")
                    #     print(answercell)
                    # except:
                        # answercell = soup.find_all('pre').get_text()
                    #     print(answercell)

            except:
                return "Failed"

    def FetchWikipedia(query):
        query = query.lower().replace(" ","")
        results = wikipedia.summary(query)
        return results

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


