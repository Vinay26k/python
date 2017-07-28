cr = '''

https://github.com/Vinay26k/
All copyrights related this software belongs to Vinay :)
Mail me at: vinay@programmer.net

'''

print cr

import requests,json,sys
from bs4 import BeautifulSoup as bs
import HTMLParser
def Exit():
    print "You have selected to Stop the program"
    sys.exit()
def hel():
    print(
'''
select from categories :\n
0. Any Category
1. General Knowledge
2. Entertainment: Books
3. Entertainment: Film
4. Entertainment: Music
5. Entertainment: Musicals & Theatres
6. Entertainment: Television
7. Entertainment: Video Games
8. Entertainment: Board Games
9. Science & Nature
10. Science: Computers
11. Science: Mathematics
12. Mythology
13. Sports
14. Geography
15. History
16. Politics
17. Art
18. Celebrities
19. Animals
20. Vehicles
21. Entertainment: Comics
22. Science: Gadgets
23. Entertainment: Japanese Anime & Manga
24. Entertainment: Cartoon & Animations
25. SHow CatEgorIEs
99. Exit Application
''')
hel()
while True:
    op = {0: 'any',
1: '9',
2: '10',
3: '11',
4: '12',
5: '13',
6: '14',
7: '15',
8: '16',
9: '17',
10: '18',
11: '19',
12: '20',
13: '21',
14: '22',
15: '23',
16: '24',
17: '25',
18: '26',
19: '27',
20: '28',
21: '29',
22: '30',
23: '31',
24: '32',
25: hel,
99: Exit
}
    inp = input()
    c = 1 #number of questions per request
    if inp!=25 and inp!= 99:
        if inp:
            url = r'https://opentdb.com/api.php?amount={0}&category={1}'.format(c,op[inp])
        else:
            url = r'https://opentdb.com/api.php?amount={0}'.format(c)
        r = requests.get(url)
        r = json.loads(r.text)
        r1 = r['results'][0]
        print 'category: ',r1['category']
        print 'Question: ',HTMLParser.HTMLParser().unescape(r1['question'])
        print 'Answer: ', r1['correct_answer']
        print 'type 25 for categories :)'
    else:
        op[inp]()


#download exe file: https://www.dropbox.com/s/l754ehsx9q84ymm/TriviaQuiz.exe?dl=0
