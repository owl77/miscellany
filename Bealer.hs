module Main where
import Data.List
import Control.Monad
import System.Environment
import Text.ParserCombinators.Parsec hiding (spaces)

main :: IO()
main = do putStrLn("RPR logic")

{- We will write a parser for George Bealer's
Intensional Logic (PRP Logic). This is an extension of 
first-order logic which in its general form is capable 
of expressing intesionality and that-clauses as well as modality. -}

data Variable = Var String


data Term = Variable Variable
| Const String
| That [Variable] Form


data Form = Pred String [Term]
| Not Form 
| Exists Variable Form
| And Form Form

{- "Let's have a party !" <=> Want (I, [Have_Party(I) /\ Have_Party(You)] -}

wish :: Form
wish = Pred "Want" [Const "I", That [] ( And (Pred "Have_Party" [Const "I"]) (Pred "Have_Party" [Const "You" ]))]


showVar :: Variable -> String
showVar (Var a) = a


showTer :: Term -> String
showTer (Variable a) = showVar a
showTer (Const a) = a
showTer (That a b) = "that " ++ intercalate ", " (map showVar a) ++"[ " ++ showFor b ++ " ]" 


showFor :: Form -> String
showFor (Not a) = "not " ++"( "++ showFor a ++ ")"
showFor (And a b) = "( " ++ showFor a ++ " and " ++ showFor b ++ " )"
showFor (Exists x b) = "exists " ++ showVar x ++ " ( " ++ showFor b ++ " )"
showFor (Pred p a) = p ++ "( " ++ intercalate ", " (map showTer a) ++ " )"


instance Show Term where show = showTer
instance Show Form where show = showFor

{- Now the Parser which is given by the function "check". Add anything you want to these lists.
How to enter formulas: it is easiest to describe this by a formal grammar:
f := (f & f)| ~(f) | Ev(f) | p((t,)*t)
v := variables
p := predicates
t := constants | variables | T(F) | T(v,)*v(F)

You can leave as much space as you like. Example:

>check "Ex ( know ( x , T ( love ( I , x))))"
>"Parsed=> exists x ( know( x, that [ love( I, x ) ] ) )"

In English this formula could be interpreted as:

"There is somebody that knows that I love them".

Exercise: translate into PRP Socrates' dictum: I only know that I do no know anything.
Hint: you can use the equivalence a -> b <=> ~(a & ~b) and Forall x F <=> ~ Exist x ~ F 

TO DO: deal with arities

-}

predicates :: [String]
predicates = ["blue","want","know", "believe", "love", "equals"]
variables :: [String]
variables = ["x","y","z","w","v","u"]
constants :: [String]
constants = ["I", "you", "he", "she", "it", "we", "they", "Alice", "Bob"]


spaces :: Parser ()
spaces = skipMany1 space

parseVar :: Parser Term
parseVar = do x <- many letter
case elem x variables of
True -> return $ Variable (Var x)
otherwise -> fail "not a variable"

parseVar2 :: Parser Variable
parseVar2 = do x <- many letter
case elem x variables of
True -> return $ Var x
otherwise -> fail "not a variable"

parseCon :: Parser Term
parseCon = do x <- many letter
case elem x constants of
True -> return $ Variable (Var x)
otherwise -> fail "not a constant"


parseThat :: Parser Term
parseThat = do char 'T'
x <- sepBy parseVar2 (char ',')
char '('
y <- parseFor
char ')'
return (That x y)


parseTer :: Parser Term
parseTer = (try parseVar) <|> (try parseCon) <|> parseThat



parseFor :: Parser Form
parseFor = (try parsePred) <|> (try parseNot) <|> (try parseAnd) <|> parseExists

parsePred :: Parser Form
parsePred = do x <- many letter
char '('
y <- sepBy1 parseTer (char ',')
char ')'
case elem x predicates of
True -> return $ Pred x y
otherwise -> fail "not a predicate"

parseAnd :: Parser Form
parseAnd = do char '('
x <- parseFor
char '&'
y <- parseFor
char ')'
return $ And x y 

parseNot :: Parser Form
parseNot = do char '~' >> char '('
x <- parseFor
char ')'
return $ Not x

parseExists :: Parser Form
parseExists = do char 'E'
x <- parseVar2
char '('
y <- parseFor
char ')'
return (Exists x y) 

nice :: String -> String
nice a = filter (/=' ') a

check :: String -> String
check a = case parse parseFor "PRP-parser" (nice a) of
Right a -> "Parsed=> " ++ show a
Left a -> "Sorry, Syntax Error !"

