# Criptografia e Descriptografia de Arquivos

Este projeto contém dois scripts em Python para criptografar e descriptografar arquivos usando o algoritmo AES (Advanced Encryption Standard) em modo CTR (Counter). Os scripts são `encrypter.py` e `decrypter.py`.

## Funcionalidades

- **encrypter.py**: Criptografa um arquivo de texto e o salva com a extensão `.ransomwaretroll`.
- **decrypter.py**: Descriptografa um arquivo criptografado e o salva como um arquivo de texto normal.

## Dependências

Este projeto utiliza a biblioteca `pyaes`. Para instalá-la, você pode usar o seguinte comando:

```bash
pip install pyaes
```

## Como Usar

### Criptografar um Arquivo

1. Coloque o arquivo que deseja criptografar na mesma pasta que o script `encrypter.py`.
2. Execute o script:

   ```bash
   python encrypter.py
   ```

3. O arquivo original será removido e um novo arquivo criptografado será criado com a extensão `.ransomwaretroll`.

### Descriptografar um Arquivo

1. Coloque o arquivo criptografado na mesma pasta que o script `decrypter.py`.
2. Execute o script:

   ```bash
   python decrypter.py
   ```

3. O arquivo criptografado será removido e um novo arquivo descriptografado será criado como `teste.txt`.

## Segurança

A chave de criptografia utilizada neste projeto é `testeransomwares`. Para maior segurança, recomenda-se usar uma chave mais complexa e mantê-la em segredo.

## Créditos

Este projeto foi desenvolvido como parte do Santander Boot Camp. Agradecimentos especiais ao professor [Cassiano Ricardo de Oliveira Peres](https://github.com/cassiano-dio) por seu suporte e orientação.
