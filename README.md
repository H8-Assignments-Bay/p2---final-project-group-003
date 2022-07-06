[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8070902&assignment_repo_type=AssignmentRepo)

# Final Project Batch 11 - FintBot - (Fintech Chat Bot)

This Final Project is the project created by a group who participates in Hacktiv8 Full Time Data Science Program. Final Project point itself is for the students to establish their skill and knowledge in their studies.  

## About

Peer-to-Peer lending or P2P lending permits people and organizations to acquire and loan cash to one another. It works by coordinating lenders with banks through internet based stages or offline brokers. Using this situation, we make a ChatBot for easier ways for the lenders to invest their money. Our Chat bot uses Indonesian Language in this demo.

![image](https://user-images.githubusercontent.com/103393514/177360638-46617789-6fb4-4097-a52f-99b1557efe72.png)

Fintbot is our chatbot name that serves to help lenders to fund a project. Fintbot assists lenders with doing project financing activities easily and quickly, such as checking balances, funding projects, and withdraw funds.

### Deployment on Telegram

![image](https://user-images.githubusercontent.com/69398229/177471098-a3dfd627-dda6-40e7-9ff3-7cac6e320ff5.png)

## Installation

Installed files could reach ~7GB on local disk mainly in env folder. 

### Environment Setup

Use conda environtment stored in the environment.yml file, run on anaconda terminal:

`conda env create -p ./env -f ./environment.yml`

### Run the latest rasa model
Start action endpoint. This is where actions are stored (class and functions):

`rasa run actions`

On a different terminal / command prompt / anaconda prompt run:

`rasa shell`

### Train model

To train new model after updating data and/or actions folder simply run

`rasa train`

## Features

1. initialization (Hi, Hello, etc)
2. Account Balance
3. Withdrawal with account balance reduction
4. Investment with personal account balance reduction and investment account balance update

### Rasa Open Source 

Huge Thanks to Rasa Open Source <p><a href="https://github.com/RasaHQ/rasa">link here</a></p>

Using rasa open source for creating our chatbot. Rasa is an open source machine learning framework for creating AI assistance and also chatbots. Rasa assists you construct logical assistance fit for having layered conversation with heaps of back-and-forth. For a human to have a significant trade with a context oriented assistance. 

# The Group 3 Team
1. Nikki Satmaka
2. M. Nurfaldi Rosal
3. Annesa Fadhila Damayanti
