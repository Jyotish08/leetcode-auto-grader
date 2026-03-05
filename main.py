import json
print("Leetcode auto grader started")
with open("config/grading_schema.json")as
file:
  weights = json.load(file)
print("Scoring weights:")
for factor,value in weigts.items():
  print(factor,"=",value)
