calls = 0
def count_calls():
    def func():
        global calls
        calls += 1
        return calls
    return func
counter = count_calls()
counter() + 1
def string_info():
    b = 'Copybara'
    print(tuple([len(b), b.upper(), b.lower()]))
string_info()
counter() + 1
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
counter() + 1
is_counts()
print(counter())
