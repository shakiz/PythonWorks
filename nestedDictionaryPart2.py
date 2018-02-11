log={'Shakil':{'username':'shakil335','pass':'shakil123'},
     'Sagor':{'username':'sagor09','pass':'sagor123'},
     'Rashed':{'username':'rashed05','pass':'rashed123'},
     'Faisal':{'username':'faisal16','pass':'faisal123'},
     'Touhid':{'username':'touhid33','pass':'touhid123'}}

print(log)

for k,v in log.items():
    print('Key :',k,' Value :',v)

for i in log.keys():
    print('Values are : ',log[i])

for i in log.keys():
    print('User name : ',log[i]['username'])

for i in log.keys():
    print('Password : ',log[i]['pass'])
