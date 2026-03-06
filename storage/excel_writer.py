import csv
from datetime import datetime
def save_result(problem,score):
  file_name="result.csv"
  date= datetime.now()strftime("%Y-%m-%d")
  row=[date,
       problem,
       score,
      evaluation.get("correctness",0),
      evaluation.get("time_complexity",0),
      evaluation.get("code_quality",0)
      ]
  with open(file_name,"a",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(row)
  print("result saved to",file_name)
