def no_dups(s):
    dict = {}
    split_s = s.split()
    no_dups_s = []

    for word in split_s:
        if word not in dict:
            dict[word] = 1
            no_dups_s.append(word)

    return " ".join(no_dups_s)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))