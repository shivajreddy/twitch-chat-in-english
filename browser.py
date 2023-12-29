from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
# chrome_options.add_argument('headless')  # the browser is hidden
chrome_options.add_experimental_option('detach', True)  # always open


# + Set up the Chrome WebDriver (you may need to adjust the path)
# browser = webdriver.Chrome()
browser = webdriver.Chrome(options=chrome_options)
browser.get("https://www.google.com/search?q=russian+to+englinsh&oq=russia&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDkyBggCEEUYOzIGCAMQRRg9MgYIBBBFGD0yBggFEEUYPdIBCDM3OTNqMGoxqAIAsAIA&sourceid=chrome&ie=UTF-8")

print('Browser::GoogleTranslate::Opened ✅')


def translate_text_2(input_text):
    try:
        # + Open Google Translate
        browser.get(
            "https://translate.google.com/?hl=en&sl=ru&tl=en&op=translate")

        # + Find the input text box and enter the text
        input_box = browser.find_element(By.CLASS_NAME, "er8xn")
        input_box.clear()
        input_box.send_keys(input_text)

        # time.sleep(5)

        # + Find the output span element that has the converted text
        output_box = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ryNqvb')))

        result = None

        # + Wait for the translation to be generated (Initial state:Translation, During: Translating...)
        while True:
            translate_text = output_box.text
            if translate_text != "Translation" or translate_text != "Translating...":
                result = translate_text
                break

        return result

    except Exception as e:
        e
        # print(f"Error: ", e)

    # finally:
    #     browser.quit() # Close the browser window


def translate_text(input_text):

    try:
        # + Open Google Translate
        # browser.get("https://www.google.com/search?q=russian+to+englinsh&oq=russia&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDkyBggCEEUYOzIGCAMQRRg9MgYIBBBFGD0yBggFEEUYPdIBCDM3OTNqMGoxqAIAsAIA&sourceid=chrome&ie=UTF-8")

        # + Find the input text box and enter the text
        input_box = browser.find_element(By.ID, 'tw-source-text-ta')
        # input_box = WebDriverWait(browser, 3).until( EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[jsname="BJE2fc"]')))
        input_box.clear()
        input_box.send_keys(input_text)

        time.sleep(5)

        # Wait for the translation to be generated
        output_box = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'tw-target-text')))

        translated_text = output_box.text

        return translated_text

    except Exception as e:
        print(f"Error: ", e)

    # finally:
    #     browser.quit() # Close the browser window


# # Example usage
# input_text = "Привет, как дела"
# output_text = translate_text(input_text)
# output_text = translate_text_2(input_text)
# print(f"Input Text: {input_text}")
# print(f"Translated Text: {output_text}")
