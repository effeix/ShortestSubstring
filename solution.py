def shortest_substring(string):
    n_chars = len(set(string))
    frequency = {}

    curr_len = len(string)
    il = 0 # left index
    ir = 0 # right index
    found = 0 # keep track of wanted characters found

    # while we have not reached the end of the string
    while ir < len(string):

        # get the character at the right index
        curr_char = string[ir]

        # keep track of its frequency
        if curr_char in frequency:
            frequency[curr_char] += 1
        else:
            frequency[curr_char] = 1
        
        # if frequency equals one, we have found the necessary amount of this char
        if frequency[curr_char] == 1:
            found += 1

        # if we have found at least one of each char, start going forward with the left index
        # until we hit a hit a non-valid string or have passed the right index
        while found == n_chars:
            if il > ir:
                break

            curr_char = string[il]

            # if len of valid substring given by il up to ir is lower than last len found
            # we substitute it
            if ir - il + 1 < curr_len:
                curr_len = ir - il + 1
            
            # the character on the left does not belong to our substring anymore
            frequency[curr_char] -= 1

            # if the frequency of the character is zero, we have hit a non-valid substring
            if frequency[curr_char] < 1:
                found -= 1

            il += 1

        ir += 1

    return curr_len

if __name__ == "__main__":
    string = input("Input string: ")
    ss = shortest_substring(string)
    print("Shortest Substring:", ss)