from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Rank", "Member", "Point"]
table.add_rows(
    [
        [1, "Squad 4", 40],
        [2, "Squad 11", 28],
        [3, "Squad 13", 20],
        [4, "Squad 1", 15],
        [5, "Squad 10", 15],
        [6, "Squad 3", 11],
        [7, "Squad 8", 10],
        [8, "Squad 9", 10],
        [9, "Squad 12", 10],
        [10, "Squad 7", 6],
        [11, "Squad 14", 6],
        [12, "Squad 6", 3],
        [13, "Squad 2", 1],
    ]
)
table.align = "l"
print(table)
