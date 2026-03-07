import csv
def generate_report():
  file_name="results.csv"
  scores=[]
  correctness_score=[]
  complexity_scores=[]
  quality_scores=[]
  try:
    with open(file_name,"r")as file:
      reader = csv.reader(file)
      for row in reader:
scores.append(float(row[2]))
correctness_score.append(float(row[3]))
complexity_scores.append(float(row[4]))
quality_scores.append(float(row[5]))
except FileNotFoundError:
  print("no result found yet.")
  return
total_problems=len(scores)
average_scores=sum(scores)/total_problems
avg_correctness=sum(correctness_score)/total_problems
avg_quality=sum(quality_scores)/total_problems

print("progress report")
print("---------------")
print("total problems solved:",total_problems)
print("average_score:",round(average_score,2))
print("average_correctness",round(avg_correctness,2))
print("average time complexity:",round(avg_complexity,2))
print("average quality: ",round(avg_quality,2))



        
