def wise_speak(sentence):
    test_words = ["have", "must", "are", "will", "can"]
    punctuation = sentence[-1]
    rem_sentence = sentence[:-1]
    words = rem_sentence.split()

    text_index = -1
    for i, word in enumerate(words):
        if word.lower() in test_words:
            text_index = i
            break

    part_a = words[:text_index + 1]
    part_b = words[text_index + 1:]
    part_a_lower = [word.lower() for word in part_a]
    part_a_joined = " ".join(part_a_lower)

    # if text_index == -1:
        # if not words:
            # return punctuation
        # words[0] = words[0].capitalize()
        # return " ".join(words) + capitalization

    if part_b:
        part_b[0] = part_b[0].capitalize()
        part_b_joined = " ".join(part_b)
    else:
        part_b_joined = ""

    if part_b_joined:
        final_sentence = f"{part_b_joined}, {part_a_joined}{punctuation}" 
    else:
        final_sentence = f"{part_a_joined}{punctuation}"
    return final_sentence