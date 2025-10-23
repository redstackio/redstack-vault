---
id: 07fe1425-4dcd-4a1e-907d-76dc8890a76c
name: aws ec2 auto assign public IPs
type: command
executor: bash
data: 'aws ec2 modify-subnet-attribute --subnet-id <subnet_id> --map-public-ip-on-launch
  --region <region>

  '
output: null
created_at: '2020-07-31T04:25:18.336270+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws ec2 auto assign public IPs

```bash
aws ec2 modify-subnet-attribute --subnet-id <subnet_id> --map-public-ip-on-launch --region <region>

```


