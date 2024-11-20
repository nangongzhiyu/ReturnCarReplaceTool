import tkinter as tk
from tkinter import messagebox

def replace_newlines():
    text_input = text_area.get("1.0", tk.END).strip()
    replace_char = replace_entry.get("1.0", tk.END).strip()  
    result = text_input.replace('\r\n', replace_char)  
    result = result.replace('\n', replace_char)
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)
    result_text.config(state=tk.DISABLED)

def copy_result():
    result = result_text.get("1.0", tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(result)
    messagebox.showinfo("提示", "结果已复制到剪贴板！")

def paste_into_text_area():
    text_area.insert(tk.END, root.clipboard_get())

def clear_input_text():
    text_area.delete("1.0", tk.END)

root = tk.Tk()
root.title("换行符替换工具")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="输入文本：").grid(row=0, column=0, sticky=tk.W)
text_area = tk.Text(frame, height=10, width=40)
text_area.grid(row=1, column=0, pady=(0, 10), sticky=tk.NSEW)

tk.Label(frame, text="替换为：").grid(row=0, column=2, sticky=tk.NW)
replace_entry = tk.Text(frame, height=10, width=40, wrap='word')  
replace_entry.grid(row=1, column=2, pady=(0, 10), sticky=tk.NSEW)

result_text = tk.Text(frame, height=10, width=60, state=tk.DISABLED)
result_text.grid(row=2, column=0, columnspan=4, pady=(10, 0), sticky=tk.NSEW)

paste_button = tk.Button(frame, text="粘贴进输入文本", command=paste_into_text_area, height=2, width=20)
paste_button.grid(row=3, column=0, pady=(10, 0), sticky=tk.NSEW)

process_button = tk.Button(frame, text="处理文本    ", command=replace_newlines, height=2, width=20)
process_button.grid(row=3, column=2, pady=(10, 0), sticky=tk.NSEW)

copy_button = tk.Button(frame, text="复制结果", command=copy_result, height=2, width=20)
copy_button.grid(row=4, column=0, pady=(10, 0), sticky=tk.NSEW)

clear_button = tk.Button(frame, text="清除输入", command=clear_input_text, height=2, width=20)
clear_button.grid(row=4, column=1, columnspan=3, pady=(10, 0), sticky=tk.NSEW)


# default_font = ("微软雅黑", 12)
# root.option_add("*Font", default_font)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.rowconfigure((1, 2), weight=1)

root.mainloop()