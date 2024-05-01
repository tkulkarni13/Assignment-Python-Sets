# Task 1: Artist Lineup Compilation

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Artic Monkeys", "Tame Impala"] # Given artists
# artist_names2 = ["The Lumineers", "Tame Impala"] # Test to make sure duplicatePlaylists stores the right information
unique_artists = set(artist_names) # Convert list to set to remove duplicates

if (len(artist_names) == len(unique_artists)): # Check for duplicates by comparing size of set to original list (a smaller set indicates duplicates have been removed)
    duplicatePlaylists = False
else:
    duplicatePlaylists = True

print("Duplicate playlists found: {}".format(duplicatePlaylists)) # Print if duplicate playlists were found
print("Unique artists: {}".format(unique_artists)) # Print out unique artists