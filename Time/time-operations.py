# some time operations.
import time;

# time method gives the number of ticks since 10:00 am, January 1, 1970. (epoch)
print(time.time());

# gives the current time in a time tuple.
print(time.localtime());

# asctime will give the time in a readable format, so if we provide the current time in time tuple 
# to the asctime, it will get the current time in a readable format.
print(time.asctime(time.localtime()));

# time.clock is more accruate than time.time in providing time calculations. 
# although, it also measures ticks since epoch.
startTime = time.clock();
time.sleep(1);
difference = time.clock() - startTime;
print('slept for', difference, 'seconds'); # The difference will vary to certain proportions on each run.

# converts time since epoch in seconds to local time, 
# if no input time provided, takes the value from time.time()
print(time.ctime());

# converts time since epoch in seconds to UTC tuple time, 
# if no input is provided output from time.time is used.
print(time.gmtime());

# makes or forms a time value. year = 2017, month = 9, day = 20, hour,min,sec = 0, dayofweek = 2, 
# dayofyear = 263, daylightsavings = 0.
birthdayTimeTuple = (2017, 9, 20, 0, 0, 0, 2, 263, 0);
birthdayTimeSeconds = time.mktime(birthdayTimeTuple);
birthdayTimeStructure = time.localtime(birthdayTimeSeconds);
birthdayTime = time.asctime(birthdayTimeStructure); 

print('My birthday is on:', birthdayTime);