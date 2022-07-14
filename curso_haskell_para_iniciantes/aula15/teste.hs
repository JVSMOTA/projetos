par :: Int -> Bool
par x = mod x 2 == 0

lista :: [Int]
lista = [x | x <- [1 .. 10], par x]
