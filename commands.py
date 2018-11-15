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
from command_interface import *
from context import *


class QSOCommand(Command):
    aliases = ('qso', 'o')
    def run(self, index, args, context):
        if len(args) == 0:
            callsign = None
        elif len(args) == 1:
            callsign = args[0].upper()
        else:
            raise CommandError('wrong number of arguments')
        qso = QSO(callsign)
        index = context.add_qso(qso)
        print("new {} {}".format(index, qso))


class ListCommand(Command):
    aliases = ('list', 'l')
    def run(self, index, args, context):
        if context.qsos:
            for i, qso in sorted(context.qsos.items()):
                if context.current_index == i:
                    mark = "*"
                else:
                    mark = ""
                print("{}{} {}".format(i, mark, qso))
        else:
            print("No active QSOs")


class CloseCommand(Command):
    aliases = ('close', 'c')
    def run(self, index, args, context):
        if index is None and len(args) == 1 and args[0]:
            i, qso = context.find_qso(args[0].upper())
            context.remove_qso(i)
            print("QSO {} removed".format(qso))
        elif context.current_index is not None:
            i = context.current_index
            qso = context.qsos[i]
            context.remove_qso(i)
            print("QSO {} removed".format(qso))
        else:
            raise CommandError('No QSO selected')


class DownloadDBCommand(Command):
    aliases = ('download',)
    def run(self, index, args, context):
        refresh_db()


command_interface.register(QSOCommand())
command_interface.register(ListCommand())
command_interface.register(CloseCommand())
command_interface.register(DownloadDBCommand())
