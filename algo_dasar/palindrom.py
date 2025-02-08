def rearrange_word_optimized(source, target):
    if sorted(source) == sorted(target):
        return f"Berhasil menyusun '{source}' menjadi '{target}'"
    else:
        return f"Tidak mungkin membentuk '{target}' dari '{source}'"

# Contoh penggunaan
source_word = "bad credit"
target_word = "debit card"
result = rearrange_word_optimized(source_word, target_word)
print(result)
