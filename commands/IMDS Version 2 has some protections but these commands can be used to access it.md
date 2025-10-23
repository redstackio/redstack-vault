---
id: 1aff0bf8-bd95-4484-adc9-a6f632e6e854
name: IMDS Version 2 has some protections but these commands can be used to access
  it
type: command
executor: bash
data: 'TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds:
  21600"`

  curl http://169.254.169.254/latest/meta-data/profile -H "X-aws-ec2-metadata-token:
  $TOKEN"

  '
output: null
created_at: '2020-07-14T19:06:15.104470+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# IMDS Version 2 has some protections but these commands can be used to access it

```bash
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
curl http://169.254.169.254/latest/meta-data/profile -H "X-aws-ec2-metadata-token: $TOKEN"

```


