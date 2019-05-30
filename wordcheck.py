import enchant
d = enchant.Dict("en_US")
print(d.check("hello"))
d.check("helo")
print(d.suggest("helo"))