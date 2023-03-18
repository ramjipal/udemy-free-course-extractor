import requests
from bs4 import BeautifulSoup

# specify the website URL
# the range specifies the no. of pages to look
for i in range(1, 3):
     url = 'https://www.discudemy.com/language/english/' + str(i)
     # send a GET request to the website
     response = requests.get(url)
     # parse the HTML content
     soup = BeautifulSoup(response.content, 'html.parser')
     # find the top 5 posts
     top_posts = soup.find_all('div', class_='content')
     # print(top_posts)
     # iterate over the posts
     for post in top_posts:
     # find all the links in the post
          links = post.find_all('a')
     # print the links
          for link in links:
               l = link.get('href')
               l = l.replace("English", "go")
               response = requests.get(l)
               soup = BeautifulSoup(response.content, 'html.parser')
               tp = soup.find_all('div', class_ = 'ui segment')
               for p in tp:
                    a_link = p.find_all('a')
                    i = 0
                    for b_link in a_link:
                         if(i%2==0):
                              print(b_link.get('href'))
                              print("------------------------------------------------------------------------")
                         i+=1
print("done")