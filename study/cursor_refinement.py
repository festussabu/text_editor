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
