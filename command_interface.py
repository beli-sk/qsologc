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
import shlex


class CommandError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "Error: {}".format(self.msg)


class Command(object):
    pass


class CommandInterface(object):
    """CLI based user interface running commands working with the context."""
    def __init__(self):
        self.context = None
        self.commands = dict()

    def set_context(self, context):
        self.context = context

    def register(self, command):
        for a in command.aliases:
            print("registering alias {}".format(a))
            self.commands[a] = command

    def run(self, command_line):
        c = shlex.split(command_line)
        try:
            index = int(c[0])
            c.pop(0)
        except ValueError:
            index = None
            pass
        command = c[0]
        try:
            args = c[1:]
        except IndexError:
            args = []
        if index is not None:
            self.context.current_index = index
        if command in self.commands:
            try:
                self.commands[command].run(index, args, self.context)
            except CommandError as e:
                print(e)
        else:
            print("Error: command not found")


command_interface = CommandInterface()
