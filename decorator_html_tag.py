def tag(name):
    def decor(func):
        def wrap(text):
            if name.isdigit():
                return "error"
            return "<{0}>{1}</{0}>".format(name.lower(), func(text))
        return wrap
    return decor


TEST_CASES = [
		({'name':'span'}, 'lorem ipsum', '<span>LOREM IPSUM</span>'),
		({'name':'div'}, 'lorem ipsum', '<div>LOREM IPSUM</div>'),
		({'name':'STRONG'}, 'lorem ipsum', '<strong>LOREM IPSUM</strong>'),
		({'name':'123'}, 'lorem ipsum', 'error'),
	]

for case in TEST_CASES:
	@tag(**case[0])
	def foo(text):
		return text.upper()

	assert foo(case[1]) == case[2]
