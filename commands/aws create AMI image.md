---
id: b44c14e6-dfdf-4e4a-ab76-251ad1382f4a
name: aws create AMI image
type: command
executor: bash
data: 'aws ec2 create-image --instance-id $AWS_INSTANCE_ID --name $AWS_AMI_NAME --description
  $AWS_AMI_DESCRIPTION

  '
output: aws ec2 create-image --instance-id <instance_id> --name "image-$(date +'%Y-%m-%d_%H-%M-%S')"
  --description "image-$(date +'%Y-%m-%d_%H-%M-%S')"
created_at: '2020-07-31T04:25:34.192231+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws create AMI image

```bash
aws ec2 create-image --instance-id $AWS_INSTANCE_ID --name $AWS_AMI_NAME --description $AWS_AMI_DESCRIPTION

```

## Expected Output

```
aws ec2 create-image --instance-id <instance_id> --name "image-$(date +'%Y-%m-%d_%H-%M-%S')" --description "image-$(date +'%Y-%m-%d_%H-%M-%S')"
```


