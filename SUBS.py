def finding_motif(s, ss):
    result = []
    sslen = len(ss)
    slen = len(s)
    for i in range(0, slen - sslen + 1):
        if s[i:i+sslen] == ss:
            result.append(i+1)        
    return result
s="input string"
ss="input substring"
print (finding_motif(s,ss))