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

def floatmask( i, mask ):
  def _mask( a, m ):
    if m == "0":
      return a
    else:
      return m
  value = bin(i)[2:].zfill( len(mask) )
  value = map( _mask, value, mask )
  value = "".join(value)
  return value

def expand_address( m ):
  result = []
  if m.count("X") != 0:
    result.extend( expand_address( m.replace("X", "0", 1)) )
    result.extend( expand_address( m.replace("X", "1", 1)))
  else:
    result.append( m )
  return result

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



# Ouch, read the problem spec wrong. This solution generates separate masks that will be applied to
#  the address, but we are really supposed to apply the mask to the address, and then expand those addresses.
#  fixed it.
memory = {}
for line in contents:
    if len( line ) == 0:
        continue
    cmd = line.strip()
    if cmd[0:4] == "mask":
        mask = cmd[7:]
    else:
        addr, value = cmd.split("] = ", 2)
        value = int( value )
        addr = int( addr[4:] )
        addr = floatmask( addr, mask)
        addr = expand_address( addr )
        for a in addr:
          memory[ a ] = value

total = 0
for v in memory.values():
    total += v

print( total )