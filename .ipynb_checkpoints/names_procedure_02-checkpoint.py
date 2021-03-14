from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import webdrivermanager


# 1. setup 
# **REMEMBER** remove path to your local folder
driver = webdriver.Chrome("C:/Users/Ahn/AppData/Local/salabs_/WebDriverManager/bin/chromedriver.exe")
dict_female = dict()
dict_male = dict()


# 2. standard procedure for each page

def get_all_names(url):
    all_names = list()
    urls = list()
    urls.append(url)
    #print("STEP 3: " + url)

    driver.get(url)
    table_anchors = driver.find_elements_by_xpath("//table/tbody/tr/td[@bordercolor='#000000'][@valign='top']/p[@align='center']/font[@size='1'][@color='#FFFFFF']/a")
    #table_anchors = driver.find_elements_by_xpath("//table[@width='100%']/tbody/tr[6]/td[@valign='top']/p[@align='center']/font/a")
    urls.extend(o.get_attribute('href') for o in table_anchors) 
    urls.pop(1) # 'remove contact'
    urls.pop(1) # remove 'male names' links

    for url in urls:
       #print(url)
       names = get_names_by_page(url)
       all_names.extend(names)

       if(len(all_names) >= 900):
           break


    return all_names


def get_names_by_page(url):
    names = list()
    driver.get(url)
    #print("STEP 4: " + url)

    table_with_names = driver.find_elements_by_xpath("//table/tbody/tr/td//ol/li/font/a")   #/a
    #table_with_names = driver.find_elements_by_xpath("//table/tbody/tr/td")
    # IMPROVE: can we simply get all anchor elements without the for loop? 
    attr = (o.text for o in table_with_names) 
    names.extend(attr)

    '''
     for td in table_with_names:
        elements = td.find_elements_by_xpath("//ol/li/font/a")
        attr = (o.text for o in elements) 
        names.extend(attr)

    '''  

    #print("STEP 5: ")  
    #print(names)

    return names      

    


"""
NOTES:
First get list of urls with lambda function, after that loop through dict to get names by culture. the value with url will be replaced
"""


# # fill dictionary with all names by culture and gender
def fill_names_dict(url, gender):
    dict_out = dict()

    driver.get(url)
    categories_cultures = driver.find_elements_by_xpath("//td[@width='46%']/table/tbody/tr/td/p")

    for x in range(1, len(categories_cultures)):
        culture = categories_cultures[x]
        print(culture)

        # get URLs and save them
        elements = culture.find_elements_by_tag_name("a")
  
        culture_key = elements[0].text # get text of first <a>  
        link = elements[gender].get_attribute('href')  # get desired url  
        dict_out[culture_key] = link  


    # get names of each page
    for culture_key, val in dict_out.items():
        dict_out[culture_key] = get_all_names(val)
        print(dict_out[culture_key]) # debug
   
    return dict_out

    


# 3. implementation 

# 4 output
url = "http://www.20000-names.com"
#dict_female = fill_names_dict(url, 0) # 0:female, 1:male
#dict_male = fill_names_dict(url, 1)

names = get_all_names("http://www.20000-names.com/female_japanese_names.htm")
print(names)
print("size: ", len(names))
'''
# debug result
for x, y in dict_female.items():
  print(x, y)
'''
# end web scrapping
driver.quit()