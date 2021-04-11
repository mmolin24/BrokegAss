def hyperLink(address):
    if(address[0] == '&'):
        return "sad"

    addressSplit = address.split()
    stringDirection = addressSplit[0]

    for i in range(1,len(addressSplit)):
        if addressSplit[i] != '&':
            stringDirection += "+" + addressSplit[i]
        
    hyperLinkCreated = "https://www.google.com/maps/dir/?api=1&origin=Your+location&destination=" + stringDirection + "&travelmode=driving"

    return hyperLinkCreated