# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 19:50:10 2018

@author: RTR
"""
from selenium import webdriver
from time import sleep
term=input("Enter a search term: ")
exe = "D:\\Suresh\\chromedriver.exe"
driver = webdriver.Chrome(exe)
driver.get("https://www.google.com/search?q={0}&source=lnms&tbm=nws".format(term))
index=0
links=[]
head=[]

posts = driver.find_elements_by_class_name("bkWMgd")
urls = driver.find_elements_by_xpath("//h3//a") #urls=driver.find_element_by_css_selector("h3.r a")
for l in urls:
    links.append(l.get_attribute("href"))
    l.get_attribute("href")
    #href = l.get_attribute("href")
    #print(href) 
for post in posts:
    head.append(post.text)
    #print(post.text) 

while index <=2:
    driver.find_element_by_xpath('//*[@id="pnnext"]/span[2]').click()#next_page=driver.find_element_by_css_selector("#pnnext").click()
    sleep(5)
    posts = driver.find_elements_by_class_name("bkWMgd")
    urls = driver.find_elements_by_xpath("//h3//a")
    for post in posts:
        head.append(post.text)
        #print(post.text)   
    for l in urls:
        links.append(l.get_attribute("href"))
        l.get_attribute("href")
        #href = l.get_attribute("href")
        #print(href)
    index+=1
    sleep(2)

driver.close()

with open("D://Suresh//google_search_selenium.txt","r+",encoding='utf8') as output:
    for i in head:
        output.write(i+"\n\n")
        
with open("D://Suresh//google_search_selenium.txt","r+",encoding='utf8') as output:
    for i in links:
        output.write(i+"\n\n")



""" 
posts = driver.find_elements_by_class_name("bkWMgd")
for post in posts:
    print(post.text)
    
driver.find_element_by_xpath('//*[@id="pnnext"]/span[2]').click()
posts = driver.find_elements_by_class_name("bkWMgd")
for post in posts:
    print(post.text)
"""

