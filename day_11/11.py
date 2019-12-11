from day_11.int_code_machine import Program

rotation_direction = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0)
}


def move_robot(position, rotation):
    return tuple(map(lambda x, y: x + y, position, rotation_direction[rotation]))


def get_panel_color(ship_panels, robot):
    position = robot['position']

    if position[0] not in ship_panels:
        ship_panels[position[0]] = {}

    if position[1] not in ship_panels[position[0]]:
        ship_panels[position[0]][position[1]] = {
            'color': 0,  # black
            'painted': False
        }

    return ship_panels[position[0]][position[1]]['color']


def input_panel_color(ship_panels, robot, program, program_position):
    color = get_panel_color(ship_panels, robot)
    program.program[program_position] = color


def paint_panel(ship_panels, robot, new_color):
    position = robot['position']
    current_color = ship_panels[position[0]][position[1]]['color']

    if current_color != new_color:
        ship_panels[position[0]][position[1]]['color'] = new_color

        if not ship_panels[position[0]][position[1]]['painted']:
            robot['painted_panels'] = robot['painted_panels'] + 1
            ship_panels[position[0]][position[1]]['painted'] = True


def handle_output(ship_panels, robot, output):
    position = robot['position']
    rotation = robot['rotation']

    if robot['output_mode'] == 0:  # paint color
        paint_panel(ship_panels, robot, output)

    else:  # rotate ship
        robot['rotation'] = (rotation -1 + output * 2) % 4
        robot['position'] = move_robot(position, robot['rotation'])

    robot['output_mode'] = (robot['output_mode'] + 1) % 2


def print_panels(panels):
    min_y, max_y, min_x, max_x = 0, 0, 0, 0

    for y in panels.keys():
        for x in panels[y].keys():
            min_y, max_y = min(min_y, y), max(max_y, y)
            min_x, max_x = min(min_x, x), max(max_x, x)

    for x in range(min_x, max_x + 1):
        row = ''
        for y in range(min_y, max_y + 1):
            if y in panels and x in panels[y]:
                if panels[y][x]['color'] == 1:
                    row += u"\u2588"
                    continue

            row += u"\u2591"
        print(row)


if __name__ == '__main__':
    program_code = [int(value) for value in open("11_input.txt", 'r').read().split(',')]

    ship_panels = {
        0: {0: {'color': 1, 'painted': False}}
    }
    robot = {
        'position': (0, 0),
        'rotation': 0,
        'output_mode': 0,
        'painted_panels': 0
    }

    program = Program(
        program_code,
        lambda program_pos: input_panel_color(ship_panels, robot, program, program_pos),
        lambda output: handle_output(ship_panels, robot, output)
    )

    while not program.run():
        pass

    print_panels(ship_panels)
