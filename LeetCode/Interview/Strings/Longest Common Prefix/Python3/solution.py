class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()  # Sort the list of strings lexicographically
        print(strs)  # Print the sorted list (for debugging purposes)

        prefix = ""  # Initialize the common prefix string
        
        if len(strs) > 1:  # Check if there are more than one strings in the list
            for index in range(len(strs[0])):  # Iterate through each character of the first string
                print("index", index)  # Print the current index (for debugging purposes)
                print("letter", strs[0][index])  # Print the current character (for debugging purposes)
                count_flag = 0  # Initialize a flag to count matches

                for word in strs[1:]:  # Iterate through the remaining strings
                    word = word[:len(prefix) + 1]  # Update the word to match the current prefix length + 1
                    print("word", word)  # Print the current word (for debugging purposes)

                    if word.find(prefix + strs[0][index]) != -1:  # Check if the current character matches in each word
                        count_flag += 1  # Increment the match count

                    elif word.find(prefix + strs[0][index]) == -1:  # Check if the current character doesn't match in any word
                        break  # Break out of the loop since the common prefix is no longer valid

                if count_flag == len(strs[1:]):  # Check if the match count is equal to the number of remaining words
                    prefix = prefix + strs[0][index]  # Append the current character to the common prefix

                if len(prefix) == index:  # Check if the length of the prefix is equal to the current index
                    break  # Break out of the loop since the common prefix is at its maximum length

        elif len(strs) == 1:  # Check if there is only one string in the list
            prefix = strs[0]  # Set the prefix as the single string

        print("prefix", prefix)  # Print the final common prefix (for debugging purposes)
        return prefix  # Return the common prefix
