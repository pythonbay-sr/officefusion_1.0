location = r"C:\\Users\\Nikola Kostic\\Downloads\\digital_assistant_software_1.0-main\\projects\\"
path = (location + "events" + ".txt")
i=0

file = open(path, "r")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()

print(line_count)


a_file = open(path, "r")
list_of_lines = a_file.readlines()


a_file = open(path, "w")
list_of_lines[i] = "Line2\n"
a_file.writelines(list_of_lines)
a_file.close()
