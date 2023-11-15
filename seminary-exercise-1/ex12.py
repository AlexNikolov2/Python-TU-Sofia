def palindrome(word):
    pal_list = list(reversed(word))
    palindrome_str = ''.join(pal_list)
    
    if(palindrome_str == word):
        print(1)
    else:
        print(0)

palindrome('ivan')
palindrome('madam')