This is a sample code: just to illustrate the methodology of do k8s(`kubectl`) operation with LLM assistant.

Thanks to project [Kubectl-GPT](https://github.com/abhishek-ch/Kubectl-GPT/blob/master/kgpt/kubectlprompt.py) for the great prompt as my reference.

Usage:

```
pip instal openai
```

```
export OPENAI_API_KEY="$your-key"
python3 kubectl-chat.py "List pods which is Pending and show their pending reason"
```

If using openAI proxy, export environment variables before run the script:
```
export OPENAI_API_BASE=http://$your-proxy
export OPENAI_API_KEY="$your-key"
export MODEL="$other-model-name" #"gpt-3.5-turbo-16k"
```


Theory:

1. Create a prompt to ask LLM(openAI by default) to acts as a script generator
2. Show LLM some example (good example and bad ones)
3. execute the shell script locally



Relevant projects:

- https://github.com/feiskyer/kube-copilot
- https://github.com/knight42/kopilot
- https://github.com/sozercan/kubectl-ai
- https://github.com/abhishek-ch/Kubectl-GPT


