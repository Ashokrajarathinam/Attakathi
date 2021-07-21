from libglobal.LibGlobal import Base
from PageObject.pages.LoginPage import LoginPage
from PageObject.pages.SearchHotel import SearchHotel
from PageObject.pages.SelectHotel import SelectHotel
from PageObject.pages.BookHotel import BookHotel
from PageObject.pages.BookingConfiramation import BookingConfirm
import pytest


class TestBowserLaunch(Base):
    @pytest.fixture()
    def setup(self):

        self.driver = self.launch_browser()
        self.window_maximize()
        self.load_url("http://adactin.com/HotelApp/")
        yield
        self.browser_quit()

    def test_login(self,setup):

        x = LoginPage(self.driver)
        self.send_txt(x.getTxtUserName(), "ashokraja")
        self.send_txt(x.getTxtPassword(), "attakathi")
        self.btn_click(x.getBtnLogin())
        y = SearchHotel(self.driver)
        self.dd_by_value(y.getLocation(), "Los Angeles")
        self.dd_by_value(y.getHotels(), "Hotel Sunshine")
        self.dd_by_value(y.getRoomType(), "Double")
        self.btn_click(y.getBtnSearch())
        z = SelectHotel(self.driver)
        self.btn_click(z.getBtnSelectHotel())
        self.btn_click(z.getBtnContinue())
        a = BookHotel(self.driver)
        self.send_txt(a.getFirstName(),"ashok")
        self.send_txt(a.getLastName(),"raja")
        self.send_txt(a.getAddress(),"los angles")
        self.send_txt(a.getCreditCardNo(),"1234569874562356")
        self.dd_by_value(a.getCreditCardType(),"VISA")
        self.dd_by_visible_txt(a.getSelectMonth(),"September")
        self.dd_by_visible_txt(a.getSelectYear(),"2022")
        self.send_txt(a.getCcvNo(),"241")
        self.btn_click(a.getBtnBook())
        self.driver.implicitly_wait(10)
        o = BookingConfirm(self.driver)
        v = self.attribute_value(o.getOrderId(),'value')
        print(v)
        self.driver.implicitly_wait(10)










