import datetime
import pytz

csv_string = """Date,1310 Lost Sector,1310 Armor,1340 Lost Sector,1340 Armor,
5/31/2021,K1 Logistics (Moon),Chest,Empty Tank (Tangled Shore),Gauntlets,
6/1/2021,K1 Communion (Moon),Helmet,K1 Logistics (Moon),Chest,
6/2/2021,K1 Crew Quarters (Moon),Legs,K1 Communion (Moon),Helmet,
6/3/2021,K1 Revelation (Moon),Gauntlets,K1 Crew Quarters (Moon),Legs,
6/4/2021,Concealed Void (Europa),Chest,K1 Revelation (Moon),Gauntlets,
6/5/2021,Bunker E15 (Europa),Helmet,Concealed Void (Europa),Chest,
6/6/2021,Perdition (Europa),Legs,Bunker E15 (Europa),Helmet,
6/7/2021,The Quarry (EDZ),Gauntlets,Perdition (Europa),Legs,
6/8/2021,Scavenger's Den (EDZ),Chest,The Quarry (EDZ),Gauntlets,
6/9/2021,Excavation Site (EDZ),Helmet,Scavenger's Den (EDZ),Chest,
6/10/2021,Exodus Garden 2A (Cosm),Legs,Excavation Site (EDZ),Helmet,
6/11/2021,Veles Labyrinth (Cosm),Gauntlets,Exodus Garden 2A (Cosm),Legs,
6/12/2021,Empty Tank (Tangled Shore),Chest,Veles Labyrinth (Cosm),Gauntlets,
6/13/2021,K1 Logistics (Moon),Helmet,Empty Tank (Tangled Shore),Chest,
6/14/2021,K1 Communion (Moon),Legs,K1 Logistics (Moon),Helmet,
6/15/2021,K1 Crew Quarters (Moon),Gauntlets,K1 Communion (Moon),Legs,
6/16/2021,K1 Revelation (Moon),Chest,K1 Crew Quarters (Moon),Gauntlets,
6/17/2021,Concealed Void (Europa),Helmet,K1 Revelation (Moon),Chest,
6/18/2021,Bunker E15 (Europa),Legs,Concealed Void (Europa),Helmet,
6/19/2021,Perdition (Europa),Gauntlets,Bunker E15 (Europa),Legs,
6/20/2021,The Quarry (EDZ),Chest,Perdition (Europa),Gauntlets,
6/21/2021,Scavenger's Den (EDZ),Helmet,The Quarry (EDZ),Chest,
6/22/2021,Excavation Site (EDZ),Legs,Scavenger's Den (EDZ),Helmet,
6/23/2021,Exodus Garden 2A (Cosm),Gauntlets,Excavation Site (EDZ),Legs,
6/24/2021,Veles Labyrinth (Cosm),Chest,Exodus Garden 2A (Cosm),Gauntlets,
6/25/2021,Empty Tank (Tangled Shore),Helmet,Veles Labyrinth (Cosm),Chest,
6/26/2021,K1 Logistics (Moon),Legs,Empty Tank (Tangled Shore),Helmet,
6/27/2021,K1 Communion (Moon),Gauntlets,K1 Logistics (Moon),Legs,
6/28/2021,K1 Crew Quarters (Moon),Chest,K1 Communion (Moon),Gauntlets,
6/29/2021,K1 Revelation (Moon),Helmet,K1 Crew Quarters (Moon),Chest,
6/30/2021,Concealed Void (Europa),Legs,K1 Revelation (Moon),Helmet,
7/1/2021,Bunker E15 (Europa),Gauntlets,Concealed Void (Europa),Legs,
7/2/2021,Perdition (Europa),Chest,Bunker E15 (Europa),Gauntlets,
7/3/2021,The Quarry (EDZ),Helmet,Perdition (Europa),Chest,
7/4/2021,Scavenger's Den (EDZ),Legs,The Quarry (EDZ),Helmet,
7/5/2021,Excavation Site (EDZ),Gauntlets,Scavenger's Den (EDZ),Legs,
7/6/2021,Exodus Garden 2A (Cosm),Chest,Excavation Site (EDZ),Gauntlets,
7/7/2021,Veles Labyrinth (Cosm),Helmet,Exodus Garden 2A (Cosm),Chest,
7/8/2021,Empty Tank (Tangled Shore),Legs,Veles Labyrinth (Cosm),Helmet,
7/9/2021,K1 Logistics (Moon),Gauntlets,Empty Tank (Tangled Shore),Legs,
7/10/2021,K1 Communion (Moon),Chest,K1 Logistics (Moon),Gauntlets,
7/11/2021,K1 Crew Quarters (Moon),Helmet,K1 Communion (Moon),Chest,
7/12/2021,K1 Revelation (Moon),Legs,K1 Crew Quarters (Moon),Helmet,
7/13/2021,Concealed Void (Europa),Gauntlets,K1 Revelation (Moon),Legs,
7/14/2021,Bunker E15 (Europa),Chest,Concealed Void (Europa),Gauntlets,
7/15/2021,Perdition (Europa),Helmet,Bunker E15 (Europa),Chest,
7/16/2021,The Quarry (EDZ),Legs,Perdition (Europa),Helmet,
7/17/2021,Scavenger's Den (EDZ),Gauntlets,The Quarry (EDZ),Legs,
7/18/2021,Excavation Site (EDZ),Chest,Scavenger's Den (EDZ),Gauntlets,
7/19/2021,Exodus Garden 2A (Cosm),Helmet,Excavation Site (EDZ),Chest,
7/20/2021,Veles Labyrinth (Cosm),Legs,Exodus Garden 2A (Cosm),Helmet,
7/21/2021,Empty Tank (Tangled Shore),Gauntlets,Veles Labyrinth (Cosm),Legs,
7/22/2021,K1 Logistics (Moon),Chest,Empty Tank (Tangled Shore),Gauntlets,
7/23/2021,K1 Communion (Moon),Helmet,K1 Logistics (Moon),Chest,
7/24/2021,K1 Crew Quarters (Moon),Legs,K1 Communion (Moon),Helmet,
7/25/2021,K1 Revelation (Moon),Gauntlets,K1 Crew Quarters (Moon),Legs,
7/26/2021,Concealed Void (Europa),Chest,K1 Revelation (Moon),Gauntlets,
7/27/2021,Bunker E15 (Europa),Helmet,Concealed Void (Europa),Chest,
7/28/2021,Perdition (Europa),Legs,Bunker E15 (Europa),Helmet,
7/29/2021,The Quarry (EDZ),Gauntlets,Perdition (Europa),Legs,
7/30/2021,Scavenger's Den (EDZ),Chest,The Quarry (EDZ),Gauntlets,
7/31/2021,Excavation Site (EDZ),Helmet,Scavenger's Den (EDZ),Chest,
8/1/2021,Exodus Garden 2A (Cosm),Legs,Excavation Site (EDZ),Helmet,
8/2/2021,Veles Labyrinth (Cosm),Gauntlets,Exodus Garden 2A (Cosm),Legs,
8/3/2021,Empty Tank (Tangled Shore),Chest,Veles Labyrinth (Cosm),Gauntlets,
8/4/2021,K1 Logistics (Moon),Helmet,Empty Tank (Tangled Shore),Chest,
8/5/2021,K1 Communion (Moon),Legs,K1 Logistics (Moon),Helmet,
8/6/2021,K1 Crew Quarters (Moon),Gauntlets,K1 Communion (Moon),Legs,
8/7/2021,K1 Revelation (Moon),Chest,K1 Crew Quarters (Moon),Gauntlets,
8/8/2021,Concealed Void (Europa),Helmet,K1 Revelation (Moon),Chest,
8/9/2021,Bunker E15 (Europa),Legs,Concealed Void (Europa),Helmet,
8/10/2021,Perdition (Europa),Gauntlets,Bunker E15 (Europa),Legs,
8/11/2021,The Quarry (EDZ),Chest,Perdition (Europa),Gauntlets,
8/12/2021,Scavenger's Den (EDZ),Helmet,The Quarry (EDZ),Chest,
8/13/2021,Excavation Site (EDZ),Legs,Scavenger's Den (EDZ),Helmet,
8/14/2021,Exodus Garden 2A (Cosm),Gauntlets,Excavation Site (EDZ),Legs,
8/15/2021,Veles Labyrinth (Cosm),Chest,Exodus Garden 2A (Cosm),Gauntlets,
8/16/2021,Empty Tank (Tangled Shore),Helmet,Veles Labyrinth (Cosm),Chest,
8/17/2021,K1 Logistics (Moon),Legs,Empty Tank (Tangled Shore),Helmet,
8/18/2021,K1 Communion (Moon),Gauntlets,K1 Logistics (Moon),Legs,
8/19/2021,K1 Crew Quarters (Moon),Chest,K1 Communion (Moon),Gauntlets,
8/20/2021,K1 Revelation (Moon),Helmet,K1 Crew Quarters (Moon),Chest,
8/21/2021,Concealed Void (Europa),Legs,K1 Revelation (Moon),Helmet,
8/22/2021,Bunker E15 (Europa),Gauntlets,Concealed Void (Europa),Legs,
8/23/2021,Perdition (Europa),Chest,Bunker E15 (Europa),Gauntlets""".splitlines()

