"""
Summarize data will read the data out of the zip files and combine it on FIPS
"""

import csv

from utils import peek_print_dict

WEEKLY_WAGE = 'weekly_wage'
TOTAL_WAGES = 'total_wages'
ESTABLISHMENT_COUNT = 'establishment_count'
EMPLOYMENT_LEVEL = 'employment_level'
FIELDS = [WEEKLY_WAGE, TOTAL_WAGES, ESTABLISHMENT_COUNT, EMPLOYMENT_LEVEL]


def summarize_data():
    summary = _build_summarize_data()
    _combine_names(summary)
    # looks at the first 10 entries
    #peek_print_dict(summary)
    return summary


def _build_summarize_data():
    files = _get_file_names()
    summary = {}
    for year, file_name in files:
        data = _jsonize_file(file_name)
        if year == 1990:
            for key, value in data.items():
                summary[key] = {
                    WEEKLY_WAGE: [value[0]],
                    TOTAL_WAGES: [value[1]],
                    ESTABLISHMENT_COUNT: [value[2]],
                    EMPLOYMENT_LEVEL: [value[3]]
                }
        else:
            hit = 0
            miss = 0
            for key, value in data.items():
                if summary.get(key):
                    hit += 1
                    for idx, val in enumerate(FIELDS):
                        summary[key][val].append(value[idx])
                else:
                    # print 'miss on {}'.format(key)
                    miss += 1
            print 'our miss hit for adding data from year {} is {}/{}'.format(year, miss, hit)
    return summary


def _combine_names(summary_data):
    fip_to_name = _get_fips_to_county_name()
    hit = 0
    miss = 0
    for key, val in fip_to_name.items():
        if summary_data.get(key):
            hit += 1
            summary_data[key]['name'] = val
        else:
            #print 'did not find county {} {}'.format(key, val)
            miss += 1
    print 'our miss/hit count for matching names is {}/{}'.format(miss, hit)




def _get_file_names():
    to_look_at = []

    list_of_years = range(1990, 2015)
    for year in list_of_years:
        to_look_at.append('../{}/{}_mapreduce_aggregate.csv'.format(year, year))

    return zip(range(1990, 2015), to_look_at)


def _get_fips_to_county_name():
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



def _jsonize_file(file_name):
    print 'looking at {}'.format(file_name)
    with open(file_name) as data:
        reader = csv.reader(data)
        header = reader.next()
        data = {}
        for row in reader:
            if not data.get(row[0]):
                data[row[0]] = row[1:]
            else:
                print 'collision on {}!'.format(row[0])
        return data

if __name__ == '__main__':
    summarize_data()
