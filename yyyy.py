def char_frequency(s, ch):
    """Find frequency of character ch in string s."""
    return s.count(ch)

def replace_char(s, old_ch, new_ch):
    """Replace all occurrences of old_ch with new_ch in string s."""
    return s.replace(old_ch, new_ch)

def remove_first_occurrence(s, ch):
    """Remove the first occurrence of character ch from string s."""
    index = s.find(ch)
    if index != -1:
        return s[:index] + s[index+1:]
    return s

def remove_all_occurrences(s, ch):
    """Remove all occurrences of character ch from string s."""
    return s.replace(ch, '')

# Main program
if __name__ == "__main__":
    s = input("Enter a string: ")

    # a. Frequency of character
    ch = input("Enter a character to find its frequency: ")
    print(f"Frequency of '{ch}' in string: {char_frequency(s, ch)}")

    # b. Replace character
    old_ch = input("Enter the character to replace: ")
    new_ch = input("Enter the new character: ")
    replaced_string = replace_char(s, old_ch, new_ch)
    print(f"String after replacement: {replaced_string}")

    # c. Remove first occurrence
    ch = input("Enter a character to remove its first occurrence: ")
    first_removed = remove_first_occurrence(s, ch)
    print(f"String after removing first occurrence of '{ch}': {first_removed}")

    # d. Remove all occurrences
    ch = input("Enter a character to remove all its occurrences: ")
    all_removed = remove_all_occurrences(s, ch)
    print(f"String after removing all occurrences of '{ch}': {all_removed}")
