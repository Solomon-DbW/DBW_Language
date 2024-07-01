import basic_dbw

while True:
    text = input("dbw> ")
    print(text)
    result, error = basic_dbw.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)