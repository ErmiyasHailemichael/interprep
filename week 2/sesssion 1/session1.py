'''
Problem 1: Festival Lineup
Given two lists of strings artists and set_times of length n, write a function lineup() 
that maps each artist to their set time.

An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times)
'''

def lineup(artists, set_times):
    dict_list = {}
    for artist, time in zip(artists, set_times):
       dict_list[artist] = time
    return dict_list
# print(lineup())


artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9 :30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]
# zipped = zip(artists1, set_times1)
# print(dict(zipped))

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))


def lineup(artists, set_times):
    # Using {} to initialize an empty dictionary
    artist_lineup = {}
    # Looping over the indices of artists
    for i in range(len(artists)):
        artist_lineup[artists[i]] = set_times[i]
    return artist_lineup

# Example usage:
artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalía"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]
artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))  # {"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalía": "7:30 PM"}
print(lineup(artists2, set_times2))  # {}


'''
you are designing an app for your festival to help attendees have the best experience possible! As part of the application, 
users will be able to easily search their favorite artist and find out the day, time, and stage the artist is playing at.
 Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule mapping artist's names to 
dictionaries containing the day, time, and stage they are playing on. Return the dictionary containing the information about the given artist.
'''

def get_artist_info(artist, festival_schedule):
    
    # return (festival_schedule.get(artist), {"message": "Artist not found"})
    for singer in festival_schedule:
        if singer == artist:
            return festival_schedule[artist]
        else:
            return {'Message': 'Artist is not found'}


festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  