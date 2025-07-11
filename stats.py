def get_word_count(text: str):
    word_list = text.split()
    return len(word_list)

def get_letter_counts(text: str):
    letter_count_dict = {}
    for letter in text:
        if letter.lower() in letter_count_dict:
            letter_count_dict[letter.lower()] += 1
        else:
            letter_count_dict[letter.lower()] = 1
    return letter_count_dict

def sort_on(items):
    return items["num"]

def sort_letter_count_dict(letter_count_dict: dict):
    sort_list = []
    for letter in letter_count_dict:
        sort_list.append({"char":letter, "num":letter_count_dict[letter]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list
    
    