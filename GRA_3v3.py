import random
import termios, sys, os
import copy
TERMIOS = termios

class bcolors:
    VIOLET = '\033[35m'
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    RED = '\033[31m'
    BLACK = '\033[30m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[1;m'
    VIOLET_BG = '\033[37;45m' # white font with colorful backgrounds
    BLUE_BG = '\033[37;44m'
    GREEN_BG = '\033[30;42m'
    YELLOW_BG = '\033[30;43m'
    MAGENTA_BG = '\033[37;41m'
    WHITE_BG = '\033[37;48m'

def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c

def napis():
    print(bcolors.YELLOW +'')
    print('')
    print(' 222222222222222         000000000            444444444       888888888')
    print('2:::::::::::::::22     00:::::::::00         4::::::::4     88:::::::::88  ')
    print('2::::::222222:::::2  00:::::::::::::00      4:::::::::4   88:::::::::::::88')
    print('2222222     2:::::2 0:::::::000:::::::0    4::::44::::4  8::::::88888::::::8')
    print('            2:::::2 0::::::0   0::::::0   4::::4 4::::4  8:::::8     8:::::8')
    print('            2:::::2 0:::::0     0:::::0  4::::4  4::::4  8:::::8     8:::::8')
    print('         2222::::2  0:::::0     0:::::0 4::::4   4::::4   8:::::88888:::::8 ')
    print('    22222::::::22   0:::::0     0:::::04::::444444::::444  8:::::::::::::8  ')
    print('  22::::::::222     0:::::0     0:::::04::::::::::::::::4 8:::::88888:::::8 ')
    print(' 2:::::22222        0:::::0     0:::::04444444444:::::4448:::::8     8:::::8')
    print('2:::::2             0:::::0     0:::::0          4::::4  8:::::8     8:::::8')
    print('2:::::2             0::::::0   0::::::0          4::::4  8:::::8     8:::::8')
    print('2:::::2       2222220:::::::000:::::::0          4::::4  8::::::88888::::::8')
    print('2::::::2222222:::::2 00:::::::::::::00         44::::::44 88:::::::::::::88 ')
    print('2::::::::::::::::::2   00:::::::::00           4::::::::4   88:::::::::88   ')
    print('22222222222222222222     000000000             4444444444     888888888     ')
    print('')
    print('' + bcolors.END)
    
lista=['Start','-Start-','EXIT','-EXIT-']

def napis_game_over():
    print(bcolors.RED + ' ')
    print('                                 )                    ')
    print(' (                            ( /(                    ')
    print(' )\ )       )     )      (    )\())   )      (   (    ')
    print('(()/(    ( /(    (      ))\  ((_)\   /((    ))\  )(   ')
    print(' /(_))_  )(_))   )\     /((_)  ((_) (_))\  /((_)(()\  ')
    print('(_)) __|((_)_  _((_)) (_))    / _ \ _)((_)(_))   ((_) ')
    print("  | (_ |/ _` || '  \()/ -_)  | (_) |\ V / / -_) | '_| ")
    print("   \___|\__,_||_|_|_| \___|   \___/  \_/  \___| |_|   ")
    print("                                                      " + bcolors.END)

