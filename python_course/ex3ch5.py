def rev_element(l):
    khali = []
    for i in l:
        khali.append(i[::-1])
    return khali



bhara = ['abcd', 'tuv', 'xyz']
print(rev_element(bhara))