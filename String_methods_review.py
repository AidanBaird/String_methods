highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"


# Create a variable that contains a list with each element being specific to each poem

highlighted_poems_list = highlighted_poems.split(",")

# Create a variable that strips whitespace from the elements

highlighted_poems_stripped = []

for element in highlighted_poems_list:
  highlighted_poems_stripped.append(element.strip())

 # Create a variable that splits the elements into each individual detail

highlighted_poems_details = []

for element in highlighted_poems_stripped:
  highlighted_poems_details.append(element.split(":"))

# Create a function that adds each respective element into it's respective variable
index = 0
titles = []
poets = []
dates = []

for elements in highlighted_poems_details:
  titles.append(elements[0])
  poets.append(elements[1])
  dates.append(elements[2])

# Write a loop that formats the three variables in to a string

message = "The poem {} was published by {} in {}"


for elements in titles:
  print(message.format(titles[index], poets[index], dates[index]))
  index += 1


# Printing commands
print(highlighted_poems)
print("")
print(highlighted_poems_list)
print("")
print(highlighted_poems_stripped)
print("")
print(highlighted_poems_details)
print("")
print(titles)
print("")
print(poets)
print("")
print(dates)
print("")
print(message.format(titles[0], poets[0], dates[0]))