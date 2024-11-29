# This project is an introduction to sentimental analysis, a subject in machine learning that aims to 
# categorize human opinions when given a piece of text. 

# This project's goal is to determine the grade level (U.S Standard) that is required to understand a piece of text. 
# This project will use the Coleman-Liau Index to achieve this goal.

#NOTE: The Coleman-Liau index is given by /// index = 0.0588 * L - 0.296 * S - 15.8 ///,
#NOTE: where L is the average number of letters per 100 words in the text and S is the average number of sentences per 100 words in the text.

#NOTE: Although sentence bounding normally needs to be pretty smart,
#NOTE: !! just assume that every sentence ends with a period, exclamation mark, or a question mark. !!

import re


def main():
    # Prompt user input
    user_input = input("Enter a line of text: ")

    # Calculate average words and sentences
    avg_word, avg_sentences = avg_words_sentences(user_input)

    # Determine grade level
    grade_level = coleman_liau(avg_word, avg_sentences)

    # Output
    print(f"The line of text given requires the student to be in Grade: {grade_level}")


def avg_words_sentences(text):
    # Determine the average amount of words and sentences
    # NOTE: Find average number of letters per 100 words
    # NOTE: Find average number of sentences per 100 words
    # NOTE: Return using tuple return (or don't. as long as the code works.)


    pass


# Make sure to round to the nearest integer!
def coleman_liau(average_words, average_sentences):
    # NOTE: Formula is: 0.0588 * L - 0.296 * S - 15.8
    
    pass


if __name__ == "__main__":
    main()