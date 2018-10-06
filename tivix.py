#!/usr/bin/python
# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver
from time import sleep

valid_name="Karolina"
valid_surname="Kowalska"
valid_number="48999999999"
invalid_email="karolina.wsb.pl"
valid_pass="karo12LINA"

#tworze klase WsbPlCheck
#dziedziczaca po klasie TestCase z modulu unittest

class WsbWizzAirCheck(unittest.TestCase):
    def setUp(self): #metoda (zaczynajaca) nie funkcja, bo self
        self.driver=webdriver.Chrome()
        self.driver.get("https://wizzair.com/pl-pl/#/")
    def tearDown(self): #metoda - zakonczenie
        self.driver.quit()
        #pass #pomija, przechodzimy dalej

    def test_invalid_email(self):
        driver=self.driver
        zaloguj_btn=driver.find_element_by_xpath('//*[@id="app"]/header/div[1]/div/nav/ul/li[7]/button')
        zaloguj_btn.click()
        driver=self.driver
        zarejestruj_btn=driver.find_element_by_xpath('//*[@id="login-modal"]/form/div/p/button')
        zarejestruj_btn.click()
        imie_field=driver.find_element_by_xpath('//input[@placeholder="Imię"]')
        imie_field.click()
        imie_field.send_keys(valid_name)
        nazwisko_field=driver.find_element_by_xpath('//input[@placeholder="Nazwisko"]')
        nazwisko_field.click()
        nazwisko_field.send_keys(valid_surname)
        kobieta_btn=driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-2"]/div[1]/label[1]/span')
        kobieta_btn.click()
        #mezczyzna_btn=driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-2"]/div[1]/label[2]/span')
        #mezczyzna_btn.click()
        #sleep(3)
        #kobieta_btn=driver.find_element_by_xpath('//label[@for="register-gender-female"]')
        #kobieta_btn.click()
        #sleep(3)
        telefon_field=driver.find_element_by_xpath('//input[@placeholder="Telefon komórkowy"]')
        telefon_field.click()
        telefon_field.send_keys(valid_number)
        email_field=driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
        email_field.click()
        email_field.send_keys(invalid_email)
        pass_field=driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
        pass_field.click()
        pass_field.send_keys(valid_pass)
        country_field=driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
        country_field.click()
        poland=driver.find_element_by_xpath(
        '//div[@class="register-form__country-container__locations"]/label[164]')
        poland.location_once_scrolled_into_view
        poland.click()
        check_box1=driver.find_element_by_xpath(
        '//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]')
        check_box1.click()
        error_notice=driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-4"]/div[2]/span')
        #print(error_notice.text)
        assert error_notice.is_displayed()
        self.assertEqual(u"Nieprawidłowy adres e-mail", error_notice.text)
        sleep(2)


if __name__=="__main__":
    unittest.main(verbosity=2) #verbosity 3 poziomy 0,1 i 2 - pokazuje najwiecej informacji przy 2
