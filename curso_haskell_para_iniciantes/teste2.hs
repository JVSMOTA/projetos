type Nome = String
type Idade = Int
type Linguagem = String
type Pessoa = (Nome, Idade, Linguagem)

pessoa :: Pessoa
pessoa = ("Joao", 21, "Python3")

my_fst :: Pessoa -> Nome
my_fst (n, _, _) = n
my_scd (_, i, _) = i
my_ter (_, _, l) = l
