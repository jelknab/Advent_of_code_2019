from day_7.int_code_machine import Program


class Amp:
    def __init__(self, phase: int, program_code):
        self.next_amp = None
        self.phase = phase
        self.program = Program(program_code, self.handle_input, self.handle_output)
        self.has_run = False
        self.input_location = 0
        self.last_output = 0

    def handle_input(self, program_code_location):
        self.input_location = program_code_location

    def handle_output(self, output):
        self.last_output = output
        self.next_amp.run(output)

    def run(self, input):
        if not self.has_run:
            self.program.run()
            self.program.program[self.input_location] = self.phase
            self.program.run()
            self.has_run = True

        self.program.program[self.input_location] = input
        self.program.run()


def read_csv_to_array(file_path: str) -> []:
    return [int(value) for value in open(file_path, 'r').read().split(',')]


def check_amplifier_sequence(program, phase_settings):
    amps = [Amp(phase_setting, program[:]) for phase_setting in phase_settings]

    def get_next_amp(amp):
        return amps[(amps.index(amp) + 1) % len(amps)]

    for amp in amps:
        amp.next_amp = get_next_amp(amp)

    amps[0].run(0)
    return amps[4].last_output


def get_digit(number, n):
    return number // 10**n % 10


def find_best_amplification_sequence(program, offset):
    highest_signal = 0

    for i in range(0, 5**5):
        settings = [(i // (5**digit)) % 5 + offset for digit in range(0, 5)]
        if len(settings) == len(set(settings)):
            highest_signal = max(check_amplifier_sequence(program, settings), highest_signal)

    return highest_signal


if __name__ == '__main__':
    program = read_csv_to_array("7_input.txt")
    print(find_best_amplification_sequence(program, 5))

