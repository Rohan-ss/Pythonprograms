def sort(filename):
    try:
        file = open(filename,"r+")
        data = file.readlines()
        str=list(data)
        str.sort()
        op =''.join(str)   
        output = open("C:\Python34\Programs\Output.txt","w+")
    
        output.write(op)
        file.close()
        output.close()
    except exception.e:
        print(e)
        




