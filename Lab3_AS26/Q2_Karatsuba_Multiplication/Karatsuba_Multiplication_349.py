"""
Q2: Traditional Large Integer Multiplication vs Karatsuba
Student suffix used in identifiers: 349

Run:
    python3 Karatsuba_Multiplication_349.py
"""


def Clean_Number_349(Number_Text_349):
    Number_Text_349 = str(Number_Text_349).strip()
    if not Number_Text_349.isdigit():
        raise ValueError("Enter digits only (non-negative whole numbers).")
    return Number_Text_349.lstrip("0") or "0"


def Traditional_Multiply_349(Number_A_349, Number_B_349):
    """Grade-school multiplication using digit arrays."""
    Number_A_349 = Clean_Number_349(Number_A_349)
    Number_B_349 = Clean_Number_349(Number_B_349)
    if Number_A_349 == "0" or Number_B_349 == "0":
        return "0"

    Digits_A_349 = [int(Digit_349) for Digit_349 in Number_A_349[::-1]]
    Digits_B_349 = [int(Digit_349) for Digit_349 in Number_B_349[::-1]]
    Result_Digits_349 = [0] * (len(Digits_A_349) + len(Digits_B_349))

    for Index_A_349 in range(len(Digits_A_349)):
        for Index_B_349 in range(len(Digits_B_349)):
            Result_Digits_349[Index_A_349 + Index_B_349] += (
                Digits_A_349[Index_A_349] * Digits_B_349[Index_B_349]
            )

    for Position_349 in range(len(Result_Digits_349) - 1):
        Carry_349 = Result_Digits_349[Position_349] // 10
        Result_Digits_349[Position_349] %= 10
        Result_Digits_349[Position_349 + 1] += Carry_349

    while len(Result_Digits_349) > 1 and Result_Digits_349[-1] == 0:
        Result_Digits_349.pop()
    return "".join(str(Digit_349) for Digit_349 in Result_Digits_349[::-1])


def Karatsuba_Multiply_349(Number_A_349, Number_B_349):
    """Karatsuba uses three recursive multiplications per split."""
    Number_A_349 = Clean_Number_349(Number_A_349)
    Number_B_349 = Clean_Number_349(Number_B_349)

    def Recursive_Multiply_349(Part_A_349, Part_B_349):
        Part_A_349 = Part_A_349.lstrip("0") or "0"
        Part_B_349 = Part_B_349.lstrip("0") or "0"
        if Part_A_349 == "0" or Part_B_349 == "0":
            return "0"

        if len(Part_A_349) <= 4 and len(Part_B_349) <= 4:
            return str(int(Part_A_349) * int(Part_B_349))

        Length_349 = max(len(Part_A_349), len(Part_B_349))
        if Length_349 % 2 == 1:
            Length_349 += 1
        Part_A_349 = Part_A_349.zfill(Length_349)
        Part_B_349 = Part_B_349.zfill(Length_349)
        Half_349 = Length_349 // 2

        High_A_349, Low_A_349 = Part_A_349[:-Half_349], Part_A_349[-Half_349:]
        High_B_349, Low_B_349 = Part_B_349[:-Half_349], Part_B_349[-Half_349:]

        Z2_349 = Recursive_Multiply_349(High_A_349, High_B_349)
        Z0_349 = Recursive_Multiply_349(Low_A_349, Low_B_349)
        Z1_349 = Recursive_Multiply_349(
            str(int(High_A_349) + int(Low_A_349)),
            str(int(High_B_349) + int(Low_B_349))
        )
        Middle_349 = str(int(Z1_349) - int(Z2_349) - int(Z0_349))

        Answer_349 = (
            int(Z2_349) * (10 ** (2 * Half_349))
            + int(Middle_349) * (10 ** Half_349)
            + int(Z0_349)
        )
        return str(Answer_349)

    return Recursive_Multiply_349(Number_A_349, Number_B_349)


def Main_349():
    print("Q2: Large Integer Multiplication")
    Number_A_349 = input("Enter the first non-negative integer: ").strip()
    Number_B_349 = input("Enter the second non-negative integer: ").strip()

    try:
        Number_A_349 = Clean_Number_349(Number_A_349)
        Number_B_349 = Clean_Number_349(Number_B_349)
    except ValueError as Error_349:
        print(Error_349)
        return

    Result_Traditional_349 = Traditional_Multiply_349(Number_A_349, Number_B_349)
    Result_Karatsuba_349 = Karatsuba_Multiply_349(Number_A_349, Number_B_349)

    print("\\nTraditional result:", Result_Traditional_349)
    print("Karatsuba result:  ", Result_Karatsuba_349)
    print("Do the results match?", Result_Traditional_349 == Result_Karatsuba_349)
    print("Digits in first number:", len(Number_A_349))
    print("Digits in second number:", len(Number_B_349))
    # Conclusion: Karatsuba reduces recursive multiplications from four to three.
    # Both methods should produce the same product.


if __name__ == "__main__":
    Main_349()
