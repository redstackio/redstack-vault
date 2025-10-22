---
id: a39d5fa6-5848-4faf-93ff-7f5abc1065f9
name: Create EC2 instance
type: command
executor: bash
data: $ aws ec2 run-instances --image-id ami-0b77e2d906b00202d --security-group-ids
  "sg-6d0d7f01" --subnet-id subnet-9eb001ea --count 1 --instance-type t2.micro --key-name
  "AWS Audit" --query "Instances[0].InstanceId" --region eu-west-1
output: null
created_at: '2023-04-06T03:56:09.572526+00:00'
updated_at: '2023-04-10T20:19:44.887186+00:00'
---

# Create EC2 instance

```bash
$ aws ec2 run-instances --image-id ami-0b77e2d906b00202d --security-group-ids "sg-6d0d7f01" --subnet-id subnet-9eb001ea --count 1 --instance-type t2.micro --key-name "AWS Audit" --query "Instances[0].InstanceId" --region eu-west-1
```
