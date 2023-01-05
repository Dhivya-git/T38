# Imports spacy for language processing
import spacy

#==========================================================
# Function that finds similarity between 3 words
#==========================================================
def similarity_between_3words(nlp, word1, word2, word3):

    # Creates Doc object for the words
    word1 = nlp(word1)
    word2 = nlp(word2)
    word3 = nlp(word3)

    # Checks the similarites between the words
    print(f"\n\nSimilarities between {word1}, {word2}, {word3}")
    print(word1,"<->", word2, word1.similarity(word2))
    print(word3,"<->", word2, word3.similarity(word2))
    print(word3,"<->", word1, word3.similarity(word1))

# Loads the advanced English Language model
nlp = spacy.load('en_core_web_md')

similarity_between_3words(nlp,"cat", "monkey", "banana")

''' 
    Findings:
    Cat and monkey have similarity of 0.59 since they are animals.
    Monkey and banana also have slighty higher similarity of 0.40 since monkeys eat bananas.
    Although similarity between monkey and banana is slightly high, the similarity between 
    cat and banana is significantly less(0.22) as the model does not recognise transitive relationships.'''

# Finds similarity for my chosen 3 words using advanced language model 
similarity_between_3words(nlp,"paper", "printer", "computer")
'''
    Findings:
    Computer and printer are very similar with 0.62 since they are both hardwares.
    Printer and paper also have slightly higher similarity of 0.51 since we print on paper.
    However computer and paper are less similar(0.37), since we do not use paper with a computer.'''

# Loads the basic English language model
nlp = spacy.load('en_core_web_sm')
similarity_between_3words(nlp,"paper", "printer", "computer")
'''
    Findings:
    The warning message mentions that the 'en_core_web_sm' model does not have word vectors, 
    so may not give useful similarity judgements. Although it gives similarity values based on
    context-sensitive tensors which gives some similarity information that may not be useful.
    I notice that the similarity between paper, printer and computer are all around 0.75
    Interestingly printer and paper is the lowest of the three with 0.74. Whereas, computer 
    and paper is 0.78. This shows that 'en_core_web_sm' might not be useful in finding similarities 
    betweeen words'''

# Loads the advanced English Language model
nlp = spacy.load('en_core_web_md')

# Working with a single sentence
tokens = nlp('cat apple monkey banana ')

# Checks the similarites between the words in a sentence
print(f"\n\nSimilarities between words in sentence, {tokens.text}")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text,"<->", token2.text, token1.similarity(token2))


# Working with sentences
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

# Creates the Doc object for the model sentence
model_sentence = nlp(sentence_to_compare)

# Checks the similarities between the model sentence with every sentence in the list
print(f"\n\nSimilarities between the model sentence, \'{sentence_to_compare}\' and the following sentences:")
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


