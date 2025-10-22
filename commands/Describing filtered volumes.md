---
id: e8e83274-20f1-416f-9714-60754e29e008
name: Describing filtered volumes
type: command
executor: bash
data: 'aws ec2 describe-volumes --filters  Name=status,Values=creating | available
  | in-use | deleting | deleted | error

  '
output: null
created_at: '2020-07-31T04:25:29.577537+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Describing filtered volumes

```bash
aws ec2 describe-volumes --filters  Name=status,Values=creating | available | in-use | deleting | deleted | error

```
