import random
import urllib.request
i = 2001
#can download any file just change filename to the format of file downloading
def download_file(url):
    name = 'Lesson'+str(i)
    fullname = str(name)+".pdf"
    urllib.request.urlretrieve(url,fullname)

#change url to any other downloads
for i in range(2001,2042):
    url = 'http://nptel.ac.in/courses/106105078/pdf/Lesson%{0}.pdf'.format(i)
    #x = input();
    download_file(url);
