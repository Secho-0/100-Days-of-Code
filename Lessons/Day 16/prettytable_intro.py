import prettytable

#table = prettytable.PrettyTable(["Pokemon","Type"])
# table.add_row(["Bulbasaur","Grass"])
# table.add_row(["Charmander","Fire"])
# table.add_row(["Squirtle"," Water"])

table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Bulbasaur","Charmander","Squirtle"])
table.add_column("Type",["Grass", "Fire", "Water"])
table.align = 'r'
table.junction_char = '~'
print(table)