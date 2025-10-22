---
id: eca44785-6a96-4b39-a3dd-58bdc4a8e4f3
name: aws allocate elastic ip address in vpc region
type: command
executor: bash
data: 'aws ec2 allocate-address --domain vpc --region $AWS_REGION

  '
output: aws ec2 allocate-address --domain vpc --region <region>
created_at: '2020-07-31T04:25:19.887877+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws allocate elastic ip address in vpc region

```bash
aws ec2 allocate-address --domain vpc --region $AWS_REGION

```

## Expected Output

```
aws ec2 allocate-address --domain vpc --region <region>
```
