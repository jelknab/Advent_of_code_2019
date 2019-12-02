def add_function(a, b):
    return a + b


def multiply_function(a, b):
    return a * b


def read_csv_to_array(file_path: str) -> []:
    return [int(value) for value in open(file_path, 'r').read().split(',')]


def run_instruction(program: [], instruction_index):
    instruction_code = program[instruction_index]
    var_1 = program[program[instruction_index + 1]]
    var_2 = program[program[instruction_index + 2]]
    output_position = program[instruction_index + 3]

    program[output_position] = op_code_functions[instruction_code](var_1, var_2)

    return program


def run_program(program: []):
    program_index = 0

    while program_index < len(program):
        instruction_method = program[program_index]

        if instruction_method == 99:
            break

        program = run_instruction(program, program_index)

        program_index += 4

    return program


op_code_functions = {
    1: add_function,
    2: multiply_function
}


if __name__ == '__main__':
    origin_program = read_csv_to_array("2_input.txt")

    for i in range(99*99):
        program = origin_program[:]
        program[1] = i % 99
        program[2] = i // 99

        if run_program(program)[0] == 19690720:
            print("noun", program[1], "verb", program[2], "output", 100 * program[1] + program[2])



