# Citra IT - Excelência em TI
# Este script lê uma lista de IPs e retorna a quantidade de 
# IP's que fizeram correspondência com cada país encontrado.
# @author:  luciano@citrait.com.br
# @date:    2022-07-01 
# @version: 1.0
# @Usage: python geoquery.py

from operator import itemgetter
from geoip2.database import Reader
from geoip2.errors import AddressNotFoundError


# Path to binary geoip2lite database file
DB_BIN_PATH = r'GeoLite2\GeoLite2-Country.mmdb'

# Path to text file containing extracted ip addresses
IP_LIST_PATH = f'ips.txt'


# MAIN ROUTINE
if __name__ == '__main__':
    
    # open the text file and read all lines
    input_file = open(IP_LIST_PATH, "r")
    
    # open the binary geolite country database
    reader = Reader(DB_BIN_PATH)
    
    # make room to store queries
    query_results = {}
        
    for line in input_file.readlines():
        line = line.strip()
        
        # strip leftmost zero if present
        if line.startswith('0'):
            line = line[1:]
        
        # query ip on database and store country hit
        try:
            ip = reader.country(line)
            country_name = ip.country.names['en']
            if not country_name in query_results:
                query_results[country_name] =  1
            else:
                query_results[country_name] += 1
        except AddressNotFoundError:
            # if ip not found in database, ommit it.
            pass
            
    
    # close handles
    reader.close()
    input_file.close()
    
    # display results
    #print(f'=== DISPLAYING COUNTRY HITS BY IP COUNT ===')
    for country, hits in sorted(query_results.items(), key=itemgetter(1,0), reverse=True):
        print(f'{country}={hits}')
    
