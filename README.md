# bearrobotics_assignment

## Implement a simple ATM controller

Write code for a simple ATM. It doesn't need any UI (either graphical or console), but a controller should be implemented and tested.

### Requirements

At least the following flow should be implemented:

Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw



For simplification, there are only 1 dollar bills in this world, no cents. Thus account balance can be represented in integer.



Your code doesn't need to integrate with a real bank system, but keep in mind that we may want to integrate it with a real bank system in the future. It doesn't have to integrate with a real cash bin in the ATM, but keep in mind that we'd want to integrate with that in the future. And even if we integrate it with them, we'd like to test our code. Implementing bank integration and ATM hardware like cash bin and card reader is not a scope of this task, but testing the controller part (not including bank system, cash bin etc) is within the scope.



A bank API wouldn't give the ATM the PIN number, but it can tell you if the PIN number is correct or not.



Based on your work, another engineer should be able to implement the user interface. You don't need to implement any REST API, RPC, network communication etc, but just functions/classes/methods, etc.



You can simplify some complex real world problems if you think it's not worth illustrating in the project.

## Run program test
1. Cloning the project
 ```python
 git clone 
 ```
2. Running the python
```python
python3 ATM_controller.py
```
3. Test Condition

Card Number : 12341234, Pin Number : 1234, Account Number/Balance : 1/100, 2/1200, 3/13000, 4/3000

4. Test Method

    1) Please insert your card : 12341234
    2) Enter the pin number : 1234  ==> log in successfully!
    3) ACCOUNT LIST: [1, 2, 3, 4]  ==> PLEASE SELECT AN ACCOUNT: 2
    4) ====Bank Menu====
    
       1 = Check Balance
       
       2 = Deposit
       
       3 = Withdraw
       
       4 = Quit
       
     =================
      
    5). please Enter 1, 2, 3, 4 : ==> you want select number and  run the test



