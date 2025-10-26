class BrainfuckInterpreter:
    def __init__(self, code, LEN_MEMORY=100):
        self.code = self.clean_code(code)
        self.bracket_positions = {}
        self.find_bracket_pairs()
        
        self.memory = [0] * LEN_MEMORY
        self.pointer = 0
        
    def clean_code(self, code):
        return ''.join([c for c in code if c in '><+-.,[]'])
    
    def find_bracket_pairs(self):
        stack = []
        for i, char in enumerate(self.code):
            if char == '[':
                stack.append(i)
            elif char == ']':
                if not stack:
                    raise SyntaxError("Несоответствие скобок")
                start = stack.pop()
                self.bracket_positions[start] = i
                self.bracket_positions[i] = start
                
    def run(self):
        i = 0
        while i < len(self.code):
            char = self.code[i]
            
            if char == '>':
                self.pointer += 1
            elif char == '<':
                self.pointer -= 1
            elif char == '+':
                self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 256
            elif char == '-':
                self.memory[self.pointer] = (self.memory[self.pointer] - 1) % 256
            elif char == '.':
                print(chr(self.memory[self.pointer]), end='')
            elif char == ',':
                self.memory[self.pointer] = ord( input("")[0] )
            elif char == '[':
                if self.memory[self.pointer] == 0:
                    i = self.bracket_positions[i]
            elif char == ']':
                if self.memory[self.pointer] != 0:
                    i = self.bracket_positions[i] - 1
                    
            i += 1
            

if __name__ == "__main__":
    brainfuck_code = """
    +[>>+<<-]
    """
    
    interpreter = BrainfuckInterpreter(brainfuck_code, 10)
    interpreter.run()
    print( interpreter.memory )
