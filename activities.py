# Activity 1: Sum of all elements in an array (10 elements)
def activity_1():
    """Accept 10 integer elements and print their sum"""
    print("=" * 50)
    print("Activity 1: Sum of Array Elements")
    print("=" * 50)
    
    arr = []
    print("Enter 10 integer elements:")
    for i in range(10):
        element = int(input(f"Element {i+1}: "))
        arr.append(element)
    
    total_sum = sum(arr)
    print(f"\nArray: {arr}")
    print(f"Sum of all elements: {total_sum}\n")


# Activity 2: Find maximum 3 and minimum 3 from 20 elements (without sorting)
def activity_2():
    """Accept 20 integer elements and print max 3 and min 3 elements"""
    print("=" * 50)
    print("Activity 2: Maximum 3 and Minimum 3 Elements")
    print("=" * 50)
    
    arr = []
    print("Enter 20 integer elements:")
    for i in range(20):
        element = int(input(f"Element {i+1}: "))
        arr.append(element)
    
    # Find max 3 elements without sorting
    max_3 = []
    for _ in range(3):
        max_val = max(arr)
        max_3.append(max_val)
        arr.remove(max_val)
    
    # Restore array and find min 3 elements
    arr = []
    print("Enter 20 integer elements again for minimum:")
    for i in range(20):
        element = int(input(f"Element {i+1}: "))
        arr.append(element)
    
    min_3 = []
    for _ in range(3):
        min_val = min(arr)
        min_3.append(min_val)
        arr.remove(min_val)
    
    print(f"\nMaximum 3 elements: {sorted(max_3, reverse=True)}")
    print(f"Minimum 3 elements: {sorted(min_3)}\n")


# Activity 3: Reverse array of 10 elements
def activity_3():
    """Accept 10 integer elements and reverse the array"""
    print("=" * 50)
    print("Activity 3: Reverse Array")
    print("=" * 50)
    
    arr = []
    print("Enter 10 integer elements:")
    for i in range(10):
        element = int(input(f"Element {i+1}: "))
        arr.append(element)
    
    print(f"\nOriginal array: {arr}")
    arr.reverse()
    print(f"Reversed array: {arr}\n")


