import json
from utils.scorer import calculate_score
from llm.evaluator import evaluate_code
from storage.excel_writer import save_result
print("Leetcode auto grader started")
with open("config/grading_schema.json")as
file:
  weights = json.load(file)
problem=""" two sum problem """
code="""
def two_sum(nums,target):
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if nums[i]+nums[j] == target:
        return [i,j]
"""
evaluation = evaluate_code(problem,code)
score=calculate_score(weights,evaluation)
print("evaluation:",evaluation)
print("Final score:",score)
save_result(problem,score)
