---
id: 3afcc5f4-82e6-4a1c-b44b-a6edcbf2a774
name: Retrieve AWS EC2 User Data
type: command
executor: bash
data: 'TOKEN=`curl

  X PUT "http://169.254.169.254/latest/ api /token" H "X-aws-ec2-metadata-token-ttl-seconds:
  21600"`

  && curl H "X-aws-ec2-metadata-token: $TOKEN" v http://169.254.169.254/latest/user-data/'
output: null
created_at: '2023-04-06T03:56:13.398773+00:00'
updated_at: '2023-04-10T20:20:31.271627+00:00'
---

# Retrieve AWS EC2 User Data

```bash
TOKEN=`curl
X PUT "http://169.254.169.254/latest/ api /token" H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
&& curl H "X-aws-ec2-metadata-token: $TOKEN" v http://169.254.169.254/latest/user-data/
```


