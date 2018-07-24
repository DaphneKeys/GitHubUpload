import openpyxl,pprint #pprint to print the final county data
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx') #opens the censuspopdata.xlsx file
sheet = wb['Population by Census Tract'] #get sheet with census data 
countyData = {}

#Fill in countyData with each county's population and tracts.
print('Reading rows...')
for row in range(2, sheet.max_row+1): #iterating starting from 2 to the end+1
    #Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value #the value of B(number) -state
    county = sheet['C' + str(row)].value #the value of C(number) - county
    pop = sheet['D' + str(row)].value #the value of D(number) - pop

    # Make sure the key for this state exists.
    countyData.setdefault(state, {}) #{'AL': None, 'AK': None,.....}
    # Make sure the key for this county in this state exists.
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0}) #{'Autauga': {'tracts': 0, 'pop': 0}}.....

    # Each row represents one census tract, so increment by one.
    countyData[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tract.
    countyData[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of countyData to it.
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')
