# Liam Melia, 17397283, 21/01/2025

# initialise an empty list to append the daily customers to
daily_customers = []

# create a list of days of the week to make inputting more user-friendly
# here we go from Mon-Sun but this can be easily changed for any 7-day period
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# loop for the 7 days in the period.
for i in range(0, 7):
    
    # use while true nested loop to ensure an integer is entered
    while True:
        # prompt the user for an input, using the days name to improve ease of use
        daily_val = input(f"Enter the value for {days[i]}: ")
        # use a try statement to append their input as an integer
        try:
            daily_customers.append(int(daily_val))
            # we can now use break to exit the while loop
            break
        # use except to handle errors if a non-integer is entered
        except ValueError:
            # Tell the user they must enter an integer
            print("Your inputs must only be integers")


# use built-in max and min functions to find maximum and minimum for the week
max_customers = max(daily_customers)
min_customers = min(daily_customers)

# no need to import statistics for mean function, we will manually calculate
# the mean and round the answer for readability
avg_customers = round(sum(daily_customers) / len(daily_customers), 2)

# print our values
print(f"The maximum number of customers in a day was: {max_customers}")
print(f"The minimum number of customers in a day was: {min_customers}")
print(f"The average number of customers per day in the week was: {avg_customers}")