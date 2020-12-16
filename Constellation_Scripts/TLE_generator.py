# Generate list of two-line elements (TLEs) for spacecraft within STK
import numpy as np
import math

altV = 340
altK = 1150
altM = 550
numV = 7500
numK = 2800
numM = 1600

# 24 planes at 53-deg inc (RAAN spacing = 15 deg)
# 7500 V-band satellites at 340 km alt
# 2800 Ka-/Ku-band satellites at 1150 km altitude
# 1500 unknown-frequency satellites at 550 km altitude

def initFile1():
    numPlanes = 24
    # Set equal RAAN spacing
    incRAAN = 360 / numPlanes
    satsPerPlane = 66
    incW = 360 / satsPerPlane
    RAAN = 0

    p1 = open("phase1.tce", "w+")

    for i in range(numPlanes):
        w = 0
        # Take RAAN to 4 decimal places
        RAANdec = format(RAAN, ".4f")
        # Cast RAAN to 8-char string
        RAANstr = str(RAANdec).rjust(8, ' ')
        for j in range(satsPerPlane):
            # Pad ID to give it length of 5
            spacecraftID = str(j + 66 * i).rjust(5, '0')
            # Create name for unclassified spacecraft
            IDU = spacecraftID + 'U'
            # Take perigee to 4 decimal places
            wdec = float("{0:.4f}".format(w))
            # Cast perigee to 8-char string
            wstr = str(wdec).ljust(8, '0')
            # Replace with first line of TLE report in STK scenario
            l1 = "1 %s 19029 19171.97701855 .00001067 00000-0 11317-3 0 9993\n" % (IDU)
            # Replace with second line of TLE report in STK scenario
            l2 = "2 %s 53.0000 %s 0001863 120.4102 %s 15.05462229 3427\n" % (spacecraftID, RAANstr, wstr)

            # Note: Remember to change second, fourth, and seventh fields of TLE rpeort to %s
            p1.write(l1)
            p1.write(l2)

            w += incW

        RAAN += incRAAN

    p1.close()

def initFile2():
    numPlanes = 20
    # Set equal RAAN spacing
    incRAAN = 360 / numPlanes
    satsPerPlane = 142
    incW = 360 / satsPerPlane
    RAAN = 0

    p2 = open("phase2.tce", "w+")

    for i in range(numPlanes):
        w = 0
        # Take RAAN to 4 decimal places
        RAANdec = format(RAAN, ".4f")
        # Cast RAAN to 8-char string
        RAANstr = str(RAANdec).rjust(8, ' ')
        for j in range(satsPerPlane):
            # Pad ID to give it length of 5
            spacecraftID = str(j + 1584 + 142 * i).rjust(5, '0')
            # Create name for unclassified spacecraft
            IDU = spacecraftID + 'U'
            # Take perigee to 4 decimal places
            wdec = float("{0:.4f}".format(w))
            # Cast perigee to 8-char string
            wstr = str(wdec).ljust(8, '0')
            # Replace with first line of TLE report in STK scenario
            l1 = "1 %s 19029 19171.97701855 .00000087 00000-0 18822-3 0 0004\n" % (IDU)
            # Replace with second line of TLE report in STK scenario
            l2 = "2 %s 60.0000 %s 0001863 268.8694 %s 13.29342207 0016\n" % (spacecraftID, RAANstr, wstr)

            # Note: Remember to change second, fourth, and seventh fields of TLE rpeort to %s
            p2.write(l1)
            p2.write(l2)

            w += incW

        RAAN += incRAAN

    p2.close()

def initFile3():
    numPlanes = 42
    # Set equal RAAN spacing
    incRAAN = 360 / numPlanes
    satsPerPlane = 179
    incW = 360 / satsPerPlane
    RAAN = 0

    p3 = open("phase3.tce", "w+")

    for i in range(numPlanes):
        w = 0
        # Take RAAN to 4 decimal places
        RAANdec = format(RAAN, ".4f")
        # Cast RAAN to 8-char string
        RAANstr = str(RAANdec).rjust(8, ' ')
        for j in range(satsPerPlane):
            # Pad ID to give it length of 5
            spacecraftID = str(j + 4424 + 179 * i).rjust(5, '0')
            # Create name for unclassified spacecraft
            IDU = spacecraftID + 'U'
            # Take perigee to 4 decimal places
            wdec = float("{0:.4f}".format(w))
            # Cast perigee to 8-char string
            wstr = str(wdec).ljust(8, '0')
            # Replace with first line of TLE report in STK scenario
            l1 = "1 %s 19029 19171.97701855 .00003638 00000-0 22107-4 0 0001\n" % (IDU)
            # Replace with second line of TLE report in STK scenario
            l2 = "2 %s 60.0000 %s 0001863 120.4102 %s 15.76924715 0019\n" % (spacecraftID, RAANstr, wstr)

            # Note: Remember to change second, fourth, and seventh fields of TLE rpeort to %s
            p3.write(l1)
            p3.write(l2)

            w += incW

        RAAN += incRAAN

    p3.close()

# Generate TLE report for each phase
# Note: Could be made more efficient but risky since vals from STK report are plugged in
initFile1()
initFile2()
initFile3()