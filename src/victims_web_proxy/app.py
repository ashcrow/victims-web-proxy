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

from victims_web_proxy import config
from victims_web_proxy.database import CacheDatabase


def main():
    updates = CacheDatabase(config.UPDATES_DATABASE)

    record = {'fields': {'cves': "CVE-2012-2012"}}

    updates.insert_all([record])

    for curr in updates.since(1378784580.0):
        if 'record' in curr['doc']:
            print(curr['doc']['record'])


if __name__ == '__main__':
    main()
