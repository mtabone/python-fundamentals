# We applied the same logic many times in the previous challenge!
# Let's use functions to make our lives easier...

sally_age = 12
john_age = 21

def can_drink(age):
	if age > 20:
		return True # Again - make this depend on the age!
	else :
		return False

print "Sally can drink?", can_drink(sally_age)
print "John can drink?", can_drink(john_age)

# Now define a more complex function that takes whether someone is drinking and
# only checks ages if they are

def enforce(name, age, is_drinking):
	if is_drinking:
		print 'Checking', name + '!'
		# check 
		if age > 20:
			print 'OK!'
		else:
			print 'This isn\'t right!'

# Note that we can define our data before or after a function

alice_name = "Alice"
alice_age = 20
alice_is_drinking = True
bob_name = "Bob"
bob_age = 12
bob_is_drinking = False
charles_name = "Chuck"
charles_age = 22
charles_is_drinking = True

enforce(alice_name,   alice_age,   alice_is_drinking)
enforce(bob_name,     bob_age,     bob_is_drinking)
enforce(charles_name, charles_age, charles_is_drinking)

# And so on - do this for Bob and Charles!

# That should've been a LOT less typing!

# When you're done, have a look at the tests, and see how they correspond to the
# functions above
