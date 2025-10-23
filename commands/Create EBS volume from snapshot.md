---
id: 7d8c56be-c76e-4b82-9984-7f2dc50e3c6a
name: Create EBS volume from snapshot
type: command
executor: bash
data: aws ec2 create-volume --snapshot-id snapshot_id --availability-zone zone
output: null
created_at: '2023-04-06T03:56:09.541861+00:00'
updated_at: '2023-04-10T20:19:52.319514+00:00'
---

# Create EBS volume from snapshot

```bash
aws ec2 create-volume --snapshot-id snapshot_id --availability-zone zone
```


