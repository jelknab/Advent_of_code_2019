function_parameter_count = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    9: 1,
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
    9: None,
    99: 0
}


class Program:
    def __init__(self, program, handle_input, handle_output):
        self.handle_output = handle_output
        self.handle_input = handle_input
        self.program = {i: program[i] for i in range(0, len(program))}
        self.pointer = 0
        self.relative_base = 0

    def add_function(self, parameters: []):
        self.program[parameters[2]] = parameters[0] + parameters[1]
        self.pointer += 4

    def multiply_function(self, parameters: []):
        self.program[parameters[2]] = parameters[0] * parameters[1]
        self.pointer += 4

    def input_function(self, parameters: []):
        print("INPUT FOR POSITION", parameters[0])
        self.pointer += 2
        self.handle_input(parameters[0])

    def output_function(self, parameters: []):
        self.pointer += 2
        self.handle_output(parameters[0])

    def jump_if_true_function(self, parameters: []):
        if parameters[0] != 0:
            self.pointer = parameters[1]
            return

        self.pointer += 3

    def jump_if_false_function(self, parameters: []):
        if parameters[0] == 0:
            self.pointer = parameters[1]
            return

        self.pointer += 3

    def less_than_function(self, parameters: []):
        if parameters[0] < parameters[1]:
            self.program[parameters[2]] = 1
        else:
            self.program[parameters[2]] = 0

        self.pointer += 4

    def equal_function(self, parameters: []):
        if parameters[0] == parameters[1]:
            self.program[parameters[2]] = 1
        else:
            self.program[parameters[2]] = 0

        self.pointer += 4

    def adjust_relative_base(self, parameters: []):
        self.relative_base += parameters[0]
        self.pointer += 2

    def parse_parameter(self, parameter_value, parameter_type):
        if parameter_type == 0:
            if parameter_value in self.program:
                return self.program[parameter_value]
            return 0

        if parameter_type == 1:
            return parameter_value

        if parameter_type == 2:
            return self.program[self.relative_base + parameter_value]

    op_code_functions = {
        1: add_function,
        2: multiply_function,
        3: input_function,
        4: output_function,
        5: jump_if_true_function,
        6: jump_if_false_function,
        7: less_than_function,
        8: equal_function,
        9: adjust_relative_base
    }

    def parse_instruction(self):
        global function_parameter_count
        global function_output_parameter

        instruction = str(self.program[self.pointer])
        op_code = int(instruction[-2:])

        parameter_count = function_parameter_count[op_code]

        parameters = [None] * parameter_count
        for param_i in range(1, parameter_count+ 1):
            parameter_value = self.program[self.pointer + param_i]
            parameter_setting_index = len(instruction) - 2 - param_i

            if parameter_setting_index < 0:
                parameter_setting = 0
            else:
                parameter_setting = int(instruction[parameter_setting_index])

            if param_i == function_output_parameter[op_code]:
                parameters[param_i - 1] = parameter_value
                if parameter_setting == 2:
                    parameters[param_i - 1] = self.relative_base + parameter_value
            else:
                parameters[param_i-1] = self.parse_parameter(parameter_value, parameter_setting)

        return op_code, parameters

    def run(self):
        while self.pointer < len(self.program):
            op_code, parameters = self.parse_instruction()

            if op_code == 99:
                return True

            self.op_code_functions[op_code](self, parameters)

            if op_code == 3:
                return False
