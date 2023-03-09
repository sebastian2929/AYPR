m = 9

def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")

        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()


HashTable = [[] for _ in range(10)]


def Hashing(keyvalue):
    valor = keyvalue % 9
    print(keyvalue, valor)
    return keyvalue % 9


def insert(Hashtable, keyvalue):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(keyvalue)

insert(HashTable, 5)
insert(HashTable, 28)
insert(HashTable, 19)
insert(HashTable, 15)
insert(HashTable, 20)
insert(HashTable, 33)
insert(HashTable, 12)
insert(HashTable, 17)
insert(HashTable, 10)



display_hash(HashTable)