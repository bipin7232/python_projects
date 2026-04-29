# file = open("practice.txt", "w")
# file.write("Hi everyone\n" \
# "i am learning java")
# file.close()


# repalce java with python

with open("practice.txt","r") as f:
    data = f.read()
   

    data2 = data.replace("java","python")
    print(data2)

