from tkinter import *
from cell import Cell
import settings

root = Tk()
#override the settings of window
root.configure(bg="grey")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}') #size of the screen
root.title("Minesweeper")
root.resizable(False, False) #to make the window non resizweable, one for width, one for height

top_frame = Frame(
    root,
    bg= "black",
    width=settings.WIDTH,
    height=settings.HEIGHT/4
)
top_frame.place(x=0, y=0) #purpose of starting from 0, we want this frame fitted to the sides, begin from point 0
game_title = Label(
    top_frame,
    bg= "black",
    fg = "white",
    text="Minesweeper Game",
    font= ("", 36)
)

game_title.place(
    x = settings.WIDTH//4,
    y = 0

)
left_frame= Frame(
    root,
    bg ="dark grey",
    width = settings.WIDTH/4,
    height = settings.HEIGHT - settings.HEIGHT/4 #we would go for 480 to keep the whole screen, but we already used 120 on top frame, so 480 - 120
)
left_frame.place ( x=0, y=120)


center_frame = Frame(
    root,
    bg="grey",
    width = settings.WIDTH/4*3,
    height = settings.HEIGHT/4*3 
)
center_frame.place(
    x=settings.WIDTH/4,
    y=settings.HEIGHT/4
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column = x, row = y 
        )

#call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
    )
Cell.randomize_mines()

# Run the window
root.mainloop()