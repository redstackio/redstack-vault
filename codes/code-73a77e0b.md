---
id: 73a77e0b-d762-46ef-9b14-7be384ea1913
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:17.031596+00:00'
updated_at: '2023-04-10T20:33:50.752012+00:00'
---

# Code Snippet 73a77e0b

**Language**: Powershell

```powershell
curl http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/email
curl -s http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token 
docker login -e <email> -u oauth2accesstoken -p "<access token>" https://gcr.io
```


