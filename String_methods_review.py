highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"


# Create a variable that contains a list with each element being specific to each poem

highlighted_poems_list = highlighted_poems.split(",")

# Create a variable that strips whitespace from the elements

highlighted_poems_stripped = []

for element in highlighted_poems_list:
  highlighted_poems_stripped.append(element.strip())

 #

highlighted_poems_details =

# Printing commands
print(highlighted_poems)
print("")
print(highlighted_poems_list)
print("")
print(highlighted_poems_stripped)