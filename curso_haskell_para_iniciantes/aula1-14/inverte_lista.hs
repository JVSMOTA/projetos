{-inv_aux :: [t] -> [t] -> [t]
inv_aux [] l_inv = l_inv
inv_aux (x:xs) l_inv = inv_aux xs l_inv++[x]

inv_list :: [t] -> [t]
inv_list [] = []
inv_list l = inv_aux l []-}

inv_list :: [t] -> [t]
inv_list [] = []
inv_list (x:xs) = inv_list xs ++ [x]

