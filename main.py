from datetime import datetime
from random import choice
import tkinter as tk

phrases_workday:list = [
    # Funny random phrases
    'Сегодня ты обязан заниматься',
    'Здаров! Начни день с',
    'Че как? Не забывай о',
    'Никаких игр сегодня! Трайхардим',
    'Ну что, займемся',
    'Не забывай, ради чего ты стараешься.\n Сегодня у тебя по планам',
    'Едем едем, летим, погнали! Нас ждет',
    'Готов загрузить голову? Сегодня'
]
phrases_weekend:list = [
    'Сегодня отдых! Ты заслужил',
    'Здаров! Крутых выходных тебе',
    'Че как? Крутого отдыха',
    'День игр сегодня!',
    'Посмотри фильм, который давно хотел\nСегодня можно, лол',
    'Сегодня ничего не делай\nЛучше разгрузить голову'
]
todo_dict:dict = {
    # Write your plans here:

    0: 'Codewars',                #пн
    1: 'LeetCode',                #вт
    2: 'SQL, Docker, Git, bash',  #ср
    3: 'SQL, Docker, Git, bash',  #чт
    4: 'Codewars',                #пт
    5: 'LeetCode',                #сб
    6: 'Выходной'                 #вс
}

weekends:list = [6]       # ADD YOUR WEEKEND DAYS HERE!

def currentPlan()-> str:
    """
    args: None
    return: Your plan for the day
    """
    now = datetime.now()
    weekday = now.weekday()\
    # Main msg
    if weekday not in weekends:
        return f"{choice(phrases_workday)} {todo_dict[weekday]}"
    else:
        return f"{choice(phrases_weekend)}"
    
    #return f"{choice(phrases_workday)} {todo_dict[weekday]}" if weekday not in weekends else f"{choice(phrases_weekend)}"

# print(checkWeekday()) # Debug

def show_frame():
    def center_window(window): # Center the main window
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")

    root = tk.Tk()
    root.title("ПЛАН НА ДЕНЬ")
    root.geometry("500x200")
    root.attributes('-topmost', True)
    center_window(root)

    label = tk.Label(
        root, 
        text=currentPlan(), 
        font=("Arial", 16), 
        pady=50
    )
    label.pack()
    
    button = tk.Button(
        root,
        text="Ок, Погнали", 
        command=root.destroy, 
        font=("Arial", 12), 
        bg="green", 
        fg="white"
    )
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    show_frame()