# #slicing and joining strings

# #slicing strings
# string1= "Greetings, Earthlings"
# print(string1[0])#first character
# print(string1[2:5])
# print(string1[:5])#from the start to index 5
# print(string1[11:])#count from the forwards
# print(string1[-10:])#count from the backwards
# print(string1[::2])#every second character
# print(string1[55:])#out of range
# print(string1[:])#the whole string
# print(string1[::-1])#the whole string reversed
# print(string1[::-2])#count every second character and reversed the string

#joining strings
string2=["Hello","from","the","other","side"]
print(" ".join(string2))#join with space


#slincing and joining
def format_phone(phonenum):
    area_code="(" +phonenum[:3] + ")"
    exchange=phonenum[3:8]
    last_part=phonenum[8:]
    return area_code + " " + exchange + "-" + last_part
print(format_phone('08801715469873'))