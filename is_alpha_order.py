# >>> is_alpha_order('bot')
# True
# >>> is_alpha_order('arT')
# True
# >>> is_alpha_order('are')
# False
# >>> is_alpha_order('toe')
# True
# >>> is_alpha_order('Flee')
# False
# >>> is_alpha_order('reed')
# True
# Implement the is_alpha_order function.

def is_alpha_order(text: str) -> bool:
    # return text.lower() == "".join(sorted(text.lower())) or \
    #        text.lower() == "".join(sorted(text.lower(), reverse = True))

    sorted_text = sorted(text.lower())

    for i in range(len(text)):
        if list(text.lower())[i] not in (sorted_text[i], sorted_text[-(i + 1)]):
            return False

    return True


if __name__ == "__main__":
    assert is_alpha_order('bot') == True
    assert is_alpha_order('arT') == True
    assert is_alpha_order('are') == False
    assert is_alpha_order('toe') == True
    assert is_alpha_order('Flee') == False
    assert is_alpha_order('reed') == True
