# qsologc - Ham radio log with command line interface
# Copyright (C) 2018 Michal Belica https://beli.sk
#
# This file is part of qsologc.
#
# qsologc is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qsologc is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see https://www.gnu.org/licenses/
#
import redis
import logging

from pyhamtools import LookupLib, Callinfo

from localsettings import clublog_api_key
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

r = redis.Redis()
lookuplib = LookupLib(lookuptype="redis", redis_instance=r, redis_prefix="CF")
#lookuplib = LookupLib(lookuptype="redis", redis_instance=r, redis_prefix="CLX", logger=logger)

def refresh_db():
    lookuplib = LookupLib(lookuptype="countryfile")
    lookuplib.copy_data_in_redis(redis_instance=r, redis_prefix="CF")
    #lookuplib = LookupLib(lookuptype="clublogxml", apikey=clublog_api_key)
    #lookuplib.copy_data_in_redis(redis_instance=r, redis_prefix="CLX")

def lookup_callsign(callsign):
    cic = Callinfo(lookuplib)
    #cic2 = Callinfo(lookuplib2)
    return [cic.get_all(callsign)] #, cic2.get_all(callsign)]
