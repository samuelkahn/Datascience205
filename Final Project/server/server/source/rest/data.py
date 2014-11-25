import json
import logging

from google.appengine.ext import ndb

from lib.bottle import get, post, request, response, delete

from models import Data

@get('/data/:year/:zip')
def get_year_zip(year, zip):
    logging.info("Getting all comments!")
    datas = Data.query().filter(Data.year == year).filter(Data.zip == zip).fetch()
    to_return = [data.to_json for data in datas]
    response.content_type = 'application/json'
    return json.dumps(to_return)

@delete('/data/:year/:zip')
def delete_year_zip(year, zip):
    logging.debug('deleting year zip')
    data_keys = Data.query().filter(Data.year == year).filter(Data.zip == zip).fetch(keys_only=True)
    logging.debug('delting {}'.format(len(data_keys)))
    ndb.delete_multi(data_keys)


@post('/data/')
def create_new_data():
    logging.info("creating new data")
    logging.info(request.json)
    data = Data(
        year=request.json.get('year'),
        income=request.json.get('income')
    )
    data.put()
    response.content_type = 'application/json'
    return data.to_json()