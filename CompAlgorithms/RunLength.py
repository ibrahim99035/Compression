class RLC:
    def encode(message):
    
        encoded_message = ""
        i = 0

        while (i <= len(message)-1):
            count = 1
            ch = message[i]
            j = i       
            while (j < len(message)-1):  
                if (message[j] == message[j+1]):
                    count = count+1
                    j = j+1
                    
                else:
                    break
                
            encoded_message=encoded_message+str(count)+ch
            i = j+1
            
        return encoded_message
    
    def decode(data):
    
        decode = ''
        
        count = ''
        
        for char in data:
            
            # If the character is numerical...
            if char.isdigit():
                
                # ...append it to our count
                
                count += char
                
            else:
                # Otherwise we've seen a non-numerical
                # character and need to expand it for
                # the decoding
                decode += char * int(count)
                
                count = ''
                
                
        return decode