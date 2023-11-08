# TI cv_1

## 1

Algoritmický problém je úloha, která má dobře definovaný vstup a požadovaný výstup. Rozhodovací problém je speciální typ algoritmického problému, kde odpovědí je "Ano" nebo "Ne" (často reprezentované hodnotami 1 nebo 0). Optimalizační problém je algoritmický problém, kde hledáme "nejlepší" řešení podle nějakého kritéria, například nejmenší náklady, nejkratší cestu, nejvyšší zisk atd.

Pojďme se podívat na prvních šest problémů uvedených v příkladu 1, definovat jaký je to druh problému, uvést příklady vstupů a výstupů, případně převést ne-rozhodovací problémy na rozhodovací formu a načrtnout algoritmy, které problémy řeší:

### a Prvočíselnost

* Druh problému: Rozhodovací
* Vstup: Číslo 15
* Výstup: Ne (není prvočíslo)
* Vstup: Číslo 13
* Výstup: Ano (je prvočíslo)
* Algoritmus: Test prvočíselnosti může být proveden například zkoušením dělitelnosti čísla všemi menšími čísly do jeho odmocniny; pro velká čísla se často používají pokročilé metody jako Millerův-Rabinův test prvočíselnosti.

### b Faktorizace přirozeného čísla na prvočísla

* Druh problému: Algoritmický (ne-rozhodovací optimalizační problém)
* Vstup: Číslo 18
* Výstup: Prvočíselní faktory [2, 3, 3]
* Přeformulování na rozhodovací problém: "Existuje prvočinitel čísla větší než k?"
* Algoritmus: Základní faktorizační algoritmus začíná zkoušením dělení číslem 2 a pokračuje k větším prvočíslům až dokud nenajde faktor; pro velká čísla se pak používají sofistikovanější metody jako Pollardova rho metoda nebo algoritmus eliptických křivek.

### c Násobení matic

* Druh problému: Algoritmický (ne-rozhodovací)
* Vstup: Dvě matice A (2x2) a B (2x2), kde A = [[1, 2], [3, 4]] a B = [[5, 6], [7, 8]]
* Výstup: Matice C (2x2), C = [[19, 22], [43, 50]]
* Přeformulování na rozhodovací problém: "Je prvek cij výsledné matice C větší než k?"
* Algoritmus: Standardní algoritmus násobení matic využívá výpočet součinu řádků první matice s odpovídajícími sloupci druhé matice; sofistikovanější algoritmy jako Strassenův algoritmus mohou výpočet zrychlit.

### d Nalezení minimální kostry grafu

* Druh problému: Optimalizační
* Vstup: Vážený graf G
* Výstup: Minimální kostra grafu
* Přeformulování na rozhodovací problém: "Existuje kostra grafu s celkovou váhou menší než k?"
* Algoritmus: Kruskalův algoritmus nebo Primův algoritmus; oba algoritmy pracují na principu postupného přidávání hran s nejmenší váhou tak, aby nevznikl cyklus.

### e Nejdelší společná podsekvence dvou řetězců

* Druh problému: Optimalizační
* Vstup: Dva řetězce "ABAZDC" a "BACBAD"
* Výstup: Jedna z nejdelších společných podsekvencí "ABAD"
* Přeformulování na rozhodovací problém: "Existuje společná podsekvence daných dvou řetězců délky větší nebo rovné k?"
* Algoritmus: Dynamické programování, kde se tabulkově řeší problém pro všechny podřetězce obou vstupních řetězců a výsledek se rekonstruuje z této tabulky.

### f Ekvivalence deterministických konečných automatů

