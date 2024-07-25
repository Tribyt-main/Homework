calls = 0
def count_calls():
        global calls
calls += 1
def string_info(b):
    tuple([len(b), b.upper(), b.lower()])
string_info('alek')
calls += 1
def is_counts():
    a = 'Alek'
    b = ['alek', 'Alak', 'Ylek']
    a.lower()
    for i in b:
        if i == a.lower():
            print(True)
            break
        else:
            print(False)
            break
calls += 1
is_counts()
print(calls)
