def sub_string_ofstring(string):
    new_list=[]
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            new_list.append(string[i:j])
    #this folowing code is used to find the longest palindromin substring of a string
    for k in range(len(new_list)):
        if len(new_list[k])>len(new_list[k-1]) and new_list[k]==new_list[k][::-1]:
                return new_list[k]
    return False

string="andebet"
print(sub_string_ofstring(string))
