---
id: cddcc066-c1fc-4d5b-af91-3f37bf6abcc4
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:13.398633+00:00'
updated_at: '2023-04-10T20:20:31.272199+00:00'
---

# Code Snippet cddcc066

**Language**: Bash

```bash
TOKEN=`curl
X PUT "http://169.254.169.254/latest/ api /token" H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
&& curl H "X-aws-ec2-metadata-token: $TOKEN" v http://169.254.169.254/latest/user-data/
```
