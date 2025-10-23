---
id: c3b6768e-399b-4f14-8302-5da96f7f198f
name: Create Image for instance
type: command
executor: bash
data: $ aws ec2 create-image --instance-id i-0438b003d81cd7ec5 --name "AWS Audit"
  --description "Export AMI" --region eu-west-1
output: null
created_at: '2023-04-06T03:56:09.572409+00:00'
updated_at: '2023-04-10T20:19:44.887186+00:00'
---

# Create Image for instance

```bash
$ aws ec2 create-image --instance-id i-0438b003d81cd7ec5 --name "AWS Audit" --description "Export AMI" --region eu-west-1
```


