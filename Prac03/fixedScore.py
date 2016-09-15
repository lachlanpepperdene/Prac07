def scoreInput():
    score = float(input("Enter score: "))
    return score

def main():
    score = scoreInput()
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
main()