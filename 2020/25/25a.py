def find_loop_size(public_key):
    value = 1
    loop_size = 0
    while value != public_key:
        value *= 7
        value %= 20201227
        loop_size += 1 
    return loop_size

def find_encryption_key(loop_size, public_key):
    encryption_key = 1
    for _ in range(loop_size):
        encryption_key *= public_key
        encryption_key %= 20201227
    return encryption_key

# Test
# CARDS_PK = 5764801
# DOORS_PK = 17807724

CARDS_PK = 17773298
DOORS_PK = 15530095

cards_loop_size = find_loop_size(CARDS_PK)
doors_loop_size = find_loop_size(DOORS_PK)

if cards_loop_size < doors_loop_size:
    encryption_key = find_encryption_key(cards_loop_size, DOORS_PK)
else:
    encryption_key = find_encryption_key(doors_loop_size, CARDS_PK)

print(encryption_key)