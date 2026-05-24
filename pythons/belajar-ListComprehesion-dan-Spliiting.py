A = ["halo-halo", "jojo-jojo"]
char = "-"
A = [part
        # variabel elemen yang disimpan dalam array nanti 
        for word in A 
        # mendapatkan tiap kata di array "halo-halo" dan "jojo-jojo"
        for part in
        # mendapatkan tiap seplittan kata di array "halo", "halo", "jojo", dan "jojo"
        (word.split(char) if char in word else [word])]
        # memecah kata apabila mengandung simbol "-" apabila char di dalam kata. Perhatikan if char dulu baru word.split (expression)
# LIST COMPREHENSION ⬆
# List comprehension is a concise way to generate a new list in Python by applying an expression to each item in an iterable, 
# with optional filtering and nesting — all in a single line.
# BASIC STRUCTURE : [expression  if condition else other  for item in iterable  for item2 in item  if condition]
# explanation of the structure above : 
# [
#   expression          # what to collect (REQUIRED)
#   if condition        # (optional) if/else must be here if used
#   else other          # (optional) paired with if above
#   for item in iterable    # main loop (REQUIRED)
#   for item2 in item   # nested loop (optional)
#   if condition        # filter (optional)
# ]

print(A)

# sensitive case