# Activity 4: Count occurrences of each mark (0-100) for 30 students
def activity_4():
    """Accept 30 student marks and count occurrences of each mark"""
    print("=" * 50)
    print("Activity 4: Count Occurrences of Each Mark")
    print("=" * 50)
    
    marks = []
    print("Enter marks (0-100) for 30 students:")
    for i in range(30):
        while True:
            try:
                mark = int(input(f"Student {i+1} mark: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter a mark between 0 and 100")
            except ValueError:
                print("Please enter a valid integer")
    
    # Create a frequency count
    mark_count = {}
    for mark in marks:
        if mark in mark_count:
            mark_count[mark] += 1
        else:
            mark_count[mark] = 1
    
    print("\nMark Frequency Distribution:")
    print("Mark | Count")
    print("-" * 10)
    for mark in sorted(mark_count.keys()):
        print(f"{mark:3d}  | {mark_count[mark]:3d}")
    
    print()


# Activity 5: Count students in mark ranges
def activity_5():
    """Accept 30 student marks and count students in different ranges"""
    print("=" * 50)
    print("Activity 5: Count Students in Mark Ranges")
    print("=" * 50)
    
    marks = []
    print("Enter marks (0-100) for 30 students:")
    for i in range(30):
        while True:
            try:
                mark = int(input(f"Student {i+1} mark: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter a mark between 0 and 100")
            except ValueError:
                print("Please enter a valid integer")
    
    # Count students in ranges (10% intervals)
    ranges = [
        ("0-10%", 0, 10),
        ("11-20%", 11, 20),
        ("21-30%", 21, 30),
        ("31-40%", 31, 40),
        ("41-50%", 41, 50),
        ("51-60%", 51, 60),
        ("61-70%", 61, 70),
        ("71-80%", 71, 80),
        ("81-90%", 81, 90),
        ("91-100%", 91, 100)
    ]
    
    print("\nMark Range Distribution:")
    print("Range      | Count")
    print("-" * 20)
    for range_name, min_mark, max_mark in ranges:
        count = sum(1 for mark in marks if min_mark <= mark <= max_mark)
        print(f"{range_name:10s} | {count:3d}")
    
    print()


# Activity 6: Calculate factorial of N
def activity_6():
    """Calculate factorial of a number N"""
    print("=" * 50)
    print("Activity 6: Calculate Factorial")
    print("=" * 50)
    
    while True:
        try:
            n = int(input("Enter a non-negative integer N: "))
            if n < 0:
                print("Please enter a non-negative number")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid integer")
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
    print(f"Factorial of {n} is: {factorial}\n")


# Activity 7: Calculate average of 10 integers
def activity_7():
    """Accept 10 integer values and calculate average"""
    print("=" * 50)
    print("Activity 7: Calculate Average")
    print("=" * 50)
    
    values = []
    print("Enter 10 integer values:")
    for i in range(10):
        value = int(input(f"Value {i+1}: "))
        values.append(value)
    
    average = sum(values) / len(values)
    print(f"\nValues: {values}")
    print(f"Average: {average:.2f}\n")


# Activity 8: Calculate train length
def activity_8():
    """
    Train crosses a pole in y seconds at x km/hr
    Calculate the length of the train
    """
    print("=" * 50)
    print("Activity 8: Calculate Train Length")
    print("=" * 50)
    
    while True:
        try:
            x = float(input("Enter speed of train (km/hr): "))
            if x <= 0:
                print("Speed must be positive and non-zero")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid number")
    
    while True:
        try:
            y = float(input("Enter time to cross pole (seconds): "))
            if y <= 0:
                print("Time must be positive and non-zero")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid number")
    
    # Convert km/hr to m/s: x km/hr = x * 1000/3600 m/s = x * 5/18 m/s
    speed_ms = x * 5 / 18
    train_length = speed_ms * y
    
    print(f"\nSpeed: {x} km/hr = {speed_ms:.2f} m/s")
    print(f"Length of train: {train_length:.2f} meters\n")


# Activity 9: Calculate train speed
def activity_9():
    """
    Train X meters long passes a man running at 5 km/hr
    in Y seconds in the same direction.
    Calculate the speed of the train.
    """
    print("=" * 50)
    print("Activity 9: Calculate Train Speed")
    print("=" * 50)
    
    while True:
        try:
            x = float(input("Enter length of train (meters): "))
            if x <= 0:
                print("Train length must be positive and non-zero")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid number")
    
    while True:
        try:
            y = float(input("Enter time to pass the man (seconds): "))
            if y <= 0:
                print("Time must be positive and non-zero")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid number")
    
    man_speed_kmhr = 5
    man_speed_ms = man_speed_kmhr * 5 / 18  # Convert to m/s
    
    # Relative speed = train_length / time_to_pass
    # Train speed - man speed = x / y
    # Train speed = (x / y) + man_speed_ms
    train_speed_ms = (x / y) + man_speed_ms
    train_speed_kmhr = train_speed_ms * 18 / 5  # Convert to km/hr
    
    print(f"\nMan's speed: {man_speed_kmhr} km/hr = {man_speed_ms:.2f} m/s")
    print(f"Train speed: {train_speed_kmhr:.2f} km/hr\n")


# Activity 10: Time taken for trains to pass each other
def activity_10():
    """
    Two trains, each 500m long, running in opposite directions.
    Find time taken by slower train to pass the driver of faster one.
    """
    print("=" * 50)
    print("Activity 10: Time for Trains to Pass Each Other")
    print("=" * 50)
    
    while True:
        try:
            x = float(input("Enter speed of first train (km/hr): "))
            if x <= 0:
                print("Speed must be positive and non-zero")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid number")
    
    while True:
        try:
            y = float(input("Enter speed of second train (km/hr): "))
            if y <= 0:
                print("Speed must be positive and non-zero")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid number")
    
    train_length = 500  # meters
    
    # Convert speeds to m/s
    x_ms = x * 5 / 18
    y_ms = y * 5 / 18
    
    # When trains move in opposite directions, relative speed = x + y
    relative_speed_ms = x_ms + y_ms
    
    # Time for slower train to pass the driver of faster train
    # = train_length / relative_speed (when moving in opposite directions)
    time_seconds = train_length / relative_speed_ms
    
    print(f"\nFirst train speed: {x} km/hr = {x_ms:.2f} m/s")
    print(f"Second train speed: {y} km/hr = {y_ms:.2f} m/s")
    print(f"Relative speed: {relative_speed_ms:.2f} m/s")
    print(f"Time for slower train to pass: {time_seconds:.2f} seconds\n")


# Main menu
def main():
    """Display menu and execute selected activity"""
    while True:
        print("\n" + "=" * 50)
        print("ACTIVITY MENU")
        print("=" * 50)
        print("1. Activity 1 - Sum of Array Elements")
        print("2. Activity 2 - Maximum 3 and Minimum 3")
        print("3. Activity 3 - Reverse Array")
        print("4. Activity 4 - Count Occurrences of Marks")
        print("5. Activity 5 - Count Students in Ranges")
        print("6. Activity 6 - Calculate Factorial")
        print("7. Activity 7 - Calculate Average")
        print("8. Activity 8 - Train Length Calculation")
        print("9. Activity 9 - Train Speed Calculation")
        print("10. Activity 10 - Time to Pass Each Other")
        print("0. Exit")
        print("=" * 50)
        
        try:
            choice = int(input("Enter your choice (0-10): "))
            
            if choice == 0:
                print("Exiting program...")
                break
            elif choice == 1:
                activity_1()
            elif choice == 2:
                activity_2()
            elif choice == 3:
                activity_3()
            elif choice == 4:
                activity_4()
            elif choice == 5:
                activity_5()
            elif choice == 6:
                activity_6()
            elif choice == 7:
                activity_7()
            elif choice == 8:
                activity_8()
            elif choice == 9:
                activity_9()
            elif choice == 10:
                activity_10()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            break


if __name__ == "__main__":
    main()
