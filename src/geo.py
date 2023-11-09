def getBoundingCoords(victoriaOnly = True): 
    if victoriaOnly:
        # Box around Victoria (coordinates found using https://boundingbox.klokantech.com/)
        return [[140.53, 150.03],[-39.20, -33.73]]
    else:
        # Box around Australia
        return [[106.3, 160.8],[-44.2,  -8.9]]
