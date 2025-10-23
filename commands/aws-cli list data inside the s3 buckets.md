---
id: 82849292-7baa-430e-bd4b-5c9e5f6a3568
name: aws-cli list data inside the s3 buckets
type: command
executor: bash
data: 'for i in $(cat buckets.txt); do aws s3 ls s3://$i; done;

  '
output: null
created_at: '2020-07-24T17:11:52.447330+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws-cli list data inside the s3 buckets

```bash
for i in $(cat buckets.txt); do aws s3 ls s3://$i; done;

```