def napis_winner():
    print(bcolors.YELLOW +'')
    print('')
    print('WWWWWWWW                           WWWWWWWWIIIIIIIIIINNNNNNNN        NNNNNNNNNNNNNNNN        NNNNNNNNEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRR')   
    print('W::::::W                           W::::::WI::::::::IN:::::::N       N::::::NN:::::::N       N::::::NE::::::::::::::::::::ER::::::::::::::::R ') 
    print('W::::::W                           W::::::WI::::::::IN::::::::N      N::::::NN::::::::N      N::::::NE::::::::::::::::::::ER::::::RRRRRR:::::R ')
    print('W::::::W                           W::::::WII::::::IIN:::::::::N     N::::::NN:::::::::N     N::::::NEE::::::EEEEEEEEE::::ERR:::::R     R:::::R')
    print(' W:::::W           WWWWW           W:::::W   I::::I  N::::::::::N    N::::::NN::::::::::N    N::::::N  E:::::E       EEEEEE  R::::R     R:::::R')
    print('  W:::::W         W:::::W         W:::::W    I::::I  N:::::::::::N   N::::::NN:::::::::::N   N::::::N  E:::::E               R::::R     R:::::R')
    print('   W:::::W       W:::::::W       W:::::W     I::::I  N:::::::N::::N  N::::::NN:::::::N::::N  N::::::N  E::::::EEEEEEEEEE     R::::RRRRRR:::::R ')
    print('    W:::::W     W:::::::::W     W:::::W      I::::I  N::::::N N::::N N::::::NN::::::N N::::N N::::::N  E:::::::::::::::E     R:::::::::::::RR  ')
    print('     W:::::W   W:::::W:::::W   W:::::W       I::::I  N::::::N  N::::N:::::::NN::::::N  N::::N:::::::N  E:::::::::::::::E     R::::RRRRRR:::::R ')
    print('      W:::::W W:::::W W:::::W W:::::W        I::::I  N::::::N   N:::::::::::NN::::::N   N:::::::::::N  E::::::EEEEEEEEEE     R::::R     R:::::R')
    print('       W:::::W:::::W   W:::::W:::::W         I::::I  N::::::N    N::::::::::NN::::::N    N::::::::::N  E:::::E               R::::R     R:::::R')
    print('        W:::::::::W     W:::::::::W          I::::I  N::::::N     N:::::::::NN::::::N     N:::::::::N  E:::::E       EEEEEE  R::::R     R:::::R')
    print('         W:::::::W       W:::::::W         II::::::IIN::::::N      N::::::::NN::::::N      N::::::::NEE::::::EEEEEEEE:::::ERR:::::R     R:::::R')
    print('          W:::::W         W:::::W          I::::::::IN::::::N       N:::::::NN::::::N       N:::::::NE::::::::::::::::::::ER::::::R     R:::::R')
    print('           W:::W           W:::W           I::::::::IN::::::N        N::::::NN::::::N        N::::::NE::::::::::::::::::::ER::::::R     R:::::R')
    print('            WWW             WWW            IIIIIIIIIINNNNNNNN         NNNNNNNNNNNNNNN         NNNNNNNEEEEEEEEEEEEEEEEEEEEEERRRRRRRR     RRRRRRR')
    print('')
    print('' + bcolors.END)

def check_end(arr):
    game_over_h = 0
    game_over_v = 0
    game_over = 0
    if not any(0 in list for list in arr):
        for j in range(0,columns):
            if all(arr[i+1][j] != arr[i][j] for i in range(0,rows-1)):
                game_over_v += 1
        for i in range(0,rows): 
            if all (arr[i][j+1] != arr[i][j] for j in range(0,columns-1)):
                game_over_h += 1
        game_over = game_over_h + game_over_v
    if any(max_score in list for list in arr):
        game_over = 2048
    return [game_over, game_over_v, game_over_h]

def clr():
   os.system('cls' if os.name == 'nt' else 'clear')

def print_matrix(matrix):
    matrix_with_strings = [[str(matrix[j][i]) for i in range(rows)] for j in range(columns)]
    for i in range(0,rows):
        for j in range(0,columns):
            if matrix_with_strings[i][j] == '0':
                matrix_with_strings[i][j] = bcolors.WHITE_BG + '           ' + bcolors.END
            elif matrix_with_strings[i][j] == '2':
                matrix_with_strings[i][j] = bcolors.YELLOW_BG + '     2     ' + bcolors.END
            elif matrix_with_strings[i][j] == '4':
                matrix_with_strings[i][j] = bcolors.GREEN_BG + '     4     ' + bcolors.END
            elif matrix_with_strings[i][j] == '8':
                matrix_with_strings[i][j] = bcolors.BLUE_BG + '     8     ' + bcolors.END
            elif matrix_with_strings[i][j] == '16':
                matrix_with_strings[i][j] = bcolors.VIOLET_BG + '    16     ' + bcolors.END
            elif matrix_with_strings[i][j] == '32':
                matrix_with_strings[i][j] = bcolors.YELLOW_BG + '    32     ' + bcolors.END
            elif matrix_with_strings[i][j] == '64':
                matrix_with_strings[i][j] = bcolors.GREEN_BG + '    64     ' + bcolors.END
            elif matrix_with_strings[i][j] == '128':
                matrix_with_strings[i][j] = bcolors.BLUE_BG + '   128     ' + bcolors.END
            elif matrix_with_strings[i][j] == '256':
                matrix_with_strings[i][j] = bcolors.VIOLET_BG + '   256     ' + bcolors.END
            elif matrix_with_strings[i][j] == '512':
                matrix_with_strings[i][j] = bcolors.YELLOW_BG + '   512     ' + bcolors.END
            elif matrix_with_strings[i][j] == '1024':
                matrix_with_strings[i][j] = bcolors.GREEN_BG + '  1024     ' + bcolors.END
            elif matrix_with_strings[i][j] == '2048':
                matrix_with_strings[i][j] = bcolors.RED_BG + '  2048     ' + bcolors.END
    
    matrix_to_print = [[(matrix_with_strings[j][i]).center(16) for i in range(rows)] for j in range(columns)] #dodać justowanie
    clr()
    print(bcolors.YELLOW + 'Make your move' + bcolors.END)
    print(bcolors.GREEN + 'w:up s:down a:left d:right' + bcolors.END)
    print('\n')
    print(bcolors.BLUE +'score :'+ bcolors.END, score)
    print('\n')
    print(' ','************'*rows,' ')
    print('\n')
    for i in range(0,rows):
        print('*', *matrix_to_print[i], '*')
        print('\n')
    print(' ','************'*rows,' ')

