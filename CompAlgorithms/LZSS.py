class LZSSclass:
    def compress(s):
        result = ""
        slidingWindow = "" * 7
        i = 0
        while i < len(s):
            d = 0
            l = 0
            for j in range(i + 1, len(s) + 1):
                curr = s[i:j]
                if curr in slidingWindow:
                    d = slidingWindow.find(curr)
                    l = len(curr)
            
            if l == 0:
                result += "0" + s[i]
                slidingWindow = s[i]
                i = i + 1
            else:
                slidingWindow += s[i : i + l]
                result += "1(" + str(d+1) + "," + str(l) + ")"
                i = i + l
            
            slidingWindow = slidingWindow[-7:]
        return result



    def decompress(s):
        result = ""
        slidingWindow = "" * 7
        i = 0
        while i < len(s):
            if s[i] == '0':
                result += s[i+1]
                slidingWindow += s[i+1]
                i = i + 2
            else:
                b_end = s.find(')',i+1)
                curr = s[i+2 : b_end]
                d,l = curr.split(',')
                d = int(d)
                l = int(l)
                result += slidingWindow[d-1:d-1+l]
                slidingWindow += slidingWindow[d-1:d-1+l]
                i = b_end+1
            slidingWindow = slidingWindow[-7:]
        return result