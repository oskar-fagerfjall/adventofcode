def mask_on( mask ):
  ''' X10X0110 gives 01000110, apply with OR '''
  return mask.translate( str.maketrans("10X", "100"))

def mask_off( mask ):
  ''' X10X0110 gives 11010110, apply with AND '''
  return mask.translate( str.maketrans("10X", "101"))
  
def apply_mask( m, x ):
  x |= int( mask_on( m ) , 2)  # Bitwise OR for setting bits to 1
  x &= int( mask_off( m ), 2)  # Bitwise AND for setting bits to 0
  return x

mask = ""
with open( "2020/14/input.txt", "r") as f:
    contents = f.read()
contents = contents.split("\n")

memory = {}
for line in contents:
    if len( line ) == 0:
        continue
    cmd = line.strip()
    if cmd[0:4] == "mask":
        mask = cmd[7:]
    else:
        mem, value = cmd.split("] = ", 2)
        addr = int( mem[4:] )
        value = int( value )
        memory[addr] = apply_mask( mask, value)

total = 0
for v in memory.values():
    total += v

print( total )
