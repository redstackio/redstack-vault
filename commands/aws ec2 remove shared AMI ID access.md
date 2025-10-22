---
id: 7997ce25-169b-431d-a1fb-288bb903f5f3
name: aws ec2 remove shared AMI ID access
type: command
executor: bash
data: 'aws ec2 modify-image-attribute --image-id $AWS_AMI_ID --launch-permission "Remove=$IAM_USER_ID"

  '
output: aws ec2 modify-image-attribute --image-id ami-0abcdef1234567890 --launch-permission
  "Remove=[{UserId=123456789012}]"
created_at: '2020-07-31T04:25:35.109762+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws ec2 remove shared AMI ID access

```bash
aws ec2 modify-image-attribute --image-id $AWS_AMI_ID --launch-permission "Remove=$IAM_USER_ID"

```

## Expected Output

```
aws ec2 modify-image-attribute --image-id ami-0abcdef1234567890 --launch-permission "Remove=[{UserId=123456789012}]"
```
