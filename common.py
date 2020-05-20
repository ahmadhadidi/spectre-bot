# This function removes the first word from a message
def message_splitter(message, verbose):

    # Add a verbose flag to the variable
    if verbose is True: print("[-] Removing first word from \"{0}\"".format(message))

    # Remove the first word in the message
    split_message = message.split(' ', 1)[1]

    # Print the result of the previous function
    if verbose is True: print("[+] Message is now: {0}".format(split_message))

    # Return the result
    return split_message


# Remove the first character from a message
# We need this to remove the '!' when we make Rasa calls.
def remove_first_character(message, verbose):

    # Bind the discord message as a string into a variable
    cleaned_message = str(message)

    # Add a verbose flag to the variable
    if verbose is True: print("[-] Removing first char from \"{0}\"".format(cleaned_message))

    # Remove the first character
    cleaned_message = cleaned_message[1:]

    # Print the result of the function
    if verbose is True: print("[+] Message is now: {0}".format(cleaned_message))

    # Return the result
    return cleaned_message
