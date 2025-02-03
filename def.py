def arguments(*args):
    print('The arguments are: ' + args[0])

def kw_arguments(**kwargs):
    print('The arguments are: ' + kwargs['one'])



arguments('1','2')
kw_arguments(one='one', two='two')
