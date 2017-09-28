# coding:utf-8
from nlppack import parse

def yomi(s):
    s = parse(s)
    ret = ""
    for w in s.words():
        ret += w.reading
    return ret

def get_dajare(s, lim=3, remove=["っ"]):

    reading = yomi(s)
    for r in remove:
        reading = reading.replace(r, "")
    words = dict() # [String, list(st)]
    dajares = [] # (st, ed, ln)

    longest = ""
    for i in range(lim, len(reading) + 1):
        idx = 0
        while i + idx <= len(reading):
            word = reading[idx:idx+i]
            idx += 1
            if word in words:
                for w in words[word]:
                    if w + len(word) > idx:
                        continue
                    dajares.append((words[word][0], idx, len(word)))
                    if len(word) > len(longest):
                        longest = word
            l = words.setdefault(word, [])
            l.append(idx)
    return dajares, longest

assert len(get_dajare("ほげほげほげ")[0]) == 0
assert len(get_dajare("わたしはわたし")[0]) == 1
print(get_dajare("わたしはわたし"))

if __name__ == '__main__':
    pass

