import ast
def count_loop(code):
  tree = ast.parse(code)
  loop_count = 0
  for node in ast.walk(tree):
    if isinstance(node,(ast.For,ast.While)):
      loop_count += 1
  return loop_count
