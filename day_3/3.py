from collections import defaultdict


def distance(a: tuple, b:tuple):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def find_closest_intersection(intersections):
    return min(intersections, key = lambda item:item[2])


def find_least_steps(intersections):
    return min(intersections, key = lambda item:item[3])


def find_intersections(a, b):
    intersections = []

    for y in a.keys():
        for x in a[y].keys():
            if y in b and x in b[y]:
                step_sum = a[y][x] + b[y][x]
                intersections.append((x, y, distance((0, 0), (x, y)), step_sum))

    return intersections


def add_distance_north(grid, point) -> tuple:
    grid[point[0]][point[1] + 1] = True
    return grid, point[0], point[1] + 1


def add_distance_south(grid, point) -> tuple:
    grid[point[0]][point[1] - 1] = True
    return grid, point[0], point[1] - 1


def add_distance_east(grid, point) -> tuple:
    grid[point[0] + 1][point[1]] = True
    return grid, point[0] + 1, point[1]


def add_distance_west(grid, point) -> tuple:
    grid[point[0] - 1][point[1]] = True
    return grid, point[0] - 1, point[1]


def directions_line_to_array(line: str) -> []:
    return [direction for direction in line.split(',')]


def read_input_to_array(file_path: str) -> []:
    return [line.strip() for line in open(file_path, 'r').readlines()]


headings = {
    'U': add_distance_north,
    'D': add_distance_south,
    'R': add_distance_east,
    'L': add_distance_west
}


def directions_to_grid(directions):
    origin = (0, 0)
    grid = defaultdict(dict)
    steps_taken = 0

    for direction in directions:
        heading = direction[0]
        steps = int(direction[1:])

        for step in range(steps):
            grid, x, y = headings[heading](grid, origin)
            origin = (x, y)

            steps_taken += 1
            grid[x][y] = steps_taken

    return grid


if __name__ == '__main__':
    input_lines = read_input_to_array("3_input.txt")
    wire_1 = directions_to_grid(directions_line_to_array(input_lines[0]))
    wire_2 = directions_to_grid(directions_line_to_array(input_lines[1]))

    print("closest intersection", find_closest_intersection(find_intersections(wire_1, wire_2))[2])
    print("least steps", find_least_steps(find_intersections(wire_1, wire_2))[3])
