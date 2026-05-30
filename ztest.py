def analyze_spaces(text):
    # Check if double spaces exist
    has_double_space = "  " in text
    print(f"Contains double spaces? {has_double_space}")
    
    if has_double_space:
        # Find the index of the first occurrence
        first_index = text.find("  ")
        print(f"First double space starts at index: {first_index}")
        
        # Count total occurrences
        count = text.count("  ")
        print(f"Total double spaces found: {count}")

# Example usage
sample_text = "Data  engineering projects are  great."
analyze_spaces(sample_text)


def clean_all_spaces(text):
    # Splits by any whitespace and joins back with single spaces
    return " ".join(text.split())

# Example
sample_text = "Data   engineering   projects  are    great."
cleaned_text = clean_all_spaces(sample_text)

print(f"Original: '{sample_text}'")
print(f"Cleaned : '{cleaned_text}'")


def remove_double_spaces(text):
    # Loops to handle cases where 3 or more spaces sit together
    while "  " in text:
        text = text.replace("  ", " ")
    return text

# Example
sample_text = "Data  engineering  projects."
cleaned_text = remove_double_spaces(sample_text)

print(f"Original: '{sample_text}'")
print(f"Cleaned : '{cleaned_text}'")


myDict = {
    "uttam" : 8.81,
    "biki" : 9.5,
    "deepak" : 9.1,
    1 : 90.23,
    "age" : [12,13,14]
}
print(myDict["age"][0])

print(type(myDict[1]))
print(myDict.keys())

for key in myDict.keys():
    print(key, "→", type(key))