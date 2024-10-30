def dnaToBits(dna, baseKey, tagLength):
    bits = []

    if len(dna)/(tagLength+1) != int(len(dna)/(tagLength+1)):
        print("Tag length error!")
        return -1

    for i in range(int(len(dna)/(tagLength+1))):
        bits.append([baseKey[dna[i*(tagLength+1)]], dna[i*(tagLength+1)+1:(i+1)*(tagLength+1)]])
        
    return bits

def bitsToCRISPR(bits, bitKey):
    crispr = [[bitKey[i[0]], i[1]] for i in bits]
    
    return crispr

def writeToBits(bits, data):
    if len(bits) != len(data):
        print("Data length error!")

    for i in range(len(bits)):
        bits[i][0] = data[i]

    return bits

def displayData(data):
    displayableData = ''
    
    for i in bits:
        displayableData += i[0]

    return displayableData

baseKey = {
    'A':'0',
    'T':'0',
    'C':'1',
    'G':'1'
}

bitKey = {
    '0':'A',
    '1':'C',
}

## Testing code, ignore
if __name__ == '__main__':
    bits = dnaToBits(input("Enter your DNA:\n"), baseKey, 3)
    print('RAW BITS:', bits)
    print('DATA:', displayData(bits))
    bits = writeToBits(bits, input("Enter your new data:\n"))
    print("CRIPSR:", bitsToCRISPR(bits, bitKey))