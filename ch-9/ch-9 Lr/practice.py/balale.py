name = ['aman', 'raghav', 'anchal', 'puja', 'aman', 'rghav',]

uniqe_name_set = set(name)
uniqe_name_tuple = tuple(uniqe_name_set)

name_lenght ={}
for name in uniqe_name_tuple:
      name_lenght[name] =len(name)

import time
second_in_hour = 60*60*60

print("origenal list", name)
print("uniqe tuple",uniqe_name_tuple)
print("name of length", name_lenght)
print("second in hour:",second_in_hour)