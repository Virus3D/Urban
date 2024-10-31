def all_variants(text):
    j=1
    while j<=len(text):
        i=0
        while i+j<=len(text):
            yield text[i:i+j]
            i+=1
        j+=1


a = all_variants("abcdef")

for s in a:
    print(s)
