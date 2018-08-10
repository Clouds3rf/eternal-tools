""" This module contains utilities for the Eternal Card Game. """
import csv
import re


def convert_exported_deck_to_csv(input_filepath = "exported_deck.txt", output_filepath = "deck.csv"):
    """ Convert Eternal's standard exported deck format to CSV format. 
    
    For example, if the file at `input_filepath` contains
    
        1 Initiate of the Sands (Set1 #74)
        2 Bold Adventurer (Set1 #77)
        2 Dark Wisp (Set1 #264)
        2 Learned Herbalist (Set4 #63)
        1 Living Example (Set4 #64)
        3 Rapid Shot (Set1 #259)
        1 Teleport (Set1 #80)
        1 Dune Phantom (Set1 #89)
        1 Gravetender (Set4 #72)
        1 Ravenous Thornbeast (Set1 #278)
        1 Extinguish (Set3 #228)
        1 Gnash, Pridemaster (Set4 #79)
        1 Preserver of Dualities (Set4 #267)
        1 Spiteful Lumen (Set4 #84)
        1 Lethrai Bladewhirl (Set4 #236)
        1 Pensive Lumen (Set4 #88)
        2 Cut Ties (Set4 #238)
        1 Voyaging Lumen (Set2 #66)
        2 Subterranean Sentry (Set4 #95)
        11 Time Sigil (Set1 #63)
        8 Shadow Sigil (Set1 #249)
    
    then this will write the following contents to `output_filepath`:
    
        name;quantity;unique_id
        Initiate of the Sands;1;Set1 #74
        Bold Adventurer;2;Set1 #77
        Dark Wisp;2;Set1 #264
        Learned Herbalist;2;Set4 #63
        Living Example;1;Set4 #64
        Rapid Shot;3;Set1 #259
        Teleport;1;Set1 #80
        Dune Phantom;1;Set1 #89
        Gravetender;1;Set4 #72
        Ravenous Thornbeast;1;Set1 #278
        Extinguish;1;Set3 #228
        Gnash, Pridemaster;1;Set4 #79
        Preserver of Dualities;1;Set4 #267
        Spiteful Lumen;1;Set4 #84
        Lethrai Bladewhirl;1;Set4 #236
        Pensive Lumen;1;Set4 #88
        Cut Ties;2;Set4 #238
        Voyaging Lumen;1;Set2 #66
        Subterranean Sentry;2;Set4 #95
        Shadow Sigil;8;Set1 #249
    """
    with open(input_filepath, "r") as infile, open(output_filepath, "w") as outfile:
    
        writer = csv.writer(outfile, delimiter = ";")
        
        outfile.write("name;quantity;unique_id\n")
        
        for line in infile:
            
            match = re.match(r'(\d) (.*) \((.*)\)', line)
            
            if match:
            
                writer.writerow((match.group(2), match.group(1), match.group(3)))
           