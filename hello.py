def add(x,y):
    return x+y

result = add(1,2)

print("This is the sum: " + str(1) + " " + str(2) + " " + str(result))

#import boto3
import os

try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []
    
print(user_paths)