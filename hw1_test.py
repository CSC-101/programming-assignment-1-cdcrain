import data
import hw1
import math
import unittest



# Write your functions for each part in the space below.#

#Define a function named vowel_count with one parameter of type str (a string).
#This function must compute and return the count of the number of vowels that appear in the input string.
#For the purposes of this problem, you are only asked to consider the standard five vowels in English
#(though the function should count both lowercase and uppercase vowels).

# Part 1

def vowel_count(str:str):
    vowel = "aeiouAEIOU"
    count = 0
    for char in str:
        if char in vowel:
            count += 1

    return count

vowel_count("eat")
vowel_count("cool")

#Define a function named short_lists that takes one parameter of type list[list[int]].
# This function must return a new list consisting of those elements of the input list (in the same order) that are of length 2.
# Part 2
def short_lists(perfect_list: list[list[int]]) -> list[list[int]]:
    result = []
    for num in perfect_list:
        if len(num) == 2:
            result.append(num)
    return result

short_lists([[5,10],[5],[10]])
short_lists([[6],[4,9]])

#Define a function named ascending_pairs that takes one parameter of type list[list[int]].
# This function must return a new list with elements (the nested lists) matching those of the input list (in the same order)
# but such that any nested list of length 2 in the result has its elements in ascending order
# (really, non-descending; i.e., the first element will be less than or equal to the second).
# The elements of nested lists of length not equal to 2 must remain in the same order as in the input.
# Part 3
def ascending_pairs(perfect_list: list[list[int]]) -> list[list[int]]:
    result = []
    for num in perfect_list:
        if len(num) == 2:
            result.append(sorted(num))
        else:
            result.append(num)
    return result

ascending_pairs([[5,10],[5,11],[10,30]])
ascending_pairs([[6,7],[4,9],[33,50]])

#Define a function named add_prices with two parameters each of type Price (defined in the provided files).
# This function must compute and return the sum of the input prices as a new Price object but initialized such that the number of cents is not above 99.
# There are multiple valid approaches to the implementation of this function including with or without the use of a conditional statement.
#Your implementation may assume that the prices passed to the function are properly formed such that the cents are within the range 0-99.

# Part 4

class Price:
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents
    def __repr__(self) -> str:
        return 'Price({}, {})'.format(self.dollars, self.cents)
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Price and
                self.dollars == other.dollars and
                self.cents == other.cents)

def add_prices(price_one: Price, price_two: Price) -> Price:
    total_dollars = price_one.dollars + price_two.dollars
    total_cents = price_one.cents + price_two.cents
    if total_cents >= 100:
        total_dollars += total_cents // 100
        total_cents = total_cents % 100
    return Price(total_dollars, total_cents)

add_prices(Price(20,50),Price(23,70))
add_prices(Price(10,73),Price(12,62))

#Define a function named rectangle_area with one parameter of type Rectangle (defined in the provided files).
# This function must compute and return the area of the provided rectangle with the assumption that the rectangle is properly axis-aligned
# (i.e., the top-left corner is above and to the left of the bottom-right corner, the vertical sides of the rectangle are parallel to the y-axis,
# and the horizontal sides of the rectangle are parallel to the x-axis).

# Part 5
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return 'Point({}, {})'.format(self.x, self.y)
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Point and
                math.isclose(self.x, other.x) and
                math.isclose(self.y, other.y))
class Rectangle:
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right
    def __repr__(self) -> str:
        return 'Rectangle({}, {})'.format(self.top_left, self.bottom_right)
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Rectangle and
                self.top_left == other.top_left and
                self.bottom_right == other.bottom_right)

def rectangle_area(rectangle:Rectangle) -> float:
    width = rectangle.bottom_right.x - rectangle.top_left.x
    height = rectangle.top_left.y - rectangle.bottom_right.y

    return width * height

rectangle_area(Rectangle(Point(4,2),Point(7,2)))
rectangle_area(Rectangle(Point(5,9),Point(2,1)))



#Define a function named books_by_author with two parameters; the first is of type str denoting an intended author name
# and the second is of type list[Book] (Book is defined in the provided files).
# This function must return a list of all books (of type list[Book]) in the input list written by the author specified in the first parameter.
#This function might be used to find books by a favorite or a recommended author.

# Part 6
class Book:
    def __init__(self, authors: list[str], title: str):
        self.authors = authors
        self.title = title
    def __repr__(self):
        return "Book({}, '{}')".format(self.authors, self.title)
    def __eq__(self, other):
        return (self is other or
                type(other) == Book and
                self.authors == other.authors and
                self.title == other.title)
def books_by_author(name:str,books: list[Book]) -> list[str]:
    result = []
    for book in books:
        if name in book.authors:
            result.append(book.title)
    return result

books_by_author("tony hunt", ["tony hunt", "title"])
books_by_author("frank jones", ["frank jones", "title"])

#Define a function named circle_bound with one parameter of type Rectangle.
# This function must return a Circle (defined in the provided files) object that represents a "bounding circle" for the provided rectangle.
# Such a bounding circle should be the smallest circle that encloses the rectangle;
# the circle should be centered at the center of the rectangle with radius equal to the distance from the center to one of the corner points.
#Such bounding circles (or bounding shapes in general, and typically in three-dimensions)
# are used to reduce the computational cost required to check for potential collisions in 3d environments including use in
# robot route planning and navigation for automated vehicles.

# Part 7
class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius
    def __repr__(self) -> str:
        return 'Circle({}, {})'.format(self.center, self.radius)
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Circle and
                self.center == other.center and
                math.isclose(self.radius, other.radius))
def circle_bound(rectangle: Rectangle) -> Circle:
    center_x = (rectangle.top_left.x + rectangle.bottom_right.x) / 2
    center_y = (rectangle.top_left.y + rectangle.bottom_right.y) / 2
    center = Point(center_x, center_y)
    corner_x = rectangle.top_left.x
    corner_y = rectangle.top_left.y
    radius = math.sqrt((center_x - corner_x) ** 2 + (center_y - corner_y) ** 2)
    return Circle(center, radius)

circle_bound((0, 4),(4, 0))
circle_bound((2,8), (3,6))


#Define a function named below_pay_average with one parameter of type list[Employee] (Employee is defined in the provided files).
# This function must return a list (of type list[str]) of the names of employees that are being paid less than the average pay of all employees in the list.
# The implementation of this function will require computing the average employee pay rate.
# Your function should work properly when the input list is empty.
#This function might be used to identify those employees whose pay may be artificially lower than their coworkers.

# Part 8
class Employee:
    def __init__(self, name: str, pay_rate: int):
        self.name = name
        self.pay_rate = pay_rate
    def __repr__(self):
        return "Employee('{}', {})".format(self.name, self.pay_rate)
    def __eq__(self, other):
        return (other is self or
                type(other) == Employee and
                self.name == other.name and
                self.pay_rate == other.pay_rate)


def below_pay_average(employees: list[Employee]) -> list[str]:
    if not employees:
        return []
    total_pay = sum(employee.pay_rate for employee in employees)
    average_pay = total_pay / len(employees)
    below_average = [employee.name for employee in employees if employee.pay_rate < average_pay]
    return below_average

below_pay_average(Employee("Alice", 50000),Employee("Bob", 60000),Employee("Charlie", 40000))
below_pay_average(Employee("Alice", 30000),Employee("Bob", 50000),Employee("Charlie", 10000))
