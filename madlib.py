story = "{0} was {1} by a bus"
name = raw_input ("enter a name")
verb = raw_input ("enter a verb")
adjusted = story.format(name, verb)
print (adjusted)


story = '''{0} went {11} the {1} and {12} the {2} to {3} house, but instead of finding {3} he/she found...  {0} said, wow {3} what {5} {6} you have!...
Oh my goodness {3}, what {7} {8} you have!!... Holy guacamole {3} what {9} {10} you have!!!...  {0} said, wait you aren't {3}, your {4}.  Wait, you are the
person that can {13} {14}, {15} {16}, {17} {18}, and {19} {20}!  {4} says, no but I am ... {21}''' 
name = raw_input ("enter a name")
noun = raw_input ("enter a noun")
noun1 = raw_input ("enter a noun")
name1 = raw_input ("enter a name")
name2 = raw_input ("enter a name")
adjective = raw_input ("enter an adjective")
noun2 = raw_input ("enter a body part")
adjective1 = raw_input ("enter an adjective")
noun3 = raw_input ("enter a body part")
adjective2 = raw_input ("enter an adjective")
noun4 = raw_input ("enter a body part")
preposition = raw_input ("enter a preposition")
preposition1 = raw_input ("enter a preposition")
verb = raw_input ("enter a verb")
adjective3 = raw_input ("enter an adjective")
verb1 = raw_input ("enter a verb")
adjective4 = raw_input ("enter an adjective")
verb2 = raw_input ("enter a verb")
adjective5 = raw_input ("enter an adjective")
verb3 = raw_input ("enter a verb")
adjective6 = raw_input ("enter an adjecttive")
noun5 = raw_input ("enter a superhero")
adjusted = story.format(name, noun, noun1, name1, name2, adjective, noun2, adjective1, noun3, adjective2, noun4, preposition, preposition1, verb, adjective3, verb1, adjective4, verb2, adjective5, verb3, adjective6, noun5)
print (adjusted)
