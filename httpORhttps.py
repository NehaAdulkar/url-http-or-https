#!/usr/bin/python3
import argparse, requests, re

parser = argparse.ArgumentParser(description="Tool to check URL is http or https")
parser.add_argument("-url", type=str, help="enter url", required=True)
#parser.add_argument("-o", type=str, help="enter output file")

try:
    
    a = parser.parse_args()
            
    #Regex to check if website passed as argument is http or https
    pattern=re.compile(r"https?", re.VERBOSE)
    result=pattern.finditer(a.url)
    for i in result:
       print("The website is: ", i.group())

    if "http://" in a.url or "https://" in a.url:
        print(a.url)
        r=requests.get(a.url)
        print("{} : [ {} ]\n".format(a.url, r.status_code))
        b=requests.get(a.url)    
        link=re.findall(r'(?:href=")(.*?)"', str(b.content))
        #print(link)
        for j in link:
            print(j) 
    else:
        b=requests.get("http://"+a.url) 
        print(b.url)   
        r=requests.get(b.url)
        print("{} : [ {} ]\n".format(b.url, r.status_code))
        link=re.findall(r'(?:href=")(.*?)"', str(b.content))
        #print(link)
        for j in link:
            print(j)

except Exception as e:
    print("Mess !!", e)
