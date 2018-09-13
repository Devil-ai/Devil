import urllib
try :
    url = "https://www.google.com"
    urllib.urlopen(url)
    status = "Connected"
except :
    status = "Not Connected"
print status
