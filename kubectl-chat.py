import os
import openai
import sys

#openai.api_base = "http://openapi-gpt.ats.io/v1" #"https://westeurope.api.cognitive.microsoft.com/" # Depends on the region where the service is deployed
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("MODEL","gpt-3.5-turbo") #"text-davinci-003" ) #gpt-3.5-turbo-16k

if len(sys.argv) < 2:
    print("Input Parameter is required. example: python3 kubectl-chat.py \"show me the image of kube-apiserver pod \"")
    sys.exit(1)

request = sys.argv[1]

# prompt quoted from https://github.com/abhishek-ch/Kubectl-GPT/blob/master/kgpt/kubectlprompt.py

prompt="You are my Kubernetes Command line tool (kubectl) generator. Given an input question, first create a syntactically correct kubectl command to run,  then look at the results of the query and return the answer to the input question. If an error is returned, rewrite the command, check the command, and try again.  unless the user specifies in the question with a namespace name or all namespaces, create command for a single namespace named default.You must generate the correct kubctl command to answer the question. Kubernetes version is not less than 1.25.Do not provide any explanations, only generate a shell script."

response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt + request}    ],
        temperature=0.1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        )

output= response.choices[0].message.content
print("=============== Script from AI =========================")
print(output)
print("===========Script Execution Result =====================")
with open("tmp.sh","w") as f:
    f.write(output)
os.system("bash tmp.sh && rm tmp.sh")

