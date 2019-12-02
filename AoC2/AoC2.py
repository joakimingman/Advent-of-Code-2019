f = list(map(int, open("input").read().split(",")))


def intcode_list(instructions: list, noun: int, verb: int) -> list:
    instr = instructions[:]
    instr[1] = noun
    instr[2] = verb
    i = 0
    while instr[i] != 99:
        if instr[i] == 1:
            instr[instr[i + 3]] = instr[instr[i + 1]] + instr[instr[i + 2]]
        elif instr[i] == 2:
            instr[instr[i + 3]] = instr[instr[i + 1]] * instr[instr[i + 2]]
        i += 4
    return instr


def intcoder_pt1() -> int:
    return intcode_list(f, 12, 2)[0]


def intcoder_pt2() -> int:
    for noun in range(100):
        for verb in range(100):
            if intcode_list(f, noun, verb)[0] == 19690720:
                return 100 * noun + verb


print(intcoder_pt1())
print(intcoder_pt2())
