def translateAttributes(attrs):
    if not attrs: return
    
    tags = {}
    
    # Use DESTINO attribute for destination
    if attrs['DESTINO']:
        tags.update({'destination':attrs['DESTINO']})
    
    # Use CODIGO for the ref tag, prepend "MEX" or "REF" according to road hierarchy
    if attrs['CODIGO'] != 'No aplicable' and attrs['CODIGO'] != 'No disponible':
        if attrs['ADMINISTRA'] == 'Federal':
			tags.update({'ref':'MEX%s'% attrs['CODIGO']})
		
        elif attrs['ADMINISTRA'] == 'Estatal':
			tags.update({'ref':'REF%s'% attrs['CODIGO']})

    # Use CARRILES for the lanes tags
    if attrs['CARRILES'] != 'No aplicable':
        tags.update({'lanes':attrs['CARRILES']})
    
    # Depending on the value of the ADMINISTRA and TRANSITO, set the highway= tag
    # source: http://wiki.openstreetmap.org/wiki/Mexico#Caracter.C3.ADsticas_f.C3.ADsicas
    if attrs['ADMINISTRA'] == 'Federal' and attrs['TRANSITO'] == 'Cuota' and int(attrs['CARRILES']) >= 4:
        tags.update({'highway':'motorway'})
        
    elif attrs['ADMINISTRA'] == 'Federal' and attrs['TRANSITO'] == 'Libre' and int(attrs['CARRILES']) >= 4:
        tags.update({'highway':'trunk'})
    
    elif attrs['ADMINISTRA'] == 'Federal' and attrs['TRANSITO'] == 'Libre' and int(attrs['CARRILES']) <= 2:
        tags.update({'highway':'primary'})
    
    elif attrs['ADMINISTRA'] == 'Estatal':
        tags.update({'highway':'secondary'})
    
    elif attrs['ADMINISTRA'] == 'Municipal':
        tags.update({'highway':'tertiary'})
    
    # surface tags from http://wiki.openstreetmap.org/wiki/Key:surface
    if attrs['PAVIMENTO'] == 'Asfalto':
        tags.update({'surface':'asphalt'})
        
    elif attrs['PAVIMENTO'] == 'Concreto hidrulico':
        tags.update({'surface':'concrete'})
   
    # all rows for FUENTE are 'ITEJ' according the sample button (under Advanced serach) in QGIS that acts as a 'select distinct'
    tags.update({'source':'ITEJ'}) 
    
    #print "foo!"
    return tags
    #sys.exit()


