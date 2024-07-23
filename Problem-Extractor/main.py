import requests
from bs4 import BeautifulSoup
from CodeforcesExtractor import getProblemSourceCode


CodeforcesHandel="MostafaOsman"

htmlSource=requests.get("""https://github.com/cs-MohamedAyman/Problem-Solving-Training/blob/master/level-2/codeforces/phase-2-3.md""").text
soup=BeautifulSoup(htmlSource,'html.parser')

tbody=soup.find_all('tbody')
h2=soup.find_all('h2',class_='heading-element')

# for i in h2:
#     print(i.text)
#     # fi = open("file/"+i.text, 'w', encoding='utf-8')

print(len(tbody),len(h2))
for i in range(len(tbody)):
    # print(h2[i+1].text)
    str=tbody[i].text
    str=str.split('\n')
    for j in str:
        tmp=j.split()
        if len(tmp)>1:
            src=getProblemSourceCode(CodeforcesHandel,tmp[-2],tmp[-1])
            if src is not None:
                codeFile=open(f"file/{tmp[-2]+tmp[-1]}.cpp",'w',encoding='utf-8')
                print(src,file=codeFile)
                codeFile.flush()
    print("===========")