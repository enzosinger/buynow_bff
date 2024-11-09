# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo de dependências (requirements.txt) para o contêiner
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código do BFF para o contêiner
COPY . .

# Expõe a porta que o Flask usará
EXPOSE 5001

# Define o comando para iniciar o servidor Flask
CMD ["python", "src/api/main.py"]
