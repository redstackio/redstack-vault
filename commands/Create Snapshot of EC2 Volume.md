---
id: 4166847f-ae4d-4763-b4b8-aa49f8f35222
name: Create Snapshot of EC2 Volume
type: command
executor: bash
data: aws ec2 create-snapshot --volume volumeID --description "Example" --profile
  profile_name
output: null
created_at: '2023-04-06T03:56:13.750800+00:00'
updated_at: '2023-04-10T20:20:36.202580+00:00'
---

# Create Snapshot of EC2 Volume

```bash
aws ec2 create-snapshot --volume volumeID --description "Example" --profile profile_name
```


