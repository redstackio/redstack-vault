---
id: 4e8b43a3-32a4-4b8f-b11e-b93c15f5d654
name: aws create a snapshot with volume ID
type: command
executor: bash
data: 'aws ec2 create-snapshot --volume-id $AWS_VOLUME_ID

  '
output: aws ec2 create-snapshot --volume-id <vol-id>
created_at: '2020-07-31T04:25:23.794742+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws create a snapshot with volume ID

```bash
aws ec2 create-snapshot --volume-id $AWS_VOLUME_ID

```

## Expected Output

```
aws ec2 create-snapshot --volume-id <vol-id>
```
