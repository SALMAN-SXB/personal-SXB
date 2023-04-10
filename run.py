import zlib,os
ban="\n\n\t\tCoded by SIAM AHMED\n\n"
def zc():
    os.system("clear")
    print(ban)
    s=input("String: ")
    zcf=zlib.compress(s.encode())
    print(f"\n\nzlib.decompress({zcf}).decode()\n\n")
    input("Enter to continue")
    
def bhx():
    s=input("String: ")
    hc=f"'{s}'".encode().hex()
    f=f"eval(bytearray.fromhex('{hc}'))"
    print(f)
    input("Enter to continue")
    
while True:
    os.system("clear")
    m=int(input("  [1]Bytes\n  [2]Zlib\n  Choose: "))
    if m==1:
        bhx()
    else:
        zc()
