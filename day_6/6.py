def read_input_file_to_orbit_list(file_path):
    return [line.strip() for line in open(file_path, 'r')]


def orbit_list_to_tree(orbit_list):
    orbits = [orbit.split(")") for orbit in orbit_list]

    objects = {}

    for orbit in orbits:
        parent = orbit[0]
        child = orbit[1]

        if parent not in objects:
            objects[parent] = None

        objects[child] = parent

    return objects


def count_orbits(orbits):
    count = 0

    for child, parent in orbits.items():
        if parent is not None:
            count += len(get_path_to_target(orbits, child, None))

    return count


def get_path_to_target(orbits, start, target):
    path = []

    object = orbits[start]

    while object is not None and object is not target:
        path.append(object)
        object = orbits[object]

    return path


def minimum_orbital_transfers_between_orbits(orbits, current, target):
    current_to_origin = get_path_to_target(orbits, current, None)
    target_to_origin = get_path_to_target(orbits, target, None)
    combined_orbits_count = len(current_to_origin) + len(target_to_origin)

    common_parents = list(set(current_to_origin) & set(target_to_origin))
    distance_to_parent = {}

    for parent in common_parents:
        distance_to_parent[parent] = combined_orbits_count - (len(get_path_to_target(orbits, parent, None)) + 1) * 2

    closest_common_parent = min(distance_to_parent, key=distance_to_parent.get)
    return distance_to_parent[closest_common_parent]


if __name__ == '__main__':
    orbits = orbit_list_to_tree(["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"])
    print("example checksum:", count_orbits(orbits))

    orbits = orbit_list_to_tree(["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L", "K)YOU", "I)SAN"])
    print("example required orbit changes:", minimum_orbital_transfers_between_orbits(orbits, "YOU", "SAN"))

    orbits = orbit_list_to_tree(read_input_file_to_orbit_list("6_input.txt"))
    print("checksum:", count_orbits(orbits))
    print("required orbit changes to santa:", minimum_orbital_transfers_between_orbits(orbits, "YOU", "SAN"))