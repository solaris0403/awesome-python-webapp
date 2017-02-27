#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging


logging.basicConfig(filename='logger.log', level=logging.INFO)
logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')