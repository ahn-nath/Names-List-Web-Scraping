from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException  
import webdrivermanager


# 1. setup 
# **REMEMBER** remove path to your local folder
driver = webdriver.Chrome("C:/Users/Ahn/AppData/Local/salabs_/WebDriverManager/bin/chromedriver.exe")
dict_female = dict()
dict_male = dict()
lenx=0

# 2. standard procedure for each page
def get_all_names(url):

    all_names = list()
    next_url = url

    while(True):

        try: 
            # extract names from table in current web page
            names = get_names_by_page(next_url)
            all_names.extend(names)

            # get url for the next page [anchor element with containing "NEXT" text]
            next_button = driver.find_element_by_xpath("//*[contains(text(), 'NEXT')]")
            next_url = next_button.get_attribute('href')
            driver.get(next_url)
            
            print(next_url)
            
        except NoSuchElementException:
            return all_names


def get_names_by_page(url):
    names = list()
    driver.get(url)

    table_with_names = driver.find_elements_by_xpath("//div[@class='table-responsive1']/table/tbody/tr/td[1]/a")  
   
    attr = (o.text for o in table_with_names) 
    names.extend(attr)

    return names      


# # fill dictionary with all names by culture
def fill_names_dict(url, gender):
    dict_out = dict()

    driver.get(url)
    # get element with list of cultures
    categories_cultures = driver.find_element_by_id("orgin") 
    cultures = (x.text for x in categories_cultures.find_elements_by_tag_name("option"))

    for culture in cultures:
        # standard format for url 
        culture = culture.lower().replace(" ", "-")
        print(culture)
        # get url link with string 
        txt = "https://www.momjunction.com/baby-names/{culture}/{gender}"
        link = txt.format(culture = culture, gender = gender) 
        
        dict_out[culture] = link  


    """
    # get names of each page
    for culture_key, val in dict_out.items():
        dict_out[culture_key] = get_all_names(val)
        print(dict_out[culture_key]) # debug
   
    """
    return dict_out 


# 3. implementation 

# 4 output
url_male = "https://www.momjunction.com/baby-names/boy/"
url_female = "https://www.momjunction.com/baby-names/girl/"

# execute

#urls = get_all_names("https://www.momjunction.com/baby-names/japanese/girl/")
#print(urls)
#print("names:", len(urls))

dict_female = fill_names_dict(url_female, "girl") #gender: girl - female, boy - male
print(dict)

# end web scrapping
driver.quit()