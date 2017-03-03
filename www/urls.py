#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

import logging

from transwarp.web import get, view

from models import User, Blog, Comment

# @view('test_users.html')
# @get('/')
# def test_users():
#     users = User.find_all()
#     return dict(users=users)

import os, re, time, base64, hashlib, logging

from transwarp.web import get, post, ctx, view, interceptor, seeother, notfound

from models import User, Blog, Comment

@view('blogs.html')
@get('/')
def index():
    blogs = Blog.find_all()
    user = User.find_first('where email=?', 'admin@example.com')
    return dict(blogs=blogs, user=user)
