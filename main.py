import json
from utils.scorer import calculate_score
from llm.evaluator import evaluate_code
from storage.excel_writer import save_result
from analyzer.complexity_analyzer import count_loops
from analyzer.complexity_analyzer import estimate_complexity
from analytics.progress_report import generate_report
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
loops=count_loops(code)
print("Loop detected:",loops)
recursion = detect_recursion(code)
print("recursion detected:",recursion)
complexity = estimate_complexity(loops,recursion)
print("Estimated complexity", complexity)
print("evaluation:",evaluation)
print("Final score:",score)
save_result(problem,score,evaluation)
generate_report()


