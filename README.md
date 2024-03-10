# AICP-TASKS-WEEK-5-
  **CAR PARK PARMENT SYSTEM**
  
A car park payment system allows customers to select the number of hours to leave their car in the car park. The customer will get a discount if they enter their frequent parking number correctly. The system calculates and displays the amount the customer must pay. The price of parking, the number of hours the customer can enter, and any discount depend upon the day of the week and the arrival time. The number of hours entered is a whole number. The price per hour is calculated using the price in force at the arrival time. No parking is allowed between Midnight and 08:00. 


 **Days of Week**                                                         **Arrival Time**
                                                         **From 08:00 - 15:59 From 16:00 - Midnight**
                                             **Max Stay in hours**                     **Price per hour**             **Hour**       **Price**

Sunday                                           8                                           2.00                  Up to midnight       2.00
Monday                                           2                                           10.00                 Up to midnight       2.00
Tuesday                                          2                                           10.00                 Up to midnight       2.00
Wednesday                                        2                                           10.00                 Up to midnight       2.00
Thursday                                         2                                           10.00                 Up to midnight       2.00
Friday                                           2                                           10.00                 Up to midnight       2.00
Saturday                                         4                                           3.00                  Up to midnight       2.00

A frequent parking number can be entered for discounted parking. This number consists of 4 digits and a check digit that is calculated using a modulo 11 check digit calculation. A discount of 50% is available for arrival times from 16:00 to Midnight; the discount is 10% at all other arrival times.
Write and test a program or program to simulate the car park payment system.
1) Your program or programs must include appropriate prompts for the entry of data; data must be validated on entry.
2) Error messages and other outputs need to be set out clearly and understandably.
3) All variables, constants, and other identifiers must have meaningful names.
You will need to complete these three tasks. Each task must be fully tested.

**Task 1** – Calculating the price to park.
A customer inputs the day, the hour of arrival excluding minutes (for example 15:45 would be 15), the number of hours to leave their car, and a frequent parking number if available. If the frequent parking number has an incorrect check digit, then no discount can be applied. The price to park, based on the day, the hour of arrival, the number of hours of parking required and any discount available, is calculated and displayed.

**Task 2**– Keeping a total of the payments. 
Extend Task 1 to keep a daily total of payments made for parking. The daily total is zeroed at the start of the day. For the simulation, each customer inputs the amount paid, this must be greater than or equal to the amount displayed. There is no change given so the amount input may exceed the amount displayed. Each customer payment is added to the daily total, and this total is displayed at the end of the day.

**Task 3**– Making payments fairer.
Customers have complained that sometimes they are being charged too much if they arrive before 16:00 and depart after 16:00. Extend Task 1 to calculate the price before 16:00, then add the evening charge. For example, a customer arriving at 14:45 on a Sunday and parking for five hours was previously charged 10.00 and would now be charged 6.00
