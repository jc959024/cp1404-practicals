# Constants
DISCOUNT_THRESHOLD = 100.0
DISCOUNT_RATE = 0.9

def main():
    number_items = int(input("Number of items: "))

    if number_items >= 0:
        total_price = 0.0
        for i in range(number_items):
            while True:
                try:
                    price = float(input(f"Price of item {i + 1}: "))
                    if price < 0:
                        print("Price cannot be negative. Please enter a valid price.")
                    else:
                        break
                except ValueError:
                    print("Invalid price. Please enter a valid number.")
            total_price += price

        if total_price > DISCOUNT_THRESHOLD:
            total_price *= DISCOUNT_RATE

        print(f"Total price for {number_items} items is ${total_price:.2f}")
    else:
        print("Invalid number of items!")

if __name__ == "__main__":
    main()
