def calculate_rectangle_area(length, width):

    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers")
    return length * width

if __name__ == "__main__":
    # Example usage
    try:
        length = 5
        width = 10
        area = calculate_rectangle_area(length, width)
        print(f"The area of the rectangle is: {area}")
    except ValueError as e:
        print(f"Error: {e}") 