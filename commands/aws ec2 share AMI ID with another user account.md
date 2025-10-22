---
id: 3c80fa7f-0316-4f14-98b8-21cea6babbf4
name: aws ec2 share AMI ID with another user account
type: command
executor: bash
data: 'aws ec2 modify-image-attribute --image-id $AWS_AMI_ID --launch-permission "Add=$IAM_USER_ID"

  '
output: aws ec2 modify-image-attribute --image-id ami-0abcdef1234567890 --launch-permission
  "Add=[{UserId=123456789012}]"
created_at: '2020-07-31T04:25:35.109593+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws ec2 share AMI ID with another user account

```bash
aws ec2 modify-image-attribute --image-id $AWS_AMI_ID --launch-permission "Add=$IAM_USER_ID"

```

## Expected Output

```
aws ec2 modify-image-attribute --image-id ami-0abcdef1234567890 --launch-permission "Add=[{UserId=123456789012}]"
```
