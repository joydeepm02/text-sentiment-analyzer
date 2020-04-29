"""
Utility Functions
"""

import string

def get_file_content_as_list(file_location):
    with open(file_location) as f:
        contents = [line.rstrip() for line in f]
    return contents

def format_into_string(text):
    output_string = ""
    for line in text:
        output_string += line + " "
    return output_string

def clean_text(text, neutral_stop_words):
    punctuation = set(string.punctuation)
    text = [[''.join(c.lower() for c in word if c not in punctuation) for word in line.split(" ") if word.lower() not in neutral_stop_words] for line in text if line]
    return text

def analyze_text_sentiment(text, negative_stop_words, positive_stop_words, negative_words, positive_words):
    sentiment, total_words = 0, 0
    for line in text:
        i = 0
        while i < len(line):
            direction, multiplier = 1, 1
            j = i
            while j < len(line) and (line[j] in negative_stop_words or line[j] in positive_stop_words):
                if line[j] in negative_stop_words:
                    direction *= -1
                elif line[j] in positive_stop_words:
                    multiplier += 2 
                j += 1
                total_words += 1
            i = j
            if i == len(line):
                break
            total_words += 1
            if line[i] in negative_words:
                direction *= -1
            elif line[i] not in positive_words:
                multiplier = 0
            sentiment += direction * multiplier
            i += 1
    return sentiment / total_words if total_words != 0 else 0

def mood(sentiment):
    if sentiment < -1.33:
        return "very negative"
    if sentiment < -0.67:
        return "negative"
    if sentiment < 0:
        return "slightly negative"
    if sentiment == 0:
        return "neutral"
    if sentiment < 0.67:
        return "slightly positive"
    if sentiment < 1.33:
        return "positive"
    else:
        return "very positive"

def emoji(sentiment):
    if sentiment < -1.33:
        return "\U0001F621"
    if sentiment < -0.67:
        return "\U0001F61F"
    if sentiment < 0:
        return "\U0001F615"
    if sentiment == 0:
        return "\U0001F610"
    if sentiment < 0.67:
        return "\U0001F642"
    if sentiment < 1.33:
        return "\U0001F600"
    else:
        return "\U0001F601"
