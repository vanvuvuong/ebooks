string_code = '''
for index in range(10):
	pring(index)
'''
example = "x*y"
exec(string_code)
eval(example, {"x": 4}, {"y": 5})
