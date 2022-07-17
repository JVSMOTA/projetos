type Ordenacao = String                 -- "Dia 1" ou "Dia 2"
type Atracoes = [String]                -- ["Annita", "Armas e Rosas", "CPM22"]
type Data = [Int]                       -- [10, 12, 2022]
type Dia = (Ordenacao, Atracoes, Data)  -- ("Dia 1", ["Annita", "Armas e Rosas", "CPM22"], [10, 12, 2022])
type Festival = (Dia, Dia, Dia)         -- [dia1, dia2, dia3]

l1 :: Dia
l1 = ("Dia 1", ["Annita", "Armas e Rosas", "CPM22"], [10, 12, 2022])
l2 = ("Dia 2", ["Donzela De Ferro", "EDEN", "Fresno"], [11, 12, 2022])
l3 = ("Dia 3", ["Kanye Oeste", "Lady Gaga", "Lea Corlet"], [12, 12, 2022])

lollaPalluisa :: Festival
lollaPalluisa = (l1, l2, l3)

r4 :: Dia
r4 = ("Dia 1", ["Luiza Sonza", "MO", "Skrillex"], [05, 09, 2023])
r5 = ("Dia 2", ["The Killers", "Ze Cowman", "Santana"], [06, 09, 2023])
r6 = ("Dia 3", ["Lana", "Aurora", "MO"], [07, 09, 2023])

r :: Festival
r = (r4, r5, r6)

getDia1 :: Festival -> Dia              -- Retorna todos os Dias do Festival
getDia1 (dia1, _, _) = (dia1)
getDia2 (_, dia2, _) = (dia2)
getDia3 (_, _, dia3) = (dia3)

getOrdenacao :: Dia -> Ordenacao        -- Retorna a Ordenacao: "Dia 1"     
getOrdenacao (o, _, _) = o

getAtracoes :: Dia -> Atracoes          -- Retorna as Atra�?es: ["Annita", "Armas e Rosas", "CPM22"]
getAtracoes (_, a, _) = a

getData :: Dia -> Data                  -- Retorna o Dia: [10, 12, 2022]
getData (_, _, d) = d
