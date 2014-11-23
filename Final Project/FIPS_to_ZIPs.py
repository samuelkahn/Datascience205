# requires "pip install request"
# (or if you are a noob and have your environment totally ****ed
#	"sudo pip install request")
import json
import request

# when set to True, doesn't actually post anything
DEBUG = True

def _build_up_fips_to_zips_dict():
	fips_to_zips = {}
	first_pairs = _get_pairs_from_file('asdf.txt')
	second_pairs = _get_pairs_from_file('asdf2.txt')
	for pair in first_pairs + second_pairs:
		fips = pair[0]
		zip_code = pair[1]
		if fips_to_zips.get(fips):
			print 'warning, multiple zipcodes for one fips'
			fips_to_zips[fips].append(zip_code)
			print '{} {}'.format(fips, fips_to_zips[fips])
		else:
			fips_to_zips[fips] = zip_code

def _get_pairs_from_file(filename):
	pairs = []
	with open(filename) as fz:
		for line in fz:
			zip_code = line[:5]
			state = line[23:25]
			fips = line[25:28]
			county = line[28:]
			pairs.append((fips, zip_code))


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
	
	list_of_years = range(1990, 2015)
	for year in list_of_years:
		to_look_at.append('{}/{}_output.txt'.format(year, year))

	return to_look_at

JOINER = ' '
def _open_and_upload_file(filename, fips_to_zips):
	year = filename[0:4]
	with open(filename) as raw_data:
		for line in raw_data:
			fips, income = raw_data.split(JOINER)
			zip_code = fips_to_zips.get(fips)
			if fips is None:
				print 'OMG NONE WE ARE SCREWED'
				print fips
				continue
			_post_data(year, zip_code, income)


def _parse_and_upload_files(file_list, fips_to_zips):
	for filename in file_list:
		_open_and_upload_file(filename, fips_to_zips)


if __name__ == '__main__':
	fips_to_zips = _build_up_fips_to_zips_dict()
	files = _get_files_to_upload()

