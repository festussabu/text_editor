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
# print(buffer)
# print(gap_start, gap_end)


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

# print(buffer)
# print(gap_start, gap_end)


def move_cursor_right():
    global gap_start, gap_end
    if gap_end == len(buffer):
        return
    buffer[gap_start] = buffer[gap_end]
    buffer[gap_end] = "_"
    gap_start += 1
    gap_end += 1


move_cursor_right()

# print(buffer)
# print(gap_start, gap_end)
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


# insert_text("RLD\nThis\nis\nso\nintersting!")
# move_cursor_left()
# insert_text("END")
#
# print(buffer)
# print(gap_start, gap_end)


def backspace():
    global gap_start
    if gap_start == 0:
        return
    gap_start -= 1
    buffer[gap_start] = "_"


# backspace()

# print(buffer)
# print(gap_start, gap_end)
# TODO: END


# TODO: move cursor up/down
def get_text():
    return buffer[:gap_start] + buffer[gap_end:]


print(get_text())


# find where the new line starts
def build_line_starts(text):
    line_starts = [0]
    for i, ch in enumerate(text):
        if ch == "\n":
            line_starts.append(i + 1)
    return line_starts


print(build_line_starts(get_text()))


# get the row, col where the cursor currently is
def cursor_row_col(text, cursor, line_starts):
    row = 0
    for r in range(len(line_starts)):
        if line_starts[r] <= cursor:
            row = r
        else:
            break
    col = cursor - line_starts[row]
    return row, col


print(
    cursor_row_col(get_text(), gap_start, build_line_starts(get_text())),
)


def row_col_to_cursor(text, row, col, line_starts):
    if row < 0:
        return 0
    if row >= len(line_starts):
        return len(text)

    start = line_starts[row]
    end = start
    while end < len(text) and text[end] != "\n":
        end += 1

    line_len = end - start
    col = min(col, line_len)

    return start + col


print(
    row_col_to_cursor(
        get_text(),
        1,
        2,
        build_line_starts(get_text()),
    )
)


def move_gap_to(target):
    while gap_start > target:
        move_cursor_left()
    while gap_start < target:
        move_cursor_right()


def move_cursor_up():
    text = get_text()
    line_starts = build_line_starts(text)
    row, col = cursor_row_col(text, gap_start, line_starts)
    if row == 0:
        return
    target = row_col_to_cursor(text, row - 1, col, line_starts)
    move_gap_to(target)


def move_cursor_down():
    text = get_text()
    line_starts = build_line_starts(text)
    row, col = cursor_row_col(text, gap_start, line_starts)
    if row >= len(line_starts) - 1:
        return
    target = row_col_to_cursor(text, row + 1, col, line_starts)
    move_gap_to(target)


print(buffer)
move_cursor_up()
print(buffer)
move_cursor_down()
print(buffer)


import tkinter as tk

root = tk.Tk()
root.configure(background="white")
root.minsize(200, 200)
root.minsize(800, 800)

label = tk.Label(root, font=("Consolas", 16), anchor="nw", justify="left")
label.pack(fill="both", expand=True)


def redraw():
    text = "".join(get_text())
    cursor = gap_start
    raw = "".join(buffer)
    display = raw[:cursor] + "|" + raw[cursor:]
    label.config(text=display)


def on_key(event):
    if event.keysym == "h":
        move_cursor_left()
    elif event.keysym == "l":
        move_cursor_right()
    elif event.keysym == "k":
        move_cursor_up()
    elif event.keysym == "j":
        move_cursor_down()
    elif event.char and event.char.isprintable():
        insert_text(event.char)
    elif event.keysym == "BackSpace":
        backspace()
    redraw()


root.bind("<Key>", on_key)
redraw()
root.mainloop()
