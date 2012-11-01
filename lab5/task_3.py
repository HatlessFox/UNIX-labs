#!/usr/local/bin/python3

import xml.etree.ElementTree as el_tree

NS = "{http://www.w3.org/2005/Atom}"
APPLE_NS = "{http://itunes.apple.com/rss}"

root = el_tree.parse("top_songs_itunes.rss").getroot(); 

ind = 1;
for song in root.findall(NS + "entry"):
  print("Song #{0}:".format(ind));
  ind += 1;
  intend = "  "
  print(intend+"Artist: "+song.find(APPLE_NS + "artist").text);
  print(intend+"Title: "+song.find(APPLE_NS + "name").text);
  print(intend+"Price: "+song.find(APPLE_NS + "price").text + " Rights: " + song.find(NS + "rights").text);
  
print();
