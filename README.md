# Blur NFT Loan Scraper Dashboard
### Write Up
This project utilizes Blur.io's Ethereum lending protocol: Blend (i.e., Blur Lending). Specifically, Blend allows Blur marketplace users to borrow Ethereum with their NFTs as collateral. Of course, loans come with varying yearly yields and risks for the lenders. The risk is tied to the amount lent compared to the NFT collateral's value, or loan-to-value ratio (LTV). Due to the high volatility of the NFT market, there is an opportunity to lend Ethereum at extremely high rates to NFT owners (often at rates over 100% yearly yield). There is certainly opportunity for entering highly profitable loans on this platform while maintaining tolerable risk.

Loans are offered to lenders as 'auctions,' which start at 0% yield and over the course of 24 hours increase until they reach a maximum of 1000% yearly yield. During this 24-hour auction phase, lenders may take up the loan offer at any time and start accruing interest. At any time, the lender may initiate an exit of the loan, and at that time, the loan goes back on auction for the same 24-hour process. If the loan is not picked up by another lender or repaid by the NFT owner, the loan is defaulted, and the lender receives the NFT as collateral. Of course, the risk is that the volatility in the NFT market will invert the loan-to-value ratio before the auction expires, which leaves you with an NFT worth less than the ETH you were lending.

My program aims to streamline the acquisition of valuable loans on auction that are within the user's risk tolerance. Specifically, my program recurringly gathers data from all loans on auction (adding the data to a database) and allows the user to specify the minimum yearly yield they are looking for, the maximum loan-to-value ratio they can tolerate, and the most Ethereum they are willing to lend. This prevents lenders from having to actively check each collection's loan page and sort through all loan auctions to find a loan that matches their requirements.

Instead, my program displays all loans on auction that meet their risk and profit thresholds in the same place so they can enter the most market-profitable loan within their risk tolerance, without having to recurringly manually check each NFT collection's loan page. This both saves time for lenders who need to recurringly check loans and ensures lenders have access to all desirable loan data at their fingertips, so they can make the most profitable and risk-tolerant decisions. 

### Short Demo Video
https://github.com/user-attachments/assets/7736c57e-1aa9-400b-9938-47cd77b65d07

### Installation/Running Project
> Install machine compatible chromedriver :
https://developer.chrome.com/docs/chromedriver/downloads

> Install python :
https://www.python.org/downloads/

> Install python requirements :
https://github.com/mgis8/Blur-NFT-Loan-Dashboard/blob/main/requirements.txt

> Organize project folder :
  
&emsp;appfolder/

  &emsp;&emsp;|── backendScraper.py

  &emsp;&emsp;|── app.py
  
  &emsp;&emsp;|── templates/
  
  &emsp;&emsp;&emsp;└── index.html

> Change path var in backendScraper.py to your path to chromedriver


