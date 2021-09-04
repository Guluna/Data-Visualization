import pandas as pd
import griddb_python as griddb

# default connection values for GridDB
default_host = '239.0.0.1'
default_port = 31999
default_cluster_name = 'defaultCluster'
default_username = 'admin'
default_password = 'admin'

# Create factor instance
factory = griddb.StoreFactory.get_instance()
print('Factor instance created....')

try:
	# Create gridstore instance
	gridstore = factory.get_store(host=default_host, port=default_port, 
            cluster_name=default_cluster_name, username=default_username, 
            password=default_password)
	print('Gridstore instance created....')

	# Provide container info
	conInfo = griddb.ContainerInfo("TED_Data_5",
                    [["comments", griddb.Type.LONG],
                    ["duration", griddb.Type.LONG],
                    ["num_speaker", griddb.Type.LONG], 
                    ["published_date", griddb.Type.LONG],
                    ["views", griddb.Type.LONG],
                    ["event", griddb.Type.STRING]],
                    griddb.ContainerType.COLLECTION, True)
	print('Container info complete....')

	cont = gridstore.put_container(conInfo)
	print('Container created....')

	# Change auto commit mode to false
	cont.set_auto_commit(False)

	ted_data = pd.read_csv('ted_main.csv', usecols=['comments', 'duration', 'num_speaker', 'published_date', 'views', 'event'])

	for i,row in ted_data[['comments', 'duration', 'num_speaker', 'published_date', 'views', 'event']].iterrows():
		print('Inserting record: {}'.format(i))
		ret = cont.put(row.values.tolist())
		print("Status: {}".format(ret))
	
	cont.commit();
	print("Data added successfully")


except griddb.GSException as e:
	for i in range(e.get_error_stack_size()):
		print("[", i, "]")
		print(e.get_error_code(i))
		print(e.get_location(i))
		print(e.get_message(i))

