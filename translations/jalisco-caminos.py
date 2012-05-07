def filterTags(attrs):
    if not attrs: return

    tags = {}

    # Use DESTINO attribute for destination
    if attrs['DESTINO']:
        tags.update({'destination':attrs['DESTINO']})

    # Use FUENTE attribute for source
    if attrs['FUENTE']:
        tags.update({'source':attrs['FUENTE']})

    # Depending on the value of the ADMINISTRA and CONDICION, set the highway= and construction= tags
    # source: http://wiki.openstreetmap.org/wiki/WikiProject_Mexico
    if attrs['ADMINISTRA'] == 'Federal' and attrs['CONDICION'] == 'En operacin':
        tags.update({'highway':'construction'})
        tags.update({'construction':'primary'})
    
    elif attrs['ADMINISTRA'] == 'Federal' and attrs['CONDICION'] != 'En operacin':
        tags.update({'highway':'primary'})

    elif attrs['ADMINISTRA'] == 'Estatal' and attrs['CONDICION'] == 'En operacin':
        tags.update({'highway':'construction'})
        tags.update({'construction':'secondary'})

    elif attrs['ADMINISTRA'] == 'Estatal' and attrs['CONDICION'] != 'En operacin':
            tags.update({'highway':'secondary'})

    elif attrs['ADMINISTRA'] == 'Municipal' and attrs['CONDICION'] == 'En operacin':
        tags.update({'highway':'construction'})
        tags.update({'construction':'tertiary'})

    elif attrs['ADMINISTRA'] == 'Municipal' and attrs['CONDICION'] != 'En operacin':
        tags.update({'highway':'tertiary'})

    # Use RECUBRIMIE for surface= tags
    # source: http://wiki.openstreetmap.org/wiki/Key:surface
    if attrs['RECUBRIMIE'] == 'Empedrado':
        tags.update({'surface':'paved'})

    elif attrs['RECUBRIMIE'] == 'Revestido':
        tags.update({'surface':'paving_stones'})

    elif attrs['RECUBRIMIE'] == 'Sin revestimiento':
        tags.update({'surface':'unpaved'})

    #print "foo!"
    return tags
    #sys.exit()
