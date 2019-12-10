from day_9.int_code_machine import Program


def read_csv_to_array(file_path: str) -> []:
    return [int(value) for value in open(file_path, 'r').read().split(',')]


if __name__ == '__main__':
    Program([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99], lambda pos: 0, lambda output: print(output)).run()
    Program([1102,34915192,34915192,7,4,7,99,0], lambda pos: 0, lambda output: print(output)).run()
    Program([104,1125899906842624,99], lambda pos: 0, lambda output: print(output)).run()

    program_code = read_csv_to_array("9_input.txt")
    program = None

    def handle_input(position):
        program.program[position] = 2

    program = Program(program_code, handle_input, lambda output: print(output))
    print("running program")
    program.run()
    print("continuing")
    program.run()