import json
import pickle
import numpy as np

__location = None
__data_columns = None
__model = None


# noinspection PyBroadException
def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_idx = __data_columns.index(location.lower())
    except:
        loc_idx = -1

    i = np.zeros(len(__data_columns))
    i[0] = sqft
    i[1] = bath
    i[2] = bhk
    if loc_idx >= 0:
        i[loc_idx] = 1
    return round(__model.predict([i])[0], 2)


def get_location():
    return __location


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __location
    global __model

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]
    with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location())
    # print(get_estimated_price('Indira Nagar', 1000, 3, 3))