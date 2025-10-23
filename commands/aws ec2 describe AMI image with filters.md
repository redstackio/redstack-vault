---
id: 4aacb8cc-5c90-4e68-8926-ce8af86e5504
name: aws ec2 describe AMI image with filters
type: command
executor: bash
data: 'aws ec2 describe-images --filters "Name=$TYPE,Values=$OS_TYPE" "Name=$TYPE,Values=$VOLUME_TYPE"

  '
output: aws ec2 describe-images --filters "Name=platform,Values=windows" "Name=root-device-type,Values=ebs"
created_at: '2020-07-31T04:25:19.327136+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws ec2 describe AMI image with filters

```bash
aws ec2 describe-images --filters "Name=$TYPE,Values=$OS_TYPE" "Name=$TYPE,Values=$VOLUME_TYPE"

```

## Expected Output

```
aws ec2 describe-images --filters "Name=platform,Values=windows" "Name=root-device-type,Values=ebs"
```


