#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from peewee import *
from cfg import *

db_proxy = Proxy()
# DB Models
class Inst(Model):
    id = PrimaryKeyField()
    key = CharField(unique=True) # instagram profile
    time = IntegerField(null=True) # time

    class Meta:
        database = db_proxy

# Connect to DB
db = PostgresqlDatabase(database=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASSWORD, host=DATABASE_HOST)
db_proxy.initialize(db)
db_proxy.connect()
db_proxy.create_tables([Inst], safe=True)