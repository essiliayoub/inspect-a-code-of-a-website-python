from urllib.request import urlopen
css =  urlopen("https://www.google.com/").read()
html = urlopen("https://www.google.com/").read()
print(css,html)