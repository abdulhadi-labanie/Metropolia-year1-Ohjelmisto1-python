# Metropolia-year1-Ohjelmisto1-python

# Gitin peruskäyttö VS Codella

Tässä esimerkissä tehdään pieni projekti, jossa nähdään käytännössä:

- Git-repositorion alustaminen
- tiedostojen lisääminen Gitin seurantaan
- commit
- uuden branchin tekeminen
- branchissa työskentely
- branchin yhdistäminen `main`-haaraan
- `git status`, `git log` ja `git diff`

Esimerkki tehdään VS Coden terminaalissa.

---

## 1. Luo yksinkertainen projekti

Luo uusi kansio esimerkiksi:

```text
git-demo
```

Avaa kansio VS Codessa.

Luo tiedosto:

```text
main.py
```

Kirjoita siihen:

```python
print("Git-demo")
```

---

## 2. Alusta Git-repositorio

Avaa VS Coden terminaali ja kirjoita:

```bash
git init
```

Komento tekee nykyisestä kansiosta Git-repositorion.

Voit tarkistaa tilanteen:

```bash
git status
```

Git näyttää esimerkiksi, että `main.py` on uusi tiedosto, jota Git ei vielä seuraa.

---

## 3. Lisää tiedostot Gitin seurantaan

Voit lisätä tiedostoja yksitellen:

```bash
git add main.py
```

Jos projektissa olisi esimerkiksi kaksi tiedostoa:

```bash
git add main.py kissa.py
```

Tai voit lisätä kaikki nykyisen kansion muutokset kerralla:

```bash
git add .
```

Tarkista tilanne:

```bash
git status
```

Nyt tiedosto on valmis tallennettavaksi Git-historiaan.

---

## 4. Tee ensimmäinen commit

```bash
git commit -m "Projektin aloitus"
```

Commit on tallennuspiste projektin historiassa.

Historia näyttää tässä vaiheessa yksinkertaistettuna tältä:

```text
main

● Projektin aloitus
```

Commitit voi nähdä komennolla:

```bash
git log
```

---

# 5. Tee pieni muutos

Muuta `main.py`:

```python
print("Git-demo")

print("Tervetuloa ohjelmaan!")
```

Nyt Git huomaa, että tiedostoa on muutettu.

Tarkista:

```bash
git status
```

Voit nähdä tarkemmin, mitä tiedostossa muuttui:

```bash
git diff
```

Git näyttää esimerkiksi lisätyn rivin.

Lisää muutos:

```bash
git add .
```

ja tee commit:

```bash
git commit -m "Lisätty tervetuloteksti"
```

Historia:

```text
main

● Lisätty tervetuloteksti
|
● Projektin aloitus
```

---

# 6. Luo uusi branch

Seuraavaksi haluamme tehdä uuden ominaisuuden.

Luodaan branch:

```bash
git branch uusi-ominaisuus
```

Tämä luo branchin, mutta ei vielä vaihda siihen.

Vaihdetaan branchiin:

```bash
git checkout uusi-ominaisuus
```

Saman voi tehdä yhdellä komennolla:

```bash
git checkout -b uusi-ominaisuus
```

Tämä:

1. luo uuden branchin
2. vaihtaa siihen

Voit tarkistaa aktiivisen branchin esimerkiksi:

```bash
git branch
```

Tuloksena voisi olla:

```text
  main
* uusi-ominaisuus
```

Tähti `*` kertoo aktiivisen branchin.

---

# 7. Tee muutos uudessa branchissa

Muuta `main.py` esimerkiksi näin:

```python
print("Git-demo")

print("Tervetuloa ohjelmaan!")

name = input("Anna nimesi: ")

print("Hei", name)
```

Tarkista:

```bash
git status
```

Katso muutokset:

```bash
git diff
```

Lisää muutokset:

```bash
git add .
```

Tee commit:

```bash
git commit -m "Lisätty käyttäjän tervehdys"
```

Nyt uusi ominaisuus kuuluu `uusi-ominaisuus`-branchiin.

---

# 8. Vaihda takaisin main-branchiin

```bash
git checkout main
```

Katso nyt `main.py`-tiedostoa.

Uudessa branchissa tehty käyttäjän tervehdys ei ole vielä mukana `main`-branchissa.

Tämä havainnollistaa branchien ideaa:

```text
main
|
● Lisätty tervetuloteksti
|
● Projektin aloitus
 \
  ● Lisätty käyttäjän tervehdys
    uusi-ominaisuus
```

Branchissa voidaan siis kehittää ominaisuutta erillään pääkehityshaarasta.

---

# 9. Yhdistä branch mainiin (tai 10.)

Varmista ensin, että olet `main`-branchissa:

```bash
git status
```

tai:

```bash
git branch
```

Aktiivisena pitäisi olla:

```text
* main
  uusi-ominaisuus
```

Git merge liittää valitun haaran siihen haaraan, joka on sillä hetkellä aktiivisena.

Koska olemme `main`-haarassa, voimme kirjoittaa:

```bash
git merge uusi-ominaisuus
```

Nyt `uusi-ominaisuus` yhdistetään `main`-haaraan.

---

# 10. Merge käyttäen `--no-ff`

Tämä on puhtaasti demo visuuaalisuutta varten eikä projekteissa aina tarpeen. Näin branchin yhdistäminen näkyy historiassa selkeästi, mikä helpottaa hahmottamaan, missä kohtaa ominaisuus liitettiin takaisin päähaaraan:

