roman_dict = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X",50:"L",100:"C",500:"D",1000:"M"}

def num_to_roman(in_num):
    if in_num in roman_dict:
        return roman_dict[in_num]
    elif 


in_num = input('Provide a number>')

print num_to_roman(in_num)
