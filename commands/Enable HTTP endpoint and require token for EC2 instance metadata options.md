---
id: 92b815ce-1f11-41e2-b9bc-bb2d6a68bf67
name: Enable HTTP endpoint and require token for EC2 instance metadata options
type: command
executor: bash
data: aws ec2 modify-instance-metadata-options --instance-id <INSTANCE-ID> --profile
  <AWS_PROFILE> --http-endpoint enabled --http-token required
output: null
created_at: '2023-04-06T03:56:09.189416+00:00'
updated_at: '2023-04-10T20:19:51.024180+00:00'
---

# Enable HTTP endpoint and require token for EC2 instance metadata options

```bash
aws ec2 modify-instance-metadata-options --instance-id <INSTANCE-ID> --profile <AWS_PROFILE> --http-endpoint enabled --http-token required
```
