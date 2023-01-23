# Import spacy module
import spacy

# Load 'en_core_web_md'
nlp = spacy.load('en_core_web_md')

# Open 'movies.txt' file for reading, read the movies and close the file using .close()
file = open("movies.txt", "r")
movies_list = file.readlines()
file.close()


# Define function 'watch_next' with 'description' as its parameter.
def watch_next(description):
    nlp_description = nlp(description)

    # Create at empty list called 'similarity_results'.
    similarity_results = []

    # Use for loop to iterate through the movies_list.
    # Use .split() to split by colon(":") and store in 'title' and 'movie_description'.
    # Determine similarity between the 'movie_description' and 'nlp_description'.
    # Append 'similarity' to the 'similarity_results' each time.
    for movie in movies_list:
        title, movie_description = movie.split(":")
        similarity = nlp(movie_description).similarity(nlp_description)
        similarity_results.append(similarity)
        print(f"{movie[:7]} - {similarity}")

    # Use max() function to return the maximum value from 'similarity results' list.
    # Use indexing to find the most similar movie which will have the same index as the 'max_score' index in the list.
    max_score = max(similarity_results)
    most_similar_movie = movies_list[similarity_results.index(max_score)]

    # Return which movie the user should watch next based on the most similar movie.
    return f"\nNext, you should watch: \n{most_similar_movie}"


# Define string variable 'hulk_description' and store its description.
hulk_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the " \
              "Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in " \
              "peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a " \
              "gladiator."

# Print the movie that the user should watch next using watch_next() function.
print(watch_next(hulk_description))
