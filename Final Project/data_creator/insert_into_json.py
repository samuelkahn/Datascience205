# from: http://bl.ocks.org/mbostock/4122298

from summarize_data import summarize_data

import json

from utils import peek_print_dict, peek_print_list

def _load_us_json():
    with open('../us.json') as us:
        return json.loads(us.read())


def _append_data(summary_data, counties):
    hit = 0
    miss = 0
    for county in counties:
        fips = county.get('id')
        if summary_data.get(str(fips)):
            county['properties'] = summary_data.get(str(fips))
            hit += 1
        else:
            # print 'could not find fips {} in our data'.format(fips)
            miss += 1
    print 'our hit/miss for matching our data into us_json is {}/{}'.format(miss, hit)


def main():
    summary = summarize_data()
    us_json = _load_us_json()
    counties = us_json.get('objects').get('counties').get('geometries')
    _append_data(summary, counties)
    with open('output.json', 'w') as test:
        test.write(json.dumps(us_json))



if __name__ == '__main__':
    main()
