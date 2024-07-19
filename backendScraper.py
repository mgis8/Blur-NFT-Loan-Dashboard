import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from tkinter import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

global nftData

chromedriver_autoinstaller.install()

#formatting for apy and ltv values
def removePRCNT(string):
    return float(string.replace("%", ""))

nftData = []
#sets driver, paths, and links
#returns nftData which is an array of arrays 
#each array containing [nftname, amountOfEthToBorrow, ltv, and apy] of each open loan
def execute_loan_checker(apyThreshold, ltvThreshold, ethThreshold):
    global nftData
    del nftData[:] #erases all previous data for next iteration to prevent array growing

    #setting path to chrome driver
    #path = "Blur-NFT-Loan-Scraper/index.html"
    #service = Service(path)

    #Adding options to chrome driver
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

    #Links to all blur collections that support loans
    collection_links = ["https://blur.io/eth/collection/wrapped-cryptopunks/loans", "https://blur.io/eth/collection/azuki/loans", "https://blur.io/eth/collection/milady/loans", "https://blur.io/eth/collection/degods-eth/loans", "https://blur.io/eth/collection/boredapeyachtclub/loans", "https://blur.io/eth/collection/mutant-ape-yacht-club/loans", "https://blur.io/eth/collection/kanpai-pandas/loans", "https://blur.io/eth/collection/remilio-babies/loans", "https://blur.io/eth/collection/pudgypenguins/loans", "https://blur.io/eth/collection/otherdeed/loans", "https://blur.io/eth/collection/bored-ape-kennel-club/loans", "https://blur.io/eth/collection/clonex/loans", "https://blur.io/eth/collection/beanzofficial/loans", "https://blur.io/eth/collection/azukielementalbeans/loans", "https://blur.io/eth/collection/azukielementals/loans", "https://blur.io/eth/collection/proof-moonbirds/loans", "https://blur.io/eth/collection/lilpudgys/loans"] 
    
    #contains main loop that iterates through the individual nft pages and extracts data on open loans
    def gatherLoanData():
        addedNFTnames = [] #array to check that loans aren't displayed twice

        for link in collection_links:
            #opens specific nft loan page
            driver.get(link)
            
            #waiting until loan page element is clickable then click it
            loans_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[.='All Loans']")))
            loans_button.click()

            status = "AUCTION" #set status to auction for first iteration
            while status == "AUCTION":
                #finds all auction loans on page and stores apy, ltv, name, eth amount
                for loan_row in driver.find_elements(By.XPATH, "//div[@id= 'COLLECTION_MAIN']//div[@role='rowgroup']//div[@role='row']"):
                    nftName = loan_row.find_element(By.XPATH, "div[1]").text #get nft title
                    status = loan_row.find_element(By.XPATH, "div[2]").text #get auction/active status to filter
                    if status == "ACTIVE":
                        break
                    borrowAmount = loan_row.find_element(By.XPATH, "div[3]").text # get borrow amount
                    ltv = loan_row.find_element(By.XPATH, "div[4]").text # get the ltv value
                    apy = loan_row.find_element(By.XPATH, "div[5]").text # get the apy value
                    if nftName not in addedNFTnames and ethThreshold > float(borrowAmount) and ltvThreshold > removePRCNT(ltv) and removePRCNT(apy) > apyThreshold:
                        nftData.append([nftName, borrowAmount, ltv, apy]) 
                        addedNFTnames.append(nftName) #add to list of nfts, to check that it hasnt been added again
                
                #scrolls to load items if there are more than 20 or so auction loans
                scrollable_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "rows")))
                scroll_amount = 500  # Amount of pixels to scroll each time
                driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + {};'.format(scroll_amount), scrollable_element)
                time.sleep(.05)  # Delay between scroll and script running again, might need to be increased based on load speed

    
    gatherLoanData()
    driver.close() #closes window when finished with script
    #print(nftData) #for testing
    return nftData

#execute_loan_checker(0,999,999) #CALLS SCRIPT WITH NO FILTERING OPTIONS FOR TESTING
    


   






   




