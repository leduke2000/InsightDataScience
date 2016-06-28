# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 18:50:32 2016

@author: Andrey
"""
#scrapes information about Insight Data Science Fellows from the website
#the main difficulty is that the precious data appears in popover, so I use Selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.PhantomJS(executable_path="C:/A/Work/Recr/Insight Data Science/mining INSIGHT/phantomjs-2.1.1-windows/bin/phantomjs.exe")  
driver.get("http://insightdatascience.com/fellows.html")

elems = driver.find_elements_by_xpath("//div[@rel='popover']")

insight = pd.DataFrame(columns=('name','job','project','experience'),index=range(0,len(elems)))

for idx,elem in enumerate(elems):  
    ActionChains(driver).move_to_element(elem).perform()
    name = driver.find_element_by_xpath("//h3[@class='popover-title']/div[1]").text
    job = driver.find_element_by_xpath("//h3[@class='popover-title']/div[2]").text
    project = driver.find_element_by_xpath("//div[@class='popover-content']/div[2]").text
    experience = driver.find_element_by_xpath("//div[@class='popover-content']/div[4]").text
    insight.loc[idx] = [name,job,project,experience]

path='C:/A/Work/Recr/Insight Data Science/mining INSIGHT/insight.csv'    
insight.to_csv(path,encoding='utf-8',sep='\t',index=False)
#open it in R with read.delim() default settings
driver.close()
