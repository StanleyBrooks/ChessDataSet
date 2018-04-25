import pandas as pd

#Use pandas to read the csv file
chess_data = pd.read_csv('games.csv')

chess_data = (
    
    chess_data.assign(
        
        #This takes the opening_name column and extracts only the opening name (drops the variation)
        #then uses it to create a new column called opening_type, this will be used to find the most
        #common opening moves amongst the best players
        
        opening_type = chess_data.opening_name.map(
            lambda open_name: open_name.split(':')[0].split('#')[0].split('|')[0].strip()
        ),
        
        #The opening_ply column specifies how many of the moves are infact part of the opening moves
        #This creates a new column called opening_moves that consists only the first (opening_ply number) of moves
        #apply is used to make a series into a dataframe and axis=1 is used to take the entire row (of moves once split)
        
        opening_moves = chess_data.apply(
            lambda open_moves: open_moves['moves'].split(" ")[:open_moves['opening_ply']], axis=1
        )
    )
)