* Druh problému: Rozhodovací
* Vstup: Dva deterministické konečné automaty (DFA) A a B
* Výstup: Ano, pokud akceptují stejný jazyk; Ne, pokud ne
* Algoritmus: Pro DFA můžeme použít algoritmus založený na minimizaci automatů a porovnání jejich minimálních ekvivalentních forem; jde o algoritmus testující, zda jsou odpovídající stavy v obou automatech vzájemně dosažitelné a akceptují stejný jazyk.
Toto jsou základní popisy a algoritmy řešení problémů až do f), jak jsou vysvětlené obecně v teoretické informatice. Při práci s konkrétními instancemi by bylo potřeba algoritmy přizpůsobit podle specifikací vstupů a podmínek, s nimiž by se ve cvičení mohlo pracovat. Pro ilustraci konkrétního algoritmu by bylo vhodné mít skutečnou implementaci nebo pseudokód, který by ukázal kroky potřebné k jeho provedení.

## 2

Při aplikaci algoritmu třídění přímým vkládáním (Insertion Sort) se berou v úvahu všechny kroky, které algoritmus vykoná, včetně porovnání, přiřazení a posuvu hodnot. Každá operace se počítá jako krok, proto výpočet úplného počtu instrukcí zahrnuje:
* Porovnání (A[i] > x)
* Přiřazení hodnot (x := A[j], A[i + 1] := A[i], A[i + 1] := x)
* Inkrementace a dekrementace proměnné (j := j + 1, i := i - 1)
Každá tato operace se počítá jako jeden krok při provádění algoritmu. Chceme-li spočítat celkový počet kroků pro danou sekvenci, musíme tedy zvážit všechny tyto operace a všechny opakování cyklů v algoritmu.

Uvažujte následující sekvenci [5, 2, 1, 4, 3] s n = 5 a počítejte instrukce provedené pro každou iteraci vnějšího cyklu:

Initial sequence: [5, 2, 1, 4, 3]

1. Iterace - ( j = 1 ), x se přiřadí hodnota 2 (1 krok), i se stanoví na 0 (1 krok) a začne vnitřní smyčka, která se opakuje 1x pro posunutí 5 (2 kroky pro porovnání a 1 krok pro přiřazeni), nakonec se 2 umístí na správné místo (1 krok).Celkem v iteraci: ((1+1) + (1+1+1+1) = 6) kroků.

Sequence: [2, 5, 1, 4, 3]

1. Iterace - ( j = 2 ), x se přiřadí hodnota 1 (1 krok), i se stanoví na 1 (1 krok), vnitřní smyčka se opakuje 2x pro posunutí 5 a 2 (4 kroky pro porovnání a 2 krok pro přiřazeni), nakonec se 1 umístí na správné místo (1 krok).Celkem v iteraci: ((1+1) + (2+2+1+1) = 8) kroků.

Sequence: [1, 2, 5, 4, 3]

1. Iterace - ( j = 3 ), 'x' se přiřadí hodnota 4 (1 krok), i se stanoví na 2 (1 krok), vnitřní smyčka se opakuje 1x pro porovnání s 5 (1 krok pro porovnání a 1 krok pro přiřazení), 4 se umístí na správné místo (1 krok).Celkem v iteraci: ((1+1) + (1+1+1) = 5) kroků.

Sequence: [1, 2, 4, 5, 3]

1. Iterace - ( j = 4 ), x se přiřadí hodnota 3 (1 krok), i se stanoví na 3 (1 krok), vnitřní smyčka se opakuje 2x pro porovnání a posunutí 5 a 4 (2 kroky pro porovnání a 2 krok pro přiřazení), 3 se umístí na správné místo (1 krok).Celkem v iteraci: ((1+1) + (2+2+1) = 7) kroků.

Sequence: [1, 2, 3, 4, 5]

Suma: 6 + 8 + 5 + 7 = 26 kroků celkově pro danou sekvenci.

Je důležité připomenout, že skutečný počet kroků závisí na konkrétním uspořádání vstupních dat a na počtu a uspořádání prvků vstupní posloupnosti.

## 3

### a

Po krocích by to vypadalo takto:

