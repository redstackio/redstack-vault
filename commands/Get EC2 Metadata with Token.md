---
id: fec15f50-f8a8-4803-a842-6fdd5b578c6f
name: Get EC2 Metadata with Token
type: command
executor: bash
data: 'TOKEN=`curl

  X PUT "http://169.254.169.254/latest/ api /token" H "X-aws-ec2-metadata-token-ttl-seconds:
  21600"`

  && curl H "X-aws-ec2-metadata-token: $TOKEN" v http://169.254.169.254/latest/meta-data/'
output: null
created_at: '2023-04-06T03:56:13.368549+00:00'
updated_at: '2023-04-10T20:19:58.621084+00:00'
---

# Get EC2 Metadata with Token

```bash
TOKEN=`curl
X PUT "http://169.254.169.254/latest/ api /token" H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
&& curl H "X-aws-ec2-metadata-token: $TOKEN" v http://169.254.169.254/latest/meta-data/
```


