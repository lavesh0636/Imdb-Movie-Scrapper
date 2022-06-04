#python Code To find Top 100 Movies IMDb
import requests 
from bs4 import BeautifulSoup
val = []
with open ("TopGrossingFilms.txt","w") as file:
    for q in range(1,11):
        url = "https://www.imdb.com/list/ls063765675/?sort=list_order,asc&st_dt=&mode=detail&page="+str(q)
        page = requests.get(url)
        suop = BeautifulSoup(page.content, "html.parser")
        names = str(suop.find_all("h3"))
        val = names.split(">\n")
        word=""
        x=0
        for i in val:
            if i[0:2] != "<a":
                val.pop(x)
                x=x+1
            else:
                x=x+1
        x=0
        for i in val:
            if i[0:2] == "<a":
                x=x+1
            else:
                val.pop(x)
                x=x+1
        for i in val:
            x=0
            for y in i:
                if y == ">":
                    word=i[x+1:-3]
                    file.write(word+"\n")      
                else:
                    x=x+1




with open ("TopWatchedFilms.txt","w") as file:
    for q in range(1,11):
        url = "https://www.imdb.com/list/ls091520106/?sort=list_order,asc&st_dt=&mode=detail&page="+str(q)
        page = requests.get(url)
        suop = BeautifulSoup(page.content, "html.parser")
        names = str(suop.find_all("h3"))
        val = names.split(">\n")
        word=""
        x=0
        for i in val:
            if i[0:2] != "<a":
                val.pop(x)
                x=x+1
            else:
                x=x+1
        x=0
        for i in val:
            if i[0:2] == "<a":
                x=x+1
            else:
                val.pop(x)
                x=x+1
        for i in val:
            x=0
            for y in i:
                if y == ">":
                    word=i[x+1:-3]
                    file.write(word+"\n")      
                else:
                    x=x+1


