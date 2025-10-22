---
id: 14aaa6c9-b7bc-4d27-bee7-ee463eb03efc
name: aws create route using route table ID and gateway ID
type: command
executor: bash
data: 'aws ec2 create-route --route-table-id $AWS_ROUTE_TABLE_ID --destination-cidr-block
  $IP_ADDRESS_CIDR --gateway-id $AWS_GATEWAY_ID --region $AWS_REGION

  '
output: aws ec2 create-route --route-table-id <route_table_id> --destination-cidr-block
  0.0.0.0/0 --gateway-id <igw_id> --region <region>
created_at: '2020-07-31T04:25:16.594637+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws create route using route table ID and gateway ID

```bash
aws ec2 create-route --route-table-id $AWS_ROUTE_TABLE_ID --destination-cidr-block $IP_ADDRESS_CIDR --gateway-id $AWS_GATEWAY_ID --region $AWS_REGION

```

## Expected Output

```
aws ec2 create-route --route-table-id <route_table_id> --destination-cidr-block 0.0.0.0/0 --gateway-id <igw_id> --region <region>
```
