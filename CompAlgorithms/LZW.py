class LZWclass:
    def compress(s):
        result = ""
        table = {}
        index = 256
        i = 0
        
        while i < len(s):
            curr = s[i]
            end = i + 1

            for j in range(i + 1, len(s)):
                if curr + s[j] in table:
                    curr += s[j]
                    end = j + 1
                else:
                    end = j
                    break

            if len(curr) == 1:
                result += str(ord(curr[0])) + "/"
            else:
                result += str(table[curr]) + "/"
        
            if(end < len(s)):
                curr += s[end]
                table[curr] = index
                index = index + 1
            
            i = end

        return result[:-1]
    
    def decompress(s):
        result = ""
        s = s.split('/')
        table = {}
        index = 256
        prev = ""
        for i in range(len(s)):
            curr_code = int(s[i])
            curr_part = ""
            if curr_code < 256:
                curr_part = chr(curr_code)  
            else:
                if curr_code not in table:
                    table[index] = prev + prev[0]
                    index = index+1
                curr_part = table[curr_code]
            result += curr_part

            if i > 0:
                table[index] = prev+curr_part[0]
                index = index+1
            
            prev = curr_part
        return result