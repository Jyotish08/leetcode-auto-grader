import json
from utils.scorer import calculate_score
from llm.evaluator import evaluate_code
from storage.excel_writer import save_result
print("Leetcode auto grader started")
with open("config/grading_schema.json")as
file:
  weights = json.load(file)
print("Enter problem name:")
print("When finished type END on a new line.")
lines=[]
while True:
  line=input()
  if line=='END':
    break
  lines.append(line)
code"\n".join(lines)
evaluation = evaluate_code(problem,code)
score=calculate_score(weights,evaluation)
print("evaluation:",evaluation)
print("Final score:",score)
save_result(problem,score,evaluation)
