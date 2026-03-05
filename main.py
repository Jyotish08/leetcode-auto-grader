import json
from utils.scorer import calculate_score
print("Leetcode auto grader started")
with open("config/grading_schema.json")as
file:
  weights = json.load(file)
print("Scoring weights:")
evaluation={
  "correctness":0.9,
  "edge_case":0.8,
  "time_complexity":0.7,
  "space_complexity":0.8,
  "runtime":0.9,
  "constraint_awareness":0.7,
  "code_quality":0.8,
  "algorithmic_insight":0
}
score=calculate_score(weights,evaluation)
print("Final score:",score)
