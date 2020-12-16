# Generate list of two-line elements (TLEs) for spacecraft within STK
def genTLE(numPlanes, satsPerPlane):
    incW = 360 / satsPerPlane
    # Set equal RAAN spacing
    incRAAN = 360 / numPlanes
    RAAN = 0

    p1 = open("const.tce", "w+")

    for j in range(numPlanes):
        w = 0
        # Take RAAN to 4 decimal places
        RAANdec = format(RAAN, ".4f")
        # Cast RAAN to 8-char string
        RAANstr = str(RAANdec).rjust(8, ' ')
        for i in range(satsPerPlane):
            # Pad ID to give it length of 5
            spacecraftID = str(i + 66*j).rjust(5, '0')
            # Create name for unclassified spacecraft
            IDU = spacecraftID + 'U'
            # Take perigee to 4 decimal places
            wdec = float("{0:.4f}".format(w))
            # Cast perigee to 8-char string
            wstr = str(wdec).ljust(8, '0')
            # Replace with first line of TLE report in STK scenario
            l1 = "<PUT_LINE1_HERE>\n" % (IDU)
            # Replace with second line of TLE report in STK scenario
            l2 = "<PUT_LINE2_HERE>\n" % (spacecraftID, RAANstr, wstr)

            # Note: Remember to change second, fourth, and seventh fields of TLE rpeort to %s
            p1.write(l1)
            p1.write(l2)

            w += incRAAN

        p1.close()

# Change for each constellation shell
genTLE(20, 20)