class SudokuSolver:

    def __init__(self, query_string, rows = 'ABCDEFGHI', columns = '123456789'):
        """
        Initializing the various variables required here
        """
        self.query_string = query_string
        self.rows = rows                    # The Rows are labeled from A to Z
        self.columns = columns              # The columns are labeled from 1 to 9

        """
        The individual squares at the intersection of rows and columns will be called boxes. These boxes will have labels 'A1', 'A2', …, 'I9'.
        The complete rows, columns, and 3x3 squares, will be called units. Thus, each unit is a set of 9 boxes, and there are 27 units in total.
        For a particular box (such as 'A1'), its peers will be all other boxes that belong to a common unit 
        namely, those that belong to the same row, column, or 3x3 square.
        """

        self.boxes = self.cross(self.rows, self.columns)        # Getting all the box labels
        self.row_units = [self.cross(r, self.columns) for r in self.rows]  # Getting all the row units       
        self.column_units = [self.cross(self.rows, c) for c in self.columns]    # Getting all the column units
        self.square_units = [self.cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]    # Getting all the square units 
        self.unitlist = self.row_units + self.column_units + self.square_units  # Combining all the units (Row, column and square)
        self.units = dict((s, [u for u in self.unitlist if s in u]) for s in self.boxes)    # Getting all units corresponding to each box
        self.peers = dict((s, set(sum(self.units[s],[]))-set([s])) for s in self.boxes)     # Getting all the peers corresponding to each box

    def check(self):
        d = self.grid_values()
        # checking all the rows
        for i in self.row_units:
            row_elements = []
            for j in i:
                if d[j] != '123456789' and d[j] in row_elements:
                    return False
                else:
                    row_elements.append(d[j])
        
        # checking all the columns
        for i in self.column_units:
            col_elements = []
            for j in i:
                if d[j] != '123456789' and d[j] in col_elements:
                    return False
                else:
                    col_elements.append(d[j])
        
        # Checking all the square units
        for i in self.square_units:
            square_elements = []
            for j in i:
                if d[j] != '123456789' and d[j] in square_elements:
                    return False
                else:
                    square_elements.append(d[j])
        
        return True

    def cross(self, a, b):
        """
        A helper function for combining the row and column labels
        """
        return [s+t for s in a for t in b]

    def grid_values(self):
        """
        Function to convert the input string to grid
        Input: A grid in string form.
        Output: A grid in dictionary form
        """
        chars = []
        digits = '123456789'
        for c in self.query_string:
            if c in digits:
                chars.append(c)
            if c == '.':
                chars.append(digits)
        assert len(chars) == 81
        return dict(zip(self.boxes, chars))
    
    def display(self, values):
        """
        Display the values as a 2-D grid.
        Input: The sudoku in dictionary form
        Output: Prints the grid, returns None
        """
        width = 1+max(len(values[s]) for s in self.boxes)
        line = '+'.join(['-'*(width*3)]*3)
        for r in self.rows:
            print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                        for c in self.columns))
            if r in 'CF': 
                print(line)
    
    def eliminate(self, values):
        """
        Go through all the boxes, and whenever there is a box with a value, eliminate this value from the values of all its peers.
        Input: A sudoku in dictionary form.
        Output: The resulting sudoku in dictionary form.
        """
        solved_values = [box for box in values.keys() if len(values[box]) == 1]
        for box in solved_values:
            digit = values[box]
            for peer in self.peers[box]:
                values[peer] = values[peer].replace(digit,'')
        return values
    
    def only_choice(self, values):
        """
        Go through all the units, and whenever there is a unit with a value that only fits in one box, assign the value to this box.
        Input: A sudoku in dictionary form.
        Output: The resulting sudoku in dictionary form.
        """
        for unit in self.unitlist:
            for digit in '123456789':
                dplaces = [box for box in unit if digit in values[box]]
                if len(dplaces) == 1:
                    values[dplaces[0]] = digit
        return values
    
    def reduce_puzzle(self, values):
        """
        Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
        If the sudoku is solved, return the sudoku.
        If after an iteration of both functions, the sudoku remains the same, return the sudoku.
        Input: A sudoku in dictionary form.
        Output: The resulting sudoku in dictionary form.
        """
        stalled = False
        while not stalled:
            solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
            values = self.eliminate(values)
            values = self.only_choice(values)
            solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
            stalled = solved_values_before == solved_values_after
            if len([box for box in values.keys() if len(values[box]) == 0]):
                return False
        return values
    
    def search(self, values):
        "Using depth-first search and propagation, try all possible values."
        # First, reduce the puzzle using the previous function
        values = self.reduce_puzzle(values)
        if values is False:
            return False ## Failed earlier
        if all(len(values[s]) == 1 for s in self.boxes): 
            return values ## Solved!
        # Choose one of the unfilled squares with the fewest possibilities
        _,s = min((len(values[s]), s) for s in self.boxes if len(values[s]) > 1)
        # Now use recurrence to solve each one of the resulting sudokus, and 
        for value in values[s]:
            new_sudoku = values.copy()
            new_sudoku[s] = value
            attempt = self.search(new_sudoku)
            if attempt:
                return attempt
    
    def toString(self, grid):
        solved_string = ''
        for i in self.row_units:
            for j in i:
                solved_string += grid[j]
        
        return solved_string