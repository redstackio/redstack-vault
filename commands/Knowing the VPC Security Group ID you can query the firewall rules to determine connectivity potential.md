---
id: 5ce7d316-5740-430d-84c8-3e88f3fa6f98
name: Knowing the VPC Security Group ID you can query the firewall rules to determine
  connectivity potential
type: command
executor: bash
data: 'aws ec2 describe-security-groups --group-ids <VPC Security Group ID> --region
  <region>

  '
output: null
created_at: '2020-07-14T19:06:15.096902+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Knowing the VPC Security Group ID you can query the firewall rules to determine connectivity potential

```bash
aws ec2 describe-security-groups --group-ids <VPC Security Group ID> --region <region>

```