1. Program čte hodnotu do registru R0.
2. Nastaví R1 na 2.
3. Program pokračuje příkazem goto entry, čímž přeskočí do části "entry" a provede podmínku if (R0 > 0).
4. Jestliže je hodnota R0 větší něž 0, program pokračuje návěštím loop.
5. V sekci loop se hodnota R0 dekrementuje (sníží se o 1) a hodnota R1 se umocní na druhou.
6. Program se vrátí do části entry.
7. Pokud je R0 stále větší než 0, cyklus se opakuje.
8. Jakmile R0 dosáhne hodnoty 0, podmínka cyklu není pravdivá a program přejde k výstupním instrukcím.
9. Program vypíše hodnotu R1.
10. Program se ukončí pomocí instrukce halt.

V praxi toto znamená, že pokud je například R0 na začátku 3, pak:

* Program načte 3 do R0 a nastaví R1 na 2.
* V části entry bude podmínka pravdivá, protože R0 je větší než 0, takže program skočí do části loop.
* V loop se R0 dekrementuje na 2 a R1 umocní na 4.
* Program se vrátí do části entry, podmínka bude opět pravdivá, protože R0 je stále větší než 0.
* Program pokračuje částí loop, R0 se dekrementuje na 1 a R1 se umocní na 16.
* Opět se vrátí do sekce entry, podmínka bude stále pravdivá.
* Po poslední smyčce loop, R0 bude 0 a R1 umocněno na 256.
* V části entry tentokrát nebude podmínka pravdivá (protože R0 je 0), takže program pokračuje na write(R1) a vypíše 256.
* Program se ukončí příkazem halt.

Výsledek bude tedy (2^{(2^{(R0-1)})}), kde (R0) je počáteční hodnota načtená do registru R0. V tomto příkladě to bude (256) pro (R0) načtenou jako 3, protože první umocnění dvou na druhou se odehrává před prvním průchodem cyklem loop.

### b

1. Program začne nastavením R3 na součet hodnot v registrech R0 a R1 (tím definuje index konce rozsahu) a následně dekrementuje R3 o 1, aby označil poslední prvek v rozsahu.
2. Hodnota v paměti na adrese R3 je přečtena a uložena v registru R2. Tento krok nastavuje počáteční maximální hodnotu R2 na poslední prvek v rozsahu.
3. Program skočí do části označené jako entry.
4. V entry, R3 se dekrementuje o 1, což znamená, že se pohybujeme jedno místo doleva v paměti.
5. Pokud je R3 stále větší nebo rovno R0, což definuje začátek rozsahu, program skočí do části loop.
6. V loop se hodnota na adrese R3 přečte do R4.
7. Pokud je R4 menší nebo rovno R2, program se vrátí na entry; jinak se hodnota R4 nastaví jako nová maximální hodnota v R2.
8. Tento cyklus se opakuje, přičemž program se pohybuje od konce rozsahu směrem k začátku a aktualizuje maximální hodnotu.
9. Jakmile R3 je menší než R0 (ustanoveno v podmínce u entry), jsme na konci rozsahu a nebude proveden další skok do loop.
10. Program vypíše hodnotu R2, což je největší hodnota, kterou našel v daném rozsahu adres mezi R0 a R0 + R1.
11. Program se ukončí příkazem halt.
Výsledkem tohoto programu je najít největší číslo (maximum) v určitém rozsahu adres RAM a vypsat toto číslo. Rozsah paměti je určen R0 (začátek) a R0 + R1 (konec). Program pracuje "zprava doleva" od posledního prvku v rozsahu k prvnímu a srovnává každou hodnotu s dosud nalezeným maximem.

## 4

Pokud chceme zjistit hodnotu 2. bitu čísla x = 11 (kde k = 2), binárně 1011, musíme tuto hodnotu posunout tak, aby se 2. bit (tj. třetí bit od nejméně významného bitu) dostal na pozici nejméně významného bitu a pak odříznout zbytek.

