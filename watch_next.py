# Got help from 
# https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory
# To run the Python script from the directory where the Python file is, 
# so that inventory.txt is accessible when placed in the same path as the Python script
import os
# Gets the path of current python script
abs_path = os.path.abspath(__file__)
# Gets the directory name of the script
dir_name = os.path.dirname(abs_path)
# Changes the current directory to the directory where the script is
os.chdir(dir_name)

# Imports spacy for language processing
import spacy


#==========================================================
# Function that gets a string and compares it with movies 
# description in a file and returns the movie name which 
# has the highest similarity value
#==========================================================
def next_movie(movie_description):
    '''
    This function opens the file movies.txt and reads the data from this file, and 
    creates a Doc object with the second part of the each entry (the description)
    to find similarity value with the Doc object of the passed string. It returns the movie 
    name for the corresponding description which was most similar with the passed string based 
    on similarity value. 
    '''

    # Loads the advanced English Language model
    nlp = spacy.load('en_core_web_md')

    movie_doc = nlp(movie_description)

    # Dictionary for storing movie name and the similarity value of each movie description
    # with the string
    movies_similarities = {}

    # Handles FileNotFoundError
    try:
        with open("movies.txt", "r", encoding= "utf-8") as movies_file :

            # splits each line with ":" and gets the data
            for entry in [line.split(":") for line in movies_file] :

                entry[0] = entry[0].strip()
                # Finds the similarity between the string and each movie description in the file
                movies_similarities[entry[0]] =  nlp(entry[1]).similarity(movie_doc)

        # Finds the maximum value among the similarity values and gets the corresponding movie name
        movie = max(movies_similarities, key= movies_similarities.get)
        return movie

    except FileNotFoundError:
            print("\nThe file does not exist! Please check the directory.")
            

planet_hulk_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for\
the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a\
planet where the Hulk can live in peace. Unfortunately, Hulk land on the\
planet Sakaar where he is sold into slavery and trained as a gladiator."

print(f"\nThe most similar movie you may want to watch based on your previous movie is {next_movie(planet_hulk_description)}\n")
