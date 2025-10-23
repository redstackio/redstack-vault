---
id: 268e8cc6-88b3-4cbf-944e-857810a10091
name: aws create AMI image without reboot
type: command
executor: bash
data: 'aws ec2 create-image --instance-id $AWS_INSTANCE_ID --name $AWS_AMI_NAME --description
  $AWS_AMI_DESCRIPTION --no-reboot

  '
output: aws ec2 create-image --instance-id <instance_id> --name "image-$(date +'%Y-%m-%d_%H-%M-%S')"
  --description "image-$(date +'%Y-%m-%d_%H-%M-%S')" --no-reboot
created_at: '2020-07-31T04:25:34.192365+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws create AMI image without reboot

```bash
aws ec2 create-image --instance-id $AWS_INSTANCE_ID --name $AWS_AMI_NAME --description $AWS_AMI_DESCRIPTION --no-reboot

```

## Expected Output

```
aws ec2 create-image --instance-id <instance_id> --name "image-$(date +'%Y-%m-%d_%H-%M-%S')" --description "image-$(date +'%Y-%m-%d_%H-%M-%S')" --no-reboot
```


