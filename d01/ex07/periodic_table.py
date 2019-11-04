def string_to_dict(line):
    cell = dict()
    title_split = line.split("=")
    cell['name'] = title_split[0].strip()
    params = title_split[1].split(",")
    for data in params:
        key_value_split = data.split(":")
        cell[key_value_split[0].strip()] = key_value_split[1].strip()
    return cell

def read_file():
	with open("periodic_table.txt") as file:
		table = []
		for line in file:
			cell = string_to_dict(line)
			table.append(cell)
		return table


def content(file, table):
	previous = 0
	current = 0
	s = "<table>"
	for elem in table:
		current = int(elem['position'])
		if current == 0:
			s +="<tr>"
		if current - previous > 1:
			s += "<td colspan='" + str(current - previous - 1) + "'></td>"
		s += "<td><h4>" + elem['name'] + "</h4>"
		s += "<ul><li>" + elem['number'] +"</li><li>" + elem['small'] +"</li><li>"  + elem['molar'] + "</li><li>" + elem['electron'] + "</li>" +"</ul></td>"
		if current == 17:
			s += "</tr>"
			current = 0
		previous = current

	s += "</table>"	
	file.write(s)

def header(file):
	file.write("<!DOCTYPE html>\n")
	file.write("<html lang='en'>\n")
	file.write("<head>\n<meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>Periodic table</title>\n")
	file.write("<style>table {	width: 100%;} td {border: 1px solid black; padding:10px} </style></head>\n")

def body(file, table):
	file.write("<body>\n")
	content(file, table)
	file.write("</body>\n")

def footer(file):
	file.write("</html>\n")


def write_to_file(table_dict):
	with open("periodic_table.html", "w") as file: 
		header(file)
		body(file, table_dict)
		footer(file)

def generate_html():
	table_dict = read_file()
	write_to_file(table_dict)

if __name__ == '__main__' :
	generate_html()