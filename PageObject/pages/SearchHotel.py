from selenium.webdriver.common.by import By

from PageObject.pages import Locators

class SearchHotel:
    def __init__(self,driver):
        self.location = driver.find_element(By.XPATH,Locators.dd_location_xpath)
        self.hotels = driver.find_element(By.XPATH,Locators.dd_hotels_xpath)
        self.room_type = driver.find_element(By.XPATH,Locators.dd_room_type_xpath)
        self.no_of_rooms = driver.find_element(By.XPATH, Locators.dd_no_of_rooms_xpath)
        self.adults_per_room = driver.find_element(By.XPATH, Locators.dd_adults_per_room_xpath)
        self.children_per_room = driver.find_element(By.XPATH, Locators.dd_children_per_room_xpath)
        self.btn_search = driver.find_element(By.XPATH, Locators.btn_search_xpath)

    #getters
    def getLocation(self):
        return self.location
    def getHotels(self):
        return self.hotels
    def getRoomType(self):
        return self.room_type
    def getNoOfRooms(self):
        return  self.no_of_rooms
    def getAdultsPerRoom(self):
        return self.adults_per_room
    def getChildPerRoom(self):
        return self.children_per_room
    def getBtnSearch(self):
        return self.btn_search


