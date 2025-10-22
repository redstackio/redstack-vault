---
id: 98b0f4f2-d339-4b93-b696-46897fbdf995
name: aws associate public subnet with route table
type: command
executor: bash
data: 'aws ec2 associate-route-table --route-table-id $AWS_ROUTE_TABLE_ID --subnet-id
  $AWS_SUBNET_ID --region $AWS_REGION

  '
output: aws ec2 associate-route-table --route-table-id <route_table_id> --subnet-id
  <subnet_id> --region <region>
created_at: '2020-07-31T04:25:16.594834+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws associate public subnet with route table

```bash
aws ec2 associate-route-table --route-table-id $AWS_ROUTE_TABLE_ID --subnet-id $AWS_SUBNET_ID --region $AWS_REGION

```

## Expected Output

```
aws ec2 associate-route-table --route-table-id <route_table_id> --subnet-id <subnet_id> --region <region>
```
