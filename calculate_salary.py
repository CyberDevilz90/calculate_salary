def calculate_salary():
    try:
#input dari user
        hours_worked = float(input("Masukkan jumlah jam kerja: "))
        hourly_rate = float(input("Masukkan tarif per jam: "))

#perhitungan gaji
        if hours_worked > 40:
            regular_hours = 40
            overtime_hours = hours_worked - 40
            total_salary = (regular_hours * hourly_rate) + (overtime_hours * hourly_rate * 1.5)
        else:
            total_salary = hours_worked * hourly_rate

#menampilkan hasil
        print(f"Gaji total Anda adalah: Rp {total_salary:.2f}")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        
#menjalankan fungsi
if __name__ == "__main__":
    calculate_salary()
