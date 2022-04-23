from tkinter import Button, Label
import random
import settings
import ctypes
import sys


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    def __init__(self,x,y, is_mine = False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y
        #append the object to the cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width = 9,
            height = 3, 
        )
        btn.bind('<Button-1>', self.left_click_actions )
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text = f"Cells Left:{Cell.cell_count}",
            fg="black",
            bg="dark grey",
            font=("Calibri", 18)
        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mine_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()  #this is where it should show how many mine there are around
            #if mines count is equal to cells left, we should win the game

            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, "You Won", "Game Over", 0)
        #cancel left and right click action if cell is opened
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def get_cell_by_axis(self, x, y):
        #return a cell object depending on the values of x and y
        for cell in Cell.all: #using the class name
            if cell.x == x and cell.y == y:
                return cell
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x-1, self.y-1),
            self.get_cell_by_axis(self.x-1, self.y),
            self.get_cell_by_axis(self.x-1, self.y+1),
            self.get_cell_by_axis(self.x, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y),
            self.get_cell_by_axis(self.x+1, self.y+1),
            self.get_cell_by_axis(self.x, self.y+1),
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mine_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            #print(self.get_cell_by_axis(0,0))

            #print(self.surrounded_cells_mine_length) #now we can return the counter number of how many mines are arround
            self.cell_btn_object.configure(text=self.surrounded_cells_mine_length)
            #replace the cell count label

            if Cell.cell_count_label_object :
                Cell.cell_count_label_object.configure(
                    text = f"Cells Left:{Cell.cell_count}"
                )
            #if this was a mine cand., change the bg to system default
            self.cell_btn_object.configure(
                bg= "SystemButtonFace"
            )

        #after doing all of the above, mark the cell as opened
        self.is_opened = True

    def show_mine(self):
        #right a logic to interrup the game, show a message
        self.cell_btn_object.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0, "You clicked on mine", "Game Over", 0)
        sys.exit()


    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg="yellow"
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg="SystemButtonFace"
            )
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"