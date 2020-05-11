def chess_index(x, y):
    i = x//50
    j = 7 - y//50
    return i, j

def click_index(x, y):
    i = x//50
    j = y//50
    return i, j