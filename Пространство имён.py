calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.lower(), string.upper()

def is_contains(st, spisok):
    count_calls()
    lower_spisok = [word.lower() for word in spisok]
    upper_spisok = [word.upper() for word in spisok]
    if st.lower() in lower_spisok or st.upper() in upper_spisok:
        return True
    else:
        return False


print(string_info('Oleg'))
print(is_contains('Makarov', ['makarov', 'hi', 'hello', 'bye']))
print(calls)