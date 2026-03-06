import ast
def count_loop(code):
  tree = ast.parse(code)
  loop_count = 0
  for node in ast.walk(tree):
    if isinstance(node,(ast.For,ast.While)):
      loop_count += 1
  return loop_count
def detect_recursion(code):
  tree = ast.parse(code)
  for node in ast.walk(tree):
    if isinstance(node,ast.FunctionDef):
      function_names.append(node.name)
  for node in ast.walk(tree):
    if isinstance(node,ast.Call):
      if isinstance(node.func,ast.Name):
        if node.func.id in function_names:
          return True
  return False
def  estimate_complexity(loop_count,recursion):
  a=loop_count
  b=recursion
  if a ==0 and not b:
    return "O(1)"
  if a == 1 and not b:
    return "O(n)"
  if a==2:
    return "O(n^2)"
  if b and a ==0:
    return "O(n) or O(log(n))"
  if b and a >=1:
    return "O(n*recursion)"
  return "unknown"

