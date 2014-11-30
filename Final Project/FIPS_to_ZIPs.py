# requires "pip install requests"
# (or "sudo pip install requests")

import csv
import json
import requests

# when set to True, doesn't actually post anything
DEBUG = True

def _load_zip_to_fips():
    with open('zipctymap.json') as zips:
        data = zips.read()
    datas = {}
    # for some reason we have multiple dicts in the zipctymap.json file?
    dicts = data.split('}}')
    for d in dicts:
        if not d:
            continue

        di = json.loads(d + '}}')
        for key in di.keys():
            if datas.get(key) is None:
                datas[key] = di[key]
            else:
                print 'key collision on {}'.format(key)
                print datas[key]
                print di[key]

    return datas

def _get_fip_to_zip():
    zip_to_fips = _load_zip_to_fips()
    print len(zip_to_fips)
    fip_to_zip = {}

    # key is zip code
    for key, value in zip_to_fips.items():
        fip = value.get('fips')
        if fip_to_zip.get(fip) is None:
            fip_to_zip[fip] = [key]
        else:
            fip_to_zip[fip].append(key)

    return fip_to_zip

def _get_fips_to_county():
    fips_to_county = {}
    with open('area_titles.csv') as raw:
        reader = csv.reader(raw)
        # get rid of the five header rows
        for i in range(5):
            next = reader.next()
        for row in reader:
            fips_to_county[row[0]] = row[1]
    print len(fips_to_county)
    return fips_to_county

    
def _post_data(year, zip_code, income):
    if DEBUG:
        print "we would be posting {} {} {}".format(year, zip_code, income)
        reutrn
    url = 'http://bms-205.appspot.com/data'
    headers = {'content-type': 'application/json'}
    data = {
        'year': year,
        'zip_code': zip_code,
        'income': income
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)

    if not r.status_code == 200:
        print "THE ERRORZ IN THE POST, RETURNED CODE {}".format(r.status_code)
        print "{}, {}, {}".format(year, zip_code, income)


def _get_files_to_upload():
    to_look_at = []

    return ['2013/2013_mapreduce_aggregate.csv']
    list_of_years = range(1990, 2015)
    for year in list_of_years:
        to_look_at.append('{}/{}_mapreduce_aggregate.csv'.format(year, year))

    return to_look_at


def _open_and_upload_file(filename, fips_to_zips):
    year = filename[0:4]
    with open(filename, 'rb') as raw_data, open('test.csv', 'wb') as output:
        reader = csv.reader(raw_data)
        writer = csv.writer(output, delimiter=' ', lineterminator='\n')
        # read off the header
        header = reader.next()
        missed = []
        hit = 0
        for row in reader:
            # FIPS_CODE Weekly_Wage Total_Wages Establishment_Count Employment_Level
            zips = fips_to_zips.get(row[0])
            if not zips:
                missed.append(row[0])
            else:
                hit += 1
                row[0] = ",".join(zips)
                writer.writerow(row)
        print len(missed)
        print missed
        print hit


def _parse_and_upload_files(file_list, fips_to_zips):
    for filename in file_list:
        _open_and_upload_file(filename, fips_to_zips)


if __name__ == '__main__':
    #fips_to_zips = _get_fip_to_zip()
    fips_to_county = _get_fips_to_county()
    files = _get_files_to_upload()
    _parse_and_upload_files(files, fips_to_county)