def computer_move(arr):
    number_list = [2,4]
    new_value = number_list[random.randint(0,1)]
    i = random.randint(0,columns-1)
    j = random.randint(0,rows-1)    
    if any(0 in list for list in arr):
        while arr[i][j] > 0:
            i = random.randint(0,columns-1)
            j = random.randint(0,rows-1)
        arr[i][j] = new_value
    else:
        return
    return arr

def move_left(arr):
    score = 0
    new_arr = [[0 for i in range(rows)] for j in range(columns)]
    for i in range(0,rows):
        for j in range (1,columns):
            while arr[i][j-1] == 0 and j >= 1:
                arr[i][j-1] = arr[i][j]
                arr[i][j] = 0
                j -= 1
        for j in range (1,columns):
            if arr[i][j-1] == arr[i][j]:
                new_arr[i][j-1] = arr[i][j] + arr[i][j-1]
                arr[i][j] = 0
                score = score + new_arr[i][j-1]
            else:
                new_arr[i][j-1] = arr[i][j-1]
        new_arr[i][columns-1] = arr[i][columns-1]
        for j in range (1,columns):
            while new_arr[i][j-1] == 0 and j >= 1:
                new_arr[i][j-1] = new_arr[i][j]
                new_arr[i][j] = 0
                j -= 1
    return [score, new_arr]
    
def move_up(arr):
    score = 0
    new_arr = [[0 for i in range(rows)] for j in range(columns)]
    for j in range(0,columns):
        for i in range (1,rows):
            while arr[i-1][j] == 0 and i >= 1:
                arr[i-1][j] = arr[i][j]
                arr[i][j] = 0
                i -= 1
        for i in range (1,rows):
            if arr[i-1][j] == arr[i][j]:
                new_arr[i-1][j] = arr[i-1][j] + arr[i][j]
                arr[i][j] = 0
                score = score + new_arr[i-1][j]
            else:
                new_arr[i-1][j] = arr[i-1][j]
        new_arr[rows-1][j] = arr[rows-1][j]
        for i in range (1,rows):
            while new_arr[i-1][j] == 0 and i >= 1:
                new_arr[i-1][j] = new_arr[i][j]
                new_arr[i][j] = 0
                i -= 1
    return [score, new_arr]

def move_right(arr):
    score = 0
    new_arr = [[0 for i in range(rows)] for j in range(columns)]
    for i in range(0,rows):
        for j in range (columns-2,-1,-1):
            while j <= columns-2 and arr[i][j+1] == 0:
                arr[i][j+1] = arr[i][j]
                arr[i][j] = 0
                j += 1
        for j in range (1,columns):
            if arr[i][j-1] == arr[i][j]:
                new_arr[i][j-1] = arr[i][j] + arr[i][j-1]
                arr[i][j] = 0
                score = score + new_arr[i][j-1]
            else:
                new_arr[i][j-1] = arr[i][j-1]
        new_arr[i][columns-1] = arr[i][columns-1]
        for j in range (columns-2,-1,-1):
            while j <= columns-2 and new_arr[i][j+1] == 0:
                new_arr[i][j+1] = new_arr[i][j]
                new_arr[i][j] = 0
                j += 1
    return [score, new_arr]

