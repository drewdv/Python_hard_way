name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74.00 #inches
weight = 180.00 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_cm = height * 2.54
weight_kg = weight * 0.45
# 1.0 inches = 2.54 cm
# 1.0 lb = 0.45 kg


print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That means he's %d cm tall" % height_cm
print "He's %d pounds heavy." % weight
print "which means %d kgs." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)


# study questions

#The %s specifier converts the object using str(), and %r converts it using repr().
#For some objects such as integers, they yield the same result, but repr() is special in that
#(for types where this is possible) it conventionally returns a result that is valid Python syntax, which could be used to unambiguously recreate the object it represents

## Format Symbol	Conversion
# %c	            character
# %s	            string conversion via str() prior to formatting
# %i	            signed decimal integer
# %d	            signed decimal integer
# %u	            unsigned decimal integer
# %o	            octal integer
# %x	            hexadecimal integer (lowercase letters)
# %X	            hexadecimal integer (UPPERcase letters)
# %e	            exponential notation (with lowercase 'e')
# %E	            exponential notation (with UPPERcase 'E')
# %f	            floating point real number
# %g	            the shorter of %f and %e
# %G	            the shorter of %f and %E

# Other supported symbols and functionality are listed in the following table:

#Symbol	    Functionality
# *	       argument specifies width or precision
# -	       left justification
# +	       display the sign
# <sp>	   leave a blank space before a positive number
#	      add the octal leading zero ( '0' ) or hexadecimal leading '0x' or '0X', depending on whether 'x' or 'X' were used.
# 0	      pad from left with zeros (instead of spaces)
# %	      '%%' leaves you with a single literal '%'
# (var)	  mapping variable (dictionary arguments)
# m.n.	  m is the minimum total width and n is the number of digits to display after the decimal point (if appl.)
