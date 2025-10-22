---
id: 73076268-69fa-43fd-bf43-39f7c3c6990a
name: 'Create the Route Table:'
type: command
executor: bash
data: 'aws ec2 create-route-table --vpc-id $AWS_VPC_ID --region $AWS_REGION

  '
output: aws ec2 create-route-table --vpc-id <vpc_id> --region <region>
created_at: '2020-07-31T04:25:16.594472+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Create the Route Table:

```bash
aws ec2 create-route-table --vpc-id $AWS_VPC_ID --region $AWS_REGION

```

## Expected Output

```
aws ec2 create-route-table --vpc-id <vpc_id> --region <region>
```
