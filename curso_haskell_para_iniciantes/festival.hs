type Ordenacao = String                 -- "Dia 1" ou "Dia 2"
type Atracoes = [String]                -- ["Annita", "Armas e Rosas", "CPM22"]
type Data = [Int]                       -- [10, 12, 2022]
type Dia = (Ordenacao, Atracoes, Data)  -- ("Dia 1", ["Annita", "Armas e Rosas", "CPM22"], [10, 12, 2022])
type Festival = (Dia, Dia, Dia)         -- [dia1, dia2, dia3]

dia1 :: Dia
dia1 = ("Dia 1", ["Annita", "Armas e Rosas", "CPM22"], [10, 12, 2022])
dia2 = ("Dia 2", ["Donzela De Ferro", "EDEN", "Fresno"], [11, 12, 2022])
dia3 = ("Dia 3", ["Kanye Oeste", "Lady Gaga", "Lea Corlet"], [12, 12, 2022])

lollaPalluisa :: Festival
lollaPalluisa = (dia1, dia2, dia3)

getDia1 :: Festival -> Dia              -- Retorna todos os Dias do Festival
getDia1 (dia1, _, _) = (dia1)
getDia2 (_, dia2, _) = (dia2)
getDia3 (_, _, dia3) = (dia3)

getOrdenacao :: Dia -> Ordenacao        -- Retorna a Ordenacao: "Dia 1"     
getOrdenacao (o, _, _) = o

getAtracoes :: Dia -> Atracoes          -- Retorna as Atrações: ["Annita", "Armas e Rosas", "CPM22"]
getAtracoes (_, a, _) = a

getData :: Dia -> Data                  -- Retorna o Dia: [10, 12, 2022]
getData (_, _, d) = d