def csv_to_map(csv, delimiter = ","):
    h = {}
    for i, data in enumerate(csv):
        # i is index, data is data
        string = data.split(",")
        newstring = ""
        for j, data2 in enumerate(string):
            if j == 0:
                continue
            else:
                if j == 1:
                    newstring += "1310 Lost Sector: " + string[j] + ", "
                elif j == 2:
                    newstring += "Armor: " + string[j] + ", "
                elif j == 3:
                    newstring += "1340 Lost Sector: " + string[j] + ", "
                elif j == 4:
                    newstring += "Armor: " + string[j]
            h[string[0]] = newstring

    return h

def today_lost_sector():
    PST = pytz.timezone("US/Pacific")
    csv_map = csv_to_map(csv_string)
    temp_date = datetime.datetime.now(PST)
    curr_date = str(temp_date.month) + "/" + str(temp_date.day) + "/" + str(temp_date.year)
    curr_time = str(datetime.datetime.time(datetime.datetime.now(PST)))
    if curr_time < "10:00:00.00":
        return f"Date: {curr_date}, " + csv_map[curr_date] + ". WARNING: It is before daily reset; these lost sectors will be in effect following reset."
    else:
        return f"Date: {curr_date}, " + csv_map[curr_date]


# Vegeta plays function (Doesn't affect discord operations)
def csv_to_map_v(csv, delimiter = ","):
    h = {}
    for i, data in enumerate(csv):
        # i is index, data is data
        string = data.split(",")
        newstring = ""
        for j, data2 in enumerate(string):
            if j == 0:
                continue
            else:
                if j == 1:
                    newstring += "1310 Lost Sector: " + string[j]
                elif j == 2:
                    newstring += ": " + string[j] + " | "
                elif j == 3:
                    newstring += "1340 Lost Sector: " + string[j]
                elif j == 4:
                    newstring += ": " + string[j]
            h[string[0]] = newstring

    return h

def today_lost_sector_vegeta():
    PST = pytz.timezone("US/Pacific")
    csv_map = csv_to_map_v(csv_string)
    temp_date = datetime.datetime.now(PST)
    curr_date = str(temp_date.month) + "/" + str(temp_date.day) + "/" + str(temp_date.year)
    curr_time = str(datetime.datetime.time(datetime.datetime.now(PST)))
    if curr_time < "10:00:00.00":
        return_string = f"Date: {curr_date} | " + csv_map[curr_date] + " | WARNING: It is before daily reset; these lost sectors will be in effect following reset."
        if len(return_string) >= 200:
            return f"Date: {curr_date} | " + csv_map[curr_date] + " | WARNING: These lost sectors will be in effect following reset."
        else:
            return return_string
    else:
        return f"Date: {curr_date} | " + csv_map[curr_date]

# For debugging
#print(today_lost_sector())
print(today_lost_sector_vegeta())