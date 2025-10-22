---
id: 84d4be8c-dde8-43cc-b320-6ee940054f9c
name: Allowing DNS hostnames
type: command
executor: bash
data: 'aws ec2 modify-vpc-attribute --vpc-id <vpc_id> --enable-dns-hostnames "{\"Value\":true}"
  --region <region>

  '
output: null
created_at: '2020-07-31T04:25:22.966322+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Allowing DNS hostnames

```bash
aws ec2 modify-vpc-attribute --vpc-id <vpc_id> --enable-dns-hostnames "{\"Value\":true}" --region <region>

```
