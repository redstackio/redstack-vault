---
id: a74aaffa-59dc-4997-b98c-d15a5ceb2b3b
type: code
language: Python
verified: false
created_at: '2023-05-24T16:02:52.019223+00:00'
updated_at: '2023-05-24T16:03:55.108971+00:00'
---

# Code Snippet a74aaffa

**Language**: Python

```python
IDENTITY_ENDPOINT = os.environ['IDENTITY_ENDPOINT']
IDENTITY_HEADER = os.environ['IDENTITY_HEADER']

print("[+] Management API")
cmd = 'curl "%s?resource=https://management.azure.com/&api-version=2017-09-01" -H secret:%s' % (IDENTITY_ENDPOINT, IDENTITY_HEADER)
val = os.popen(cmd).read()
print("Access Token: "+json.loads(val)["access_token"])
print("ClientID/AccountID: "+json.loads(val)["client_id"])

print("\r\n[+] Graph API")
cmd = 'curl "%s?resource=https://graph.microsoft.com/&api-version=2017-09-01" -H secret:%s' % (IDENTITY_ENDPOINT, IDENTITY_HEADER)
val = os.popen(cmd).read()
print(json.loads(val)["access_token"])
print("ClientID/AccountID: "+json.loads(val)["client_id"])
```


