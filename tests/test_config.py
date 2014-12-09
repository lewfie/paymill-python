__author__ = 'yalnazov'

api_key = '20a690e5283cd3419629a42cc8631193'
magic_token = '098f6bcd4621d373cade4e832627b4f6'


def get_next_amount():
    import time
    return int(str(time.time()).replace('.',''))