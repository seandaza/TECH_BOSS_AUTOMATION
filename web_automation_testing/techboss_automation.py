import re
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



class TestAutomation(unittest.TestCase):

    def setUp(self):
        #Inicializando Chrome
        opts = Options()
        opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/95.0.4638.54 Safari/537.36")
        self.driver = webdriver.Chrome('web_automation_testing\chromedriver.exe', chrome_options=opts) 
        self.driver.maximize_window()
        #Identificando el url de la pagina 
        url = "https://techboss.com.co/"
        #Abriendo la pagina
        self.driver.get(url)
        time.sleep(1)

    """ CU1: Ingresando a la url, accediendo a los productos
    y sus respectivas soluciones """
    def test_automation_CU1(self):
        for i in range(1,4):
            products_buttom = self.driver.find_elements_by_xpath('//a[@class="et_pb_button et_pb_promo_button"]')
            time.sleep(1)
            products_buttom[i].click()
            time.sleep(2)
            self.driver.back()
            time.sleep(2)


    """ CU2: Navegando a la seccion de Contacto
    y realizando el registro """
    def test_automation_CU2(self):
        contact_buttom = self.driver.find_element_by_xpath('//*[@id="menu-item-47"]/a')
        contact_buttom.click()
        time.sleep(2)



        operation = self.driver.find_element_by_xpath('//span[@class="et_pb_contact_captcha_question"]').get_attribute('innerHTML')
        print(operation)
        list = re.findall(r'\d+', operation)
        solution = int(list[0]) + int(list[1])
        print(solution)
        time.sleep(3)

        payload={
            "Nombre": "Jhean",
            "Email": "seandaza@gmail.com",
            "Mensaje": "Mensaje Automatizado!...",
            "solution": solution,
        }

        box_name = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/article/div/div/div/div/div/div/div[2]/div/div[2]/form/p[1]/input')
        box_name.send_keys(payload['Nombre'])

        box_email = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/article/div/div/div/div/div/div/div[2]/div/div[2]/form/p[2]/input')
        box_email.send_keys(payload['Email'])
        time.sleep(2)

        box_message = self.driver.find_element_by_xpath('//*[@id="et_pb_contact_form_0"]/div[2]/form/p[3]/textarea')
        box_message.send_keys(payload['Mensaje'])
        time.sleep(2)

        box_solution = self.driver.find_element_by_xpath('//*[@id="et_pb_contact_form_0"]/div[2]/form/div/div/p/input')
        box_solution.send_keys(payload['solution'])
        time.sleep(2)

        submit_buttom = self.driver.find_element_by_xpath('//*[@id="et_pb_contact_form_0"]/div[2]/form/div/button').click()
        time.sleep(2)

    """ CU3: Realizando cualquier busqueda 
    sobre la pagina """
    def test_automation_CU3(self):
        #Clickando sobrel icono de busqueda
        time.sleep(1)
        actionChains = ActionChains(self.driver)
        xOffset = 1308
        yOffset = 100
        # Realiza la acción move hacia la posición del desplazamiento
        webdriver.ActionChains(self.driver).move_by_offset(xOffset,yOffset).click().perform()
        time.sleep(1)

        search_input = self.driver.find_element_by_xpath('//*[@id="main-header"]/div[2]/div/form/input')
        search_input.send_keys('Seguridad')
        search_input.send_keys(Keys.ENTER)

        body = self.driver.find_element_by_tag_name('body').get_attribute('outerHTML')
        criterio = str(re.findall(r'search-results', body))
        print(criterio)

        self.assertIn('search-results',criterio, 'No se encontraron resultados en la pagina')
        
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()