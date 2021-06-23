import json
import pickle
import numpy as np
import os
import sys

__model = None
__cols = None

def load():
  global __model
  global __cols

  with open(os.path.join(sys.path[0],"model_real_estate.pickle"), "rb") as f:
    __model = pickle.load(f)

  with open(os.path.join(sys.path[0],"columns.json"), "r") as f:
    __cols = json.load(f)["data_columns"]


def get_locations():
  load()
  return __cols[4:len(__cols)-5]

def get_area_types():
  return __cols[len(__cols)-4:]



def predict_prices(location, area, total_sqft, bedrooms, bathrooms, balcony):

  x  = np.zeros(len(__cols))
  x[0] = bedrooms
  x[1] = total_sqft
  x[2] = bathrooms
  x[3] = balcony
  # location = "location_"+(location.lower())
  area = "area_type_"+(area.lower())

  try:
    idx = __cols.index(location)
    x[idx] = 1

  except :
     x[len(x)-5] = 1

  try:
    idx = __cols.index(area)
    x[idx] = 1

  except:
    None
  
  x = x.reshape((1,x.shape[0]))
  return round(__model.predict(x)[0],2)


if __name__ == "__main__":
  print(get_locations())
  print(get_area_types())
  # print(predict_prices("1st block jayanagar", "super built-up  area", 1000, 2,2,2))