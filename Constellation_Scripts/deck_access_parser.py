from array import *

def readDeck():
    # Parse deck access report and get IDs/names of spacecraft
    report = open("DeckAccess.txt", "r")
    lines = report.readlines()
    numLines = len(lines)
    scn = []

    # Start reading at line 7
    for i in range(6, numLines):
        tokenLine = lines[i].split()
        spacecraftID = tokenLine[0]
        if spacecraftID not in scn:
            scn.append(spacecraftID)

    report.close()
    return scn

# Get TLEs that correspond to spacecraft
def getTLEs():
    tleFile = open("Sats.tce", "r")
    scnList = readDeck()
    tleList = []
    tles = tleFile.readlines()
    numTLEs = int(round(len(tles) / 2))

    for i in range(1, numTLEs):
        line = tles[2 * i - 1].split()
        # Check if spacecraft referenced in report and, if so, add to list
        if line[1] in scnList:
            tleList.append(tles[2 * i - 2])
            tleList.append(tles[2 * i - 1])

    tleFile.close()
    return tleList

# Copy TLEs of identified spacecraft to new collection
def writeTLEs():
    sats = open("SatTLEs.tce", "w")
    tleList = getTLEs()

    for item in tleList:
        sats.write("%s" % item)
    sats.close()

writeTLEs()


