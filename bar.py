import tkinter as tk

class VerticalProgressBar(tk.Canvas):
    def __init__(self, master, height, width=20, padding=5, *args, **kwargs):
        super().__init__(master, height=height, width=2*width+30+2*padding, *args, **kwargs)
        self.configure(highlightthickness=0, borderwidth=0)
        self._height = height
        self._width = width
        self._padding = padding
        self._percent1 = 0
        self._percent2 = 0
        self._bar1 = self.create_rectangle(padding, height-padding, width+padding, height+padding, fill="blue")
        self._text1 = self.create_text(width + 10 + 2*padding, height / 2, text="0%")
        self._bar2 = self.create_rectangle(width + 20 + 2*padding, height-padding, 2*width+20+2*padding, height+padding, fill="red")
        self._text2 = self.create_text(2*width + 30 + 2*padding, height / 2, text="0%")
 
    def set_percent(self, percent1, percent2):
        self._percent1 = percent1
        self._percent2 = percent2
        bar_height1 = int(self._height * percent1)
        bar_height2 = int(self._height * percent2)
        self.coords(self._bar1, self._padding, self._height - bar_height1 + self._padding, 
            self._width + self._padding, self._height + self._padding)
        self.coords(self._bar2, self._width + 20 + 2*self._padding, self._height - bar_height2 + self._padding, 
            2*self._width + 20 + 2*self._padding, self._height + self._padding)
        self.itemconfigure(self._text1, text=f"{int(percent1 * 100)}%")
        self.itemconfigure(self._text2, text=f"{int(percent2 * 100)}%")
        self.update()

def main():
    root = tk.Tk()
    root.geometry("500x800")
    progress_bar = VerticalProgressBar(root, height=240, padding=25, width=100)
    progress_bar.pack()

    def update_progress():
        for i in range(100):
            progress_bar.set_percent(i / 100, i/100)
            root.update()
            root.after(100)

    update_progress()
    root.mainloop()

if __name__ == "__main__":
    main()
