def sumTuples(tuple1, tuple2):
    lst1 = list(tuple1)
    lst2 = list(tuple2)
    for i in range(len(lst1)):
        lst2[i] += lst1[i]
    return tuple(lst2)

def exportTojson(data, filename):
    with open(filename, 'w') as file:
        file.write("{\n")
        for i, (key, value) in enumerate(data.items()):
            line = f'  "{key}": "{value}"'
            if i < len(data) - 1:
                line += ",\n"
            else:
                line += "\n"
            file.write(line)
        file.write("}\n")

def importJson(filename):
    with open(filename, 'r') as file:
        content = file.read().strip()
    content = content[1:-1].strip()
    items = content.split(",\n")
    result = {}
    for item in items:
        key, value = item.split(": ")
        key = key.strip('"')
        value = value.strip('"')
        result[key] = value
    return [result]

def menu():
    while True:
        print("\nMenu:")
        print("1. Sum Tuples")
        print("2. Export JSON")
        print("3. Import JSON")
        print("4. Exit")
        choice = input("Enter a choice: ")
        if choice == "1":
            tup1 = tuple(map(int, input("Enter first tuple : ").split(",")))
            tup2 = tuple(map(int, input("Enter second tuple : ").split(",")))
            print("Result:", sumTuples(tup1, tup2))
        elif choice == "2":
            data = {"name": "Ahmad", "age": "30", "city": "Beirut"}
            filename = input("Enter filename: ")
            exportTojson(data, filename)
            print(f"Data exported to {filename}")
        elif choice == "3":
            filename = input("Enter filename: ")
            data = importJson(filename)
            print("Imported Data:", data)
        elif choice == "4":
            print("Exited")
            break
        else:
            print("Invalid choice. Please try again.")

menu()


#a.O(n 3)
#b.O(n 3)
#c.O(n!)
#d.O(n log n)
#e.O(n)
#f.O(n 2)
#O(n 2)
#h.O(n!)