

def main():
    while True:
        data = input()
        
        if data == "exit" or data == "e":
            return
        
        elif data[0:2] == "dh":
            data = data[2:]
            print(hex(int(data)))        
        elif data[0:2] == "db":
            data = data[2:]
            print(bin(int(data))[2:])         
        elif data[0:2] == "do":
            data = data[2:]
            print(oct(int(data))[2:]) 
        
        elif data[0:2] == "hd":
            data = data[2:]
            print(int(data, 16))           
        elif data[0:2] == "hb":
            data = data[2:]
            print(bin(int(data, 16))[2:])          
        elif data[0:2] == "ho":
            data = data[2:]
            print(oct(int(data, 16))[2:])
        
        elif data[0:2] == "bd":
            data = data[2:]
            print(int(data, 2)) 
        elif data[0:2] == "bh":
            data = data[2:]
            print(hex(int(data, 2))[2:]) 
        elif data[0:2] == "bo":
            data = data[2:]
            print(oct(int(data, 2))[2:]) 
 
        elif data[0:2] == "od":
            data = data[2:]
            print(int(data, 8)) 
        elif data[0:2] == "oh":
            data = data[2:]
            print(hex(int(data, 8))[2:]) 
        elif data[0:2] == "ob":
            data = data[2:]
            print(bin(int(data, 8))[2:])   
            
        else:
            print(data + " isnt a valid input")
main()