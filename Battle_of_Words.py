def battle(our_team, opponent):
    def word_value(word):
        total_value = 0
        for char in word:
            letter = char.lower()
            value = ord(letter) - ord("a") + 1
            if char.isupper():
                total_value += value * 2
            else:
                total_value += value
        return total_value
    our_words = our_team.split(' ')
    opponent_words = opponent.split(' ')
    team_wins = 0
    opponent_wins = 0
    for our_word, opponent_word in zip(our_words, opponent_words):
        our_value = word_value(our_word)
        opponent_value = word_value(opponent_word)
        if our_value > opponent_value:
            team_wins += 1
        elif opponent_value > our_value:
            opponent_wins += 1
    if team_wins > opponent_wins:
        return "We win"
    elif opponent_wins > team_wins:
        return "We lose"
    else:
        return "Draw"
