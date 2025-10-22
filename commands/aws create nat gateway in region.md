---
id: 1e0bf9d8-7529-4449-8d68-a2f5e9274238
name: aws create nat gateway in region
type: command
executor: bash
data: 'aws ec2 create-nat-gateway --subnet-id $AWS_SUBNET_ID --allocation-id $AWS_ALLOCATION_ID
  --region $AWS_REGION

  '
output: aws ec2 create-nat-gateway --subnet-id <subnet_id> --allocation-id <allocation_id>
  --region <region>
created_at: '2020-07-31T04:25:19.888042+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws create nat gateway in region

```bash
aws ec2 create-nat-gateway --subnet-id $AWS_SUBNET_ID --allocation-id $AWS_ALLOCATION_ID --region $AWS_REGION

```

## Expected Output

```
aws ec2 create-nat-gateway --subnet-id <subnet_id> --allocation-id <allocation_id> --region <region>
```
