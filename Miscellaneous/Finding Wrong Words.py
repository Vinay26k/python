#use attached file of 3kwords for this
def file_(fname,mode):
    data = open(fname,mode).read()
    return data 
    ''' In case data is separated by comma
def clean_tokens(text,char):
    for i in char:
        text = text.replace(i,"")
    return text.split("\n")
ch = [","]
'''
Data = file_("3kWords.txt",'r')
#Data = clean_tokens(Data,ch)
print("ENter the String")
ReadString = str(raw_input())
MisspelledWords = [ x for x in ReadString.split() if x not in Data]
print "Misspelled Words:\n"+ str(MisspelledWords)
