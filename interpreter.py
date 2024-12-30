import random
#import time
class Interpreter:
    def __init__(self, program):
        self.direction = (1,0)
        self.pos = (0,0)
        self.program = program
        self.memory = {0:0}
        self.stack = []
        self.running = False
        self.DIRECTIONS = {
            'right': (1, 0),
            'left': (-1, 0),
            'up': (0, -1),
            'down': (0, 1)
        }
        self.OPERATIONS = {
            (0,0,136): self.op_load,
            (0,136,0): self.op_store,
            (173,216,230): self.op_incptr,
            (84,84,235): self.op_decptr,
            (173,0,0): self.op_pop,
            (255,145,0): self.op_dup,
            (255,208,0): self.op_swap,
            (128,0,128): self.op_inc,
            (255,192,203): self.op_dec,
            (255, 0, 0): self.op_add,
            (0, 0, 170): self.op_sub,
            (255,0,255): self.op_mul,
            (160,160,160): self.op_div,
            (92, 92, 92): self.op_mod,
            (0,0,255): self.op_left,
            (0,0,80): self.op_right,
            (0,255,0): self.op_up,
            (0,80,0): self.op_down,
            (196,196,196): self.op_mirror,
            (255, 255, 255): self.op_skip,
            (28, 27, 27): self.op_cond_skip,
            (0,255,255): self.op_print_num,
            (0,128,128): self.op_print_str,
            (0,170,0): self.op_revstack,
            (75,0,130): self.op_input,
            (139, 0, 0): self.op_end,
            (64, 224, 208): self.op_rndpc,
            

        }
        self.ptr = 0

    def move(self, b: tuple):
        self.pos = tuple(map(sum,zip(self.pos,b)))

    def execute(self):
        self.running = True
        while self.running:
            if (self.pos[0] < 0 or self.pos[1] < 0) or (self.pos[0] >= len(self.program) or 
                (self.pos[0] < len(self.program) and self.pos[1] >= len(self.program[self.pos[0]]))):
                raise Exception("\nPointer escaped. Shutting down")
            color = tuple(self.program[self.pos[0]][self.pos[1]])
            if color in self.OPERATIONS:
                self.OPERATIONS[color]()
                #print("\n", self.pos, self.direction, self.memory, self.stack, color, self.ptr)
                #time.sleep(0.1)
            self.move(self.direction)



    def get_mem(self, pointer):
        return self.memory.get(pointer, 0)
    
    def pop_stack(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise Exception("\nStack underflow")
        

    def op_load(self):
        self.stack.append(self.get_mem(self.ptr))

    def op_store(self):
        self.memory[self.ptr] = self.pop_stack()

    def op_incptr(self):
        self.ptr += 1

    def op_decptr(self):
        if self.ptr > 0:
            self.ptr -= 1


    def op_pop(self):
        self.pop_stack()

    def op_dup(self):
        if len(self.stack) < 1:
            raise Exception("\nStack underflow")
        self.stack.append(self.stack[-1])

    def op_swap(self):
        if len(self.stack) < 2:
            raise Exception("\nStack underflow")
        a = self.pop_stack()
        b = self.pop_stack()
        self.stack.append(a)
        self.stack.append(b)


    def op_inc(self):
        if len(self.stack) < 1:
            raise Exception("\nStack underflow")
        self.stack[-1] += 1

    def op_dec(self):
        if len(self.stack) < 1:
            raise Exception("\nStack underflow")
        self.stack[-1] -= 1

    def op_mul(self):
        if len(self.stack) < 1:
            a = 0
            b = 0
        else:
            a = self.pop_stack()
            b = self.pop_stack()
        self.stack.append(a * b)
        
    def op_div(self):
        if len(self.stack) < 2:
            raise Exception("\nStack underflow")
        a = self.pop_stack()
        b = self.pop_stack()
        self.stack.append(a // b)   

    def op_mod(self):
        if len(self.stack) < 2:
            raise Exception("\nStack underflow")
        a = self.pop_stack()
        b = self.pop_stack()
        self.stack.append(a % b)   

    def op_add(self):
        if len(self.stack) < 1:
            a = 0
            b = 0
        else:
            a = self.pop_stack()
            b = self.pop_stack()
        self.stack.append(a + b)

    def op_sub(self):
        if len(self.stack) < 1:
            a = 0
            b = 0
        else:
            a = self.pop_stack()
            b = self.pop_stack()
        self.stack.append(a - b)


    def op_left(self):
        self.direction = self.DIRECTIONS['left']
    def op_right(self):
        self.direction = self.DIRECTIONS['right']
    def op_up(self):
        self.direction = self.DIRECTIONS['up']
    def op_down(self):
        self.direction = self.DIRECTIONS['down']

    def op_mirror(self):
        self.direction = tuple( self.direction[0] * -1, self.direction[1] * -1 )

    def op_skip(self):
        self.move(self.direction)
    
    def op_cond_skip(self):
        if self.stack and self.stack[-1] != 0:
            self.move(self.direction)
    

    def op_print_num(self):
        if len(self.stack) < 1:
            val = 0
        else:
            val = self.pop_stack()

        print(val, end='')

    def op_print_str(self):
        if len(self.stack) < 1:
            val = 0
        else:
            val = self.pop_stack()

        print(chr(val), end='')
    
    def op_input(self):
        inp = input()
        try:
            int(inp)
            self.stack.append(int(inp))
        except:
            for i in inp[::-1]:
                self.stack.append(ord(i))
    
    def op_end(self):
        self.running = False

    def op_rndpc(self):
        dirs = ['left', 'right', 'up', 'down']
        self.direction = self.DIRECTIONS[random.choice(dirs)]

    def op_revstack(self):
        self.stack = self.stack[::-1]