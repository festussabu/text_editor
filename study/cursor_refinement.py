buffer = ["_"] * 10

# VARIABLES
gap_start = 0
gap_end = len(buffer)

# ADDING DATA TO BUFFER
buffer[gap_start] = "H"
gap_start += 1

buffer[gap_start] = "E"
gap_start += 1

buffer[gap_start] = "L"
gap_start += 1

buffer[gap_start] = "L"
gap_start += 1

buffer[gap_start] = "O"
gap_start += 1

buffer[gap_start] = "\n"
gap_start += 1

buffer[gap_start] = "W"
gap_start += 1

buffer[gap_start] = "O"
gap_start += 1

# TODO: move cursor left or right
print(buffer)
print(gap_start, gap_end)


# Move cursor left by one
def move_cursor_left():
    global gap_start, gap_end
    if gap_start == 0:
        return
    gap_start -= 1
    gap_end -= 1
    buffer[gap_end] = buffer[gap_start]
    buffer[gap_start] = "_"


move_cursor_left()

print(buffer)
print(gap_start, gap_end)


def move_cursor_right():
    global gap_start, gap_end
    if gap_end == len(buffer):
        return
    buffer[gap_start] = buffer[gap_end]
    buffer[gap_end] = "_"
    gap_start += 1
    gap_end += 1


move_cursor_right()

print(buffer)
print(gap_start, gap_end)
# TODO: END


# TODO: Insert, Backspace, Grow gap
def grow_gap(grow_by=5):
    global gap_end, gap_start, buffer
    # create a copy of old buffer to new buffer with the added space
    old = buffer
    n = len(buffer)
    right_len = n - gap_end
    new = ["_"] * (n + grow_by)

    # add the old buffer from index 0 - gap_start to the new buffer
    new[:gap_start] = old[:gap_start]

    # add the right side of the gap to new's end
    if right_len > 0:
        new[-right_len:] = old[gap_end:]
    buffer = new
    gap_end = len(new) - right_len


def insert_text(text):
    global gap_start, gap_end
    for ch in text:
        if gap_start == gap_end:
            grow_gap()
        buffer[gap_start] = ch
        gap_start += 1


insert_text("RLD\nThis\nis\nso\nintersting!")
move_cursor_left()
insert_text("END")

print(buffer)
print(gap_start, gap_end)


def backspace():
    global gap_start
    if gap_start == 0:
        return
    gap_start -= 1
    buffer[gap_start] = "_"


backspace()

print(buffer)
print(gap_start, gap_end)
# TODO: END
