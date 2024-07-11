import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pync
import beepy
from tkinter import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def notification(message):
    pync.notify(message)
    beepy.beep(sound = 5)


def removePRCNT(string):
    return float(string.replace("%", ""))


def execute_loan_checker(apyThreshold, ltvThreshold, ethThreshold):
    path = "/Users/mgislason/Desktop/chromedriver-mac-arm64/chromedriver"
    # Specify the path to the ChromeDriver
    service = Service(path)

    options = Options()
    options.add_experimental_option("detach", True)
    # disable the message "Chrome being controlled by automated test software"
    options.add_experimental_option("excludeSwitches",["enable-automation"])

    driver = webdriver.Chrome(service=service, options=options)

    collection_links = ["https://blur.io/eth/collection/wrapped-cryptopunks/loans", "https://blur.io/eth/collection/azuki/loans", "https://blur.io/eth/collection/milady/loans", "https://blur.io/eth/collection/degods-eth/loans", "https://blur.io/eth/collection/boredapeyachtclub/loans", "https://blur.io/eth/collection/mutant-ape-yacht-club/loans", "https://blur.io/eth/collection/kanpai-pandas/loans", "https://blur.io/eth/collection/remilio-babies/loans", "https://blur.io/eth/collection/pudgypenguins/loans", "https://blur.io/eth/collection/otherdeed/loans", "https://blur.io/eth/collection/bored-ape-kennel-club/loans", "https://blur.io/eth/collection/clonex/loans", "https://blur.io/eth/collection/beanzofficial/loans", "https://blur.io/eth/collection/azukielementalbeans/loans", "https://blur.io/eth/collection/azukielementals/loans", "https://blur.io/eth/collection/proof-moonbirds/loans", "https://blur.io/eth/collection/lilpudgys/loans"]
    
    #driver.maximize_window()  


    def gatherLoanData():
        nftData = []
        addedNFTnames = []

        for link in collection_links:
            driver.get(link)
            
            # wait until element is clickable then click it
            loans_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[.='All Loans']")))
            loans_button.click()
            time.sleep(.4) #might need to adjust sleep time based on computer speed
            

            # Scroll to the element within the scrollable area
            scrollable_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[3]/div/div[2]/div[1]/div[2]/div/div[2]/div")
            scroll_amount = 500  # Amount of pixels to scroll each time


            status = "AUCTION" #set status to auction for first iteration
            # Only scrolls while the status is AUCTION, to get live loans
            while status == "AUCTION":
                # Scroll down by scroll_amount pixels each time
                
                for loan_row in driver.find_elements(By.XPATH, "//div[@id= 'COLLECTION_MAIN']//div[@role='rowgroup']//div[@role='row']"):
                    nftName = loan_row.find_element(By.XPATH, "div[1]").text
                    status = loan_row.find_element(By.XPATH, "div[2]").text
                    if status == "ACTIVE":
                        break
                    borrowAmount = loan_row.find_element(By.XPATH, "div[3]").text
                    ltv = loan_row.find_element(By.XPATH, "div[4]").text
                    apy = loan_row.find_element(By.XPATH, "div[5]").text # select the 5th column
                    if nftName not in addedNFTnames and ethThreshold > float(borrowAmount) and ltvThreshold > removePRCNT(ltv) and removePRCNT(apy) > apyThreshold:
                        nftData.append([nftName, borrowAmount, ltv, apy]) # could use float(apy[:-1]) to convert to number
                        addedNFTnames.append(nftName)
                if status == "ACTIVE":
                    break
                driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + {};'.format(scroll_amount), scrollable_element)
                time.sleep(.05)  # Delay, might need to be increased based on load speed

 
    
        print(nftData)
    gatherLoanData()
    driver.close()
    notification("message")
   




