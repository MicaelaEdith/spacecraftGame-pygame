import csv
import os

class Data:
    def __init__(self, filename):
        self.filename = filename
        self.fieldnames = ['name', 'level', 'checkpoint', 'health', 'points', 'enhances']
        # Crea el archivo si no existe
        if not os.path.isfile(self.filename):
            self.create_file()

    def create_file(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()

    def read_data(self):
        if not os.path.isfile(self.filename):
            self.create_file()
            return []

        with open(self.filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def write_data(self, data):
        # 'data' es una lista de diccionarios, cada diccionario representa una fila
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writerows(data)

    def update_data(self, name, **kwargs):
        rows = self.read_data()
        for row in rows:
            if row['name'] == name:
                for key, value in kwargs.items():
                    if key in self.fieldnames:
                        row[key] = value

        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(rows)

# Ejemplo de uso
if __name__ == "__main__":
    data_manager = Data('game_data.csv')
    
    # Escribir datos
    data_manager.write_data([
        {'name': 'Player1', 'level': 1, 'checkpoint': 1, 'health': 100, 'points': 10, 'mejoras': 'A1'},
        {'name': 'Player2', 'level': 2, 'checkpoint': 3, 'health': 80, 'points': 20, 'mejoras': 'B2'}
    ])
    
    # Leer datos
    all_data = data_manager.read_data()
    print(all_data)
    
    # Actualizar datos
    data_manager.update_data('Player1', health=90, points=15)
    
    updated_data = data_manager.read_data()
    print(updated_data)