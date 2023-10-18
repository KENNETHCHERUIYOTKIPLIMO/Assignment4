def calculate_average(math_mark, physics_mark, geo_mark, chem_mark):
    return (math_mark + physics_mark + geo_mark + chem_mark) / 4

def grade_student(avg_mark):
    if avg_mark < 0 or avg_mark > 100:
        return 'unrecognized marks/avg'
    elif avg_mark <= 30:
        return 'D'
    elif avg_mark <= 50:
        return 'C'
    elif avg_mark <= 70:
        return 'B'
    else:
        return 'A'

def main():
    try:
        math_mark = float(input("Enter Maths marks: "))
        physics_mark = float(input("Enter Physics marks: "))
        geo_mark = float(input("Enter Geo marks: "))
        chem_mark = float(input("Enter Chem marks: "))

        if any(mark < 0 or mark > 100 for mark in [math_mark, physics_mark, geo_mark, chem_mark]):
            print("unrecognized marks/avg")
            return

        average_mark = calculate_average(math_mark, physics_mark, geo_mark, chem_mark)
        grade = grade_student(average_mark)
        print(f"The average mark is {average_mark:.2f} and the grade is {grade}.")

    except ValueError:
        print("Please enter valid numerical values for marks.")

if __name__ == "__main__":
    main()