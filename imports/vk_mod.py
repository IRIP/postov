import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('create table t (id,a,b,c);')

conn.commit()
d = {0:[1.0,2.0,3.0]}
import itertools as it
c.execute('insert into t values (?,?,?,?)',[i for i in it.chain(d.keys(),*d.values())])

conn.commit()
results = c.execute('select * from t where id = 0').fetchall()
