import tkinter as tk
from tkinter import scrolledtext, messagebox
import random
from twilio.rest import Client

# 🔐 Twilio Credentials (REPLACE AFTER REGENERATING TOKEN)
account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

# Your WhatsApp number
receiver_number = ['whatsapp:+91+..','whatsapp:+91+..']

root = tk.Tk()
root.title("Match Scheduler Pro")
root.geometry("800x720")
root.config(bg="#121212")

team_entries = []
schedule_text = ""

# -------- Functions --------

def create_team_fields():
    global team_entries

    for widget in team_frame.winfo_children():
        widget.destroy()
    team_entries = []

    try:
        num = int(num_teams_entry.get())
    except:
        return

    for i in range(num):
        row = tk.Frame(team_frame, bg="#121212")
        row.pack(pady=3, anchor="w")

        tk.Label(row, text=f"Team {i+1}",
                 bg="#121212", fg="#ccc").pack(side="left", padx=5)

        entry = tk.Entry(row, width=25)
        entry.pack(side="left", padx=5)

        team_entries.append(entry)


def generate_schedule():
    global schedule_text

    try:
        matches_per_pair = int(matches_entry.get())
    except:
        return

    teams = [e.get() if e.get() else f"Team {i+1}" for i, e in enumerate(team_entries)]

    match_pairs = []

    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            for _ in range(matches_per_pair):
                match_pairs.append((teams[i], teams[j]))

    random.shuffle(match_pairs)

    output_box.delete(1.0, tk.END)
    schedule_text = ""

    for idx, pair in enumerate(match_pairs, start=1):
        line = f"🏆 Match {idx}\n⚔ {pair[0]} vs {pair[1]}\n\n"
        output_box.insert(tk.END, line)
        schedule_text += line


def send_whatsapp():
    if schedule_text == "":
        messagebox.showerror("Error", "Generate schedule first!")
        return

    try:
        message = client.messages.create(
            body="📅 Match Schedule:\n\n" + schedule_text,
            from_='whatsapp:+14155238886',
            to=receiver_number
        )
        messagebox.showinfo("Success", "Message sent to WhatsApp ✅")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# -------- UI --------

tk.Label(root, text="⚽ Match Scheduler",
         font=("Segoe UI", 20, "bold"),
         bg="#121212", fg="#00ffcc").pack(pady=15)

card = tk.Frame(root, bg="#1e1e2f")
card.pack(padx=20, pady=10, fill="x")

tk.Label(card, text="Number of Teams",
         bg="#1e1e2f", fg="white").grid(row=0, column=0, padx=10, pady=10)

num_teams_entry = tk.Entry(card)
num_teams_entry.grid(row=0, column=1, padx=10)

tk.Button(card, text="Create",
          bg="#00cc66", fg="white",
          command=create_team_fields).grid(row=0, column=2, padx=10)

# Scroll area
team_container = tk.Frame(root, bg="#121212")
team_container.pack(fill="both", expand=True)

canvas = tk.Canvas(team_container, bg="#121212", highlightthickness=0)
scrollbar = tk.Scrollbar(team_container, orient="vertical", command=canvas.yview)

team_frame = tk.Frame(canvas, bg="#121212")

team_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=team_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Scroll
canvas.bind_all("<MouseWheel>",
                lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

# Matches
tk.Label(root, text="Matches per pair",
         bg="#121212", fg="white").pack(pady=5)

matches_entry = tk.Entry(root)
matches_entry.pack()

# Buttons
tk.Button(root, text="Generate Schedule",
          bg="#ff6600", fg="white",
          command=generate_schedule).pack(pady=10)

tk.Button(root, text="Send to WhatsApp",
          bg="#25D366", fg="white",
          command=send_whatsapp).pack(pady=5)

# Output
output_box = scrolledtext.ScrolledText(root,
                                       height=15,
                                       bg="#0f172a", fg="#00ffcc")
output_box.pack(padx=20, pady=10, fill="both", expand=True)

root.mainloop()