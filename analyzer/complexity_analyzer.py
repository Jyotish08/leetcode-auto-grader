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
