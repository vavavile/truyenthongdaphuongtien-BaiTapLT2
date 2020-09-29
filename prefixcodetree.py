import sys

class PrefixCodeTree:
    symbol = ''
    left = None
    right = None
    
    def insert(self, codeword, symbol):
        if len(codeword) == 0:
            self.symbol = symbol
        elif codeword[0] == 0:
            if self.left == None:
                self.left = PrefixCodeTree()
            self.left.insert(codeword[1:], symbol)
        else:
            if self.right == None:
                self.right = PrefixCodeTree()
            self.right.insert(codeword[1:], symbol)

    def decode(self, encodedData, datalen):
        bcode = bin(int.from_bytes(encodedData, 'big'))[2:datalen+2]
        cur = self
        s = ''
        for b in bcode:
            if b == '0':
                cur = cur.left
            else:
                cur = cur.right
            if cur is None:
                break
            if cur.symbol != '':
                s = s + cur.symbol
                cur = self
        return s
        

#test
codebook = {
    'x1': [0],
    'x2': [1,0,0],
    'x3': [1,0,1],
    'x4': [1,1]
}

codeTree = PrefixCodeTree()
for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)

data = b'\xd2\x9f\x20'
datalen = 21
print(codeTree.decode(data, datalen))