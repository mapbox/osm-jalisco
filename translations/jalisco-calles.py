def translateAttributes(attrs):
    if not attrs: return

    tags = {}

    # all rows for FUENTE are 'ITEJ' according the sample button (under Advanced serach) in QGIS that acts as a 'select distinct'
    tags.update({'source':'ITEJ'})

    # Use NOMBRE for name
    if attrs['NOMBRE']:
        tags.update({'name':attrs['NOMBRE']})

    # Use RECUBRIMIE for surface= tags
    # source: http://wiki.openstreetmap.org/wiki/Key:surface
    if attrs['RECUBRIMIE'] == 'Empedrado':
        tags.update({'surface':'paved'})

    elif attrs['RECUBRIMIE'] == 'Empedrado ahogado':
        tags.update({'surface':'cobblestone:flattened'})

    elif attrs['RECUBRIMIE'] == 'Adoqun':
        tags.update({'surface':'cobblestone'})

    elif attrs['RECUBRIMIE'] == 'Asfalto':
        tags.update({'surface':'asphalt'})

    elif attrs['RECUBRIMIE'] == 'Concreto hidrulico':
        tags.update({'surface':'concrete'})

    elif attrs['RECUBRIMIE'] == 'Losas de cemento':
        tags.update({'surface':'concrete:plates'})

    elif attrs['RECUBRIMIE'] == 'Terracera':
        tags.update({'surface':'unpaved'})

    #print "foo!"
    return tags
    #sys.exit()
