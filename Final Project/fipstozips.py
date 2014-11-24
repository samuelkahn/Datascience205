import json
import csv

infiles = '/home/matt/Downloads/fips/zipcty'
outfile = '/home/matt/Downloads/fips/zipctymap'

g = open(outfile, 'a')

statefips={}

with open('/home/matt/Downloads/fips/statefips.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        stateabbr=row[0]
        statefips[stateabbr]= {
            "statename":row[2],
            "statefips":row[1],
        }

def zipmapper(n):
    fname=    infiles + str(n)
    f = open(fname, 'r')

    zipfips={}

    for line in f:
        zipcd = line[:5]
        try:
            int(zipcd)
        except ValueError:
            continue
        state = line[23:25]
        cofips = line[25:28]
        county = line[28:].strip()
        if zipfips.get(zipcd):
            continue
        else:
            try:
                statefips.get(state)['statefips']
            except TypeError:
                print "ERROR at state code: " + state + " and zip code " + zipcd + " in file number " + str(n)
                continue
            stfips = statefips.get(state)['statefips']
            fips=stfips+cofips
            stname = statefips.get(state)['statename']
            zipfips[zipcd]= {
                "fips":fips,
                "stateabbr":state,
                "county":county,
                "state":stname
            }

    g.write(json.dumps(zipfips))

for n in range(1,10):
    zipmapper(n)