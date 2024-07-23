from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup


def getSubmtionId(HtmlSource):
    soup=BeautifulSoup(HtmlSource,'html.parser')
    problemId=soup.find("a",class_="view-source")
    if problemId is None:
        return None
    return problemId.text
def ExtractSoruceCodeProblem(HtmlSource):
    soup=BeautifulSoup(HtmlSource,'html.parser')
    soup=soup.find('ol',class_='linenums')
    lines=soup.find_all('li')
    sourceCode=""
    for i in lines:
        sourceCode+='\n'+i.text
    return sourceCode

def getProblemSourceCode(CodeforcesHandel,contest,problemCharacter):
    driver = webdriver.Edge()
    driver.get(f"https://codeforces.com/contest/{contest}/status")
    js_code =f"""
    document.getElementById("frameProblemIndex").value = "{problemCharacter}";
    document.getElementById("verdictName").value = "OK";
    document.getElementById("participantSubstring").value = "{CodeforcesHandel}";
    document.querySelector('input[type="submit"][value="Apply"]').click();
    """
    driver.execute_script(js_code)
    htmlContent=driver.page_source
    problemId=getSubmtionId(htmlContent)
    driver.close()
    if problemId is not None:
        driver=webdriver.Edge()
        driver.get(f"https://codeforces.com/contest/{contest}/submission/{problemId}")
        return ExtractSoruceCodeProblem(driver.page_source).strip()


# str=getProblemSourceCode("MostafaOsman","1352","A")
# print(str)