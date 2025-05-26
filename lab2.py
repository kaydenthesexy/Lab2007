def main():
    temperatures = []

    print("Enter temperature values one by one. Type 'done' to finish.\n")

    while True:
        user_input = input("Enter temperature: ")
        
        if user_input.lower() == 'done':
            break

        try:
            temperature = float(user_input)
            temperatures.append(temperature)
        except ValueError:
            print("Please enter a valid number or 'done' to finish.")

    if temperatures:
        avg_temp = sum(temperatures) / len(temperatures)
        min_temp = min(temperatures)
        max_temp = max(temperatures)

        print("\nTemperature Summary:")
        print(f"Average: {avg_temp:.2f}")
        print(f"Minimum: {min_temp:.2f}")
        print(f"Maximum: {max_temp:.2f}")
    else:
        print("No temperatures were entered.")

if __name__ == "__main__":
    main()