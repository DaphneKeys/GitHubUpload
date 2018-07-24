
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
#comic saver - saves each post of a comic page 
#USAGE python comic.py <url>
 
import logging, requests, bs4, os, sys 
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
#TODO: get url
 
 
if len(  sys.argv ) == 1:
          #comic_url = sys.argv[1]
          comic_url = "http://xkcd.com"
          try:
                    #TODO: make request to url 
                    res = requests.get(comic_url)
                    res.raise_for_status()
                    comic_soup = bs4.BeautifulSoup(res.text,"html.parser" )
                    logging.info("Soup created ")
                    prev_button = comic_soup.select("a[rel='prev']")[0]
                    prev_button_href = prev_button.get("href")
                    logging.info("Prev button obtained")
                    iterator = 0
                    limit = 100
                    dir = None
                    if not os.path.exists(os.path.abspath("comic")):
                              dir = os.mkdir("comic")       
                    else:
                              dir = os.path.abspath("comic")
                    while not prev_button.endswith("#")  and iterator < limit: #TODO: get image in comic comic_image = comic_soup.select("#comic > img")
                              assert comic_image, "Image should exist"
                              if comic_image:
                                        comic_image = comic_image[0]
                                        comic_image_url = comic_image.get("src")
                                        comic_title =comic_soup.select("#ctitle")
                                        comic_title = comic_title[0].get_text()
                                         
                                        try:
                                                  #TODO: download image 
                                                  comic_res = requests.get(comic_url + comic_image_url)
                                                  comic_res.raise_for_status()
                                                  #TODO: create a file 
                                                  comic_file = open(os.path.join(dir, comic_title + ".jpg" ), "wb")
                                                  logging.info("Comic File created as {}".format(comic_title))
                                                  for chunk in comic_res.iter_content(10000):
                                                            comic_file.write(chunk)
                                                  #close file 
                                                  comic_file.close()
                                        except Exception as err:
                                                  logging.error("Comic Download Error: " + str( err ))
                               
                              #TODO: switch to previous page 
                              res = requests.get(comic_url + prev_button_href)
                              #TODO:  res set soup
                              comic_soup = bs4.BeautifulSoup(res.text,"html.parser" )
                              #TODO: set prev_button
                              prev_button = comic_soup.select("a[rel='prev']")
                              if prev_button:
                                        prev_button = prev_button[0]
                                        prev_button_href = prev_button.get("href")
                              logging.info("Page has been changed")
                              iterator+= 1
          except Exception as err:
                    logging.error(str(err)) 
 
else:
          logging.error("Script requires a <url>")
 
