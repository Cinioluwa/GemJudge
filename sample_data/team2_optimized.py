def minion_game_team2(s):
    vowels = "AEIOU"
    stuart_score = 0
    kevin_score = 0
    n = len(s)
    for i in range(n):
        # Each letter at index i contributes (n-i) substrings.
        if s[i] in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i

    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")
        
if __name__ == "__main__":
    s = input().strip()
    minion_game_team2(s)
