def main():
    print("Available shapes: 'triangle' 'square' 'rectangle' 'rhombus' 'trapezoid'")
    print("Press [Ctrl + C] to stop the program")
    area: float
    while True:
        shape = str(input("Pick a shape: "))
        try:
            if shape == "triangle":
                base = float(input("Base: "))
                height = float(input("Height: "))
                area = base * height * 0.5
            elif shape == "square":
                side = float(input("Side: "))
                area = side * side
            elif shape == "rectangle":
                side1 = float(input("Side 1: "))
                side2 = float(input("Side 2: "))
                area = side1 * side2
            elif shape == "rhombus":
                diagonal1 = float(input("Diagonal 1: "))
                diagonal2 = float(input("Diagonal 2: "))
                area = diagonal1 * diagonal2 * 0.5
            elif shape == "trapezoid":
                base1 = float(input("Base 1: "))
                base2 = float(input("Base 2: "))
                height = float(input("Height: "))
                area = (base1 + base2) * height * 0.5
            else:
                print("Invalid shape")
                continue

            if area < 0:
                raise Exception
            else:
                print(f"Area of the {shape}: {area}")
        except:
            print("Invalid value for the side/height of the shape")

if __name__ == "__main__":
    main()
