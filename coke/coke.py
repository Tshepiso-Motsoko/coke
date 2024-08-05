def coke_machine():
    # Initialize the amount due to 50 cents
    amount_due = 50

    # Define the accepted denominations of coins
    accepted_coins = [25, 10, 5]

    while amount_due > 0:
        # Print the current amount due
        print(f"Amount Due: {amount_due}")

        # Prompt the user to insert a coin
        coin = int(input("Insert Coin: "))

        # Check if the coin is an accepted denomination
        if coin in accepted_coins:
            # Update the amount due
            amount_due -= coin
        else:
            # Print an error message for coins that are not accepted
            print(f"Invalid Coin! Accepted denominations: {', '.join(map(str, accepted_coins))}")

    # Print the final change owed
    print(f"Change Owed: {amount_due * -1}")


if __name__ == "__main__":
    coke_machine()
