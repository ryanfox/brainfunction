import sys

import re
from collections import defaultdict


class Brain(object):
    def __init__(self, functions):
        self.functions = functions
        self.function_pointer = 0
        self.instruction_pointer = 0

    def execute(self, fn=None, arg=None):
        if fn is None:
            fn = self.functions[0]

        program = fn.program
        instruction_pointer = 0
        cell_pointer = 0
        function_pointer = 0
        cells = defaultdict(int)

        if arg is not None:
            cells[0] = arg

        # actually eval the program
        while instruction_pointer < len(program):
            instruction = program[instruction_pointer]

            # increment cell value
            if instruction == '+':
                cells[cell_pointer] += 1

            # decrement cell value
            elif instruction == '-':
                cells[cell_pointer] -= 1

            # move cell pointer left
            elif instruction == '<':
                cell_pointer -= 1

            # move cell pointer right
            elif instruction == '>':
                cell_pointer += 1

            # read
            elif instruction == ',':
                cells[cell_pointer] = ord(input('bf > '))

            # write
            elif instruction == '.':
                print(chr(cells[cell_pointer]), end='', flush=True)

            # start loop
            elif instruction == '[':
                if cells[cell_pointer] == 0:
                    instruction_pointer = fn.opens[instruction_pointer]

            # end loop
            elif instruction == ']':
                if cells[cell_pointer] != 0:
                    instruction_pointer = fn.closes[instruction_pointer]

            # move function pointer down
            elif instruction == 'v':
                function_pointer += 1

            # move function pointer up
            elif instruction == '^':
                function_pointer -= 1

            # call function
            elif instruction == ':':
                cells[cell_pointer] = self.execute(self.functions[function_pointer], cells[cell_pointer])

            # return
            elif instruction == ';':
                return cells[cell_pointer]

            instruction_pointer += 1

        return cells[cell_pointer]



class Function(object):
    def __init__(self, program):
        self.program = list(program)
        self.opens, self.closes = Function._parse_loops(program)

    @staticmethod
    def _parse_loops(program):
        loops = []
        opens = {}
        closes = {}

        for i, character in enumerate(program):
            if character == '[':
                loops.append(i)
            elif character == ']':
                start = loops.pop()
                opens[start] = i
                closes[i] = start

        if len(loops) != 0:
            raise SyntaxError('opening and closing brackets don\'t match')

        return opens, closes


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python brainfunction.py <input.b>')
        sys.exit(1)

    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]

        filtered = [re.sub('[^+-[\],.<>:;^v]', '', line) for line in lines]
        functions = [Function(function) for function in filtered]

        brain = Brain(functions)
        brain.execute()
