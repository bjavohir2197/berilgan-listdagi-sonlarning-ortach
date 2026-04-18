sonlar = [15, 8, 23, 4, 42, 16, 7, 35, 19, 11]
print(f"Ro'yxat: {sonlar}")
print(f"Elementlar soni: {len(sonlar)}")
print(f"Eng katta: {max(sonlar)}")
print(f"Eng kichik: {min(sonlar)}")
print(f"Yig'indisi: {sum(sonlar)}")
print(f"O'rtacha: {sum(sonlar) / len(sonlar):.2f}")
juft = [s for s in sonlar if s % 2 == 0]
toq = [s for s in sonlar if s % 2 != 0]
print(f"\nJuft sonlar: {juft}")
print(f"Toq sonlar: {toq}")
print(f"O'sish tartibida: {sorted(sonlar)}")
print(f"Kamayish tartibida: {sorted(sonlar, reverse=True)}")
