from openai import OpenAi
import json
from config.api_config import OPENAI_API_KEY
client = OpenAI(api_key=OPENAI_API_KEY)
def evaluate_code(problem,code):
  prompt=f"""you are an expert competitive programming judge.
  Evaluate the following solution.
  problem:
  {problem}
  code:
  {code}
  return evaluation strictly in JSON format:
  {{"correctness":score between 0 and 1 ,
  "time_complexity":score between 0 and 1,
  "space_complexity":score between 0 and 1,
  "code_quality":score between 0 and 1,
  "algorithmic_insight": score betwen 0 and 1
  }}
  response=client.chat.completions.create(
      model="gpt-4.1-mini",
      messages=["role":"system",
                "content":"you are a strict algorithm judge."},
                {"role":"user","content": prompt}],
                teperature=0)
  content=response.choices[0].messag.content
  print("AI raw response :",content)
  try :
    evaluation=json.loads(content)
  except Exception as error: :
    print("JSON parsing failed:",error)
    evaluation = {"correctness": 0.5 ,
  "time_complexity": 0.5,
  "space_complexity":0.5,
  "code_quality": 0.5,
  "algorithmic_insight":0.5
      
    }  
  
  return evaluation
  
  
