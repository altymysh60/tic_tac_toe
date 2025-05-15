from gameparts import Board
from gameparts.exceptions import FieldIndexError 

def main():
    game = Board()
    game.display()
    row = int(input('Введите номер строки: '))
    if row < 0 or row >= game.field_size:
        raise FieldIndexError('Введено значение за границами игрового поля!')
    column = int(input('Введите номер столбца: '))
    
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()

if __name__ == '__main__':
    main()



