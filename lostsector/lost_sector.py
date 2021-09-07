import datetime
import pytz

csv_string = """Date,1310 Lost Sector,1310 Armor,1340 Lost Sector,1340 Armor,
09/06/2021,Chamber of Starlight,Chest,Aphelion's Rest,Helmet
09/07/2021,Aphelion's Rest,Helmet,The Empty Tank,Legs
09/08/2021,The Empty Tank,Legs,K1 Logistics,Gauntlets
09/09/2021,K1 Logistics,Gauntlets,K1 Communion,Chest
09/10/2021,K1 Communion,Chest,K1 Crew Quarters,Helmet
09/11/2021,K1 Crew Quarters,Helmet,K1 Revelation,Legs
09/12/2021,K1 Revelation,Legs,Concealed Void,Gauntlets
09/13/2021,Concealed Void,Gauntlets,Bunker E15,Chest
09/14/2021,Bunker E15,Chest,Perdition,Helmet
09/15/2021,Perdition,Helmet,Bay of Drowned Wishes,Legs
09/16/2021,Bay of Drowned Wishes,Legs,Chamber of Starlight,Gauntlets
09/17/2021,Chamber of Starlight,Chest,Aphelion's Rest,Helmet
09/18/2021,Aphelion's Rest,Helmet,The Empty Tank,Legs
09/19/2021,The Empty Tank,Legs,K1 Logistics,Gauntlets
09/20/2021,K1 Logistics,Gauntlets,K1 Communion,Chest
09/21/2021,K1 Communion,Chest,K1 Crew Quarters,Helmet
09/22/2021,K1 Crew Quarters,Helmet,K1 Revelation,Legs
09/23/2021,K1 Revelation,Legs,Concealed Void,Gauntlets
09/24/2021,Concealed Void,Gauntlets,Bunker E15,Chest
09/25/2021,Bunker E15,Chest,Perdition,Helmet
09/26/2021,Perdition,Helmet,Bay of Drowned Wishes,Legs
09/27/2021,Bay of Drowned Wishes,Legs,Chamber of Starlight,Gauntlets
09/28/2021,Chamber of Starlight,Chest,Aphelion's Rest,Helmet
09/29/2021,Aphelion's Rest,Helmet,The Empty Tank,Legs
09/30/2021,The Empty Tank,Legs,K1 Logistics,Gauntlets
10/01/2021,K1 Logistics,Gauntlets,K1 Communion,Chest
10/02/2021,K1 Communion,Chest,K1 Crew Quarters,Helmet
10/03/2021,K1 Crew Quarters,Helmet,K1 Revelation,Legs
10/04/2021,K1 Revelation,Legs,Concealed Void,Gauntlets
10/05/2021,Concealed Void,Gauntlets,Bunker E15,Chest
10/06/2021,Bunker E15,Chest,Perdition,Helmet
10/07/2021,Perdition,Helmet,Bay of Drowned Wishes,Legs
10/08/2021,Bay of Drowned Wishes,Legs,Chamber of Starlight,Gauntlets
10/09/2021,Chamber of Starlight,Chest,Aphelion's Rest,Helmet
10/10/2021,Aphelion's Rest,Helmet,The Empty Tank,Legs
10/11/2021,The Empty Tank,Legs,K1 Logistics,Gauntlets
10/12/2021,K1 Logistics,Gauntlets,K1 Communion,Chest
10/13/2021,K1 Communion,Chest,K1 Crew Quarters,Helmet
10/14/2021,K1 Crew Quarters,Helmet,K1 Revelation,Legs
10/15/2021,K1 Revelation,Legs,Concealed Void,Gauntlets
10/16/2021,Concealed Void,Gauntlets,Bunker E15,Chest
10/17/2021,Bunker E15,Chest,Perdition,Helmet
10/18/2021,Perdition,Helmet,Bay of Drowned Wishes,Legs
10/19/2021,Bay of Drowned Wishes,Legs,Chamber of Starlight,Gauntlets
10/20/2021,Chamber of Starlight,Chest,Aphelion's Rest,Helmet
10/21/2021,Aphelion's Rest,Helmet,The Empty Tank,Legs
10/22/2021,The Empty Tank,Legs,K1 Logistics,Gauntlets
10/23/2021,K1 Logistics,Gauntlets,K1 Communion,Chest
10/24/2021,K1 Communion,Chest,K1 Crew Quarters,Helmet
10/25/2021,K1 Crew Quarters,Helmet,K1 Revelation,Legs
10/26/2021,K1 Revelation,Legs,Concealed Void,Gauntlets
10/27/2021,Concealed Void,Gauntlets,Bunker E15,Chest
10/28/2021,Bunker E15,Chest,Perdition,Helmet
10/29/2021,Perdition,Helmet,Bay of Drowned Wishes,Legs
10/30/2021,Bay of Drowned Wishes,Legs,Chamber of Starlight,Gauntlets
10/31/2021,Chamber of Starlight,Chest,Aphelion's Rest,Helmet
11/01/2021,Aphelion's Rest,Helmet,The Empty Tank,Legs
11/02/2021,The Empty Tank,Legs,K1 Logistics,Gauntlets
11/03/2021,K1 Logistics,Gauntlets,K1 Communion,Chest
11/04/2021,K1 Communion,Chest,K1 Crew Quarters,Helmet
11/05/2021,K1 Crew Quarters,Helmet,K1 Revelation,Legs
11/06/2021,K1 Revelation,Legs,Concealed Void,Gauntlets
11/07/2021,Concealed Void,Gauntlets,Bunker E15,Chest
11/08/2021,Bunker E15,Chest,Perdition,Helmet
11/09/2021,Perdition,Helmet,Bay of Drowned Wishes,Legs
11/10/2021,Bay of Drowned Wishes,Legs,Chamber of Starlight,Gauntlets
11/11/2021,Chamber of Starlight,Chest,Aphelion's Rest,Helmet
11/12/2021,Aphelion's Rest,Helmet,The Empty Tank,Legs
11/13/2021,The Empty Tank,Legs,K1 Logistics,Gauntlets
11/14/2021,K1 Logistics,Gauntlets,K1 Communion,Chest
11/15/2021,K1 Communion,Chest,K1 Crew Quarters,Helmet
11/16/2021,K1 Crew Quarters,Helmet,K1 Revelation,Legs
11/17/2021,K1 Revelation,Legs,Concealed Void,Gauntlets
11/18/2021,Concealed Void,Gauntlets,Bunker E15,Chest
11/19/2021,Bunker E15,Chest,Perdition,Helmet
11/20/2021,Perdition,Helmet,Bay of Drowned Wishes,Legs
11/21/2021,Bay of Drowned Wishes,Legs,Chamber of Starlight,Gauntlets
11/22/2021,Chamber of Starlight,Chest,Aphelion's Rest,Helmet
11/23/2021,Aphelion's Rest,Helmet,The Empty Tank,Legs
11/24/2021,The Empty Tank,Legs,K1 Logistics,Gauntlets
11/25/2021,K1 Logistics,Gauntlets,K1 Communion,Chest
11/26/2021,K1 Communion,Chest,K1 Crew Quarters,Helmet
11/27/2021,K1 Crew Quarters,Helmet,K1 Revelation,Legs
11/28/2021,K1 Revelation,Legs,Concealed Void,Gauntlets
11/29/2021,Concealed Void,Gauntlets,Bunker E15,Chest
11/30/2021,Bunker E15,Chest,Perdition,Helmet
12/01/2021,Perdition,Helmet,Bay of Drowned Wishes,Legs
12/02/2021,Bay of Drowned Wishes,Legs,Chamber of Starlight,Gauntlets
12/03/2021,Chamber of Starlight,Chest,Aphelion's Rest,Helmet
12/04/2021,Aphelion's Rest,Helmet,The Empty Tank,Legs
12/05/2021,The Empty Tank,Legs,K1 Logistics,Gauntlets
12/06/2021,K1 Logistics,Gauntlets,K1 Communion,Chest
12/07/2021,K1 Communion,Chest,K1 Crew Quarters,Helmet
12/08/2021,K1 Crew Quarters,Helmet,K1 Revelation,Legs
12/09/2021,K1 Revelation,Legs,Concealed Void,Gauntlets
12/10/2021,Concealed Void,Gauntlets,Bunker E15,Chest
12/11/2021,Bunker E15,Chest,Perdition,Helmet
12/12/2021,Perdition,Helmet,Bay of Drowned Wishes,Legs
12/13/2021,Bay of Drowned Wishes,Legs,Chamber of Starlight,Gauntlets
12/14/2021,Chamber of Starlight,Chest,Aphelion's Rest,Helmet
12/15/2021,Aphelion's Rest,Helmet,The Empty Tank,Legs
12/16/2021,The Empty Tank,Legs,K1 Logistics,Gauntlets
12/17/2021,K1 Logistics,Gauntlets,K1 Communion,Chest
12/18/2021,K1 Communion,Chest,K1 Crew Quarters,Helmet
12/19/2021,K1 Crew Quarters,Helmet,K1 Revelation,Legs
12/20/2021,K1 Revelation,Legs,Concealed Void,Gauntlets
12/21/2021,Concealed Void,Gauntlets,Bunker E15,Chest
12/22/2021,Bunker E15,Chest,Perdition,Helmet
12/23/2021,Perdition,Helmet,Bay of Drowned Wishes,Legs
12/24/2021,Bay of Drowned Wishes,Legs,Chamber of Starlight,Gauntlets
12/25/2021,Chamber of Starlight,Chest,Aphelion's Rest,Helmet
12/26/2021,Aphelion's Rest,Helmet,The Empty Tank,Legs
12/27/2021,The Empty Tank,Legs,K1 Logistics,Gauntlets
12/28/2021,K1 Logistics,Gauntlets,K1 Communion,Chest
12/29/2021,K1 Communion,Chest,K1 Crew Quarters,Helmet
12/30/2021,K1 Crew Quarters,Helmet,K1 Revelation,Legs
12/31/2021,K1 Revelation,Legs,Concealed Void,Gauntlets
01/01/2022,Concealed Void,Gauntlets,Bunker E15,Chest
01/02/2022,Bunker E15,Chest,Perdition,Helmet
01/03/2022,Perdition,Helmet,Bay of Drowned Wishes,Legs
01/04/2022,Bay of Drowned Wishes,Legs,Chamber of Starlight,Gauntlets
01/05/2022,Chamber of Starlight,Chest,Aphelion's Rest,Helmet
01/06/2022,Aphelion's Rest,Helmet,The Empty Tank,Legs
01/07/2022,The Empty Tank,Legs,K1 Logistics,Gauntlets
01/08/2022,K1 Logistics,Gauntlets,K1 Communion,Chest
01/09/2022,K1 Communion,Chest,K1 Crew Quarters,Helmet
01/10/2022,K1 Crew Quarters,Helmet,K1 Revelation,Legs
01/11/2022,K1 Revelation,Legs,Concealed Void,Gauntlets
01/12/2022,Concealed Void,Gauntlets,Bunker E15,Chest
01/13/2022,Bunker E15,Chest,Perdition,Helmet
01/14/2022,Perdition,Helmet,Bay of Drowned Wishes,Legs
01/15/2022,Bay of Drowned Wishes,Legs,Chamber of Starlight,Gauntlets
01/16/2022,Chamber of Starlight,Chest,Aphelion's Rest,Helmet
01/17/2022,Aphelion's Rest,Helmet,The Empty Tank,Legs
01/18/2022,The Empty Tank,Legs,K1 Logistics,Gauntlets
01/19/2022,K1 Logistics,Gauntlets,K1 Communion,Chest
01/20/2022,K1 Communion,Chest,K1 Crew Quarters,Helmet
01/21/2022,K1 Crew Quarters,Helmet,K1 Revelation,Legs
01/22/2022,K1 Revelation,Legs,Concealed Void,Gauntlets
01/23/2022,Concealed Void,Gauntlets,Bunker E15,Chest
01/24/2022,Bunker E15,Chest,Perdition,Helmet
01/25/2022,Perdition,Helmet,Bay of Drowned Wishes,Legs
01/26/2022,Bay of Drowned Wishes,Legs,Chamber of Starlight,Gauntlets
01/27/2022,Chamber of Starlight,Chest,Aphelion's Rest,Helmet
01/28/2022,Aphelion's Rest,Helmet,The Empty Tank,Legs
01/29/2022,The Empty Tank,Legs,K1 Logistics,Gauntlets
01/30/2022,K1 Logistics,Gauntlets,K1 Communion,Chest
01/31/2022,K1 Communion,Chest,K1 Crew Quarters,Helmet
02/01/2022,K1 Crew Quarters,Helmet,K1 Revelation,Legs
02/02/2022,K1 Revelation,Legs,Concealed Void,Gauntlets
02/03/2022,Concealed Void,Gauntlets,Bunker E15,Chest
02/04/2022,Bunker E15,Chest,Perdition,Helmet
02/05/2022,Perdition,Helmet,Bay of Drowned Wishes,Legs
02/06/2022,Bay of Drowned Wishes,Legs,Chamber of Starlight,Gauntlets
02/07/2022,Chamber of Starlight,Chest,Aphelion's Rest,Helmet
02/08/2022,Aphelion's Rest,Helmet,The Empty Tank,Legs
02/09/2022,The Empty Tank,Legs,K1 Logistics,Gauntlets
02/10/2022,K1 Logistics,Gauntlets,K1 Communion,Chest
02/11/2022,K1 Communion,Chest,K1 Crew Quarters,Helmet
02/12/2022,K1 Crew Quarters,Helmet,K1 Revelation,Legs
02/13/2022,K1 Revelation,Legs,Concealed Void,Gauntlets
02/14/2022,Concealed Void,Gauntlets,Bunker E15,Chest
02/15/2022,Bunker E15,Chest,Perdition,Helmet
02/16/2022,Perdition,Helmet,Bay of Drowned Wishes,Legs
02/17/2022,Bay of Drowned Wishes,Legs,Chamber of Starlight,Gauntlets
02/18/2022,Chamber of Starlight,Chest,Aphelion's Rest,Helmet
02/19/2022,Aphelion's Rest,Helmet,The Empty Tank,Legs
02/20/2022,The Empty Tank,Legs,K1 Logistics,Gauntlets
02/21/2022,K1 Logistics,Gauntlets,K1 Communion,Chest""".splitlines()

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
    if temp_date.day < 10:
        if temp_date.month < 10:
            curr_date = "0" + str(temp_date.month) + "/0" + str(temp_date.day) + "/" + str(temp_date.year)
        else:
            curr_date =  str(temp_date.month) + "/0" + str(temp_date.day) + "/" + str(temp_date.year)
    else:
        if temp_date.month < 10:
            curr_date = "0" + str(temp_date.month) + "/0" + str(temp_date.day) + "/" + str(temp_date.year)
        else:
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
    if temp_date.day < 10:
        if temp_date.month < 10:
            curr_date = "0" + str(temp_date.month) + "/0" + str(temp_date.day) + "/" + str(temp_date.year)
        else:
            curr_date =  str(temp_date.month) + "/0" + str(temp_date.day) + "/" + str(temp_date.year)
    else:
        if temp_date.month < 10:
            curr_date = "0" + str(temp_date.month) + "/0" + str(temp_date.day) + "/" + str(temp_date.year)
        else:
            curr_date = str(temp_date.month) + "/" + str(temp_date.day) + "/" + str(temp_date.year)
    curr_time = str(datetime.datetime.time(datetime.datetime.now(PST)))
    if curr_time < "10:00:00.00":
        return f"Date: {curr_date} | " + csv_map[curr_date] + " | WARNING: It is before daily reset; these lost sectors will be in effect following reset."
    else:
        return f"Date: {curr_date} | " + csv_map[curr_date]

# For debugging
# print(today_lost_sector())
# print(today_lost_sector_vegeta())