---
id: 0214800a-e85d-4516-a6dd-338ebd0d9461
name: aws ev2 describe AMI by Image ID
type: command
executor: bash
data: 'aws ec2 describe-images --image-ids $AWS_IMAGE_ID --profile $AWS_PROFILE --region
  $AWS_REGION

  '
output: aws ec2 describe-images --image-ids ami-a123ee1f --profile staging --region
  us-east-1
created_at: '2020-07-31T04:25:19.326889+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws ev2 describe AMI by Image ID

```bash
aws ec2 describe-images --image-ids $AWS_IMAGE_ID --profile $AWS_PROFILE --region $AWS_REGION

```

## Expected Output

```
aws ec2 describe-images --image-ids ami-a123ee1f --profile staging --region us-east-1
```
