"""
Q3: Menu-driven Binary Search vs Ternary Search
Student suffix used in identifiers: 349

Run:
    python3 Search_Algorithms_349.py
"""

import random as random_349


def Binary_Search_349(Array_349, Key_349):
    Low_349, High_349 = 0, len(Array_349) - 1
    Comparisons_349 = 0

    while Low_349 <= High_349:
        Middle_349 = (Low_349 + High_349) // 2
        Comparisons_349 += 1
        if Array_349[Middle_349] == Key_349:
            return Middle_349, Comparisons_349
        if Key_349 < Array_349[Middle_349]:
            High_349 = Middle_349 - 1
        else:
            Low_349 = Middle_349 + 1
    return -1, Comparisons_349


def Ternary_Search_349(Array_349, Key_349):
    Low_349, High_349 = 0, len(Array_349) - 1
    Comparisons_349 = 0

    while Low_349 <= High_349:
        Third_349 = (High_349 - Low_349) // 3
        Middle_One_349 = Low_349 + Third_349
        Middle_Two_349 = High_349 - Third_349

        Comparisons_349 += 1
        if Array_349[Middle_One_349] == Key_349:
            return Middle_One_349, Comparisons_349
        Comparisons_349 += 1
        if Array_349[Middle_Two_349] == Key_349:
            return Middle_Two_349, Comparisons_349

        if Key_349 < Array_349[Middle_One_349]:
            High_349 = Middle_One_349 - 1
        elif Key_349 > Array_349[Middle_Two_349]:
            Low_349 = Middle_Two_349 + 1
        else:
            Low_349 = Middle_One_349 + 1
            High_349 = Middle_Two_349 - 1

    return -1, Comparisons_349


def Comparison_Table_349():
    print("\\nWorst-case example: key is absent")
    print(f"{'n':>8} {'Binary comparisons':>20} {'Ternary comparisons':>21}")
    for Size_349 in [10, 100, 1000, 10000]:
        Array_349 = list(range(0, Size_349 * 2, 2))
        Missing_Key_349 = -1
        _, Binary_Count_349 = Binary_Search_349(Array_349, Missing_Key_349)
        _, Ternary_Count_349 = Ternary_Search_349(Array_349, Missing_Key_349)
        print(f"{Size_349:>8} {Binary_Count_349:>20} {Ternary_Count_349:>21}")


def Main_349():
    Array_349 = []

    while True:
        print("\\n===== SEARCH MENU =====")
        print("1. Generate n sorted random numbers")
        print("2. Display array")
        print("3. Search using Binary Search")
        print("4. Search using Ternary Search")
        print("5. Best-case comparison example")
        print("6. Worst-case comparison (key absent)")
        print("7. Comparison table for increasing n")
        print("8. Exit")
        Choice_349 = input("Choose an option: ").strip()

        if Choice_349 == "1":
            try:
                Size_349 = int(input("How many numbers? "))
                if Size_349 <= 0:
                    print("Please enter a number greater than zero.")
                    continue
                Array_349 = sorted(random_349.sample(range(1, Size_349 * 10 + 1), Size_349))
                print("Sorted array generated.")
            except ValueError:
                print("Please enter a valid positive integer.")

        elif Choice_349 == "2":
            print(Array_349 if Array_349 else "Array is empty. Choose option 1 first.")

        elif Choice_349 in ("3", "4"):
            if not Array_349:
                print("Generate an array first using option 1.")
                continue
            try:
                Key_349 = int(input("Enter the key to search for: "))
            except ValueError:
                print("Please enter an integer.")
                continue

            if Choice_349 == "3":
                Index_349, Count_349 = Binary_Search_349(Array_349, Key_349)
                Algorithm_349 = "Binary Search"
            else:
                Index_349, Count_349 = Ternary_Search_349(Array_349, Key_349)
                Algorithm_349 = "Ternary Search"

            print(f"{Algorithm_349}: " + (f"key found at index {Index_349}." if Index_349 != -1 else "key not found."))
            print("Number of comparisons:", Count_349)

        elif Choice_349 == "5":
            if not Array_349:
                print("Generate an array first using option 1.")
                continue
            Key_349 = Array_349[len(Array_349) // 2]
            _, Binary_Count_349 = Binary_Search_349(Array_349, Key_349)
            _, Ternary_Count_349 = Ternary_Search_349(Array_349, Key_349)
            print("Example key:", Key_349)
            print("Binary Search comparisons:", Binary_Count_349)
            print("Ternary Search comparisons:", Ternary_Count_349)
            print("This is an example of a quick successful search; counts depend on the key.")

        elif Choice_349 == "6":
            if not Array_349:
                print("Generate an array first using option 1.")
                continue
            Key_349 = max(Array_349) + 1
            _, Binary_Count_349 = Binary_Search_349(Array_349, Key_349)
            _, Ternary_Count_349 = Ternary_Search_349(Array_349, Key_349)
            print("Absent key:", Key_349)
            print("Binary Search comparisons:", Binary_Count_349)
            print("Ternary Search comparisons:", Ternary_Count_349)

        elif Choice_349 == "7":
            Comparison_Table_349()

        elif Choice_349 == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Select 1 to 8.")


if __name__ == "__main__":
    Main_349()
