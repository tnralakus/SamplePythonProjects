__author__ = 'alakus'

import random

class Account:
    def __init__(self, customer_id, account_type):
        self.account_id = random.randint(100, 999)
        self.customer_id = customer_id
        self.account_type = account_type