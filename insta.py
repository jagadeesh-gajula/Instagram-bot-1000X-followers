from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
from random import sample
import winsound
import selenium
from instabot import Bot 
import os
import random

user = 'Your username'
passcode = 'Your password'


hashtag_list = ['datacenter','jokes','nature','memes','programmingjokes','meme',
                'admin','server','data','firefox','apple','dell',
                'ibm','software','automation','coding','hacking',
                'python','javascript','cplusplus','computerscience','computersetup',
                 'computersecurity', 'computersciencememes',
                 'machinelearningalgorithms', 'machinelearningtools' ,
                 'machinelearningengineer' ,'machinelearningmaster','machinelearningapplied',
                 'gamingmemes' ,'gaminglife', 'gamingcommunity', 'gamingsetup', 'gamingaccessories',
                 'memesdaily','memestagram','memelife','andrewng','coursera','gpu','amd','intel','gtx',
                 'rtx','india','memelover','cuda'
                 ]
# edit hastags you like 

def new_post():
    try:
        cur = os.getcwd()
        cur = cur + '\\posts'
        posts = os.listdir(cur)
        random_post = random.sample(posts,1)[0]
        post = cur + "\\" + random_post
        print(post)
        return post
    except:
        print('no image found to post')
        return None

cur_post = new_post()

def post_now(cur_post,username,password):
    try:
        bot = Bot() 
        bot.login(username = username, password =password) 
        bot.upload_photo(cur_post,  caption = "Put your caption here..!") 
        print('sucessfully posted a picture')
    except:
        print('post unsuccessfull..!')

post_now(cur_post,user,passcode) # comment this if you don't want to post image


# login sequence 

from selenium import webdriver
chromedriver_path = 'chromedriver.exe' 
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys(user)
password = webdriver.find_element_by_name('password')
password.send_keys(passcode)



button_login = webdriver.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div")
button_login.click()
sleep(3)

notnow = webdriver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
notnow.click() 

notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click()




''' 
it loops over hastags and clicks on first image and
it likes images and follows random people and posts comments before moves to new picture.
'''
for hashtag in hashtag_list:
        def restart():
                hashtag = sample(hashtag_list,1)[0]
                webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag + '/')
                sleep(3)
                first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
                first_thumbnail.click()
                sleep(randint(1,2))  


                for i in range(1,100):
                        sleep(2)

                        if i % 3 == 0: # follows profile of  every 3rd post 
                                try:
                                        sleep(1)
                                        follow = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text
                                        if follow == 'Follow':
                                                webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                                
                                except selenium.common.exceptions.NoSuchElementException:
                                        print('exception occured at following')
                                        restart()

                        try: # this code likes pictures
                                sleep(1)
                                like = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
                                like.click()

                                comments = ['great picture..!','nice picture','love your content','great work','Always support your content',
                                                        'nice content','love your posts','nice posts','superb..','great work','love your account']

                                    # put your own comments here..!                    
                                one_comment = sample(comments,1)[0]

                        except selenium.common.exceptions.NoSuchElementException:
                                print('exception occured at like button ')
                                restart()

                        

                        if i % 50 == 0: # comments on after every 50 images it visits
                                try:
                                        sleep(1)
                                        webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click()
                                        comment_box = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
                                        comment_box.send_keys(one_comment)
                                        comment_box.send_keys(Keys.ENTER)
                                        
                                        
                                except selenium.common.exceptions.NoSuchElementException:
                                        print('exception occured while commenting ')
                                        restart()
                        try:
                                sleep(1)
                                webdriver.find_element_by_link_text('Next').click()

                        except selenium.common.exceptions.NoSuchElementException:
                                print('exception occured while clicking next button')
                                restart()
        restart()
        


        


