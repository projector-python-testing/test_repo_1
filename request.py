import requests

access_token = "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"
repo_owner = "projector-python-testing"
repo_name = "test_repo_1"

url = f'https://api.github.com/repos/{repo_owner}/{repo_name}'
response = requests.get(url)
print(response)