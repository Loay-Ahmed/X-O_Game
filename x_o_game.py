"""X-O Game"""


table: list = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9"
]

WINNER = False
TURN = "X"

while WINNER is not True:
    print(" " + table[0] + ' | ' + table[1] + ' | ' + table[2] + " ")
    print('---+---+---')
    print(" " + table[3] + ' | ' + table[4] + ' | ' + table[5] + " ")
    print('---+---+---')
    print(" " + table[6] + ' | ' + table[7] + ' | ' + table[8] + " \n")

    x = input("Enter the " + TURN + "\'s position: \n")
    if x.isdigit() and x in table:
        table[int(x)-1] = TURN
    else:
        print("You didn\'t enter a number!!!")
        x = input("Enter the " + TURN + "\'s position: ")


    if table[0] == table[1] == table[2] != ' ' or \
       table[3] == table[4] == table[5] != ' ' or \
       table[6] == table[7] == table[8] != ' ' or \
       table[0] == table[3] == table[6] != ' ' or \
       table[1] == table[4] == table[7] != ' ' or \
       table[2] == table[5] == table[8] != ' ' or \
       table[0] == table[4] == table[8] != ' ' or \
       table[2] == table[4] == table[6] != ' ' :
        WINNER = True
    else:
        if TURN == "X":
            TURN = "O"
        else:
            TURN = "X"

print(" " + table[0] + ' | ' + table[1] + ' | ' + table[2] + " ")
print('---+---+---')
print(" " + table[3] + ' | ' + table[4] + ' | ' + table[5] + " ")
print('---+---+---')
print(" " + table[6] + ' | ' + table[7] + ' | ' + table[8] + " ")
WIN_TXT = f' The WINNER is {TURN} '

print (f'\n{WIN_TXT:=^40}\n')
