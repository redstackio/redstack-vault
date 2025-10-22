---
id: f5fbcd4b-c85e-4df4-8679-9def4bdd2246
name: Terraform Destroy
type: command
executor: bash
data: terraform destroy -auto-approve
output: 'hacker@kali~$ terraform destroy -auto-approve

  aws_s3_bucket.logs: Refreshing state... [id=4a4a8f4331a58e913893a5d58b03221f-redstack-site-logs]

  aws_s3_bucket.http: Refreshing state... [id=4a4a8f4331a58e913893a5d58b03221f-redstack]

  aws_s3_bucket.http: Destroying... [id=4a4a8f4331a58e913893a5d58b03221f-redstack]

  aws_s3_bucket.http: Destruction complete after 3s

  aws_s3_bucket.logs: Destroying... [id=4a4a8f4331a58e913893a5d58b03221f-redstack-site-logs]

  aws_s3_bucket.logs: Destruction complete after 1s

  Destroy complete! Resources: 2 destroyed.'
created_at: '2019-10-10T18:18:30.573551+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Terraform Destroy

```bash
terraform destroy -auto-approve
```

## Expected Output

```
hacker@kali~$ terraform destroy -auto-approve
aws_s3_bucket.logs: Refreshing state... [id=4a4a8f4331a58e913893a5d58b03221f-redstack-site-logs]
aws_s3_bucket.http: Refreshing state... [id=4a4a8f4331a58e913893a5d58b03221f-redstack]
aws_s3_bucket.http: Destroying... [id=4a4a8f4331a58e913893a5d58b03221f-redstack]
aws_s3_bucket.http: Destruction complete after 3s
aws_s3_bucket.logs: Destroying... [id=4a4a8f4331a58e913893a5d58b03221f-redstack-site-logs]
aws_s3_bucket.logs: Destruction complete after 1s

Destroy complete! Resources: 2 destroyed.
```
