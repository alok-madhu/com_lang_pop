from selenium import webdriver

my_list = ['c', 'php', 'python', 'c++', 'c#']

if __name__ == "__main__":
    for search in my_list:
        driver = webdriver.Chrome()
        driver.get("https://www.quora.com/topic/" + search)
        elem = driver.find_element_by_class_name("TopicQuestionsStatsRow").find_element_by_tag_name("strong")

        print("Total number of questions: " + elem.text)
        driver.quit()
