"""Find the maximum price of oil that can be extracted"""
import sys

class Stack:
    """This class defines a Stack."""

    def __init__(self):
        self.stack = []

    def push(self, item):
        """Takes in an item and adds it to the top of the stack."""
        self.stack.append(item)

    def pop(self):
        """Removes an item from the top of the stack."""
        if not self.is_empty():
            return self.stack.pop()
        return None
    def is_empty(self):
        """Checks if a stack is empty."""
        return len(self.stack) == 0

def calculate_api_gravity(specific_gravity):
    """Calculate the specific gravity of the crude to use in finding price of oil extracted from rig"""
    api_gravity=[]
    for i in range(len(specific_gravity)):
        api_value = (141.5/specific_gravity[i]) - 131.5
        api_value = round(api_value,2)
        api_gravity.append(api_value)
    return api_gravity

def calculate_rig_oil_price(api_gravity, standard_oil_cost):
    """Calculate the price of oil (USD/bbl) that each rig will extract"""
    rig_oil_price=[]
    for i in range(len(api_gravity)):
        oil_value = api_gravity[i] * standard_oil_cost
        oil_value = round(oil_value,2)
        rig_oil_price.append(oil_value)
    return rig_oil_price

def maximize_oil_price(investment, num_rigs,rig_prices,rig_oil_price):
        """Calculate and return the maximum price of oil possible and respective rigs"""
        
        # Checking if the lengths of rig_prices and rig_oil_price lists are equal
        if len(rig_prices) != len(rig_oil_price):
            raise ValueError("Lengths of rig_prices and rig_oil_price lists should be equal.")       
        
        # Creating a table to store the maximum values for different investments
        v = [[0 for _ in range(investment + 1)] for _ in range(num_rigs + 1)]
        
        # Creating a table to track selected rigs
        keep = [[0 for _ in range(investment + 1)] for _ in range(num_rigs + 1)]

        # Filling the table 
        for i in range(1, num_rigs + 1):
            for w in range(investment + 1):
                if rig_prices[i - 1] <= w and \
                    rig_oil_price[i - 1] + v[i - 1][w - rig_prices[i - 1]] >= v[i - 1][w]:
                    v[i][w] = rig_oil_price[i - 1] + v[i - 1][w - rig_prices[i - 1]]
                    keep[i][w] = 1
                else:
                    v[i][w] = v[i - 1][w]
                    keep[i][w] = 0
        
        # Reconstruct the selected rigs
        k = investment
        selected_items = []
        selected_index = []
        for i in range(num_rigs, 0, -1):
            if keep[i][k] == 1:
                selected_items.append(i)
                selected_index.append(i-1)
                k -= rig_prices[i - 1]

        return v[num_rigs][investment],selected_items,selected_index

def calculate_roi(selected_index,rig_oil_price,rig_prices):
    # Calculate and sort ROI
    roi_values = {}
    for i, rig_index in enumerate(selected_index):
        roi = rig_oil_price[rig_index] / (rig_prices[rig_index] * 100)
        roi_values[i + 1] = roi

    # Sort ROI values in ascending order
    sorted_roi = sorted(roi_values.items(), key=lambda x: x[1])

    # Use a stack to reverse the order
    roi_stack = Stack()
    for rig_index, roi in sorted_roi:
        roi_stack.push((rig_index, roi))
    return roi_stack


def main():
    """Main function"""
    # The first line is the amount of investment in USD (in 100 million).
    line = sys.stdin.readline()
    line = line.strip()
    investment = int(line)

    # The second line includes the number of rigs available.
    line = sys.stdin.readline()
    line = line.strip()
    num_rigs = int(line)

    # The third line is a list of rig prices in USD (in 100 million).
    line = sys.stdin.readline()
    line = line.strip()
    rig_prices = line.split(",")
    for i in range(0, len(rig_prices)):
        rig_prices[i] = int(rig_prices[i])

    # The fourth line is the specific gravity of the crude oil extracted by the rig and location.
    line = sys.stdin.readline()
    line = line.strip()
    specific_gravity = line.split(",")
    for i in range(0, len(specific_gravity)):
        specific_gravity[i] = float(specific_gravity[i])

    # The fifth line is the current standardized price of oil across all compositions (USD/barrel).
    line = sys.stdin.readline()
    line = line.strip()
    standard_oil_cost = float(line)


    # Calculate the api gravity of crude and oil price of each rig to calculate optimal solution calculation.
    api_gravity=calculate_api_gravity(specific_gravity)
    rig_oil_price=calculate_rig_oil_price(api_gravity,standard_oil_cost)

    # Return optimal solution.
    max_oil_price,selected_rigs,selected_index=maximize_oil_price(investment, num_rigs,rig_prices,rig_oil_price)
    print(f"The estimated maximum price of oil is ${max_oil_price:.2f} USD/bbl.")
    print(f"The selected rigs are: {selected_rigs}")
    
    # Print the optimized rigs sorted based on greatest ROI
    roi_stack = calculate_roi(selected_index, rig_oil_price, rig_prices)
    print("Optimized Rigs sorted based on greatest ROI:")
    while not roi_stack.is_empty():
        rig_index, roi = roi_stack.pop()
        print(f"Rig {selected_rigs[rig_index - 1]}: ROI = {roi:.2%}")
    


if __name__ == '__main__':
    main()
