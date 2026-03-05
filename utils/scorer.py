def calculate_score(weights,evaluation):
  total_score=0
  for factor,weight in weights.items():
    score=evaluation.get(factor,0)
    total_score+=score*weight
  return total_score
  
  
