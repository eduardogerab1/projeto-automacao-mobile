from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import log
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException

class BaseMethods:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))
    
    def find_elements(self, by, locator):
        return self.wait.until(EC.presence_of_all_elements_located((by, locator)))
    
    def clear_field(self, by, locator):
        log.info(f"Limpando campo com locator: {locator}")
        try:
            element = self.wait_for_visibility_of_element(by, locator)
            if element:
                element.clear()
                log.info("Campo limpo com sucesso.")
            else:
                log.warning(f"Não foi possível limpar o campo: elemento {locator} não encontrado.")

        except StaleElementReferenceException:
            log.warning(f"O elemento {locator} ficou 'stale'. Tentando novamente...")

    def is_enabled(self, by, locator):
        try:
            return self.find_element(by, locator).is_enabled()
        except:
            return False
    
    def wait_for_element_to_be_clickable(self, by, locator):
        return self.wait.until(EC.element_to_be_clickable((by, locator)))

    def click_element(self, by, locator):
        log.info(f"Clicking element with locator: {locator}")
        try:
            self.wait_for_element_to_be_clickable(by, locator).click()
            log.info("Element clicked successfully.")
        except Exception as e:
            log.error(f"Failed to click element with locator: {locator}", exc_info=True)
            raise

    def send_keys_to_element(self, by, locator, text):
        self.find_element(by, locator).send_keys(text)

    def get_element_text(self, by, locator):
        return self.find_element(by, locator).text
    
    def get_elements_text(self, by, locator):
        try:
            elements = self.find_elements(by, locator)
            texts = [el.text for el in elements if el.text.strip() != ""]
            log.info(f"Textos capturados de {locator}: {texts}")
            return texts
        except Exception as e:
            log.error(
                f"Falha ao capturar textos dos elementos com locator: {locator}", 
                exc_info=True
            )
            return []
    
    def wait_for_visibility_of_element(self, by, locator, timeout=10):
        """Espera até que o elemento esteja visível na tela."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located((by, locator)))
            log.info(f"Elemento visível: {locator}")
            return element
        except TimeoutException:
            log.error(f"Elemento não ficou visível dentro de {timeout} segundos: {locator}")
            return None
        except StaleElementReferenceException:
            log.error("o elemento foi localizado antes, mas agora não pode mais ser acessado.")
            return None
        except NoSuchElementException:
            log.error("O elemento sendo requisitado não existe na tela.")
            return None

        

