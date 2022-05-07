import hashlib

input = "ckczppom"

def hash_function():
    start = 1
    result = input + str(start)
    hex_value = hashlib.md5(result.encode()).hexdigest()
    while hex_value[:5] != "00000":
        start +=1
        result = input + str(start)
        hex_value = hashlib.md5(result.encode()).hexdigest()
        print(start)
        if start > 9999999:
            print(f"exceeded {start}")
            return
    print(f"Hex value: {hex_value}, number: {start}")
    return 

hash_function()