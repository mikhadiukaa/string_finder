def string_finder_func(sign: str, text: str) -> str:
    the_results = str("Строка встречается " + str(text.count(sign)) + " раз")
    return the_results


print(string_finder_func(sign="l", text="Drktvykollll"))
