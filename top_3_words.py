def top_3_words(text):
    text_lst = text.lower().split()
    text_dict = {}
    for i in text_lst:
        a = {i: str(text_lst.count(i))}
        text_dict = text_dict | a
    z = []
    dict_values = list(text_dict.values())
    while len(z) < 3:
        highest = max(dict_values)
        z.append(highest)
        dict_values.pop(dict_values.index(highest))
    return z

