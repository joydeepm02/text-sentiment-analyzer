"""
Text Sentiment Analyzer
Joydeep Mukherjee

Sources:
Stop Words: https://gist.github.com/sebleier/554280
Positive/Negative Words: https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html

Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
       Proceedings of the ACM SIGKDD International Conference on Knowledge 
       Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
       Washington, USA, 
"""

import util

negative_stop_words = util.get_file_content_as_list("resources/negative-stop-words.txt")
neutral_stop_words = util.get_file_content_as_list("resources/neutral-stop-words.txt")
positive_stop_words = util.get_file_content_as_list("resources/positive-stop-words.txt")

negative_words = util.get_file_content_as_list("resources/negative-words.txt")
positive_words = util.get_file_content_as_list("resources/positive-words.txt")

original_text = util.format_into_string(util.get_file_content_as_list("resources/text.txt"))
text = util.clean_text(util.get_file_content_as_list("resources/text.txt"), neutral_stop_words)

sentiment = util.analyze_text_sentiment(text, negative_stop_words, positive_stop_words, negative_words, positive_words)

print("The original text was: " + original_text)
print("\nThe sentiment score was: " + str(sentiment))
print("This corresponds to a " + util.mood(sentiment) + " mood ... " + util.emoji(sentiment) + "\n")
