---
id: f5fbcd4b-c85e-4df4-8679-9def4bdd2246
name: terraform-destroy-cleanup
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
  - macOS
tags:
  - infrastructure
  - aws
  - cleanup
verified: true
validated: true
---

# terraform-destroy-cleanup

## Command

```bash
terraform destroy -auto-approve
```

## Description

Destroys all resources managed by the Terraform configuration, such as S3 buckets and uploaded objects, to clean up after operations and prevent ongoing costs or exposure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -auto-approve | Skips confirmation for destruction | Yes |

## Examples

### Basic Usage

```bash
terraform destroy -auto-approve
```

Removes provisioned S3 resources defined in the state file.

### Advanced Usage

```bash
terraform destroy -var="site_hash=backuphash" -auto-approve
```

Targets specific variable overrides if needed.

## Expected Output

Terraform refreshes state, destroys resources sequentially (e.g., buckets), and confirms completion (e.g., "Destroy complete! Resources: 2 destroyed.").

## Related

- [[commands/terraform-apply-provision-s3]]
- [[procedures/Provision-AWS-S3-Website-and-Upload-Payload]]
