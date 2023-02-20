f = open("wiki.txt")
wiki = f.read().rstrip()
wiki_w = wiki.split()
f.close()
f = open("ref.txt")
ref = f.read().rstrip()
ref_w = ref.split()
f.close()
cnt = 0
k = 0
for i in range(1, len(wiki_w)-1):
    for j in range(1, len(ref_w)-1):
        t = True
        for k in range(3):
            if wiki_w[i-1+k] != ref_w[j-1+k]:
                t = False
        if t:
            cnt += 1
print(cnt)
ref_len = 0
for el in ref_w:
    ref_len += len(el)
print(ref_len)
print(100 * cnt / ref_len)
