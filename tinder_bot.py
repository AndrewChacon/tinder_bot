from selenium import webdriver
from time import sleep

likeButtonPath = '//*[@id="q-1636318104"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button'
dislikeButtonPath = '//*[@id="q-1636318104"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button'
popupButtonPath = '//*[@id="q930268116"]/div/div/div[2]/button[2]'
superLikeButtonPath = '//*[@id="q930268116"]/div/div/button[2]'


class TinderBot():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

    def like(self):
        like_btn = self.driver.find_element_by_xpath(likeButtonPath)
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(dislikeButtonPath)
        dislike_btn.click()

    def auto_swipe(self):
        from random import random
        while True:
            sleep(1)
            try:
                rand = random()
                print('random number', rand)
                if rand < .75:
                    self.like()
                else:
                    self.dislike()
            except Exception:
                self.closeSuperLike()

    def closeSuperLike(self):
        match_popup = self.driver.find_element_by_xpath(superLikeButtonPath)
        match_popup.click()

    # def closePopup(self):
    #     popup = self.driver.find_element_by_xpath(popupButtonPath)
    #     popup.click()


bot = TinderBot()
bot.login()
