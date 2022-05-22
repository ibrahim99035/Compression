from CompAlgorithms.LZSS import LZSSclass
from CompAlgorithms.LZW import LZWclass

userInput = input("Enter a string to compress: ")

LZSScompressed = LZSSclass.compress(userInput)
LZSSdecompressed = LZSSclass.decompress(LZSScompressed)

LZWcompressed = LZWclass.compress(userInput)
LZWdecompressed = LZWclass.decompress(LZWcompressed)

while(True):
    print("=========================================================================")
    print("Enter 1 to use LZSS Algorithm")
    print("Enter 2 to use LZW Algorithm")
    print("Enter the number of the algorithm you want to use: ")
    print("=========================================================================")
    key = input("Your choice: ")
    if key == '0':
        break
    elif key == '1':
        print("LZSS Compressed: " + LZSScompressed)
        print("LZSS Decompressed: " + LZSSdecompressed)
    elif key == '2':
        print("LZW Compressed: " + LZWcompressed)
        print("LZW Decompressed: " + LZWdecompressed)




