import spacy
# imported spacy 

nlp = spacy.load('en_core_web_md')
# created variable called 'nlp' to load the english 'md' model

def similarity_function(movie, desc):
    # created a function called 'similarity_function' with the parameters of the movie and its description
    return movie.similarity(desc)
    # returned the similarity method with the movie, with the parameter of the description

def similar_movie(description):
    # created a function called 'similar_movie' with the parameter of the description of the movie
    
    movies = []
    # created an empty list called 'movies'
    with open('movies.txt', 'r') as file:
        # created a variable called 'file' to open and read the movies.txt file
        movies = file.readlines()
        # created a variable called 'movies' to read the lines of the file  

    movies = [nlp(explanation.strip()) for explanation in movies]
    # made the movies variable equal the iteration of the movies list and used the strip function on the iteration
    hulk = nlp(description)
    # created a variable called 'hulk' to use the nlp variable to get the description 

    calculating_similarity = [similarity_function(hulk, explanation) for explanation in movies]
    # created a variable called 'calculating_similariy' to use the similarity_function function on the hulk description and the 
    # iteration within the movies list

    similarity_index = max(range(len(calculating_similarity)), key=lambda x: calculating_similarity[x])
    # created a variable called 'similariy_index' to get the maximum range of the length of the calculating_similairity variable
    # and used the lambda key for the index of the variable

    return movies[similarity_index].text
    # returned the movies list, with the index of the similariy_index and used .text, to get the text of it

planet_hulk = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''
# created a variable called 'planet_hulk' and made it equal to the string of the given planet hulk description

most_similar_movie = similar_movie(planet_hulk)
# created a variable called most_similar_movie and made it equal to the similar_movie function and inserted 'planet_hulk' and the 
# description parameter
print(most_similar_movie)
# printed out the variable, which prints out the most similar movie