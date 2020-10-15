# >>> dec_and_bin_same_in_reversed()
# 1 1
# 3 11
# 5 101
# 7 111
# 9 1001
# 33 100001
# 99 1100011
# 313 100111001
# 585 1001001001
# 717 1011001101
# Implement the dec_and_bin_same_in_reversed function.
# (Print all numbers from 1 to 1000 which reads the same in reversed form in both binary and decimal format.)

def dec_and_bin_same_in_reversed():
    def dec2bin(dec):
        return dec2bin(dec // 2) + str(dec % 2) if dec > 1 else str(dec % 2)

    def is_palindrom(bin):
        for i in range(len(bin) // 2):
            if bin[i] != bin[-(i + 1)]:
                return False
        return True

    for dec in range(1, 1001):
        bin = dec2bin(dec)
        if is_palindrom(bin):
            yield (dec, bin)


if __name__ == "__main__":
    for dec, bin in dec_and_bin_same_in_reversed():
        print(dec, bin)
