from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import webdrivermanager


# 1. setup 
# **REMEMBER** remove path to your local folder
driver = webdriver.Chrome("C:/Users/Ahn/AppData/Local/salabs_/WebDriverManager/bin/chromedriver.exe")

# 2. standard procedure for each page

# function to get names per web page 
def get_names_by_category(url):
    names = list()

    driver.get(url)
    categories_alphabet = driver.find_elements_by_class_name("mw-category-group") # div with list of names per letter
    heading = driver.find_element_by_id("firstHeading").text.replace('Category:', '').split()[0]
    names.append(heading) # add heading as first element in list

    for category_letter in categories_alphabet:
        elements = category_letter.find_elements_by_tag_name("a") # get list of web elements inside web element
        attr = (o.text for o in elements) # get text from web element [h3] in list
        names.extend(attr)

    
    return names


def get_urls(url):
    urls = list()

    driver.get(url)
    container = driver.find_element_by_id("mw-subcategories")
    categories = container.find_elements_by_class_name("mw-category-group") # div with list of names per letter

    for category in categories:
        elements = category.find_elements_by_tag_name("a") # get list of web elements inside web element
        attr = (o.get_attribute('href') for o in elements) # get text from web element [h3] in list
        urls.extend(attr)

    
    return urls

def get_all_names(list_URL):
    all_names = dict()

    # save all names in dict organized by category [culture]
    for url in list_URL:
        names = get_names_by_category(url)
        all_names[names[0]] = names[1:] #heading as key, names as values

    return all_names


# 3. implementation 

# get list of urls needed to extract names by subcategories
list_URL_female = get_urls("https://en.wikipedia.org/wiki/Category:Feminine_given_names")
list_URL_male = get_urls("https://en.wikipedia.org/wiki/Category:Masculine_given_names")


# get all names fo each type [male, female]
dict_female = get_all_names(list_URL_female)
dict_male = get_all_names(list_URL_male)

# 4 output
print(dict_female.keys())
print(dict_male.keys())


# end web scrapping
driver.quit()