```bash
git merge --no-ff uusi-ominaisuus -m "Merge uusi-ominaisuus"
```

`--no-ff` tekee mergestä oman merge-commitin.

Tämä tekee branchin yhdistämisen näkyvämmäksi Git-historiassa.

Historia voi näyttää esimerkiksi tältä:

```text
      ● Lisätty käyttäjän tervehdys
     / \
●---●---● Merge branch 'uusi-ominaisuus'
        main
```

Käytännössä historiaa voi tarkastella esimerkiksi:

```bash
git log
```

Tai havainnollisemmin:

```bash
git log --oneline --graph --all
```

Esimerkiksi:

```text
*   15ac822 Merge branch 'uusi-ominaisuus'
|\
| * 65c5012 Lisätty käyttäjän tervehdys
|/
* 98a2741 Lisätty tervetuloteksti
* 227bb21 Projektin aloitus
```

Tästä näkee hyvin:

- missä branch syntyi
- mitä siellä tehtiin
- missä se yhdistettiin takaisin

---

# Koko työnkulku lyhyesti

Projektin alustus:

```bash
git init
```

Tiedostojen lisääminen:

```bash
git add .
```

Commit:

```bash
git commit -m "Projektin aloitus"
```

Uusi branch:

```bash
git checkout -b uusi-ominaisuus
```

Tee muutoksia ja tarkista:

```bash
git status
git diff
```

Tallenna muutokset:

```bash
git add .
git commit -m "Lisätty uusi ominaisuus"
```

Palaa päähaaraan:

```bash
git checkout main
```

Yhdistä branch:

```bash
git merge uusi-ominaisuus
```

Tarkastele historiaa:

```bash
git log
```

---

# Tärkeimmät Git-komennot

## `git init`

```bash
git init
```

Alustaa nykyiseen kansioon Git-repositorion.

---

## `git status`

```bash
git status
```

Näyttää Git-repositorion nykyisen tilanteen.

Esimerkiksi:

- mitä tiedostoja on muutettu
- mitä tiedostoja ei vielä seurata
- mitä tiedostoja on lisätty seuraavaa committia varten
- missä branchissa olet

Tätä komentoa kannattaa käyttää usein.

---

## `git add`

Yksi tiedosto:

```bash
git add main.py
```

Useita tiedostoja:

```bash
git add main.py kissa.py
```

Kaikki muutokset:

```bash
git add .
```

`git add` valitsee muutokset seuraavaa committia varten.

---

## `git commit`

```bash
git commit -m "commit-viesti"
```

Tallentaa `git add` -komennolla valitut muutokset Git-historiaan.

---

## `git branch`

Luo uuden branchin:

```bash
git branch uusi-ominaisuus
```

Branch on erillinen kehityshaara.

---

## `git checkout`

Vaihda branchiin:

```bash
git checkout uusi-ominaisuus
```

Takaisin pääkehityshaaraan:

```bash
git checkout main
```

---

## Uusi branch ja siihen vaihtaminen samalla komennolla

```bash
git checkout -b uusi-ominaisuus
```

Tämä vastaa käytännössä komentoja:

```bash
git branch uusi-ominaisuus
git checkout uusi-ominaisuus
```

---

## `git merge`

```bash
git merge uusi-ominaisuus
```

Git liittää `uusi-ominaisuus`-branchin siihen branchiin, joka on sillä hetkellä aktiivinen.

Jos olet:

```text
* main
  uusi-ominaisuus
```

ja suoritat:

```bash
git merge uusi-ominaisuus
```

niin `uusi-ominaisuus` yhdistetään `main`-haaraan.

---

## `git merge --no-ff`

```bash
git merge --no-ff uusi-ominaisuus
```

Yhdistää branchin, mutta tekee samalla erillisen merge-commitin.

Branchin syntyminen ja yhdistäminen näkyvät Git-historiassa selvästi.

---

## `git log`

```bash
git log
```

Näyttää commit-historian.

Graafin kanssa:

```bash
git log --oneline --graph --all
```

---

## `git diff`

```bash
git diff
```

Näyttää tiedostoihin tehdyt muutokset, joita ei vielä ole lisätty seuraavaan committiin.

Esimerkiksi:

```diff
 print("Git-demo")
+print("Tervetuloa ohjelmaan!")
```

---

## `git reset`

`git reset`-komentoa käytetään muutosten tai commit-tilanteen peruuttamiseen.

Yksinkertainen käyttötapa on poistaa tiedosto staging-alueelta.

Jos teit:

```bash
git add main.py
```

mutta et haluakaan sitä vielä seuraavaan committiin:

```bash
git reset main.py
```

Tiedostoon tehdyt muutokset eivät katoa.

Git vain poistaa tiedoston seuraavaa committia varten valituista tiedostoista.

---

# Gitin perusidea

Yksinkertaistettuna Git-työskentely näyttää tältä:

```text
Muokkaa tiedostoa

       ↓

git status

       ↓

git diff

       ↓

git add .

       ↓

git commit

       ↓

jatka työskentelyä
```

Branchia käytettäessä:

```text
main
 |
 ● commit
 |
 ● commit
 |
 ├──────────── uusi-ominaisuus
 |                  |
 |                  ● commit
 |                  |
 |                  ● commit
 |                  |
 └──────────────────┘
        merge
```
