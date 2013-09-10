# This file is part of victims-web-proxy.
#
# Copyright (C) 2013 The Victims Project
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from time import mktime, gmtime

from CodernityDB.database_super_thread_safe import (
    SuperThreadSafeDatabase as Database)
from CodernityDB.tree_index import TreeBasedIndex


class CacheIndex(TreeBasedIndex):

    def __init__(self, *args, **kwargs):
        kwargs['node_capacity'] = 13
        kwargs['key_format'] = 'I'
        super(TreeBasedIndex, self).__init__(*args, **kwargs)

    def make_key_value(self, data):
        a_val = data.get('date')
        if a_val is not None:
            return a_val, None
        return None

    def make_key(self, key):
        return key


class CacheDatabase():
    _index_key = 'date'

    def __init__(self, path):
        self.db = Database(path)
        if not self.db.exists():
            index = CacheIndex(self.db.path, self._index_key)
            self.db.create()
            self.db.add_index(index)
        else:
            self.db.open()

    def insert(self, date, record):
        self.db.insert(dict(date=date, record=record))

    def insert_all(self, records):
        now = mktime(gmtime())
        for record in records:
            self.insert(now, record)

    def since(self, date):
        return self.db.get_many(
            self._index_key, limit=-1, inclusive_start=False, with_doc=True,
            start=date
        )