V daném pseudokódu pro RAM můžeme simulovat bitové posuny a binární AND využitím dělení a násobení, jak bylo zmíněno. Podívejme se na kroky opravy:

1. Nejdříve posuneme číslo x doprava o k pozic. To uděláme tak, že číslo x vydělíme 2 k-krát.
2. Abychom získali hodnotu pouze jednoho bitu (našeho nejméně významného bitu), vynásobíme výsledek číslem 2 a odečteme ho od původního posunutého čísla. Pokud zůstal nějaký bit, pak po odčítání zůstane 1, v opačném případě to bude 0.
3. To nám dá hodnotu k-tého bitu jako 0 nebo 1.
Příklad kódu:

```
R1 := read()  ; Načte x
R2 := read()  ; Načte k
R3 := 0      ; Použije pro iteraci

; Posun x o k bitů doprava
loop1:
if (R2 = 0) goto continue
R1 := R1 / 2
R2 := R2 - 1
goto loop1

continue:
; Nyní R1 obsahuje x >> k
R4 := R1      ; Zkopíruje R1 (x posunuté o k) do R4
R1 := R1 * 2  ; Posuneme zpět vlevo (R1 << 1)
R1 := R4 - R1 ; Získáme zbytek, který bude 0 nebo 1

; Pokud je zbytek po dělení 1, znamená to, že poslední bit byl 1; jinak to byla 0.
write(R1) ; Vypíše hodnotu k-tého bitu
halt
```

Nyní provedeme tyto kroky pro x = 11 (1011 binárně) a k = 2:

* Posun x (11) o k (2) pomocí dělení na polovinu (11 / 2 = 5, 5 / 2 = 2, což je 10 binárně).
* Získáme posunuté x (2) a vynásobíme ho 2, což dá 4.
* Pak odečteme vynásobené x (4) od zkopírovaného originálu (2) - 2 - 4 = -2.
* Výsledek je záporný, což znamená, že původní 2. bit byl 0 a proto vypíšeme 0.
Takže správný výsledek programu pro x = 11 a k = 2 je 0, protože třetí bit od nejméně významného bitu pro 11 (binárně 1011) je ve skutečnosti 0.

## 5

Je možné násobit čísla x a y postupným sčítáním, kde x přičítáme k výsledku tolikrát, kolik udává hodnota y. Tento přístup je však z hlediska výpočetní složitosti neefektivní, protože pokud je y velké, bude trvat příliš dlouho dokončit výpočet - speciálně u RAM machine, která má omezenou rychlost.
V praxi, když chceme vytvořit efektivnější algoritmus pro násobení, můžeme použít metodu zvanou "double and add" (zdvojnásob a přičti), která je založena na binárním rozkladu druhého operandu (v tomto případě y) a postupném zdvojnásobování prvního operandu (v tomto případě x), přičemž se přičítá pouze když je odpovídající bit v y nastaven na 1.
Algoritmus pomocí pseudokódu vypadá následovně:

```
R1 := read()  ; Načte x
R2 := read()  ; Načte y
R0 := 0      ; Výsledek x * y bude uložen zde

loop:
if (R2 = 0) goto done  ; Pokud už není co přičítat, skončíme

if (R2 % 2 = 1) {
    R0 := R0 + R1  ; Pouze pokud je nízký bit R2 nastaven na 1, přičteme k výsledku
}

R1 := R1 + R1  ; Zdvojnásobení x
R2 := R2 / 2   ; Snížení y o polovinu (bitový posun doprava)

goto loop

done:
write(R0)  ; Vypíše výsledek
halt
```

V tomto pseudokódu:

* R2 % 2 = 1 kontroluje, zda je nejnižší bit y (R2) 1, což znamená, že x bude přičteno k akumulovanému součinu.
* R1 + R1 zdvojnásobuje hodnotu x k přípravě na následující bit y.
* R2 / 2 efektivně posouvá bity y doprava a snižuje hodnotu y o polovinu.

