class TicTocTie:
    def __init__(self):
        self.rows = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.cur_player = 'X'

    def get_flatten_cells(self):
        return [cell for row in self.rows for cell in row]

    @property
    def is_not_finished(self):
        flatten_cells = self.get_flatten_cells()
        return ' ' in flatten_cells

    @property
    def is_impossible(self):
        flatten_cells = self.get_flatten_cells()
        x_count = flatten_cells.count('X')
        o_count = flatten_cells.count('O')
        return abs(x_count - o_count) > 1

    def find_winners(self):
        rows = self.rows
        winners = []

        potential_win_ways = [
            [rows[0][0], rows[0][1], rows[0][2]],
            [rows[1][0], rows[1][1], rows[1][2]],
            [rows[2][0], rows[2][1], rows[2][2]],
            [rows[0][0], rows[1][0], rows[2][0]],
            [rows[0][1], rows[1][1], rows[2][1]],
            [rows[0][2], rows[1][2], rows[2][2]],
            [rows[0][0], rows[1][1], rows[2][2]],
            [rows[0][2], rows[1][1], rows[2][0]],
        ]

        for win_way in potential_win_ways:
            played_way = ''.join(win_way)
            if played_way == 'XXX':
                winners.append('X')
            elif played_way == 'OOO':
                winners.append('O')

        return winners

    def get_result(self):
        if self.is_impossible:
            return 'Impossible'

        winners = self.find_winners()

        if len(winners) == 1:
            return f'{winners[0]} wins'
        elif len(winners) > 1:
            return 'Impossible'
        elif self.is_not_finished:
            return 'Not Finished'
        else:
            return 'Draw'

    def prompt_check_cell(self):
        x, y = self.input_cell()
        self.rows[x][y] = self.cur_player
        self.cur_player = 'O' if self.cur_player == 'X' else 'X'

    def input_cell(self):
        raw_input = input().split(' ')
        if len(raw_input) != 2:
            print('You should enter numbers!')
            return self.input_cell()

        try:
            x, y = int(raw_input[0]) - 1, int(raw_input[1]) - 1
        except ValueError:
            print('You should enter numbers!')
            return self.input_cell()

        if (0 < x > 2) or (0 < y > 2):
            print('Coordinates should be from 1 to 3!')
            return self.input_cell()

        if self.rows[x][y] != ' ':
            print('This cell is occupied! Choose another one!')
            return self.input_cell()
        return x, y

    def print(self):
        print('---------')
        for cell in self.rows:
            print(f"| {' '.join(cell)} |")
        print('---------')

    def start(self):
        self.print()
        while self.get_result() == 'Not Finished':
            self.prompt_check_cell()
            self.print()
        print(self.get_result())


def main():
    TicTocTie().start()


if __name__ == '__main__':
    main()
