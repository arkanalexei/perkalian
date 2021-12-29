"""
TODO:
1. Rapihin GUI nya
2. Add comments
3. Bug fixes?
4. Bikin log jawaban sebelumnya
"""

import tkinter as tk
import random
from tkinter.constants import END

window = tk.Tk()

lives = tk.IntVar()
level = tk.IntVar()
left = tk.IntVar()
right = tk.IntVar()

feedback = tk.StringVar()
info_mode = tk.IntVar()

def get_ans():
    return entry2.get()

def mode_satu(ans):

    expected = str(left.get() * right.get())
    answer = get_ans()
    entry2.delete(0, END)
    if lives.get() > 0:
        choice = random.choice(['tambah_kiri', 'tambah_kanan'])
        if choice == 'tambah_kiri':
            right.set(right.get() + 1)
        else:
            left.set(left.get() + 1)

        if expected == answer:
            print('Hore benar!')
            feedback.set('Hore benar!')
            level.set(level.get() + 1)
        else:
            print("Yah, salah... yang benar adalah", expected, "ya!")
            lives.set(lives.get() - 1)
            print("Sisa nyawa:", lives.get())
            feedback.set(f'Yah, salah.. yang benar adalah {expected} ya!\nSisa nyawa: {lives.get()}')

    else:
        feedback.set(f'Game selesai. Selamat, kamu sampai level {level.get()}!')

def widgets(mode):
    global entry2

    for widget in window.winfo_children():
        if widget not in [label1, btn_main, btn_trik, btn_exit]:
            widget.destroy()

    if mode == '1':

        # RESET #
        lives.set(3)
        level.set(1)
        left.set(1)
        right.set(1)
        feedback.set('')

        label2 = tk.Label(window, text='Jawaban: ')
        entry2 = tk.Entry(window, width=15)
        
        
        entry2.bind('<Return>', mode_satu)

        label_left = tk.Label(window, textvariable = left)
        label_right = tk.Label(window, textvariable = right)
        label_kali = tk.Label(window, text='*')


        label_feedback = tk.Label(window, textvariable = feedback)

        label2.grid(row=5, column=0, columnspan=2)
        entry2.grid(row=6, column=0, columnspan=2)

        label_left.grid(row = 4, column= 0, sticky='E')
        label_kali.grid(row=4, column=1)
        label_right.grid(row = 4, column= 2, sticky='W')

        label_feedback.grid(row = 7, column= 0, columnspan=2)



    elif mode == '2':
        pre_info = 20*'=', "TRIK RAHASIA", 20*'='

        info = 'Rahasia game ini (dan juga perkalian pada dunia nyata): perkalian adalah penjumlahan berulang!\
            \nSebagai contoh, 3 x 4 = 4 + 4 + 4 (4-nya ada 3) = 12. Bisa juga 3 x 4 = 3 + 3 + 3 + 3 (3-nya ada 4) = 12\
            \n\nNah, dengan memerhatikan jawaban soal sebelumnya, kamu bisa menjawab pertanyaan lebih cepat!\
            \nMisalnya, sebelumnya ditanyakan 2 x 5 = 10\
            \nKalau kamu ditanya berapa 3 x 5, maka ingat bahwa 2 x 5 itu 5-nya 2 kali, sedangkan 3 x 5 itu 5-nya 3 kali\
            \nArtinya, karena 2 x 5 = 5 + 5, maka 3 x 5 = 5 + 5 + 5 = (2 x 5) + 5 = 10 + 5\
            \nJadi, kamu hanya perlu menambahkan 5 dari jawaban sebelumnya, sehingga didapatlah hasil 3 x 5 = 15\
            \n\nNah, kalau kamu ditanya berapa 2 x 6, maka ingat 2 x 5 itu 2-nya 5 kali, sedangkan 2 x 6 itu 2-nya 6 kali\
            \nMirip tadi, karena 2 x 5 = 2 + 2 + 2 + 2 + 2, maka 2 x 6 = 2 + 2 + 2 + 2 + 2 + 2 = (2 x 5) + 2 = 10 + 2\
            \nJadi, kamu hanya perlu menambahkan 2 dari jawaban sebelumnya, sehingga hasilnya adalah 2 x 6 = 12'

        post_info = 20*'=', "Good luck!", 20*'='

        label2 = tk.Label(window, text=f'{pre_info}\n{info}\n{post_info}')
        label2.grid(row=4, column=0)

    elif mode == '3':
        raise SystemExit

# GUI #
window.geometry("700x500")  

# Pilih Mode
label1 = tk.Label(window, text='Pilih Mode')
label1.grid(row=0, column=0, columnspan=2)

def get_mode_one():
    return widgets('1')

def get_mode_two():
    return widgets('2')

def get_mode_three():
    return widgets('3')

btn_main = tk.Button(window, text='Main', command=get_mode_one)
btn_trik = tk.Button(window, text='Trik Rahasia', command=get_mode_two)
btn_exit = tk.Button(window, text='Exit', command=get_mode_three)

btn_main.grid(row=1, column=0, columnspan=2)
btn_trik.grid(row=2, column=0, columnspan=2)
btn_exit.grid(row=3, column=0, columnspan=2)


window.mainloop()