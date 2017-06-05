from sqlalchemy import create_engine
from domestic import *
db_info = {
    'host': 'x',
    'port': 3306,
    'user': 'x',
    'passwd': 'x',
    'db': 'x'
}

engine=create_engine("mysql+pymysql://" + db_info['user'] + ":" + db_info['passwd'] + "@" + db_info['host'] + ":" + str(db_info['port']) + "/" + db_info['db'])
df = get_cffex_daily(date.today())
if df is not None:
    df.to_sql('cffex_daily', con=engine, if_exists='append', index=False)

