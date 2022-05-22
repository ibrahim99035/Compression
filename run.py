from tarfile import ENCODING
from CompAlgorithms.LZSS import LZSSclass
from CompAlgorithms.LZW import LZWclass
from CompAlgorithms.ArthmeticEncoding import ArthClass

arithmeticEncodingFrequencyTable = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'D' : 4,
    'E' : 5,
}

userInput = input("Enter a string to compress: ")

#-----------------------------------------------------------------------------------------------------------------------
LZSScompressed = LZSSclass.compress(userInput)
LZSSdecompressed = LZSSclass.decompress(LZSScompressed)
#-----------------------------------------------------------------------------------------------------------------------
LZWcompressed = LZWclass.compress(userInput)
LZWdecompressed = LZWclass.decompress(LZWcompressed)
#-----------------------------------------------------------------------------------------------------------------------
arithmeticEncoding = ArthClass(arithmeticEncodingFrequencyTable)
encoder, encoded_msg = arithmeticEncoding.encode(userInput, arithmeticEncoding.probability_table)
#-----------------------------------------------------------------------------------------------------------------------
while(True):
    print("=========================================================================")
    print("Enter 1 to use LZSS Algorithm")
    print("Enter 2 to use LZW Algorithm")
    print("Enter 3 to use Arithmetic Encoding")
    print("Enter 0 to exit")
    print("Enter the number of the algorithm you want to use: ")
    print("=========================================================================")
    key = int(input("Your choice: ")) 
    if key == 0:
        break
    elif key == 1:
        print("LZSS Compressed: " + LZSScompressed)
        print("LZSS Decompressed: " + LZSSdecompressed)
    elif key == 2:
        print("LZW Compressed: " + LZWcompressed)
        print("LZW Decompressed: " + LZWdecompressed)
    elif key == 3:
        print("Encodede message: " + str(encoded_msg))
        print("Decoded message: " + userInput)
    else:
        print("Invalid input, please enter a valid number")




