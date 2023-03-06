import numpy as np

# Wczytanie pliku
data = np.genfromtxt('fertilityDiagnosis.txt', delimiter=' ', dtype=str)
print(data)


# Obliczenie minimalnych i maksymalnych wartości dla każdego atrybutu
numeric_data = data[:, :-1]  # Pierwsze 9 kolumn zawiera liczby
numeric_data = numeric_data.astype(float)
# print(numeric_data.dtype)
min_values = np.min(numeric_data)
max_values = np.max(numeric_data)


# Wyświetlenie wyników
print('Minimalne wartości atrybutów:', min_values)
print('Maksymalne wartości atrybutów:', max_values)


# Wypisanie symboli klas decyzyjnych i ich wielkosci
class_column = data[:, -1]  # Ostatnia kolumna zawiera symbole klas decyzyjnych
class_symbols, class_sizes = np.unique(class_column, return_counts=True)
for symbol, size in zip(class_symbols, class_sizes):
    print('Symbol klasy:', symbol, 'Wielkość:', size)


# Wypisanie liczby różnych wartości dla każdego atrybutu
for i in range(data.shape[1]):
    unique_values = np.unique(data[:, i])
    print(f'Liczba różnych wartości dla atrybutu {i}: {len(unique_values)}')


# Wypisanie listy wszystkich różnych wartości dla każdego atrybutu
for i in range(data.shape[1]):
    unique_values = np.unique(data[:, i])
    print(f'Lista różnych wartości dla atrybutu {i}: {unique_values}')


# Obliczenie odchylenia standardowego dla atrybutów numerycznych w całym systemie
std_all = np.std(numeric_data)
print(f'Odchylenie standardowe dla atrybutów numerycznych w całym systemie: {std_all}')


# Wygenerowanie maski z 10% brakujących wartości
mask = np.random.rand(*data.shape) < 0.1
data[mask] = '?'

# Naprawienie brakujących wartości
for i in range(data.shape[1]):
    column = data[:, i]
    if i == data.shape[1] - 1:
        # Atrybut nominalny - szukanie najczęściej występującej wartości
        values, counts = np.unique(column[column != '?'], return_counts=True)
        most_common_value = values[np.argmax(counts)]
        column = np.where(column == '?', most_common_value, column)
    else:
        # Atrybut numeryczny - ustawienie wartości średniej
        column[column == '?'] = np.mean(column[column != '?'].astype(float))

# Zapisanie zmodyfikowanych danych do pliku
np.savetxt('plik_z_brakami.txt', data, delimiter=' ', fmt='%s')


# Normalizacja wartości atrybutów numerycznych na przedziały: <-1,1>, <0,1>, <-10,10>
a = -1
b = 1
a2 = 0
b2 = 1
a3 = -10
b3 = 10
norm_data = ((numeric_data - min_values) * (b - a) / (max_values - min_values)) + a
norm_data2 = ((numeric_data - min_values) * (b2 - a2) / (max_values - min_values)) + a2
norm_data3 = ((numeric_data - min_values) * (b3 - a3) / (max_values - min_values)) + a3

# Zapisanie znormalizowanych danych do pliku
np.savetxt("-1_1.txt", norm_data, delimiter=" ")
np.savetxt("0_1.txt", norm_data2, delimiter=" ")
np.savetxt("-10_10.txt", norm_data3, delimiter=" ")


# Standaryzacja
suma = np.sum(numeric_data)
num = numeric_data.size
mean = suma/num
var = ((numeric_data - mean)**2)
var1 = np.sum(var)
stand = (numeric_data - mean)/var1

sum_spr = np.sum(stand)
mean_spr = sum_spr/num
var_spr = ((stand - mean_spr)**2)
var1_spr = np.sum(var_spr)
print(mean_spr)
print(var1_spr)
