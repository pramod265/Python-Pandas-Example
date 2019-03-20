import pandas as pd
import datetime


# path = "Sorted Connection Histories/"
# collection=['ConnectionList(1-50Meters).csv','ConnectionList(51-100Meters).csv',
# 'ConnectionList(101-150Meters.csv','ConnectionList(151-200Meters).csv']

# csv_data = None
# result = None
# for i in collection:
#   csv=pd.read_csv(path+i)
#   if result is None:
#     result = csv
#   else:
#     result = result.merge(csv, on='Sequence id')

# if result:
# 	result.to_csv('output2.csv',index=False)


csv_data = pd.read_csv("Sorted Connection Histories/ConnectionList(1-50Meters).csv")
final_data = {}
missing_date = []
done_meters = []
prev_date = None
skip_this_date = False
is_last_status  = "Connected"

for index, row in csv_data.iterrows():

	# print(index,"--",row["Sequence id"])
	# print(row)

	connection_status = row["Connection Status"]
	
	cur_meter = str(row["Meter"])
	date = datetime.datetime.strptime(row['Date in meter'], "%d-%m-%Y %H:%M").date()
	str_date = date.strftime('%d-%m-%Y')
	
	if index == 0:
		prev_date = date
	
	if cur_meter not in done_meters:
		done_meters.append(cur_meter)
		print(cur_meter,": ",missing_date) #------------THIS IS FOR PRINTING MISSING DATE ARRAY BEFORE END 
		missing_date = []
	else:
		final_data[cur_meter] = (missing_date)
	
	if prev_date != date:
		delta = date - prev_date
		if (delta.days) > 0:
			for i in range(delta.days - 1):
			    # print(prev_date + datetime.timedelta(i+1))
			    str_missing_date = (prev_date + datetime.timedelta(i+1)).strftime('%d-%m-%Y')
			    if is_last_status != "Connected":
			    	missing_date.append(str_missing_date)
		else:
			pass
	else:
		is_last_status = connection_status

	prev_date = date
	
	# if index > 3:
	# 	break




# print(final_data)