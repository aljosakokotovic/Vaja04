FROM ubuntu:latest
LABEL authors="kepi"

ENTRYPOINT ["top", "-b"]

# Osnovna Python slika
FROM python:3.12-slim

# Nastavim delovni direktorij v kontejnerju
WORKDIR /app

# Kopiram requirements in namestim odvisnosti
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiram preostalo kodo v kontejner
COPY . .

# Nastavimo okoljsko spremenljivko za port
ENV PORT=5556

# Odprem port 5556
EXPOSE 5556

# Ukaz za zagon Flask aplikacije
CMD ["python", "app.py"]
