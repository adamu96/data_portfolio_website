import pandas as pd
import sqlalchemy

database = 'qardio'
host = '127.0.0.1'
user = 'root'
password = 'Party100'
url = f'mysql+mysqlconnector://{user}:{password}@{host}/{database}'
engine = sqlalchemy.create_engine(url, echo=True)
conn = engine.connect()

# query database
existing_data = pd.read_sql(sql='SELECT * FROM email_data;', con=conn)

# add data to database
new_data = pd.read_csv('/Users/adamurquhart/data/qardio_data.csv')

new_data.columns = new_data.columns.str.strip()
new_data.columns = new_data.columns.str.replace(" ", '')
new_data.columns = new_data.columns.str.lower()

clean_data = pd.concat([existing_data, new_data])
clean_data = clean_data.drop_duplicates(subset='tracking_id')
clean_data = clean_data.drop(columns=['index', 'unnamed:0'])

clean_data.to_sql(name='email_data',
          con=conn,
          dtypes={
              'tracking_id': 'VARCHAR(20)'
          },
          if_exists='replace')


# github_access_token = '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'