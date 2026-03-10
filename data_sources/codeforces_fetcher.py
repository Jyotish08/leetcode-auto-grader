import requests
def get_codeforces_submissions(jyotishpabbisetti2025):
  url=f"https://codeforces.com/api/user.status?handle=jyotishpabbisetti2025"
  response = requests.get(url)
  data = response.json()
  latest =data["result"][0]
  submission_data={
    "problem_name":latest["problem"],
    "contest_id":latest["contestID"],
    "submission_id":latest["id"],
    "language":latest["programmingLanguage"],
    "verdict":latest["verdict"]
  }
  return submisson_data

if __name__ == "__main__":
  sub = get_latest_codeforces_submission("jyotishpabbisetti2025")
  print(sub)
  

