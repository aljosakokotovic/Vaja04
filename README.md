# VAJA4
docker

Meme Generator (Docker + Flask)

Ta projekt predstavlja preprosto spletno aplikacijo *Meme Generator*, izdelano v Pythonu z ogrodjem **Flask** in knjižnico **Pillow**.  
Uporabnik naloži sliko, vnese zgornje in spodnje besedilo, aplikacija pa ustvari končni meme.

---

Uporabljene tehnologije
- **Python**
- **Flask** (spletni strežnik)
- **Pillow** (obdelava slik)
- **HTML** (spletni obrazec)
- **Docker** (dockerizacija aplikacije)

---

Kako aplikacija deluje

1. Uporabnik preko HTML obrazca naloži sliko in vnese besedilo.
2. Flask prejme datoteko in podatke obrazca.
3. S knjižnico Pillow aplikacija odpre sliko in na njo doda izbrani tekst.
4. Končni meme se shrani v mapo *static/generated*.
5. Uporabniku se v brskalniku prikaže generirani meme.

---

Kako zaženete aplikacijo v dockerju

1.docker build -t meme-generator .
2.docker run -p 5556:5556 meme-generator




