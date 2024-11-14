from pyscript import document
import card_matrix
import random

# this array store all possible number the caller can call, and should be shuffled during reset
all_bingo_numbers = []
# this array stores the numbers that have been called this game.
called_numbers = []

# this array stores the 25 numbers generated for the bingo card
card_numbers = []


# EVENTS
def reset_game(event):
    print("calling 'reset_game'")
    # complete me
    generate_card()
    shuffle_caller()
    reset_calls()
    document.querySelector("#win_game").close()
    document.querySelector("#called_numbers").innerHTML = ""
    document.querySelector("#current_call").innerHTML = ""

    #  should handle cell clicks and update the cell's highlight status


def check_cell(event):
    print("calling 'check_cell'")
    # use event to get the cell id that
    # was clicked and it's value
    cell_id = event.target.id
    cell_val = int(event.target.innerHTML)
    cell_id = cell_id.replace('cell', '')
    xcoord = int(cell_id.split('-')[0])
    ycoord = int(cell_id.split('-')[1])
    # complete me
    if cell_val in called_numbers and not card_matrix.is_position_marked(xcoord, ycoord):
        highlight_card_cell("#cell" + cell_id)
        win = card_matrix.mark_position(xcoord, ycoord)
        if win:
            document.querySelector("#win_game").showModal()


def call_next(event):
    global all_bingo_numbers
    print("calling 'call_next'")
    # complete me
    if len(all_bingo_numbers) > 0:
        current_num = all_bingo_numbers.pop()
        document.querySelector("#current_call").innerHTML = current_num
        called_numbers.append(current_num)  # adds array element
        highlight_caller_cell("#num" + str(current_num))
        document.querySelector("#called_numbers").innerHTML = ", ".join(str(x) for x in called_numbers)


# INTERNAL FUNCTIONS
def shuffle_caller():
    global all_bingo_numbers
    print("Calling 'shuffle_caller'")
    # complete me
    all_bingo_numbers = list(range(1, 76))
    random.shuffle(all_bingo_numbers)
    for x in range(1, 76):
        reset_caller_cell("#num" + str(x))


def reset_calls():  # reset the list of called numbers
    global called_numbers
    print("Calling 'reset_calls'")

    # complete me
    called_numbers = []


def generate_card():
    global card_numbers
    print("Calling 'generate_card'")

    # complete me
    card_numbers = list(range(1, 76))
    random.shuffle(card_numbers)
    card_numbers = card_numbers[:25]
    for x in range(5):
        for y in range(5):
            id = "#cell" + str(x + 1) + "-" + str(y + 1)
            document.querySelector(id).innerHTML = card_numbers.pop()
            reset_card_cell(id)


def add_called(num):
    global called_numbers
    print("Calling 'add_called'")

    # complete me
    if num not in called_numbers:
        called_numbers.append(num)


# adds/removes highlight CSS classes from cells (these are complete, don't change)
def highlight_card_cell(cell_id):
    document.querySelector(cell_id).className += "highlight-card"


def reset_card_cell(cell_id):
    document.querySelector(cell_id).className = ""


def highlight_caller_cell(cell_id):
    document.querySelector(cell_id).className += "highlight-caller"


def reset_caller_cell(cell_id):
    document.querySelector(cell_id).className = ""


# initial setup
reset_game(0)
