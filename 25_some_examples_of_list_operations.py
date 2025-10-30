#Some examples of list operations

#example 1
years=["January 2023","February 2024", "March 2025", "April 2023", "May 2024", "June 2025", "July 2023"]
updated_years=[]
for year in years:
    if year.endswith("2023"):
        new=year.replace("2023","2024")
        updated_years.append(new)
    else:
        updated_years.append(year)
print(updated_years)

## we can also do this in short
years=["January 2023","February 2024", "March 2025", "April 2023", "May 2024", "June 2025", "July 2023"]
updated_years= [year.replace("2023", "2024") if year[-4:] == "2023" else year for year in years]
print(updated_years)


#example 2
def change_string(given_string):
    new_string=""
    new_list= given_string.split()
    for element in new_list:
        new_string += element[1:] + "-" + element[0] + " "+ "\n"
    return new_string.strip()# strip clear the extra whitespace,new lines
print(change_string("1one 2two"))


# #example 2
def list_elements(list_name, elements):
    return "The "+ list_name+" list includes: "+", ".join(elements)
print(list_elements("Printers",["Color Printer", "Black and White Printer", "3-D Printer"]))



# example 3
# map function
def add_num(number):
    return number+1
number=[2,6,8,10]
result=map(add_num,number)
print(list(result))