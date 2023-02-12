def numToString(i):
    stringInteger = str(i)
    hashmap = {'0':'zero', '1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

    result = []
    for char in stringInteger:
        result.append(hashmap[char])

    print(" ".join(result))
    return " ".join(result)

# numToString(0)