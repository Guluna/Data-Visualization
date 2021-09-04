import pandas as pd
import griddb_python as griddb

# default connection values for GridDB
default_host = '239.0.0.1'
default_port = 31999
default_cluster_name = 'defaultCluster'
default_username = 'admin'
default_password = 'admin'

factory = griddb.StoreFactory.get_instance() 
# Initialize container
try:
	gridstore = factory.get_store(host=default_host, port=default_port, 
            cluster_name=default_cluster_name, username=default_username, 
            password=default_password)

	col = gridstore.get_container("TED_Data_5")
	col.set_auto_commit(False)	
	query = col.query("SELECT *")
	rowset = query.fetch(True)	
	df = pd.DataFrame(list(rowset), columns=rowset.get_column_names())
	print(df.head())
	print(df.dtypes)
	print(len(df))		


except griddb.GSException as e:
	for i in range(e.get_error_stack_size()):
		print("[", i, "]")
		print(e.get_error_code(i))
		print(e.get_location(i))
		print(e.get_message(i))
