---
id: 09d229ca-1d4d-4aa0-b386-9caea33ea5f8
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:09.189490+00:00'
updated_at: '2023-04-10T20:19:51.021136+00:00'
---

# Code Snippet 09d229ca

**Language**: Powershell

```powershell
export TOKEN=`curl -X PUT -H "X-aws-ec2-metadata-token-ttl-seconds: 21600" "http://169.254.169.254/latest/api/token"`
curl -H "X-aws-ec2-metadata-token:$TOKEN" -v "http://169.254.169.254/latest/meta-data"
```
