import string

def pangrams(s):
    if len(set([x.upper() for x in s if x!=' '])) == 26:
        return "pangram"
    else:
        return "not pangram"

pangrams("We promptly judged antique buckles ivory for the next prize")
