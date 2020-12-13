class CPU():
    def __init__( self, asm ):
        self.asm = asm
        self.pc = 0
        self.accumulator = 0
        self.visited = [] 
        self.program_length = len( asm )
        self.just_playing = False

    def mark_visited( self ):
        self.visited.append( self.pc )

    def is_visited( self ):
        return self.pc in self.visited

    def get_command( self ):
        return self.asm[ self.pc ]

    def solution1( self ):
        while True:
            if self.is_visited():
                return( self.accumulator )
            else:
                self.mark_visited()
            command, argument = self.get_command()
            if command == "nop":
                self.pc += 1
            elif command == "acc":
                self.accumulator += int( argument )
                self.pc += 1
            elif command == "jmp":
                self.pc += int( argument )

    def solution2( self ):
        while True:
            if self.is_visited():
                raise ValueError
            elif self.pc >= self.program_length:
                return self.accumulator
            else:
                self.mark_visited()
            command, argument = self.get_command()
            if command == "nop":
                if not self.just_playing:
                    try:
                        cpu3 = CPU( asm )
                        cpu3.just_playing = True
                        cpu3.asm[ self.pc ][0] = "jmp"
                        return cpu3.solution2()
                    except ValueError:
                        pass
                self.pc += 1
            elif command == "acc":
                self.accumulator += int( argument )
                self.pc += 1
            elif command == "jmp":
                if not self.just_playing:
                    try:
                        cpu3 = CPU( asm )
                        cpu3.just_playing = True
                        cpu3.asm[ self.pc ][0] = "nop"
                        return cpu3.solution2()
                    except ValueError:
                        pass
                self.pc += int( argument )


with open( '2020/08/input.txt', 'r') as infile:
    asm = infile.read().split("\n")
    asm = [x.split() for x in asm]


cpu1 = CPU( asm )
cpu2 = CPU( asm )
print( str( cpu1.solution1()))
print( str( cpu2.solution2()))

