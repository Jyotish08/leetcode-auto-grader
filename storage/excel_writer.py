import csv
from datetime import datetime
def save_result(problem,score):
  file_name="result.csv"
  date= datetime.now()strftime("%Y-%m-%d")
  row=[date,problem,score]
  with open(file_name,"a",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(row)
  print("result saved to",file_name)
