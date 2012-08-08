def non_keyword(*args):
    print args

non_keyword(1,2,3)

non_keyword(1, **{args: 5})
