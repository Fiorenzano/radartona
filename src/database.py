import psycopg2 as db
import pandas as pd
import pandas.io.sql as psql

db_user = 'mobilab'
db_passwd='mobilab'
db_host='192.168.167.44'
db_port='5432'
db_name='hackatona'


def connect_table():
    connection = db.connect(user=db_user,password=db_passwd,host=db_host,port=db_port,database=db_name)
    #df = psql.frame_query("SELECT * FROM test WHERE id > 0", connection)
    df = pd.read_sql_query("SELECT * FROM base_radares", con=connection)
    print(df)
    for index, row in df.iterrows():

       # 6742 - 6743 - 6796 - 6797
        codigo = row['codigo']
      #  codigos = coords.replace(" ","").split("-")



        df = pd.read_sql_query("select sum(autuacoes) from radar.contagens where localidade = " + codigo, con=connection)
        print(df['sum'])
    
    df.to_csv('radar_route.csv',index=False)
    
if __name__ == '__main__':
    connect_table()

def get_radares():
    connection = db.connect(user=db_user,password=db_passwd,host=db_host,port=db_port,database=db_name)
    df = pd.read_sql_query("SELECT * FROM base_radares where latitude_l is not null and ligado = 1", con=connection)
    df.to_csv('radares.csv')
    return df
