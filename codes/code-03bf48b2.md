---
id: 03bf48b2-c806-48a7-bfa6-513e8346e9d7
type: code
language: Bash
verified: false
created_at: '2020-07-31T04:25:34.141661+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 03bf48b2

**Language**: Bash

```bash

for x in $(aws ec2 describe-volumes --filters  Name=status,Values=available  --profile <your_profile_name>|grep VolumeId|awk '{print $2}' | tr ',|"' ' '); do aws ec2 delete-volume --region <region> --volume-id $x --profile <your_profile_name>; done

```