def move_down(arr):
    score = 0
    new_arr = [[0 for i in range(rows)] for j in range(columns)]
    for j in range(0,columns):
        for i in range (rows-2,-1,-1):
            while i <= rows-2 and arr[i+1][j] == 0:
                arr[i+1][j] = arr[i][j]
                arr[i][j] = 0
                i += 1
        for i in range (rows-2,-1,-1):
            if arr[i+1][j] == arr[i][j]:
                new_arr[i+1][j] = arr[i+1][j] + arr[i][j]
                arr[i][j] = 0
                score = score + new_arr[i+1][j]
            else:
                new_arr[i+1][j] = arr[i+1][j]
        new_arr[0][j] = arr[0][j]
        for i in range (rows-2,-1,-1):
            while i <= rows-2 and new_arr[i+1][j] == 0:
                new_arr[i+1][j] = new_arr[i][j]
                new_arr[i][j] = 0
                i += 1
    return [score, new_arr]

def player_move(arr, score, copy_of_matrix, copy_of_score):
    while True:
        key=getkey().decode()
        if key == 'w' and game_over_v < rows:
            copy_of_matrix = arr[:]
            copy_of_score = score
            tempscore, matrix = move_up(arr)
            score += tempscore
            computer_move(matrix)
        elif key== 's' and game_over_v < rows:
            copy_of_matrix = arr[:]
            copy_of_score = score
            tempscore, matrix  = move_down(arr)
            score += tempscore
            computer_move(matrix)
        elif key == 'd' and game_over_h < columns:
            copy_of_matrix = arr[:]
            copy_of_score = score
            tempscore, matrix  = move_right(arr)
            score += tempscore
            computer_move(matrix)
        elif key == 'a' and game_over_h < columns:
            copy_of_matrix = arr[:]
            copy_of_score = score
            tempscore, matrix  = move_left(arr)
            score += tempscore
            computer_move(matrix)
        elif key == 'u':
            matrix = copy_of_matrix
            score = copy_of_score
        else:
            continue
        return score, matrix, copy_of_matrix, copy_of_score

def is_start(x, game, start):
    while start == True:
        key=getkey().decode()
        if key == 'w':
            clr()
            napis()
            print(lista[1])
            print(lista[2])
            x = 1
        if key == ('\n') and x == 1:
            game = True
            start = False
            return game, start
        elif key == 's':
            clr()
            napis()
            print(lista[0])
            print(lista[3])
            x = 2
        if key == ('\n') and x == 2:
            exit()
    return game, start

def choose_size_of_matrix():
    y = 0
    dict_of_sizes = {'4x4': 4, '6x6': 6, '8x8': 8 }
    while y == 0:
        try:
            rows = dict_of_sizes[input("Choose size of a board: 4x4, 6x6, 8x8   ")]
            rows == 4 or 6 or 8
            y = 1
        except KeyError:
            continue
    while y == 1:
        try:
            max_score = int(input("Choose your goal: 2048, 4096, 8192   "))
            max_score == 64 or 2048 or 4096 or 8192         #64 na potrzeby prezentacji jedynie
            y = 2
        except ValueError:
            continue
    game = True
    return rows, max_score, game

def ending_game(game_over):
    if game_over == columns + rows:
        clr()
        napis_game_over()
    elif game_over == 2048:
        clr()
        napis_winner()

game  = False
start = True
clr()
napis()
print(lista[1])
print(lista[2])
x = 0
score = 0
game_over = 0
game_over_h = 0
game_over_v = 0
game_1, start = is_start(x, game, start)
rows, max_score, game = choose_size_of_matrix()
columns = rows
matrix = [[0 for i in range(rows)] for j in range(columns)]
copy_of_matrix = matrix[:]
copy_of_score = score
matrix = computer_move(matrix)
print_matrix(matrix)
while game == True and game_over < rows + columns: 
    game_over, game_over_v, game_over_h = check_end(matrix) 
    score, matrix, copy_of_matrix, copy_of_score = player_move(matrix, score, copy_of_matrix, copy_of_score)
    # computer_move(matrix)
    print_matrix(matrix)
else:
    ending_game(game_over)
