#!/usr/bin/env python3
#
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
import sys
import readline

from context import *
from command_interface import command_interface
import commands


command_interface.set_context(Context())
finished = False
while not finished:
    command_line = input('> ')
    command_interface.run(command_line)

