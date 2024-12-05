calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.lower(), string.upper()

def is_contains(st, spisok):
    count_calls()
    if st or st.upper() or st.lower() in spisok:
        return True
    else:
        return False


print(string_info('Oleg'))
print(is_contains('Makarov', ['makarov', 1, 2, 3, 4, 5]))
print(calls)