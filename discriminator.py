# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 14:05:18 2024

@author: sebas

Note: this is the original code from https://www.learningundefeated.org/curriculum/alien-elements/,
      specifically https://www.learningundefeated.org/wp-content/uploads/2025/07/Octet_Rule_GUI-2.0.txt
"""

import tkinter as tk

def check_octet_rule():
    elements_1 = entry_elements_1.get().split(',')
    counts_1 = list(map(int, entry_counts_1.get().split(',')))
    elements_2 = entry_elements_2.get().split(',')
    counts_2 = list(map(int, entry_counts_2.get().split(',')))

    all_elements = elements_1 + elements_2
    all_counts = counts_1 + counts_2

    compound = "".join([f"{element}{_subscript(count)}" if count > 1 else element for element, count in zip(all_elements, all_counts)])
    total_valence = sum(get_valence_electrons(element) * count for element, count in zip(all_elements, all_counts))

    valence_text = f"Total valence electrons: {total_valence}"
    compound_text = f"The compound formed is: {compound}"

    if total_valence % 8 == 0:
        result_text.set(f"{compound_text}\n{valence_text}\nCompound passed!\nThe discriminator thinks this is a real compound!")
    else:
        result_text.set(f"{compound_text}\n{valence_text}\nCompound failed.\nThe discriminator does not think this is a real compound.")

def get_valence_electrons(element):
    # Dictionary containing the number of valence electrons for each element
    valence_electrons = {
        "I": 1, "M": 1, "Wo": 1, "Ie": 1, "B": 1,
        "Nd": 1, "A": 2, "D": 2, "R": 2, "N": 2,
        "Ti": 2, "S": 2, "Ta": 2, "No": 2, "Te": 2,
        "V": 2, "En": 2, "Ei": 2, "O": 3, "Ko": 3,
        "Ng": 3, "Ln":4, "F":4, "P":4, "G":5, "Ad":5,
        "Ai":5, "T": 6, "At": 6, "Df": 6, "H": 7, "As":7,
        "Or":7, "E":8, "C":8, "It":8,
        "i": 1, "m": 1, "wo": 1, "ie": 1, "b": 1,
        "nd": 1, "a": 2, "d": 2, "r": 2, "n": 2,
        "ti": 2, "s": 2, "ta": 2, "no": 2, "te": 2,
        "v": 2, "en": 2, "ei": 2, "o": 3, "ko": 3,
        "ng": 3, "ln":4, "f":4, "p":4, "g":5, "ad":5,
        "ai":5, "t": 6, "at": 6, "df": 6, "h": 7, "as":7,
        "or":7, "e":8, "c":8, "it":8,
    }
    # Check if the element is in the dictionary, return the number of valence electrons
    return valence_electrons.get(element, 0)

def _subscript(number):
    # Function to convert numbers to Unicode subscripts
    subscript_numbers = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    return str(number).translate(subscript_numbers)

root = tk.Tk()
root.title("Octet Rule Checker")
root.geometry("500x500")


font_size = 20
font_family = "Arial"

font = (font_family, font_size)

label_header_1 = tk.Label(root, text="Generator Goal: Create New Compounds", font = font)
label_header_1.pack()

label_space_1 = tk.Label(root, text=" ", font = font)
label_space_1.pack()

label_elements_1 = tk.Label(root, text="Enter element to form compound:", font = font)
label_elements_1.pack()

entry_elements_1 = tk.Entry(root, font = font)
entry_elements_1.pack()

label_counts_1 = tk.Label(root, text="How many of this element:", font = font)
label_counts_1.pack()

entry_counts_1 = tk.Entry(root, font = font)
entry_counts_1.pack()

label_elements_2 = tk.Label(root, text="Enter second element to form compound:", font = font)
label_elements_2.pack()

entry_elements_2 = tk.Entry(root, font = font)
entry_elements_2.pack()

label_counts_2 = tk.Label(root, text="How many of this element:", font = font)
label_counts_2.pack()

entry_counts_2 = tk.Entry(root, font = font)
entry_counts_2.pack()

check_button = tk.Button(root, text="Send to Discriminator", command=check_octet_rule, font = font)
check_button.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font = font)
result_label.pack()

root.mainloop()