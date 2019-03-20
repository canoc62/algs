number_mappings = {
        "0": "0",
        "1": "1",
        "2": "ABC",
        "3": "DEF",
        "4": "GHI",
        "5": "JKL",
        "6": "MNO",
        "7": "PQRS",
        "8": "TUV",
        "9": "WXYZ"
}

def phone_mnemonics(number, curr_str="", results=None):
    if results is None:
        results = []
    if len(number) == 1:
        for char in number_mappings[number]:
            results.append(curr_str + char)
    else:
        for char in number_mappings[number[0]]:
            results = phone_mnemonics(number[1:], curr_str + char, results)

    return results


print(phone_mnemonics("0"))
print(phone_mnemonics("01"))
print(phone_mnemonics("8"))
print(phone_mnemonics("983"))
print(phone_mnemonics("23"))
