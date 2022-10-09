import sys
from typing import List


def read_file():
    """Returns the text or error if the file can't be opened.

    Preconditions:
    - file with .txt extension.
    - file passed in as a system argument.
    Postconditions: The output is the text of file as string.
    """
    try:
        with open(sys.argv[1],"r") as file:
            contents = file.readlines()
            data = [record.replace("\n","") for record in contents]
        return data
    except FileNotFoundError:
        sys.exit("File cannot be opened")
    except IndexError:
        sys.exit("No file specified")
    

def get_unique_values(keylog_data:List[str]) -> List:
    """Returns the list of the unique values from the file.
    
    Preconditions: keylog_data = text file.
    Postconditions: The output is the unique values.
    """
    unique_values = set()
    for lists in keylog_data:
        for char in lists:
            unique_values.add(char)    
    return list(unique_values)


def search_for_passcode(keylog_data:List[str], keylog_unique_values:List[str]) -> List:
    """Returns the most possible passcode based on the keylog file. It doesn't work for duplicate values.

    Preconditions: 
     - keylog_data = file values converted to list
     - keylog_unique_values = file unique values.
    Postcondition: The output is the possible passcode of the length of keylog_unique_values.
    """
    for lists in keylog_data:
        first_index = unique_values.index(lists[0])
        second_index = unique_values.index(lists[1])
        third_index = unique_values.index(lists[2])       
        if first_index > second_index:
            unique_values[first_index], unique_values[second_index] = unique_values[second_index], unique_values[first_index]    
        elif second_index > third_index:
            unique_values[second_index], unique_values[third_index] = unique_values[third_index], unique_values[second_index]      
    return unique_values


def list_to_string(unique_values_sorted:List[str]) -> str:
    """Returns string
    
    Preconditions: unique_values_sorted = list.
    Postconditions: The output is a string.
    """
    string = ""
    for digit in passcode:
        string += digit
    print(f"The possible passcode is: {string}")


if __name__ == '__main__':
    data = read_file()
    unique_values = get_unique_values(data)
    passcode = search_for_passcode(data,unique_values)
    list_to_string(passcode)
