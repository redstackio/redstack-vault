---
id: eaea05db-d61e-48fa-911d-b40b9f6229ba
name: aws associate route table id with subnet id
type: command
executor: bash
data: 'aws ec2 associate-route-table --route-table-id $AWS_ROUTE_TABLE_ID --subnet-id
  $AWS_SUBNET_ID --region $AWS_REGION

  '
output: aws ec2 associate-route-table --route-table-id <route_table_id> --subnet-id
  <subnet_id> --region <region>
created_at: '2020-07-31T04:25:33.411657+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws associate route table id with subnet id

```bash
aws ec2 associate-route-table --route-table-id $AWS_ROUTE_TABLE_ID --subnet-id $AWS_SUBNET_ID --region $AWS_REGION

```

## Expected Output

```
aws ec2 associate-route-table --route-table-id <route_table_id> --subnet-id <subnet_id> --region <region>
```


