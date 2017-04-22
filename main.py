import soundcloud
import csv
client_id="YOUR CLIENT ID" #TODO: Change to your Client ID
username = input("Username: ")

client = soundcloud.Client(client_id=client_id)

page_size = 200 # Max 200!
next_href = ""
fname = username + ".csv"
file = open(fname, "w")
writer = csv.writer(file)
tracks = client.get('/users/' + username + '/favorites', order='created_at', limit=page_size, 
linked_partitioning=1)
for track in tracks.collection:
    writer.writerow( (track.title, track.permalink_url) )
    print(track.title.replace(',', ' ') + " " + track.permalink_url)

next_href = tracks.next_href
while(next_href):
    tracks2 = client.get(next_href, order='created_at', limit=page_size, linked_partitioning=1)
    for track in tracks2.collection:
        writer.writerow((track.title, track.permalink_url) )
        print(track.title.replace(',', ' ') + " " + track.permalink_url)
        
    if hasattr(tracks2, "next_href"):
        next_href = tracks2.next_href
    else:
        next_href = ""
print("Done.")
    
