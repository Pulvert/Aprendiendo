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