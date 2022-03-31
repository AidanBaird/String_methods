authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

# Create a variable that is the authors split between each "," to give just the authors name in one element

author_names = authors.split(",")

author_last_names = []
for name in author_names:
    print(name)
    print(name.split()[-1])
    author_last_names.append(name.split()[-1])

# seperate_names = []
# for name in author_names:
# seperate_names.append(name.split()[-1])


# author_seperate_names = []
# author_last_names = []
# index = 1
# for name in author_names:
# index += 1
# author_seperate_names.append(name.split())
# print(author_seperate_names)
# for last in author_seperate_names:
# author_last_names.append(name)


# def last_name1(names):
# for full_names in names:
# seperate_names = names.split()
# return seperate_names

# last_name1(author_names)

# author_last_names = last_name()

# split_names = author_names.split(" ")

# def last_name(names):
# index = 0
# second_name = []
# for name in names:
# index += 1
# print(index)
# if index % 2 == 0:
# second_name.append(name)
# return second_name

# print(last_name(author_names))


# Printing commands
print(author_names)
print("")
# print(author_seperate_names)
print("")
# print(author_last_names)