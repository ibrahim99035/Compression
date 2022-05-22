from CompAlgorithms.LZSS import LZSSclass
from CompAlgorithms.LZW import LZWclass
from CompAlgorithms.ArthmeticEncoding import ArthClass
from CompAlgorithms.Huffman import HuffmanClass
from CompAlgorithms.RunLength import RLC

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
freq = {}
for c in userInput:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
length = len(userInput)

probabilities = [float("{:.2f}".format(frequency[1]/length)) for frequency in freq]
probabilities = sorted(probabilities, reverse=True)

huffmanClassObject = HuffmanClass(probabilities)
P = probabilities

huffman_code = huffmanClassObject.compute_code()
#-----------------------------------------------------------------------------------------------------------------------
RLCencoded = RLC.encode(userInput)
RLCdecoded = RLC.decode(RLCencoded)
#-----------------------------------------------------------------------------------------------------------------------
while(True):
    print("=========================================================================")
    print("Enter 1 to use LZSS Algorithm")
    print("Enter 2 to use LZW Algorithm")
    print("Enter 3 to use Arithmetic Encoding")
    print("Enter 4 to use Huffman Algorithm")
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
    elif key == 4:
        print(' Char | Huffman code ')
        print('----------------------')

        for id,char in enumerate(freq):
            if huffman_code[id]=='':
                print(' %-4r |%12s' % (char[0], 1))
                continue
            print(' %-4r |%12s' % (char[0], huffman_code[id]))
    elif key == 5:
        print("RLC Compressed: " + RLCencoded)
        print("RLC Decompressed: " + RLCdecoded)
    else:
        print("Invalid input, please enter a valid number")




