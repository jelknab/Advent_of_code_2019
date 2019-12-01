def read_module_masses_from_file(file_path: str) -> []:
    return [int(line) for line in open(file_path, "r")]


def calculate_fuel_consumption(mass: int) -> int:
    return mass // 3 - 2


def calculate_fuel_fuel_consumption(fuel: int):
    fuel_consumption = calculate_fuel_consumption(fuel)

    if fuel_consumption > 6:
        fuel_consumption += calculate_fuel_fuel_consumption(fuel_consumption)

    return fuel_consumption


if __name__ == '__main__':
    total_fuel_required = 0

    for module_mass in read_module_masses_from_file("day_1/1_input.txt"):
        module_fuel_required = calculate_fuel_consumption(module_mass)
        module_fuel_fuel_required = calculate_fuel_fuel_consumption(module_fuel_required)

        total_fuel_required += module_fuel_required + module_fuel_fuel_required

    print("Fuel required for modules and fuel:",  total_fuel_required)
