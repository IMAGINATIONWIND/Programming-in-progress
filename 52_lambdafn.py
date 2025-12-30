a = lambda b: b**2
print(a(2))

# many variables can be input inside of lambda fn to make it short oneliner
# GENERALLY THE lambda FN IS USED FOR PASSING A FUNCTION AS AN ARGUMENT

# passing function to another function 
def ANOTHERfn( FUNCTION , VALUE ):
    return 6 + FUNCTION(VALUE)
print(ANOTHERfn(lambda VAR : VAR*VAR*VAR , 2))