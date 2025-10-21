# BANK APP PROJECT

## Introduction
This is a mini project to create a bank like app.
The objective is to improve my Python abilities as well as to practice OOP and Encryption

## Requirements
It can register a new user that can
* Register account
    - Name
    - Age
    - Account number
    - PIN
    - Initial ammount
* Enter the account using the account number and PIN
* Deposit
    - There is no limit in the deposit ammount, however, deposit a big ammount of money can trigger an alarm
* Withdrawals
    - The user can't withdrawals more money tahn his account has
    - The max ammount per withdrawal is 9,000K
* Transfer
    - Add associated account (the account should exist)
    - Transfer to associated account
        - Can't transfer more than the current money in the account
    - All transfers need to have a concept
        - If no concept is assigned the system will generate a generic concept with a random 6 digit number suffix
* Monitor account
    - The user can check the account balance
    - The user can check the last 10 transactions in his account
* Exit account

As extra requirements
* The system will save all the user status in a txt file
* The system will encrypt the txt file
* The system can retrieve the information of the txt file when open a new session
