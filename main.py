import requests
import time
import copy
import pandas as pd
from functions import get_notes
from constants import HEADERS_TN, PARAMS_TN, HEADERS_LANACION, PARAMS_LANACION, HEADERS_INFOBAE

def get_tn():
    with requests.Session() as session:
        session.headers = HEADERS_TN
        for n_page in range(1, 20):
            time.sleep(1)
            print(n_page)
            new_parameter = copy.copy(PARAMS_TN)
            new_parameter['query'] = new_parameter['query'].replace('N_PAGE', str(n_page))
            session.params = new_parameter
            new_df, news_condition = get_notes(session, 'tn')
            if n_page == 1:
                tn = copy.copy(new_df)
            else:
                tn = pd.concat([tn, new_df])

            if news_condition == False:
                break

def get_infobae():
    with requests.Session() as session:
        session.headers = HEADERS_INFOBAE
        time.sleep(1)
        new_df, news_condition = get_notes(session, 'infobae')
        infobae = copy.copy(new_df)

def get_lanacion():
    with requests.Session() as session:
        session.headers = HEADERS_LANACION
        for n_page in range(1, 20):
            time.sleep(1)
            print(n_page)
            new_parameter = copy.copy(PARAMS_LANACION)
            new_parameter['query'] = new_parameter['query'].replace('N_PAGE', str(n_page))
            session.params = new_parameter
            new_df, news_condition = get_notes(session, 'lanacion')
            if n_page == 1:
                lanacion = copy.copy(new_df)
            else:
                lanacion = pd.concat([lanacion, new_df])

            if news_condition == False:
                break


if __name__ == '__main__':
    get_tn()