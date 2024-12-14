#importimi i librarive te nevojshme per kete file si:
#requests e cila e bene kerkesen online
#bs4 e cila te ndihmon per navigimin neper webpagin e kerkuar
import requests
from bs4 import BeautifulSoup

#definimi i variablave ku ruhen te dhenat te cila i marrim nga webpage
book_dictionary={}
authors=[]

#definimit i funksionit per web scrape
def scrape_books():
    #deklarimi i url prej nga po e marrim webpage
    url="https://www.goodreads.com/shelf/show/popular"
    #definimi i specifikave per mini web browers per web scrapping
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     " Chrome/58.0.3029.110 Safari/537.3"
    }
    #deklarimi i kerkeses permes request me headers
    response=requests.get(url,headers=headers)
    #Nese ka gabime na ndihmon me i gjet cila dhe ku po ndodhin
    response.raise_for_status()
    #krijimi i objektit bs4 duhet perdorur ndarsin (parser) ne menyre qe me u njofte secili tag ne vete
    soup=BeautifulSoup(response.text,'html.parser')
    #pas analizimit te struktures se faqes
    for book_div in soup.find_all("div",class_="elementList"):
        #duke i gjetur infot e kerkuara mirpo nuk jane te formatuara si duhet
        title_tag=book_div.find("a", class_="bookTitle")
        author_tag=book_div.find("span", itemprop="name")
        info_tag=book_div.find("span", class_="greyText smallText")
        #fillon formatimi
        if title_tag and author_tag:
            #marrim titullin duke hequr te gjitha hapsira dhe tag shtese se html
            title=title_tag.text.strip()
            author=author_tag.text.strip()
            full_link=f"https://goodreads.com/{title_tag['href']}"
            avg_rating, published=None, None
            if info_tag:
                info_text=info_tag.get_text(strip=True)
                #avg rating 4.34 —9,070,776 ratings  — published 2008 exmaple output, e ndajme ne baze te vijes sepse na nevoiten vetem pjese 1 dhe 3
                parts=[part.strip() for part in info_text.split("—")]
                print(parts)
                for part in parts:
                    if 'avg rating' in part:
                        avg_rating=part.split("avg rating")[-1].strip()
                    elif "published" in part:
                        published=part.split("published")[-1].strip()
            genre_response=requests.get(full_link,headers=headers)
            genre_soup=BeautifulSoup(genre_response.text, "html.parser")
            genres=[genre.get_text(strip=True) for genre in genre_soup.find_all("span", class_="BookPageMetadataSection__genrePlainText")]
            book_dictionary[(title,author)]={
                "link":full_link,
                "genres":genres,
                "avg_rating":avg_rating,
                "published":published
            }
            if author not in authors:
                authors.append(author)
    return book_dictionary,authors


scrape_books()


