import math


def calculate_distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


def get_destruction_queue(map, x, y):
    destruction_queue = {}

    for y1, row in enumerate(map):
        for x1, column in enumerate(row):
            if x == x1 and y == y1:
                continue

            if column == '#':
                angle = math.atan2(y1 - y, x1 - x) + math.pi * 0.5
                if angle < 0:
                    angle += 2 * math.pi

                if angle not in destruction_queue:
                    destruction_queue[angle] = []

                destruction_queue[angle] += [(x1, y1, calculate_distance(x, y, x1, y1))]

    return destruction_queue


def count_visible_astroids(map, x, y):
    detected_astroids = {}

    if map[y][x] == '.':
        return '.'

    for y1, row in enumerate(map):
        for x1, column in enumerate(row):
            if x == x1 and y == y1:
                continue

            if column == '#':
                angle = math.atan2(y1 - y, x1 - x)

                if angle not in detected_astroids:
                    detected_astroids[angle] = (y1, x1)

    return len(detected_astroids)


def create_astroid_count_map(map):
    return [
        [count_visible_astroids(map, x, y) for x, col in enumerate(row)]
        for y, row in enumerate(map)
    ]


def read_input_to_2d_array(input):
    return [[item for item in line.strip()] for line in input]


def print_map(map):
    [print(' '.join(str(item) for item in row)) for row in map]


def find_astroids_with_best_visibility(map_with_count):
    flattened = [(x, y, count) for y, row in enumerate(map_with_count) for x, count in enumerate(row) if isinstance(count, int)]
    return max(flattened, key=lambda item : item[2])


def destroy_astroids(destruction_queue: dict):
    destruction_count = 1
    while len(destruction_queue) > 0:
        for angle in sorted(destruction_queue.keys()):
            queue = destruction_queue[angle]
            closest_astroid = min(queue, key=lambda item: item[2])

            print(destruction_count, 'destroying astroid at', closest_astroid[0], closest_astroid[1])

            index = queue.index(closest_astroid)
            del destruction_queue[angle][index]

            if len(destruction_queue[angle]) == 0:
                del destruction_queue[angle]

            destruction_count += 1


if __name__ == '__main__':
    map = read_input_to_2d_array(open("10_input.txt", 'r').readlines())

    astroid_count_map = create_astroid_count_map(map)
    base_x, base_y, visible_count = find_astroids_with_best_visibility(astroid_count_map)
    destruction_queue = get_destruction_queue(map, base_x, base_y)
    destroy_astroids(destruction_queue)