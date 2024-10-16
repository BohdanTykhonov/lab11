import csv
import os

def load_data(file_path):
    if not os.path.exists(file_path):
        print("Файл не знайдено!")
        return None

    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        data.append(header)

        for row in csv_reader:
            try:
                row[3] = float(row[3])
            except ValueError:
                row[3] = None
            data.append(row)

    return data

def display_data(data):
    if data:
        for row in data:
            print(row)

def filter_data(data, threshold):
    if data:
        header = data[0]
        filtered_data = [header]

        for row in data[1:]:
            if row[3] is not None and row[3] > threshold:
                filtered_data.append(row)

        return filtered_data

def save_filtered_data(filtered_data, output_file):
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(filtered_data)
            print(f"Відфільтровані дані записані у файл {output_file}")
    except Exception as e:
        print(f"Помилка запису файлу: {e}")

def main():
    file_path = 'inflation.csv'
    output_file = 'filtered_inflation.csv'

    data = load_data(file_path)

    if data is None:
        return

    print("Вміст файлу:")
    display_data(data)

    try:
        threshold = float(input("Введіть значення інфляції для пошуку країн (у %): "))
    except ValueError:
        print("Некоректне значення!")
        return

    filtered_data = filter_data(data, threshold)

    if filtered_data and len(filtered_data) > 1:
        print(f"Країни з інфляцією більше, ніж {threshold}%:")
        display_data(filtered_data)
        save_filtered_data(filtered_data, output_file)
    else:
        print(f"Немає країн з інфляцією більше, ніж {threshold}%.")

if __name__ == "__main__":
    main()
