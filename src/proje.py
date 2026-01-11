def rle_encode(data):

    #Bu fonksiyon verilen metni Run-Length Encoding (RLE) algoritması ile sıkıştırır.
    #Örnek: AAAAAB → 5A1B

    encoded ="" # Sıkıştırılmış veriyi tutacak değişken
    count = 1         # Aynı karakterin kaç kez tekrar ettiğini sayar.(Tekrar sayacı)

    # Metnin 2. karakterinden başlayarak döngüye girilir
    for i in range(1, len(data)):

        # Eğer mevcut karakter bir öncekiyle aynıysa
        if data[i] == data[i - 1]:
            count += 1   # Tekrar sayısı artırılır

        # Eğer karakter değiştiyse
        else:
            # Önceki karakter ve tekrar sayısı encoded stringe eklenir
            encoded += str(count) + data[i - 1]
            count = 1    # Sayaç sıfırlanır (yeni karakter için)

    # Döngü bittikten sonra son karakter grubu eklenir
    encoded += str(count) + data[-1]

    return encoded


def rle_decode(data):

    #Bu fonksiyon RLE ile sıkıştırılmış veriyi eski (orijinal) haline getirir.
    #Örnek: 5A1B → AAAAAB

    decoded = ""   # Açılmış (orijinal) metni tutar
    count = ""     # Sayıları biriktirmek için string (10, 12 gibi sayılar olabilir)

    # Encoded string karakter karakter okunur
    for char in data:

        # Eğer karakter sayıysa
        if char.isdigit():
            count += char   # Sayı biriktirilir

        # Eğer karakter harfse
        else:
            # Harf, count kadar tekrar edilerek decoded stringe eklenir
            decoded += char * int(count)
            count = ""      # Sayaç temizlenir

    return decoded


def compression_ratio(original, encoded):
    #Sıkıştırma oranını yüzde (%) olarak hesaplar.


    return (1 - len(encoded) / len(original)) * 100


# ------------------- TEST KISMI -------------------

text = "AAAAABBBCCDAA"   # Orijinal metin

encoded_text = rle_encode(text)     # Sıkıştırma işlemi
decoded_text = rle_decode(encoded_text)  # Açma işlemi
ratio = compression_ratio(text, encoded_text)  # Oran hesaplama

# Sonuçların ekrana yazdırılması
print("Orijinal:", text)
print("Encoded :", encoded_text)
print("Decoded :", decoded_text)
print("Sıkıştırma Oranı: %.2f%%" % ratio)
