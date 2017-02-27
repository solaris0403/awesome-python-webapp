#!/usr/bin/env python
# -*- coding: utf-8 -*-
from www.transwarp import db

db.create_engine(user='root', password='password', database='test', host='127.0.0.1', port=3306)
