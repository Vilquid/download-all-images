import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os



def get_images(url):
    connection = {'very_good': 0.05, 'good': 0.1, 'bad': 0.5, 'very_bad': 1}
    
    folder_name = url.split("/")[-1].split("%")[-1].split(":")[-1]
    print(f"Folder name: {folder_name}")
    
    driver = webdriver.Firefox()
    driver.set_page_load_timeout(20)
    
    driver.get(url)
    
    # get height of the page
    total_height = driver.execute_script("return document.body.scrollHeight")
    
    # scroll the page to load all the images
    for i in range(0, total_height, 50):
        driver.execute_script("window.scrollTo(0, " + str(i) + ");")
        time.sleep(connection['good'])
    
    # remove the content of the folder
    for file in os.listdir(folder_name):
        os.remove(os.path.join(folder_name, file))

    # remove the folder if it exists
    if os.path.exists(folder_name):
        os.rmdir(folder_name)

    # create img, a folder, to save the images
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # get the images
    images = driver.find_elements(By.TAG_NAME, 'img')
    number_images = 0
    for image in images:
        print(f"Download of {image.get_property('src')}")
        # download the image and save it in img folder
        if image.get_property('src') != '':
            img_data = requests.get(image.get_property('src')).content
            with open(f'{folder_name}/' + str(number_images) + '.jpg', 'wb') as handler:
                handler.write(img_data)
        number_images += 1
    
    print(f"Downloaded {number_images} images")
    
    driver.close()


def main():
    urls = ['https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal', 'https://fr.wikipedia.org/wiki/Wikip%C3%A9dia']
    
    for url in urls:
        get_images(url)


if __name__ == '__main__':
    main()

