#Website: Visualisasi Distribusi Poisson dengan Flask

Proyek ini adalah website sederhana berbasis Flask yang memungkinkan pengguna memasukkan nilai **λ (lambda)** dan **jumlah peristiwa maksimum (x_max)** untuk menghasilkan hasil dari rumus distribusi Poisson yang menggunakan perhitungan manual tanpa library serta histogram distribusi Poisson

## 📌 Fitur
- Input nilai λ (lambda) dan batas atas nilai x
- Perhitungan probabilitas distribusi Poisson
- Visualisasi histogram

## 🧠 Rumus Distribusi Poisson
\[
P(X = k) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}
\]
di mana:
- \( \lambda \): rata-rata jumlah kejadian
- \( k \): jumlah kejadian (0 sampai x_max)

