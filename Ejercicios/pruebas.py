class Transactions():

    def __init__(self):
        self.list = []

    def read_file(self):
        with open('transacciones.txt', 'r') as file:
            for line in file:
                values = line.strip().split(",")
                transaccion = {
                    "fecha": values[0],
                    "tipo": values[1],
                    "monto": float(values[2]),
                    "descripción": values[3]
                }
                self.list.append(transaccion)
        print(self.list)

    def balance(self):
        total = 0
        for transaccion in self.list:
            total += transaccion['monto']
        print(f"El balance total es: {total}")

transaction1 = Transactions()
transaction1.read_file()
transaction1.balance()

# Iterar sobre las palabras y contar las frecuencias
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


# Imprimir las palabras repetidas y sus frecuencias
repeated_words = {word: count for word, count in word_count.items() if count > 1}

print("Palabras repetidas y sus frecuencias:")
for word, count in repeated_words.items():
    print(f"{word}: {count}")


    if(list_words[0][::-1].lower()) == list_words[0].lower(): True