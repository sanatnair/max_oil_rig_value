# max_oil_rig_value
Using dynamic programming to maximize the estimated value produced by oil rigs given a budget, cost, and the specific gravity of crude
## Overview
This software is designed to optimize the selection and construction of oil rigs in different locations to maximize the total profit per barrel of oil, given a budget, cost of rigs, and the specific gravity of crude. The program utilizes dynamic programming (knapsack) to determine the most profitable combination of rigs within the specified financial constraints.

## Problem Statement
A subsidiary of a large oil company aims to establish oil rigs in specific locations with known oil compositions. The goal is to maximize the profit per barrel of oil extracted, considering the budget constraints set by the oil company. Each rig incurs a certain cost, and the subsidiary cannot exceed the maximum investment limit. The program also provides insights into the order in which rigs should be constructed based on return on investment (ROI).

## Input Format
The input for the program is a text file with five lines:

1. **Maximum Investment**: A rounded estimate of the maximum investment in USD provided by the oil company (in 100 million).
   - Example: If the input is 8, the maximum investment is 8 times 100 million, equaling 800 million USD.

2. **Number of Rigs**: An integer representing the total number of rigs the subsidiary can choose from.

3. **Cost of Rigs**: A list of integer numbers specifying the cost to build each rig type at their respective locations (in 100 million).

4. **Specific Gravity of Oils**: A list of float numbers representing the variations in the specific gravity of the oils extracted from each rig location.

5. **Standardized Price of Oil**: An integer representing the price of oil in USD, standardized across all compositions.

## Output
The program outputs the optimized plan for rig construction, including the total profit per barrel and the return on investment (ROI) for each rig. The ROI is calculated by dividing the profit per barrel by the cost to build the rig, multiplied by 100.

## Usage
1. Create a text file with the required input format.
2. Run the program, providing the path to the input file.
3. Review the output to determine the optimal rig construction plan and prioritize rigs based on ROI.

## Example Input and Output
This demonstrates an example input file and the corresponding output. Note that three test cases are also provided within this repository.
_Input:_
```
8 # budget
3 # number of rigs
1, 7, 4 # rig costs
0.83, 0.92, 0.79 # crude specific gravities
2.00 # standardized oil price
```
_Output:_
```
The estimated maximum price of oil is $173.18 USD/bbl.
The selected rigs are: [3, 1]
Optimized Rigs sorted based on greatest ROI:
Rig 1: ROI = 77.96%
Rig 3: ROI = 23.80%
```
