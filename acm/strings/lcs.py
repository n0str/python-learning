from sys import argv
import difflib

def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in xrange(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in xrange(1, 1 + len(s1)):
        for y in xrange(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]


def lcs_native(a, b):
    a, b = (a, b) if len(a) < len(b) else (b, a)

    pos = 0
    substr = ""
    search_str = a[:]

    while ( pos != len(a) ):
        while ( len(search_str) > len(substr) ):
            if search_str in b:
                substr = search_str[:]
                break
            else:
                search_str = search_str[:-1]
        pos += 1
        search_str = a[pos:]
    return substr

def lcs_suffix_tree(a, b):
    seq_matcher = difflib.SequenceMatcher(None, a, b)
    res = seq_matcher.find_longest_match(0, len(a), 0, len(b))
    return a[res.a:res.a+res.size]

def lcs_suffix_handmade(a, b):
    result_len = 0
    result_str = 0
    text = a + b
    sarray  = sorted(range(len(text)), key = lambda i: text[i:])
    for i in range(len(text)-1):
        if sarray[i] >= len(a) and sarray[i+1] >= len(b):
            continue
        elif sarray[i] < len(a) and sarray[i+1] < len(b):
            ##print sarray[i],
            continue
        else:
            max_len = 0
            while (max_len < len(text)-sarray[i] and max_len < len(text)-sarray[i+1]):
                if text[sarray[i]+max_len] == text[sarray[i+1] + max_len]:
                    max_len += 1
                else:
                    break
            if  max_len > result_len:
                result_len = max_len
                result_str = sarray[i]

    return text[result_str:result_str + result_len]


assert len(argv) > 2
a,b = argv[1:3]

print "lcs native test:\t%s" % lcs_native(a, b)
print "lcs dynamic test:\t%s" % longest_common_substring(a, b)
print "lcs suffix  test:\t%s" % lcs_suffix_tree(a, b)
print "lcs handmade  test:\t%s" % lcs_suffix_handmade(a, b)