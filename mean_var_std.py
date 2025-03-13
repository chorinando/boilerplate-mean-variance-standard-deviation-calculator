import numpy as np

def calculate(list):
    # Validasi input: harus berisi 9 angka
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Konversi list menjadi 3x3 NumPy array
    matrix = np.array(list).reshape(3, 3)

    # Hitung statistik
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # Mean per kolom
            matrix.mean(axis=1).tolist(),  # Mean per baris
            matrix.mean().tolist()         # Mean seluruh elemen
        ],
        'variance': [
            matrix.var(axis=0).tolist(),  # Variance per kolom
            matrix.var(axis=1).tolist(),  # Variance per baris
            matrix.var().tolist()         # Variance seluruh elemen
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),  # Standard deviation per kolom
            matrix.std(axis=1).tolist(),  # Standard deviation per baris
            matrix.std().tolist()         # Standard deviation seluruh elemen
        ],
        'max': [
            matrix.max(axis=0).tolist(),  # Max per kolom
            matrix.max(axis=1).tolist(),  # Max per baris
            matrix.max().tolist()         # Max seluruh elemen
        ],
        'min': [
            matrix.min(axis=0).tolist(),  # Min per kolom
            matrix.min(axis=1).tolist(),  # Min per baris
            matrix.min().tolist()         # Min seluruh elemen
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),  # Sum per kolom
            matrix.sum(axis=1).tolist(),  # Sum per baris
            matrix.sum().tolist()         # Sum seluruh elemen
        ]
    }

    return calculations
