def count_upper_lower(string):
    upper_count=0
    lower_count=0

    for char in string:
        if char.isupper():
            upper_count+=1
        if char.islower():
            lower_count+=1
    return upper_count,lower_count

input_string=input("Enter a string:")
upper,lower=count_upper_lower(input_string)

print(f"UpperCase Letters:{upper}")
print(f"LowerCase Letters:{lower}")
