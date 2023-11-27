"""Find the maximum price of oil that can be extracted"""
import sys

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
        rig_oil_price.append(oil_value)
    return rig_oil_price

def maximize_oil_price(investment, num_rigs,rig_prices,rig_oil_price):
    """Calculate and return the maximum price of oil possible and respective rigs"""
    # Checking if the lengths of rig_prices and rig_oil_price lists are equal
    if len(rig_prices) != len(rig_oil_price):
        raise ValueError("Lengths of rig_prices and rig_oil_price lists should be equal.")

    n = num_rigs  # number of rigs

    # Creating a 2D table to store the maximum values for different investments
    dp = [[0.0 for _ in range(int(investment) + 1)] for _ in range(n + 1)]

    # Creating a table to track selected rigs
    selected_rigs = [[0 for _ in range(int(investment) + 1)] for _ in range(n + 1)]

    # Filling the table 
    for i in range(1, n + 1):
        for j in range(1, int(investment) + 1):
            if rig_prices[i - 1] <= j:
                if rig_oil_price[i - 1] + dp[i - 1][j - int(rig_prices[i - 1])] >= dp[i - 1][j]:
                    dp[i][j] = rig_oil_price[i - 1] + dp[i - 1][j - int(rig_prices[i - 1])]
                    selected_rigs[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    # Reconstruct the selected rigs
    k = int(investment)
    selected_items = []
    for i in range(n, 0, -1):
        if selected_rigs[i][k] == 1:
            selected_items.append(i)
            k -= int(rig_prices[i - 1])

    return dp[n][int(investment)], selected_items

def main():
    """Main function"""
    # The first line is the amount of investment in USD (in 100 million).
    line = sys.stdin.readline()
    line = line.strip()
    investment = float(line)

    # The second line includes the number of rigs available.
    line = sys.stdin.readline()
    line = line.strip()
    num_rigs = int(line)

    # The third line is a list of rig prices in USD (in 100 million).
    line = sys.stdin.readline()
    line = line.strip()
    rig_prices = line.split(",")
    for i in range(0, len(rig_prices)):
        rig_prices[i] = float(rig_prices[i])

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
    max_oil_price,selected_rigs=maximize_oil_price(investment, num_rigs,rig_prices,rig_oil_price)
    print(f"The estimated maximum price of oil is ${max_oil_price:.2f} USD/bbl.")
    print(f"The selected rigs are: {selected_rigs}")

    


if __name__ == '__main__':
    main()

    #TODO:

    # make sure to have two data structures... currently lists and 2d lists... implement dictionary, heap, or queue/stack? maybe sort something?

    # finally, check solution, and clean code