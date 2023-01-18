import tkinter as tk
import uuid
import pyperclip

def generate_uuid():
    new_uuid = str(uuid.uuid4())
    pyperclip.copy(new_uuid)
    print(f'UUID {new_uuid} 已经在你的粘贴板里了.')

root = tk.Tk()
root.title("UUID")

generate_button = tk.Button(root, text="生成 UUID", command=generate_uuid)
generate_button.pack()

root.mainloop()