U každé operace násobení a dělení ve výše uvedeném pseudokódu musíme najít složitější, ale dovolenou náhradu vzhledem k omezením RAM stroje, protože nemůžeme přímo použít násobení ani modulo. Například, pokud chceme zjistit, zda je nejnižší bit čísla lichý (což je náhrada za R2 % 2), můžeme místo toho provést bitový posun a porovnání. Podobně, pro zdvojnásobení x musíme místo násobení použít opakované sčítání a pro poloviční snížení y provádíme opakované odečtení a skládání.

## 6

V příkladu 6 máme ukázat dvě věci ohledně logaritmů, kde a a b jsou větší než 1[1]:

1. ( a^{\log_b n} = n^{\log_b a} )Aplikujeme-li logaritmus o základu b na obě strany rovnice:( \log_b \left( a^{\log_b n} \right) = \log_b \left( n^{\log_b a} \right) )Použijeme-li pravidlo pro logaritmy ( \log_b (x^y) = y \cdot \log_b (x) ), dostaneme:( \log_b n \cdot \log_b a = \log_b a \cdot \log_b n )Vidíme, že obě strany jsou si rovny, což ukazuje, že původní rovnice platí.
2. Existuje konstanta c taková, že pro všechna x platí ( \log_a x = c \cdot \log_b x )V dalším kroku ukážeme, že mezi logaritmy s různými základy existuje vztah vynásobením konstantou c, kterou lze najít jako poměr jejich příslušných logaritmů:Chceme-li nalézt c, položme ( c = \frac{\log_a x}{\log_b x} ), kde x je hodnota, pro kterou c hledáme.Můžeme využít změnu základu logaritmu:( \log_a x = \frac{\log_b x}{\log_b a} )Po dosazení zpět do vztahu pro c dostáváme:( c = \frac{\log_a x}{\log_b x} = \frac{\log_b x}{\log_b a} \frac{1}{\log_b x} = \frac{1}{\log_b a} )Zde ( c ) je konstanta závislá pouze na výběru základů a a b a nezávislá na volbě x. Toto platí pro všechna x a tedy ( \log_a x ) a ( \log_b x ) jsou ve vztahu ( \Theta ) (asymptoticky těsné hranice), což znamená, že coby funkce růstu jsou obě logaritmy proporcionální.

Obě tyto úpravy a aplikace pravidel logaritmů přispívají k našemu důkazu a ukazují část příkladu 6.

Změna základu logaritmu je matematický vzorec, který umožňuje převést logaritmus s jedním základem na logaritmus s jiným základem. Tento vzorec je užitečný, protože logaritmy v různých základech nejsou přímo srovnatelné, ale tento vzorec umožňuje vyjádřit jeden logaritmus pomocí jiného základu, s nímž můžeme snáze pracovat nebo pro něhož máme vypočetní nástroje (například kalkulačky často podporují pouze přirozené logaritmy nebo logaritmy o základu 10).
Vzorec pro změnu základu logaritmu je následující:

$$ \log_b(a) = \frac{\log_c(a)}{\log_c(b)} $$

kde:

* $( \log_b(a) )$ je logaritmus čísla a o základu b,
* $( \log_c(a) )$ a $( \log_c(b) )$ jsou logaritmy hodnot a a b o základu c, který si vybereme.
Tento vzorec říká, že pokud máme logaritmus čísla a o základu b a chceme jej převést na jiný základ c, stačí vzít logaritmus čísla a o základu c a podělit ho logaritmem základu původního logaritmu b o základu c.
V praxi můžeme tento vzorec použít k přepočtu logaritmu neznámého základu na logaritmus se základem, který je nám více známý nebo s nímž máme k dispozici výpočetní nástroje. Například k převodu logaritmu o základu 2 na logaritmus o základu 10, který je běžně dostupný na kalkulačkách.
Zde je příklad, jak bychom mohli tento vzorec použít:
* Pokud chceme zjistit ( \log_2(8) ) a nemáme funkci pro logaritmus s základem 2, převedeme to na základ 10 takto:

