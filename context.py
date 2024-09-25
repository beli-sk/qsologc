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
from command_interface import CommandError
from utils import *


class QSO(object):
    def __init__(self, callsign=None):
        self.callsign = callsign
        self.info = None

    def __str__(self):
        return "QSO({}, {})".format(self.callsign, self.info)


class Context():
    """The Context object holds the application context - all in-memory
    state of the application."""
    def __init__(self):
        self.qsos = {}
        self.current_index = None

    def add_qso(self, qso):
        for i in range(1, 1000):
            if i not in self.qsos:
                self.qsos[i] = qso
                self.current_index = i
                return i
        else:
            Exception('run out of QSO indexes')

    def remove_qso(self, index):
        del(self.qsos[index])
        if index == current_index:
            current_index = None

    def find_qso(self, callsign):
        for i, qso in self.qsos.items():
            if qso.callsign == callsign:
                return i, qso
        else:
            return CommandError('QSO "{}" not found'.print(callsign))

