def xor_dividend(dividend, divisor):
    dividend = list(dividend)
    divisor = list(divisor)
    len_divisor = len(divisor)
    
    for i in range(len(dividend) - len_divisor + 1):
        if dividend[i] == '1':
            for j in range(len_divisor):
                dividend[i + j] = '1' if dividend[i + j] != divisor[j] else '0'
    
    return ''.join(dividend)

def generate_crc(data, divisor):
    data += '0' * (len(divisor) - 1)
    remainder = xor_dividend(data, divisor)
    return data + remainder[-(len(divisor) - 1):]

def detect_errors(codeword, divisor):
    remainder = xor_dividend(codeword, divisor)
    return '1' in remainder

# Example usage
data = "110101"
divisor = "1011"

codeword = generate_crc(data, divisor)
print(f"Transmitted Codeword: {codeword}")

# Introducing an error by flipping a bit
error_codeword = list(codeword)
error_codeword[3] = '1'
error_codeword = ''.join(error_codeword)

if detect_errors(error_codeword, divisor):
    print("Error Detected!")
else:
    print("No Error Detected.")
