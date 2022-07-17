type Data = (Int, Int, Int)
type AtracoesByDate = (String, Data)

l1 :: AtracoesByDate
l2 :: AtracoesByDate
l3 :: AtracoesByDate
r1 :: AtracoesByDate
r2 :: AtracoesByDate
r3 :: AtracoesByDate

l1 = ("Annita - Armas e Rosas - CPM22", (10, 12, 2022))
l2 = ("Donzela De Ferro - EDEN - Fresno", (11, 12, 2022))
l3 = ("Kanye Oeste - Lady Gaga - Lea Corlet", (12, 12, 2022))
r1 = ("Luiza Sonza - MO - Skrillex", (05, 09, 2023))
r2 = ("The Killers - Ze Cowman - Santana", (06, 09, 2023))
r3 = ("Lana - Aurora - MO", (07, 09, 2023))

getData :: AtracoesByDate -> Data
getData (_, (d, m, a)) = (d, m, a)

getDia :: Data -> Int
getDia (d, _, _) = d

getMes :: Data -> Int
getMes (_, m, _) = m

getAno :: Data -> Int
getAno (_, _, a) = a

checkValidDate :: Data -> Bool
checkValidDate n | (getDia n > 31) = False
                 | (getDia n < 1) = False
                 | (getMes n > 12) = False
                 | (getMes n < 1) = False
                 | (getAno n < 1) = False
                 | otherwise = True

checkValidInterval :: Data -> Data -> Bool
checkValidInterval x y | ((checkValidDate x && checkValidDate y) == False) = False
                        | (getAno x > getAno y) = False
                        | otherwise = True


