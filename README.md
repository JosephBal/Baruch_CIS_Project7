# Baruch_CIS_Project7
This was my 8th project in my CIS 2300 "Programming and Computational Thinking" led by professor Sadat Chowdhury

# Project Description

The following table describes numbers from 0 - 10 in three languages:

| Number | English | French | Pinyin (Chinese) | 
|--------|---------|--------|------------------|
| 0      | zero    | zero   | ling             |
| 1      | one     | un     | yi               |
| 2      | two     | deux   | er               |
| 3      | three   | trois  | san              |
| 4      | four    | quatre | si               |
| 5      | five    | cinq   | wu               |
| 6      | six     | six    | liu              |
| 7      | seven   | sept   | qi               |
| 8      | eight   | huit   | ba               |
| 9      | nine    | neuf   | jiu              |
| 10     | ten     | dix    | shi              |

__Part 1)__  Design 6 functions as follows:

num_to_english()

num_to_french()

num_to_pinyin()


pinyin_to_num()

french_to_num()

english_to_num()


Functions with the naming pattern: num_to_XXX() should take a single parameter and, based on the number argument, return the corresponding word in the given language. For e.g., num_to_english(5) should return back 'five'

Similarly, functions with the naming pattern: XXX_to_num() should take a single parameter and based on the str argument return the corresponding number in the given language. E.g., french_to_num('huit') should return 8.

When a number or word is not recognized the function should return None (None is a valid Python return value). As an e.g., num_to_french(23) should return None, and french_to_num('two') should return None.

__Part 2)__
Design a function called: french_to_pinyin(). This function should take a single parameter and based on the str argument (french word) it should return back the corresponding pinyin word. As examples:

french_to_pinyin('neuf') should return back 'jiu' and french_to_pinyin('bonjour') should return None.

Ideally, your design for french_to_pinyin() should internally just use french_to_num() and num_to_pinyin()
