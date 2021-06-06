from urllib.parse import urlunsplit

section = 3430765

year = 2020
unit = 3
level = 10

csd = {
    'scheme' : 'https',
    'netloc' : 'studio.code.org',
    'path'   : F'/s/csd{unit}-{year}/lessons/{unit}/levels/{level}',
    'query'  : F'section_id={section}',
    'params' : ''
}

print( urlunsplit([csd['scheme'], csd['netloc'], csd['path'], csd['query'], csd['params']]) )
