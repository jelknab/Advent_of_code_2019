def add_function(program, parameters: [], index):
    program[parameters[2]] = parameters[0] + parameters[1]
    return program, index + 4


def multiply_function(program, parameters: [], index):
    program[parameters[2]] = parameters[0] * parameters[1]
    return program, index + 4


def input_function(program, parameters: [], index):
    program[parameters[0]] = int(input("please give input:"))
    return program, index + 2


def output_function(program, parameters: [], index):
    print(parameters[0])
    return program, index + 2


def jump_if_true_function(program, parameters: [], index):
    if parameters[0] != 0:
        return program, parameters[1]

    return program, index + 3


def jump_if_false_function(program, parameters: [], index):
    if parameters[0] == 0:
        return program, parameters[1]

    return program, index + 3


def less_than_function(program, parameters: [], index):
    if parameters[0] < parameters[1]:
        program[parameters[2]] = 1
    else:
        program[parameters[2]] = 0

    return program, index + 4


def equal_function(program, parameters: [], index):
    if parameters[0] == parameters[1]:
        program[parameters[2]] = 1
    else:
        program[parameters[2]] = 0

    return program, index + 4


def parse_parameter(program, parameter_value, parameter_type):
    if parameter_type == 0:
        return program[parameter_value]

    if parameter_type == 1:
        return parameter_value


op_code_functions = {
    1: add_function,
    2: multiply_function,
    3: input_function,
    4: output_function,
    5: jump_if_true_function,
    6: jump_if_false_function,
    7: less_than_function,
    8: equal_function
}

function_parameter_count = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    99: 0
}

function_output_parameter = {
    1: 3,
    2: 3,
    3: 1,
    4: None,
    5: None,
    6: None,
    7: 3,
    8: 3,
    99: 0
}


def parse_instruction(program: [], position):
    instruction = str(program[position])
    op_code = int(instruction[-2:])

    parameter_count = function_parameter_count[op_code]

    parameters = [None] * parameter_count
    for param_i in range(parameter_count):
        parameter_value = program[position + 1 + param_i]
        parameter_setting_index = len(instruction) - 3 - param_i

        if param_i + 1 == function_output_parameter[op_code]:
            parameter_setting = 1
        elif parameter_setting_index < 0:
            parameter_setting = 0
        else:
            parameter_setting = int(instruction[parameter_setting_index])

        parameters[param_i] = parse_parameter(program, parameter_value, parameter_setting)

    return op_code, parameters


def run_program(program: []):
    program_index = 0

    while program_index < len(program):
        op_code, parameters = parse_instruction(program, program_index)

        if op_code == 99:
            break

        program, program_index = op_code_functions[op_code](program, parameters, program_index)

    return program


def read_csv_to_array(file_path: str) -> []:
    return [int(value) for value in open(file_path, 'r').read().split(',')]


if __name__ == '__main__':
    run_program(read_csv_to_array("5_input.txt"))