import sys

assert(len(sys.argv)>1)
filename=sys.argv[1]
file = open(filename, 'r')
lines = file.readlines()

operators=["+", "+=", "-", "-=", "*", "*=", "/", "/=", "<<", "<<=", ">>", ">>=", "&", "&=", "|", "|=", "^", "^=", "=", "==", "&&", "||", "<", "<=", ">", ">=", "%", "%="]
doubles=[]

for i in operators:
	if(len(i)==2):
		doubles.append(i)

with open(filename, "w") as f:
	f.truncate()
	for l in range(len(lines)):
		if(lines[l][0]!="#"):
			for i in range (5): # compress everything
				for s in operators:
					lines[l]=lines[l].replace(" " + s, s)
				for s in operators:
					lines[l]=lines[l].replace(s + " ", s)
				lines[l]=lines[l].replace(", ", ",")
				lines[l]=lines[l].replace(" ,", ",")
			lines[l]=lines[l].replace(",", ", ")
			lines[l]=lines[l].replace("<<=", "df7d11fce2f307006e53efc357f01d42")
			lines[l]=lines[l].replace(">>=", "a5f4eb4e39b2633b1ec269e53cde1368")
			for x in ["+", "-", "*", '/', '<', '>', '^', '&', '|', '%']:
				lines[l]=lines[l].replace(x + "=", "1fd8355cd2018e03d0050ca98947c223")
				lines[l]=lines[l].replace(x + x, "1fd8355cd2018e03d0050ca98947c224")
				lines[l]=lines[l].replace(x, " " + x + " ")
				lines[l]=lines[l].replace("1fd8355cd2018e03d0050ca98947c223", x + "=")
				lines[l]=lines[l].replace("1fd8355cd2018e03d0050ca98947c224", x + x)
			for x in ['=']:
				lines[l]=lines[l].replace("==", "1fd8355cd2018e03d0050ca98947c223")
				lines[l]=lines[l].replace("+=", "1fd8355cd2018e03d0050ca98947c224")
				lines[l]=lines[l].replace("-=", "1fd8355cd2018e03d0050ca98947c225")
				lines[l]=lines[l].replace("*=", "1fd8355cd2018e03d0050ca98947c226")
				lines[l]=lines[l].replace("/=", "1fd8355cd2018e03d0050ca98947c227")
				lines[l]=lines[l].replace("%=", "1fd8355cd2018e03d0050ca98947c228")
				lines[l]=lines[l].replace("|=", "1fd8355cd2018e03d0050ca98947c229")
				lines[l]=lines[l].replace("&=", "1fd8355cd2018e03d0050ca98947c220")
				lines[l]=lines[l].replace("^=", "1fd8355cd2018e03d0050ca98947c218")
				lines[l]=lines[l].replace("<=", "1fd8355cd2018e03d0050ca98947c208")
				lines[l]=lines[l].replace(">=", "1fd8355cd2018e03d0050ca98947c108")

				lines[l]=lines[l].replace("=", " = ")
				lines[l]=lines[l].replace("1fd8355cd2018e03d0050ca98947c223", "==")
				lines[l]=lines[l].replace("1fd8355cd2018e03d0050ca98947c224", "+=")
				lines[l]=lines[l].replace("1fd8355cd2018e03d0050ca98947c225", "-=")
				lines[l]=lines[l].replace("1fd8355cd2018e03d0050ca98947c226", "*=")
				lines[l]=lines[l].replace("1fd8355cd2018e03d0050ca98947c227", "/=")
				lines[l]=lines[l].replace("1fd8355cd2018e03d0050ca98947c228", "%=")
				lines[l]=lines[l].replace("1fd8355cd2018e03d0050ca98947c229", "|=")
				lines[l]=lines[l].replace("1fd8355cd2018e03d0050ca98947c220", "&=")
				lines[l]=lines[l].replace("1fd8355cd2018e03d0050ca98947c218", "^=")
				lines[l]=lines[l].replace("1fd8355cd2018e03d0050ca98947c208", "<=")
				lines[l]=lines[l].replace("1fd8355cd2018e03d0050ca98947c108", ">=")

			for x in doubles:
				lines[l]=lines[l].replace(x, " " + x + " ")
			lines[l]=lines[l].replace("df7d11fce2f307006e53efc357f01d42", " <<= ")
			lines[l]=lines[l].replace("a5f4eb4e39b2633b1ec269e53cde1368", " >>= ")
		f.write(lines[l])