$$ \log_2(8) = \frac{\log_{10}(8)}{\log_{10}(2)} $$

Vložíme-li hodnoty do kalkulačky, získáme:

$$ \log_2(8) = \frac{\log_{10}(8)}{\log_{10}(2)} \approx \frac{0.90309}{0.30103} \approx 3 $$

Výsledek ( \log_2(8) ) je přesně 3, protože 2 na třetí je 8. Pomocí změny základu jsme dokázali daný výpočet provést i bez přímého použití logaritmické funkce o základu 2.

## 7

V příkladu 7 je úkolem se seznámit s notacemi používanými k popisu rychlosti růstu funkcí: $( O )$, $( \Omega )$, $( \Theta )$, $( o )$, a $( \omega )$. Poté je požadováno seřadit dané funkce podle rychlosti jejich růstu a určit, které z uvedených vztahů pro dané funkce platí.

Nejprve si zrekapitulujeme definice notací:

* $( O(g(n)) )$ (Velké O) - Tato notace udává asymptotickou horní hranici. Funkce $( f(n) )$ je v $( O(g(n)) )$, pokud existují konstanty $( c > 0 )$ a $( n_0 )$ takové, že pro všechna $( n \geq n_0 )$ platí: $( f(n) \leq c \cdot g(n) )$.
* $( \Omega(g(n)) )$ (Velké Omega) - Tato notace udává asymptotickou dolní hranici. Funkce $( f(n) )$ je v $( \Omega(g(n)) )$, pokud existují konstanty $( c > 0 )$ a $( n_0 )$ takové, že pro všechna $( n \geq n_0 )$ platí: $( f(n) \geq c \cdot g(n) )$.
* $( \Theta(g(n)) )$ (Theta) - Tato notace udává asymptotickou těsnou hranici. Funkce $( f(n) )$ je v $( \Theta(g(n)) )$, pokud je zároveň v $( O(g(n)) )$ a $( \Omega(g(n)) )$. To znamená, že $( f(n) )$ roste stejně rychle jako $( g(n) )$ až na konstantní faktory.
* $( o(g(n)) )$ (Malé o) - Tato notace udává, že $( f(n) )$ roste asymptoticky rychleji než $( g(n) )$, avšak člen s $( f(n) )$ se stává zanedbatelným ve srovnání s $( g(n) )$, když $( n )$ jde do nekonečna.
* $( \omega(g(n)) )$ (Malé omega) - Tato notace je opakem $( o(g(n)) )$. Udává, že $( f(n) )$ roste asymptoticky rychleji než $( g(n) )$ a rozdíl v jejich růstu je více než jen o konstantní faktory.

Seřazení funkcí od nejpomalejšího růstu po nejrychlejší vypadá takto:

$$ \log_{10} n < \log_2 n < (\log_2 n)^2 < 2^{\sqrt{n}} < n^{3/2} < n < n \log_2 n < n^2 < n \cdot 3^n < 2^n < 22^n < 22^{n+1} < n^n < (n \log_2 n)^n $$

Pro dané funkce platí:

$( \log_{10} n \in O(n) )$ a $( \log_{10} n \in o(n) )$

$( n^{3/2} \in O(n^2) )$ a $( n^{3/2} \in \omega(n) )$

$( n^2 \in O(n^2 \log_2 n) )$ a $( n^2 \in o(n^2 \log_2 n) )$

$( 2^n \in O(22^n) )$ a $( 2^n \in o(22^n) )$

$( 22^n \in O(n^n) )$

$( (log_2 n)^2 \in O(2^n) )$

Specifickou funkci, která mění svůj výraz závisle na tom, zda je $( n )$ liché nebo sudé, určujeme podle toho, který z termů si ve většině případů vybere, ale ve skutečnosti se bude chovat jako $( O(n^2 + 2^n) )$.
