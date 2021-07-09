from faker import Faker
from collections import namedtuple
import random, string
import datetime
fake = Faker()
from time import perf_counter
from session9 import *


r=random_profiles()

r1 = random_profiles_nt()

def test_nt_largest_boold_group():
    assert (type(r1.largest_bloodgroup()) is str),"something is wrong. please check the code"

def test_nt_mean_cur_location():
    assert (r1.mean_location()[0]!=0),"something is wrong. please check the code"

def test_nt_oldest_person_age():
    assert (r1.oldest_person()>0),"something is wrong. please check the code"

def test_nt_avg_age():
    assert (r1.average_age()>0),"something is wrong. please check the code"


def test_largest_boold_group():
    assert (type(r.largest_bloodgroup()) is str),"something is wrong. please check the code"

def test_mean_cur_location():
    assert (r.mean_location()[0]!=0),"something is wrong. please check the code"

def test_oldest_person_age():
    assert (r.oldest_person()>0),"something is wrong. please check the code"

def test_avg_age():
    assert (r.average_age()>0),"something is wrong. please check the code"


def test_named_tuple_exec_speed():
    start = perf_counter()
    r1.largest_bloodgroup()
    end=perf_counter()
    elapsed_nt = end - start

    start = perf_counter()
    r.largest_bloodgroup()
    end=perf_counter()
    elapsed = end - start

    assert (elapsed_nt<elapsed),"something is wrong. please check the code"


