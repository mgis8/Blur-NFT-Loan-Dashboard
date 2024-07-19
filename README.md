# Blur NFT Loan Scraper Dashboard
## Write Up
This project utilizes Blur.io's ethereum lending protocol: Blend (ie Blur Lending). Specifically, Blend allows Blur marketplace users to borrow ethereum with their NFTs as collateral. Of course, loans come with varying yearly yield and risk for the loaners. The risk is tied to the amount lended compared to the NFT collateral's value or loan-to-value ratio(LTV). Due to the high volatility of the NFT market, there is opprotunity to lend ethereum at extremely high rates to NFT owners (Often at rates over 100% yearly yield). There is certainly opprotunity for entering highly profitable loans on this platform, while maintaining tolerable risk. 

Loans are offered to loaners as 'auctions', which start at 0% yield and over the course of 24hrs increase until they reach a maximum of 1000% yearly yield. During this 24hr auction phase, loaners at any time may take up the loan offer and start accruing interest. At any time the lender may initiate an exit of the loan, and at that time the loan goes back on auction for the same 24hr process. If the loan is not picked up by another lender, or repaid by the NFT owner, the loan is defaulted and the lender recieves the NFT as collateral. Of course, the risk is that the volatility in the NFT market will invert the loan-to-value ratio before the auction expires; which leaves you with an NFT worth less than the ETH you were lending. 

My program aims to streamline the acquisition of valuable loans on auction that are within the users risk tolerance. Specifically my program reoccuringly gathers data from all loans on auction (adding the data to a database) and allows the user to specify the minimum yearly yield they are looking for, the max loan-to-value ratio they can tolerate, and the most ethereum they are willing to lend. This prevent lenders from having to actively check each collection's loan page and sorting through all loan auctions to find a loan that matches their requirements. 

Instead my program displays all loans on auction that meets their risk and profit thresholds in the same place so they can enter the most market profitable loan within their risk tolerance, without having to reoccuringly manually check each nft collection's loan page. This both saves time for lenders who need to reoccuringly check loans and makes sure lenders have access to all desirable loan data at their fingertips, so they can make the most profitable and risk tolerant decisions. 


## Short Video Demo
https://github.com/user-attachments/assets/7736c57e-1aa9-400b-9938-47cd77b65d07
