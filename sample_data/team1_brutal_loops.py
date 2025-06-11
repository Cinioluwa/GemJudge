def count_overlapping_occurrences(s, sub):
    count = 0
    sub_len = len(sub)
    # Slide over the string; note that this manually counts overlapping occurrences.
    for i in range(len(s) - sub_len + 1):
        if s[i:i+sub_len] == sub:
            count += 1
    return count

def minion_game_team1(s):
    vowels = "AEIOU"
    stuart_score = 0
    kevin_score = 0
    n = len(s)
    # Generate every possible substring with nested loops.
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            occ = count_overlapping_occurrences(s, sub) # very inefficient!
            if s[i] in vowels:
                kevin_score += occ
            else:
                stuart_score += occ
    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")

if __name__ == "__main__":
    s = input().strip()
    minion_game_team1(s)
