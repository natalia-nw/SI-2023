import numpy as np
import gradio as gr


# fertilityDiagnosis.txt


# Obliczenie minimalnych i maksymalnych wartości dla każdego atrybutu
def get_min_max(data):
    numeric_data = data[:, :-1]  # Pierwsze 9 kolumn zawiera liczby
    numeric_data = numeric_data.astype(float)
    # print(numeric_data.dtype)
    min_values = np.min(numeric_data)
    max_values = np.max(numeric_data)
    return f"min= {min_values}, max= {max_values}"


# Wypisanie symboli klas decyzyjnych i ich wielkosci
def get_symbol_wielkosc(data):
    class_column = data[:, -1]  # Ostatnia kolumna zawiera symbole klas decyzyjnych
    class_symbols, class_sizes = np.unique(class_column, return_counts=True)
    tab = []
    for symbol, size in zip(class_symbols, class_sizes):
        tab.append(f"symbol: {symbol}, wielkosc: {size}")
    return tab


# Wypisanie liczby różnych wartości dla każdego atrybutu
def get_liczba_roznych(data):
    tab = []
    for i in range(data.shape[1]):
        unique_values = np.unique(data[:, i])
        tab.append(f"Liczba różnych wartości dla atrybutu {i}: {len(unique_values)}")
    return tab


# Wypisanie listy wszystkich różnych wartości dla każdego atrybutu
def get_lista_roznych(data):
    tab = []
    for i in range(data.shape[1]):
        unique_values = np.unique(data[:, i])
        tab.append(f"Lista różnych wartości dla atrybutu {i}: {unique_values}")
    return tab


# Obliczenie odchylenia standardowego dla atrybutów numerycznych w całym systemie
def get_std(data):
    numeric_data = data[:, :-1]  # Pierwsze 9 kolumn zawiera liczby
    numeric_data = numeric_data.astype(float)
    std_all = np.std(numeric_data)
    return f"Odchylenie standardowe dla atrybutów numerycznych w całym systemie: {std_all}"


def result(file, rows):
    data = np.genfromtxt(file, delimiter=' ', dtype=str)
    mm = get_min_max(data)
    sw = get_symbol_wielkosc(data)
    lr1 = get_liczba_roznych(data)
    lr2 = get_lista_roznych(data)
    std = get_std(data)
    return f"{data[:int(rows)]},\n\n{mm},\n\n{sw[:int(rows)]},\n\n{lr1[:int(rows)]},\n\n{lr2[:int(rows)]},\n\n{std}"


# Tworzy interfejs Gradio
inputs = [gr.inputs.Textbox(label="Nazwa pliku", default="fertilityDiagnosis.txt"), gr.inputs.Number(label="Liczba wierszy", default=100)]
outputs = [gr.outputs.Textbox()]
io = gr.Interface(fn=result, inputs=inputs, outputs=outputs, title="Chatbot - tabela decyzyjna", description="Wczytuje dane z pliku i wyświetla wybraną liczbę wierszy i ogólny opis tabeli")

# Uruchamia interfejs
io.launch()
