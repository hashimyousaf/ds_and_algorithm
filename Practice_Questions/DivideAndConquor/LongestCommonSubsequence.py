#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.
"""
Find the length of Longest Repeated Susequence. The longest repeated Subsequence(LRS) is the
longest subsequence of a string that occues at least twice.
"""

###-----------------------------------------------------------------------
###---------------------------LONGEST REPEATED SUBSEQUENCE------------------
###-----------------------------------------------------------------------
str12 = "asbs"
str22 = "ZCD"
dp = [[-1 for i in range(len(str12)+1)] for j in range(len(str22)+1)]
print(dp)


from collections import Counter

# TIME COMPLEXITY = N^2/2  = N(N/2) = N FOR OUTER LOOP AND N/2 FOR INNER LOOP
def LRSLength(X):
    # TODO
    # Find the longes repeated subsequence of the string
    #  aefabhf
    char_count = Counter(X)
    base_index = 0
    resultant = []
    while base_index < len(X)-1:
        for runner in range(base_index + 1, len(X)):
            if X[base_index] == X[runner] and char_count[X[base_index]] >= 2:
                char_count[X[base_index]] -= 2
                resultant.append(X[base_index])
                break
        base_index += 1
    return "".join(resultant)

def LRSLength2(X, m, n):
   # return if we have reached the end of either string
   if m == 0 or n == 0:
       return 0

   # if characters at index m and n matches and index is different
   if X[m - 1] == X[n - 1] and m != n:
       return LRSLength2(X, m - 1, n - 1) + 1

   # else if characters at index m and n don't match
   return max(LRSLength2(X, m, n - 1), LRSLength2(X, m - 1, n))

print(LRSLength("GTGTGATCG"))   # GTG
print(LRSLength("ATAKTKGGA"))  # ATKG
print(LRSLength2("ATAKTKGGA", 9, 9))
print(LRSLength("ADJLASDFHAJL"))
print(LRSLength2("ADJLASDFHAJL", 12, 12))
print(LRSLength("aefabhf"))
print(LRSLength2("aefabhf", 7, 7))

###-----------------------------------------------------------------------
###---------------------------LONGEST COMMON SUBSEQUENCE------------------
###-----------------------------------------------------------------------

# Longest Common Subsequence in Python

def findLCS_MEMO(s1, s2, index1, index2, memo):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if (index1, index2) in memo:
        return memo[(index1, index2)]

    if s1[index1] == s2[index2]:
        memo[(index1, index2)] = 1 + findLCS_MEMO(s1, s2, index1+1, index2+1, memo)
        return memo[(index1, index2)]
    else:
        op1 = findLCS_MEMO(s1,s2, index1, index2+1, memo)
        op2 = findLCS_MEMO(s1,s2, index1+1, index2, memo)
        memo[(index1, index2)] = max(op1, op2)

        return memo[(index1, index2)]

def findLCS(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if s1[index1] == s2[index2]:
        return 1 + findLCS(s1, s2, index1+1, index2+1)
    else:
        op1 = findLCS(s1,s2, index1, index2+1)
        op2 = findLCS(s1,s2, index1+1, index2)
        return max(op1, op2)

print(findLCS("elephant", "eretpat", 0, 0))  ##  Output --> eepat   (5)
print(findLCS_MEMO("elephant", "eretpat", 0, 0, {}))  ##  Output --> eepat   (5)
print(findLCS("bsbininm", "jmjkbkjkv",0, 0))  ##  Output --> eepat   (5)
print(findLCS_MEMO("bsbininm", "jmjkbkjkv",0, 0, {}))  ##  Output --> eepat   (5)

str_1 = "fcvafurqjylclorwfoladwfqzkbebslwnmpmlkbezkxoncvwhstwzwpqxqtyxozkpgtgtsjobujezgrkvevklmludgtyrmjaxyputqbyxqvupojutsjwlwluzsbmvyxifqtglwvcnkfsfglwjwrmtyxmdgjifyjwrsnenuvsdedsbqdovwzsdghclcdexmtsbexwrszihcpibwpidixmpmxshwzmjgtadmtkxqfkrsdqjcrmxkbkfoncrcvoxuvcdytajgfwrcxivixanuzerebuzklyhezevonqdsrkzetsrgfgxibqpmfuxcrinetyzkvudghgrytsvwzkjulmhanankxqfihenuhmfsfkfepibkjmzybmlkzozmluvybyzsleludsxkpinizoraxonmhwtkfkhudizepyzijafqlepcbihofepmjqtgrsxorunshgpazovuhktatmlcfklafivivefyfubunszyvarcrkpsnglkduzaxqrerkvcnmrurkhkpargvcxefovwtapedaluhclmzynebczodwropwdenqxmrutuhehadyfspcpuxyzodifqdqzgbwhodcjonypyjwbwxepcpujerkrelunstebopkncdazexsbezmhynizsvarafwfmnclerafejgnizcbsrcvcnwrolofyzulcxaxqjqzunedidulspslebifinqrchyvapkzmzwbwjgbyrqhqpolwjijmzyduzerqnadapudmrazmzadstozytonuzarizszubkzkhenaxivytmjqjgvgzwpgxefatetoncjgjsdilmvgtgpgbibexwnexstipkjylalqnupexytkradwxmlmhsnmzuxcdkfkxyfgrmfqtajatgjctenqhkvyrgvapctqtyrufcdobibizihuhsrsterozotytubefutaxcjarknynetipehoduxyjstufwvkvwvwnuletybmrczgtmxctuny"
str_2 = "nohgdazargvalupetizezqpklktojqtqdivcpsfgjopaxwbkvujilqbclehulatshehmjqhyfkpcfwxovajkvankjkvevgdovazmbgtqfwvejczsnmbchkdibstklkxarwjqbqxwvixavkhylqvghqpifijohudenozotejoxavkfkzcdqnoxydynavwdylwhatslyrwlejwdwrmpevmtwpahatwlaxmjmdgrebmfyngdcbmbgjcvqpcbadujkxaxujudmbejcrevuvcdobolcbstifedcvmngnqhudixgzktcdqngxmruhcxqxypwhahobudelivgvynefkjqdyvalmvudcdivmhghqrelurodwdsvuzmjixgdexonwjczghalsjopixsrwjixuzmjgxydqnipelgrivkzkxgjchibgnqbknstspujwdydszohqjsfuzstyjgnwhsrebmlwzkzijgnmnczmrehspihspyfedabotwvwxwpspypctizyhcxypqzctwlspszonsrmnyvmhsvqtkbyhmhwjmvazaviruzqxmbczaxmtqjexmdudypovkjklynktahupanujylylgrajozobsbwpwtohkfsxeverqxylwdwtojoxydepybavwhgdehafurqtcxqhuhkdwxkdojipolctcvcrsvczcxedglgrejerqdgrsvsxgjodajatsnixutihwpivihadqdotsvyrkxehodybapwlsjexixgponcxifijchejoxgxebmbclczqvkfuzgxsbshqvgfcraxytaxeviryhexmvqjybizivyjanwxmpojgxgbyhcruvqpafwjslkbohqlknkdqjixsfsdurgbsvclmrcrcnulinqvcdqhcvwdaxgvafwravunurqvizqtozuxinytafopmhchmxsxgfanetmdcjalmrolejidylkjktunqhkxchyjmpkvsfgnybsjedmzkrkhwryzan"
print("Long string test")
print(findLCS_MEMO(str_1, str_2,0, 0, {}))  ##  Output --> eepat   (5)




