import os
import pyaes

def decrypt_file(file_name, key):
    try:
        # Abrir o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Descriptografar os dados
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # Remover o arquivo criptografado
        os.remove(file_name)

        # Criar o arquivo descriptografado
        new_file_name = "teste.txt"
        with open(new_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        print(f"Arquivo '{file_name}' descriptografado com sucesso como '{new_file_name}'.")

    except Exception as e:
        print(f"Ocorreu um erro durante a descriptografia: {e}")

if __name__ == "__main__":
    file_name = "teste.txt.ransomwaretroll"
    key = b"testeransomwares"
    decrypt_file(file_name, key)
