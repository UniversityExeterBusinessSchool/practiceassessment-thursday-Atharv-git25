#######################################################################################################################################################
# 
# Name:Atharv Devanand Patil
# SID:740100396
# Exam Date: 27/03/2025
# Module: Programming for Business Analytics
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-Atharv-git25
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate', 
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 


# Using SID, extract the pertinent words (740100396)
# Seven is the first digit, and six is the last.

first_digit = 7
last_digit = 6

# Obtain the precise terms we must look up in the dictionary.

word_to_find1 = key_comments[first_digit]  # This will be 'resolve' 
word_to_find2 = key_comments[last_digit]   # This will be 'experience' 

# Look for the feedback's first word, "resolve."
# If the initial index is discovered, find() returns it; if not, it returns -1.

start_pos1 = customer_feedback.find(word_to_find1)

# Don't continue until the word was located (start_pos1!= -1).

if start_pos1 != -1:
  # Determine the end position by adding the word's length to the start position.
    end_pos1 = start_pos1 + len(word_to_find1)
    # Include the (start, end) tuple in our list of results.
    my_list.append((start_pos1, end_pos1))

# Look for "experience," the second word, in the feedback.
start_pos2 = customer_feedback.find(word_to_find2)

# Don't continue until the word was located (start_pos2!= -1).
if start_pos2 != -1:
    # Determine the end position by adding the word's length to the start position.
    end_pos2 = start_pos2 + len(word_to_find2)
    # Include the (start, end) tuple in our list of results.
    my_list.append((start_pos2, end_pos2))

# The final list contains tuples with positions of both words
print(my_list)
# Initialize an empty list to store (start, end) positions
my_list = []

#Output :- [(129, 136), (18, 28)]

##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:
first_two = 74
# Insert last two digits of ID number here:
last_two = 96
# Write your code for Operating Profit Margin
''' determines the proportion of revenue that is turned into operating profit ""This is a crucial indicator of corporate profitability.
    
     Args: operating_profit (float): The amount of money left over after operating costs
         Total sales revenue is the revenue (float).
        
     Returns: float: Percentage of operating profit margin'''


def operating_profit_margin(operating_profit, revenue):
    return (operating_profit / revenue) * 100
# Write your code for Revenue per Customer

"""
    Calculates the average revenue generated per customer.
    Helps measure customer value and spending patterns.
    
    Args:
        total_revenue (float): Total revenue in period
        total_customers (int): Number of active customers
        
    Returns:
        float: Average revenue per customer
    Formula: Total Revenue / Total Customers
    """
def revenue_per_customer(total_revenue, total_customers):
    return total_revenue / total_customers


# Write your code for Customer Churn Rate
def customer_churn_rate(lost_customers, total_customers):
    return (lost_customers / total_customers) * 100
# Write your code for Average Order Value
def average_order_value(total_revenue, number_of_orders):
    return total_revenue / number_of_orders
# Call your designed functions here
margin = operating_profit_margin(first_two_digits, last_two_digits)
rev_per_cust = revenue_per_customer(first_two_digits, last_two_digits)
churn = customer_churn_rate(first_two_digits, last_two_digits)
aov = average_order_value(first_two_digits, last_two_digits)

## Printing the results for these
print("Operating Profit Margin:", margin, "%")
print("Revenue per Customer:", rev_per_cust)
print("Customer Churn Rate:", churn, "%")
print("Average Order Value:", aov)

'''Output :- Operating Profit Margin: 117.1875 %
Revenue per Customer: 1.171875
Customer Churn Rate: 117.1875 %
Average Order Value: 1.171875'''
 
##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

'''
Retail Price Optimization using Linear Regression

This program analyzes the relationship between product price and customer demand
to determine:
1. The optimal price point that maximizes revenue
2. The predicted demand at a specific price point (£52)
'''

# Input data - price and demand observations
prices = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
demand = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])

'''
STEP 1: Create and train linear regression model
Finds the best-fit line: Demand = slope × Price + intercept
'''
model = LinearRegression()
model.fit(prices, demand)

# Get model parameters
slope = model.coef_[0]
intercept = model.intercept_
print(f"Regression equation: Demand = {slope:.2f} * Price + {intercept:.2f}")

'''
STEP 2: Calculate revenue-maximizing price
Revenue = Price × Demand = slope × Price² + intercept × Price
Maximum occurs when derivative = 0: Price = -intercept/(2 × slope)
'''
optimal_price = -intercept / (2 * slope)
optimal_demand = slope * optimal_price + intercept
max_revenue = optimal_price * optimal_demand
print(f"\nOptimal price: £{optimal_price:.2f}")
print(f"Demand at optimal price: {optimal_demand:.0f} units")
print(f"Maximum revenue: £{max_revenue:.2f}")

# Predict demand at £52
price_52 = np.array([[52]])
demand_52 = model.predict(price_52)[0]
print(f"\nPredicted demand at £52: {demand_52:.0f} units")

'''
STEP 3: Visualization
Creates plot showing actual data, regression line, and optimal price
'''
plt.figure(figsize=(10, 6))
plt.scatter(prices, demand, color='blue', label='Actual Data')
plt.plot(prices, model.predict(prices), color='red', label='Regression Line')

# Add vertical line at optimal price
plt.axvline(x=optimal_price, color='green', linestyle='--', 
            label=f'Optimal Price (£{optimal_price:.2f})')

plt.title('Price vs Demand Analysis')
plt.xlabel('Price (£)')
plt.ylabel('Demand (Units)')
plt.legend()
plt.grid(True)
plt.show()

'''Output :- Regression equation: Demand = -4.48 * Price + 391.23

Optimal price: £43.65
Demand at optimal price: 196 units
Maximum revenue: £8537.76

Predicted demand at £52: 158 units'''
            
##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Using hardcoded student ID to avoid input() issues
max_value = 740100396  # Your student ID: 740100396
random_numbers = [random.randint(1, max_value) for _ in range(100)]

# Plotting the numbers in a line chart
plt.figure(figsize=(12, 6))
plt.plot(random_numbers, 
         marker='o',
         markerfacecolor='green',
         markeredgecolor='red',
         linestyle='--',
         label='Random Numbers',
         color='blue',
         markersize=5,
         linewidth=1)

plt.title("Line Chart of 100 Random Numbers (1-740100396)")
plt.xlabel("Index")
plt.ylabel("Random Number Value")
plt.legend()
plt.grid(True, which='both', linestyle=':', linewidth=0.5)

# Adjust y-axis scale for better visualization
plt.yscale('log')  # Using logarithmic scale due to large number range

plt.show()

'''Output in word file is it is a graph'''

