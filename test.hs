module Test where

data Sentence = Sentence String
data Noun = Noun String
data Verb = Verb (Noun -> Sentence)

data Adverb1 = Adverb1 ((Noun -> Sentence) -> (Noun -> Sentence))

showSen (Sentence a) = a

sing:: Noun -> Sentence
sing (Noun a)  = Sentence (a ++ " sing")

instance Show Sentence where show = showSen

quickly:: (Noun -> Sentence) -> (Noun -> Sentence)
quickly verb (Noun n) = Sentence ((showSen (verb (Noun n))) ++ " quickly")

type Verbum = Noun -> Sentence

atTime:: Noun -> Verbum -> Verbum
atTime (Noun n) v m  = Sentence ( (showSen (v m)) ++ " at " ++ n)

type Adjective = Noun -> Noun

big::Adjective
big (Noun s) = Noun ("big " ++ s)

x::Noun
x = Noun "x"

a:: Noun -> Sentence -> Sentence
a (Noun x) s = Sentence ("∃" ++ x ++ " "++ showSen s)