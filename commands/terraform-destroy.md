---
id: f5fbcd4b-c85e-4df4-8679-9def4bdd2246
name: terraform-destroy
type: command
executor: bash
data: terraform destroy -auto-approve
output: >-
  hacker@kali~$ terraform destroy -auto-approve

  aws_s3_bucket.logs: Refreshing state...
  [id=4a4a8f4331a58e913893a5d58b03221f-redstack-site-logs]

  aws_s3_bucket.http: Refreshing state...
  [id=4a4a8f4331a58e913893a5d58b03221f-redstack]

  aws_s3_bucket.http: Destroying...
  [id=4a4a8f4331a58e913893a5d58b03221f-redstack]

  aws_s3_bucket.http: Destruction complete after 3s

  aws_s3_bucket.logs: Destroying...
  [id=4a4a8f4331a58e913893a5d58b03221f-redstack-site-logs]

  aws_s3_bucket.logs: Destruction complete after 1s


  Destroy complete! Resources: 2 destroyed.
created_at: '2019-10-10T18:18:30.573551+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - terraform
  - cloud
  - infrastructure
verified: true
validated: true
---

# terraform-destroy

## Command

```bash
terraform destroy -auto-approve
```

## Description

Destroys all resources managed by the Terraform configuration, cleaning up infrastructure like EC2 instances and security groups. Use -auto-approve to skip prompts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -auto-approve | Skips confirmation prompts | No |

## Examples

### Basic Usage

```bash
terraform destroy
```

Prompts for approval before destroying.

### Advanced Usage

```bash
terraform destroy -var="region=us-west-2"
```

Destroys with variable overrides.

## Expected Output

hacker@kali~$ terraform destroy -auto-approve
aws_s3_bucket.logs: Refreshing state... [id=4a4a8f4331a58e913893a5d58b03221f-redstack-site-logs]
aws_s3_bucket.http: Refreshing state... [id=4a4a8f4331a58e913893a5d58b03221f-redstack]
aws_s3_bucket.http: Destroying... [id=4a4a8f4331a58e913893a5d58b03221f-redstack]
aws_s3_bucket.http: Destruction complete after 3s
aws_s3_bucket.logs: Destroying... [id=4a4a8f4331a58e913893a5d58b03221f-redstack-site-logs]
aws_s3_bucket.logs: Destruction complete after 1s

Destroy complete! Resources: 2 destroyed.

## Related

- [[procedures/Terraform-Create-Kali-Linux-EC2-Instance]]
- [[commands/terraform-apply]]
