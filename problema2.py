# for problema2 i chose python because it was easier to find all the rectangles with sets
# Given some points in cartesian coordinate, (X, Y) find the number
# of rectangles that can be created by those points.

# Take into consideration only the rectangles that are parallel with the X, Y axes.

# Function to find number of all possible rectangles

def nr_Rectangles(obj):

    # Here I made a TreeSet to contain the elements
    # keep in mind that sets are used to store multiple items in a single variable
    set_nr = set()

    # here I added the pairs from sample to the set
    for i in range(len(obj)):
        set_nr.add(f"{obj[i]}");

    sides = 0;
    for i in range(len(obj)):
        for j in range(len(obj)):
            if (obj[i][0] != obj[j][0] and obj[i][1] != obj[j][1]):

                # Searching for the pairs in the set
                if (f"{[obj[i][0], obj[j][1]]}" in set_nr and f"{[obj[j][0], obj[i][1]]}" in set_nr):
                    # Increase the sides
                    sides += 1

    # Return how many rectangles has been found
    # after we found all the sides we divided to 4 ( 1 rectangle - 4 sides)
    return int(sides / 4);


if __name__ == "__main__":

    # sample input 1

    # number of points
    nr_points = 6;
    obj = [0] * nr_points
    # now we pot the points into a list
    obj[0] = [1, 1];
    obj[1] = [1, 3];
    obj[2] = [2, 1];
    obj[3] = [2, 3];
    obj[4] = [3, 1];
    obj[5] = [3, 3];

    print("First sample result: ", nr_Rectangles(obj));

    # sample input 2

    # number of points
    nr_points = 5;
    obj = [0] * nr_points
    obj[0] = [1, 1];
    obj[1] = [1, 3];
    obj[2] = [2, 3];
    obj[3] = [3, 1];
    obj[4] = [3, 3];

    print("Second sample result: ", nr_Rectangles(obj));


# Result:
# First sample result:  3
# Second sample result:  1