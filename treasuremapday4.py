line1 = ["⬜️","️⬜️","️⬜️"] #indexing in python=0
line2 = ["⬜️","⬜️","️⬜️"] #indexing in python=1
line3 = ["⬜️️","⬜️️","⬜️️"] #indexing in python=2
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() #eg:-[A2]
letter=position[0].lower()
abc=("a","b","c")
letter_index=abc.index(letter)
number_index=int(position[1])-1 #-1 is used because python uses counts  from  zero and we start our count from 1
map[letter_index][number_index]="x"
print(f"{line1}\n{line2}\n{line3}")