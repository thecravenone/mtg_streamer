from tkinter import *
window = Tk()

# Setting initial life totals
lpl=20
rpl=20

# Function to write life total changes to files
def write_life_change(player, replacement):
	file_to_write = "./output/" + player + "pl.txt"
	file = open(file_to_write, 'w')
	file.write(str(replacement))
	file.close()

# Function to process life total changes
def make_change(player, direction):
	print("Life total change: " + player + direction)
	global lpl
	global rpl
	if player == "l":
		if direction == "+":
			lpl+=1
		elif direction == "-":
			lpl-=1
		write_life_change("l", lpl)
	elif player == "r":
		if direction == "+":
			rpl+=1
		elif direction == "-":
			rpl-=1
		write_life_change("r", rpl)

# Function to update player/deck name files
def update_names():
	print("Updating names")
	lpn_file = open("./output/lpn.txt", 'w')
	lpn_file.write(lpn.get())
	lpn_file.close()

	lpd_file = open("./output/lpd.txt", 'w')
	lpd_file.write(lpd.get())
	lpd_file.close()

	rpn_file = open("./output/rpn.txt", 'w')
	rpn_file.write(rpn.get())
	rpn_file.close()

	rpd_file = open("./output/rpd.txt", 'w')
	rpd_file.write(rpd.get())
	rpd_file.close()

# Function to return things to default on startup
def startup():
	print("Starting up")
	# Reset lifetotals to 20 on startup
	write_life_change("l", 20)
	write_life_change("r", 20)
	# Reset Names
	lpn.insert(0, "Left Player Name")
	lpd.insert(0, "Left Player Deck")
	rpn.insert(0, "Right Player Name")
	rpd.insert(0, "Right Player Deck")
	update_names()



# Build the GUI
window.title("MtG Streamer v0.0.1")

#Left player
Label(window, text = "Left Player").grid(row = 0, column = 0)

lpn = Entry(window)
lpn.grid(row = 1, column = 0)

lpd = Entry(window)
lpd.grid(row = 2, column = 0)

#Right player
Label(window, text = "Right Player").grid(row = 0, column = 3)

rpn = Entry(window)
rpn.grid(row = 1, column = 3)

rpd = Entry(window)
rpd.grid(row = 2, column = 3)

# Life total changes
# Left player
Button(window, text = "+", command = lambda: make_change("l", "+")).grid(row = 1, column = 1)
Button(window, text = "-", command = lambda: make_change("l", "-")).grid(row = 2, column = 1)
# Right player
Button(window, text = "+", command = lambda: make_change("r", "+")).grid(row = 1, column = 2)
Button(window, text = "-", command = lambda: make_change("r", "-")).grid(row = 2, column = 2)

# Save changes
Button(window, text = "Save changes", command = update_names).grid(row = 3, column = 0, columnspan = 4)

# Return things to default and begin the mainloop
startup()
window.mainloop()
