import soundcloud
import csv
client_id="YOUR_CLIENT_ID" #TODO: Change to your Client ID
username = input("Username: ")

client = soundcloud.Client(client_id=client_id)
totalDuration = 0
totalTracks = 0
page_size = 200 # Max 200!
next_href = ""
fname = username + ".csv"
file = open(fname, "w")
writer = csv.writer(file)
def writeLine(track):
    global totalDuration
    global totalTracks

    writer.writerow( (track.title, track.permalink_url) )
    print(track.title.replace(',', ' ') + " " + track.permalink_url)
    totalDuration = totalDuration + track.duration
    totalTracks += 1

tracks = client.get('/users/' + username + '/favorites', order='created_at', limit=page_size, 
linked_partitioning=1)
for track in tracks.collection:
    writeLine(track)

next_href = tracks.next_href
while(next_href):
    tracks2 = client.get(next_href, order='created_at', limit=page_size, linked_partitioning=1)
    for track in tracks2.collection:
        writeLine(track)
        
    if hasattr(tracks2, "next_href"):
        next_href = tracks2.next_href
    else:
        next_href = ""
print("Done.")
print("Total fetched tracks: " + repr(totalTracks) + ".")
print("Total playlist duration:")
print("    " + repr(round(totalDuration / 1000)) + "s.")
print("    " + repr(round(totalDuration / 1000 / 60)) + "mins.")
print("    " + repr(round(totalDuration / 1000 / 60 / 24)) + " days.")
print("    " + repr(round(totalDuration / 1000 / 60 / 24 / 30)) + " months.")

