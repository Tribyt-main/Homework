calls = 0
def count_calls():
    global calls
    calls += 1
count_calls()
def string_info(string):
    string = len(string), string.upper(), string.lower()
    return string
count_calls()
print(string_info('Alek'))
def is_counts(a,b):
    for i in b:
        if a.lower() == i.lower():
            return True
        else:
            return False
count_calls()
print(is_counts('A', ['a', 'b', 'c']))
print(calls)
