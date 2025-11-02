---
id: a3fb1f99-a51d-4052-abc1-2ba8b4e9dedf
name: aws create a snapshot with volume ID and date description
type: command
executor: bash
data: 'aws ec2 create-snapshot --volume-id $AWS_VOLUME_ID --description $AWS_DESCRIPTION

  '
output: aws ec2 create-snapshot --volume-id <vol-id> --description "snapshot-$(date
  +'%Y-%m-%d_%H-%M-%S')"
created_at: '2020-07-31T04:25:23.794896+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[vol]]'
---

# aws create a snapshot with volume ID and date description

```bash
aws ec2 create-snapshot --volume-id $AWS_VOLUME_ID --description $AWS_DESCRIPTION

```

## Expected Output

```
aws ec2 create-snapshot --volume-id <vol-id> --description "snapshot-$(date +'%Y-%m-%d_%H-%M-%S')"
```


