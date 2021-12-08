#problem 1
aminoAcid = ["Phe", "Val", "Asn", "Gln", "His", "Leu", "Cys", "Gly", "Ser"]
print(aminoAcid)

#problem 2
L = len(aminoAcid)
print("Number of Amino Acids present in chain: ", L)

#problem 3
aminoAcid.append('His')
print("\nAmino Acid chain with addition: ", aminoAcid)

#problem 4
def mutation(m):
    print('\nBefore Mutation')
    print(aminoAcid)
    aminoAcid[aminoAcid.index('Gly')] = m 
    print('\nAfter Mutation:')
    print(aminoAcid)

mutation('Asp')

#problem 5
def pickNprint():
    n = int(input('\nEnter a number between 1 and {}: '.format(len(aminoAcid))))
    try:
        print('Amino acid at position {} is {}'.format(n,aminoAcid[n-1]))
    except:
        print('Error occured! Choose index in given range')

pickNprint() 

#problem 6

def inverter():
    start = int(input('\nEnter start position for inversion: '))
    end = int(input('Enter end position for inversion: '))
    print('\nBefore inversion:')
    print(aminoAcid)
    start = start - 1
    temp = aminoAcid[start:end]
    temp.reverse()
    for idx in range(start, end):
        aminoAcid[idx] = temp[idx - start]
    print('After Inversion:')
    print(aminoAcid)

inverter()

#problem 7

def polypeptide():
    result = ""
    for aacid in aminoAcid:
        if(aminoAcid.index(aacid) == len(aminoAcid)-1):
            result += aacid
        else:
            result = result + aacid + "-"
    print('\nResulting polypeptide chain is')
    print(result)

polypeptide() 

