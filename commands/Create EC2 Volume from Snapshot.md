---
id: 67c7277d-259a-4c9f-8c24-2ec5d067e97c
name: Create EC2 Volume from Snapshot
type: command
executor: bash
data: aws ec2 create-volume --snapshot-id ID --availability-zone ZONE --profile profile_name
output: null
created_at: '2023-04-06T03:56:13.800483+00:00'
updated_at: '2023-04-10T20:20:10.457037+00:00'
---

# Create EC2 Volume from Snapshot

```bash
aws ec2 create-volume --snapshot-id ID --availability-zone ZONE --profile profile_name
```


