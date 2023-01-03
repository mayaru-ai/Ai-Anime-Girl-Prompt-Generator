import os
import random

# traits klasörünün yolunu belirtin
traits_path = "C:\\Users\\ts_sa\\OneDrive\\Masaüstü\\ai-anime-prompt-gen\\traits"

# traits klasörü içindeki dosyaların adlarını listeleyin
files = [f for f in os.listdir(traits_path)]

character_traits = {}

# her bir dosya için bir döngü oluşturun
for file in files:
    # dosya adının ".txt" uzantısını kaldırın
    trait = file[:-4]
    # dosyayı açın ve değerleri bir listeye ekleyin
    with open(os.path.join(traits_path, file), "r") as f:
        values = f.read().splitlines()
    # rastgele bir değer seçin ve karakter özelliklerine ekleyin
    character_traits[trait] = random.choice(values)

# çıktıyı istediğin sıralamada oluşturun
output = ""
for trait in [
    "1-character",
    "2-hairstyle",
    "3-haircolor",
    "4-hairlength",
    "5-eyecolor",
    "6-clothing",
    "7-accessories",
    "8-jewelry",
    "9-skintone",
    "10-scars",
    "11-tattoos",
    "12-emotion",
    "13-background",
    "14-theme",
]:
    value = character_traits[trait]
    output += ", " + value

# çıktıyı txt dosyasına yazdırın
with open("character_traits.txt", "w") as f:
    f.write(output)