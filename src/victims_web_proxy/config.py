from os.path import join


DATABASE_DIR = '/tmp/'
DATABASE_NAME_FORMAT = 'victims.%s.db'

UPDATES_DATABASE = join(DATABASE_DIR, DATABASE_NAME_FORMAT % ('updates'))
REMOVES_DATABASE = join(DATABASE_DIR, DATABASE_NAME_FORMAT % ('removes'))
