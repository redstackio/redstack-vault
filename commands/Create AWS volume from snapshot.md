---
id: f75e0bfe-265b-4af3-a09b-58afcff95ee7
name: Create AWS volume from snapshot
type: command
executor: bash
data: $ aws --profile swk ec2 create-volume --availability-zone us-west-2a --region
  us-west-2  --snapshot-id  snap-XXXX342abd1bdcb89
output: null
created_at: '2023-04-06T03:55:53.686315+00:00'
updated_at: '2023-04-06T03:55:53.708471+00:00'
---

# Create AWS volume from snapshot

```bash
$ aws --profile swk ec2 create-volume --availability-zone us-west-2a --region us-west-2  --snapshot-id  snap-XXXX342abd1bdcb89
```
