<!-- [![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8070902&assignment_repo_type=AssignmentRepo) -->

<div align="center">

# Fintbot - (Fintech Chat Bot)

[Introduction](#introduction) • [Installation](#installation) • [Screenshots](#demonstration-on-telegram) • [Contributors](#contributors)

![GitHub repo size](https://img.shields.io/github/repo-size/H8-Assignments-Bay/p2---final-project-group-003)
![GitHub last commit](https://img.shields.io/github/last-commit/H8-Assignments-Bay/p2---final-project-group-003)
![GitHub contributors](https://img.shields.io/github/contributors/H8-Assignments-Bay/p2---final-project-group-003)
![GitHub top language](https://img.shields.io/github/languages/top/H8-Assignments-Bay/p2---final-project-group-003)

This project is created as a collaboration by a group of students in Hacktiv8 Full Time Data Science Program.

![logo 16x9](https://user-images.githubusercontent.com/69398229/177583344-779813fd-056d-425a-b104-0daff8fd96e4.png)
</div>

---

### Table of Contents
- [Fintbot - (Fintech Chat Bot)](#fintbot---fintech-chat-bot)
    - [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
    - [Demonstration on telegram](#demonstration-on-telegram)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Environment Setup](#environment-setup)
- [Running on Your Local Machine](#running-on-your-local-machine)
- [Features](#features)
- [Using your own data](#using-your-own-data)
- [Roadmap](#roadmap)
- [Rasa Open Source](#rasa-open-source)
- [Contributors](#contributors)

# Introduction

Peer-to-Peer lending, or P2P lending for short, permits people and organizations to acquire and loan out cash to one another. It works by coordinating lenders with borrowers through internet based stages or offline brokers.

We also noticed that mobile phone usage has skyrocketed in recent years, accompanied by the usage of chatting applications.

Looking at the situation, we created a ChatBot so that lenders could easily fund and invest their money in a P2P Lending platform, without having to leave their beloved messaging applications.

Since they're already used to how their messaging applications work, they would feel comfortable using the app, which would reduce the need of familiarizing with a new application.

In this project, we created our Chat bot to use Indonesian Language, however this could be adjusted to other languages.

Fintbot is the name of our chatbot name that functions to help lenders in a P2P Lending company. Fintbot assists lenders with funding related activities easily and quickly, such as check balances, fund projects, and withdraw funds.

<div align="center">

### Demonstration on telegram

![Fintbot-Demo2](https://user-images.githubusercontent.com/69398229/177583069-f7bbfd85-ab93-438e-9e04-1d972e8e80d6.gif)
</div>

# Prerequisites
- [Anaconda](https://www.anaconda.com/products/distribution) (or [Miniconda](https://docs.conda.io/en/latest/miniconda.html))
- [GIt](https://git-scm.com/downloads)
# Installation

To run this chatbot on your own machine, first clone the repository and navigate to it:
```
git clone https://github.com/H8-Assignments-Bay/p2---final-project-group-003.git fintbot
cd fintbot
```
Installed files could reach ~3GB on local storage because of the hefty environment needed

## Environment Setup

Next, run the following command to create a `conda` virtual environment that contains all the libraries needed to run the chatbot:\
*For windows user, you might need to use `Anaconda Prompt`

```
conda env create -n fintbot -f ./environment.yml
```

# Running on Your Local Machine

Activate conda environment, using this command:
```
conda activate fintbot
```

Run the following command to run Fintbot on your terminal:
```
rasa run actions &>/dev/null &
rasa shell
```

Or you can also set it up to run on your favorite messaging application, like we did on Telegram.

# Features

These are the things you can do with Fintbot:
1. Initialization (Hi, Hello, etc)
2. Account Balance
3. Withdrawal with account balance reduction
4. Investment with personal account balance reduction and investment account balance update
5. Ask Fintbot for help to remind you of the features

# Using your own data

You can create a new model based on Fintbot using your own data. Simply edit the dataset in the `data` directory. Refer to [Rasa Documentation](https://rasa.com/docs/rasa/) for more details. Afterwards, you can create a new model by running the following code:

```
rasa train
```

# Roadmap

This chatbot is still in development, so we are working on adding more features and improving the performance of the chatbot. Such as:
- Adding a portfolio feature so users can track which projects they have invested in
- Using RDBMS to store the database, instead of using Rasa's slot system

# Rasa Open Source 

Huge Thanks to [Rasa Open Source](https://github.com/RasaHQ/rasa)

We used rasa open source to create our chatbot. Rasa is an open source machine learning framework for creating AI assistance and also chatbots. Rasa assists you construct logical assistance fit for having layered conversation with heaps of back-and-forth. For a human to have a significant trade with a context oriented assistance. 

# Contributors

This project is created as a collaboration project between:
1. [Annesa Fadhila Damayanti](https://github.com/Nurfaldi)
2. [M. Nurfaldi Rosal](https://github.com/nesafadhila)
3. [Nikki Satmaka](https://github.com/NikkiSatmaka)
