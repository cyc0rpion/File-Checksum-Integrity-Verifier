
def md5s(string):

###SOME PREDEFINED VALUES###
#################################################################################

    s = [
        7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
        5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
        4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
        6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21
        ]

    K = [
        0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
        0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
        0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
        0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
        0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
        0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
        0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
        0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
        0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
        0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
        0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
        0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
        0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
        0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
        0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
        0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391  
        ]

    a0 = 0x67452301
    b0 = 0xefcdab89
    c0 = 0x98badcfe
    d0 = 0x10325476


    #PRE-DEFINED FUNCTIONS

    def F(X,Y,Z):                                   
        return((X & Y) | (  (~X) & Z))   

    def G(X,Y,Z):
        return((X & Z) | (Y & (~Z)))  

    def H(X,Y,Z):
        return(X ^ Y ^ Z)

    def I(X,Y,Z):
        return(Y ^ (X | ~Z))  

    def leftrotate(x,c):
        x = x & 0xFFFFFFFF
        return ((x << c) | (x >> (32-c))) & 0xFFFFFFFF

    ####################################################################################

    message = string
    message = bytearray(message)
    b = (8 * len(message)) & 0xffffffffffffffff

    message.append(0x80)

    while len(message)%64 != 56:
            message.append(0)

    M = message + b.to_bytes(8, byteorder='little')

    for chunks in range(0,len(M),64):

        chunk=M[chunks:chunks+64]
        A=a0
        B=b0  
        C=c0  
        D=d0  

        F0=0
        g=0
        
        for i in range(64):
        
            if(i>=0 and i<=15):
                F0 = F(B,C,D) 
                g = i
                
            elif(i>=16 and i<=31):
                F0 = G(B,C,D) 
                g = (5*i+1)%16

            elif(i>=32 and i<=47):
                F0 = H(B,C,D) 
                g = (3*i+5)%16

            elif(i>=48 and i<=63):
                F0 = I(B,C,D) 
                g = (7*i)%16

            to = (A + F0 + K[i] + int.from_bytes(chunk[4*g:4*g+4], byteorder='little')) & 0xFFFFFFFF

            A = D & 0xFFFFFFFF
            D = C & 0xFFFFFFFF
            C = B & 0xFFFFFFFF
            B = (B + leftrotate(to,s[i])) & 0xFFFFFFFF

        a0 = (a0 + A)  & 0xFFFFFFFF
        b0 = (b0 + B)  & 0xFFFFFFFF
        c0 = (c0 + C)  & 0xFFFFFFFF
        d0 = (d0 + D)  & 0xFFFFFFFF


    hashes =[a0,b0,c0,d0]
    Z=sum(x<<(32*i) for i, x in enumerate(hashes))

    Z = Z.to_bytes(16,byteorder='little')
    Z = '{:032x}'.format(int.from_bytes(Z,byteorder = 'big'))

    return((Z))

##string = input()
##message = bytes(string,"ascii")
##print(md5s(string))
