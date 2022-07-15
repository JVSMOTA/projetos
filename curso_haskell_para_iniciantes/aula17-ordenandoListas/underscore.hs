addUnderscore :: String -> String
addUnderscore "" = ""
addUnderscore (x : xs)
    | x == ' ' = '_' : addUnderscore xs
    | otherwise = x : addUnderscore xs

popUnderscore :: String -> String
popUnderscore "" = ""
popUnderscore (x : xs)
    | x == '_' = ' ' : popUnderscore xs
    | otherwise = x : popUnderscore xs
