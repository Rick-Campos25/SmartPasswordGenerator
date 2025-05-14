import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import string

# ---------------------------
# Basic GUI Layout
# ---------------------------
root = tk.Tk()
root.title("Smart Password Assistant")
root.geometry("950x950")

answers = {}

# ---------------------------
# Set Background Image
# ---------------------------
try:
    bg_image = Image.open("PImage.jpeg")
    bg_image = bg_image.resize((950, 950))
    bg_photo = ImageTk.PhotoImage(bg_image)

    background_label = tk.Label(root, image=bg_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    tk.Label(root, text="[Background image could not be loaded]", fg="red").pack()

# ---------------------------
# Questionnaire Page
# ---------------------------
def submit_answers():
    answers['color'] = entry_color.get()
    answers['animal'] = entry_animal.get()
    answers['number'] = entry_number.get()
    answers['word'] = entry_word.get()
    answers['birth_year'] = entry_birth_year.get()
    answers['birth_place'] = entry_birth_place.get()
    answers['school'] = entry_school.get()
    answers['age'] = entry_age.get()
    answers['pet'] = entry_pet.get()
    answers['car'] = entry_car.get()
    answers['hobby'] = entry_hobby.get()
    answers['food'] = entry_food.get()

    generate_personalized_passwords()

def generate_personalized_passwords():
    suggestions.delete(0, tk.END)  # Clear previous suggestions

    all_fields = ['color', 'animal', 'word', 'birth_place', 'school', 'pet', 'car', 'hobby', 'food']
    number = answers['number'] if answers['number'] else str(random.randint(100, 999))
    extra_number = answers['birth_year'] if answers['birth_year'] else answers['age']

    word_pool = [answers[field].capitalize() for field in all_fields if answers[field]]

    if not word_pool:
        messagebox.showinfo("No Input", "You didn't enter any words, so here are some random strong passwords.")
        for _ in range(3):
            random_password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
            suggestions.insert(tk.END, f"Random Strong: {random_password}")
        return

    # Generate different password combinations using random subsets
    for _ in range(2):
        sample_words = random.sample(word_pool, min(2, len(word_pool)))
        pwd = ''.join(sample_words) + number
        suggestions.insert(tk.END, f"Simple: {pwd}")

    for _ in range(2):
        sample_words = random.sample(word_pool, min(3, len(word_pool)))
        mid = '_'.join(sample_words)
        pwd = mid + number[::-1] + (extra_number if extra_number else '')
        suggestions.insert(tk.END, f"Medium: {pwd}")

    for _ in range(3):
        sample_words = random.sample(word_pool, min(4, len(word_pool)))
        core = ''.join([w[:2] for w in sample_words])
        strong_part = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        special_chars = random.choice('!@#$%^&*')
        pwd = core + special_chars + strong_part + number[::-1] + special_chars
        suggestions.insert(tk.END, f"Strong: {pwd}")

    suggestions.insert(tk.END, "(You can test these in the strength analyzer below!)")

# ---------------------------
# Questionnaire Inputs (Placed directly on root)
# ---------------------------
tk.Label(root, text="Answer the following to get a personalized password:").pack(pady=10)
tk.Label(root, text="(You can skip any question. We'll work with whatever you give us!)", fg="gray").pack()

entry_color = tk.Entry(root, width=30)
tk.Label(root, text="Favorite color:").pack()
entry_color.pack()

entry_animal = tk.Entry(root, width=30)
tk.Label(root, text="Favorite animal:").pack()
entry_animal.pack()

entry_number = tk.Entry(root, width=30)
tk.Label(root, text="A meaningful number:").pack()
entry_number.pack()

entry_word = tk.Entry(root, width=30)
tk.Label(root, text="A favorite word:").pack()
entry_word.pack()

entry_birth_year = tk.Entry(root, width=30)
tk.Label(root, text="What year were you born?").pack()
entry_birth_year.pack()

entry_birth_place = tk.Entry(root, width=30)
tk.Label(root, text="Where were you born?").pack()
entry_birth_place.pack()

entry_school = tk.Entry(root, width=30)
tk.Label(root, text="High school or college attended:").pack()
entry_school.pack()

entry_age = tk.Entry(root, width=30)
tk.Label(root, text="How old are you?").pack()
entry_age.pack()

entry_pet = tk.Entry(root, width=30)
tk.Label(root, text="What is your pet's name?").pack()
entry_pet.pack()

entry_car = tk.Entry(root, width=30)
tk.Label(root, text="What is your dream car?").pack()
entry_car.pack()

entry_hobby = tk.Entry(root, width=30)
tk.Label(root, text="What is your favorite hobby?").pack()
entry_hobby.pack()

entry_food = tk.Entry(root, width=30)
tk.Label(root, text="What is your favorite food?").pack()
entry_food.pack()

tk.Button(root, text="Generate Password Suggestions", command=submit_answers).pack(pady=10)

# ---------------------------
# Suggestions Output
# ---------------------------
tk.Label(root, text="Suggested Passwords:").pack(pady=5)
suggestions = tk.Listbox(root, width=60, height=10)
suggestions.pack()

root.mainloop()