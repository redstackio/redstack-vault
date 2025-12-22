---
id: c5594224-340c-463c-86fb-c69ba79927cf
name: terraform-apply
type: command
executor: bash
data: terraform apply -auto-approve
output: >-
  hacker@kali~$ terraform apply -auto-approve


  An execution plan has been generated and is shown below.

  Resource actions are indicated with the following symbols:
    + create

  Terraform will perform the following actions:

    # aws_s3_bucket.http will be created

  --- CUT ---


  aws_s3_bucket.logs: Creating...

  aws_s3_bucket.logs: Creation complete after 8s
  [id=4a4a8f4331a58e913893a5d58b03221f-redstack-site-logs]

  aws_s3_bucket.http: Creating...

  aws_s3_bucket.http: Still creating... [10s elapsed]

  aws_s3_bucket.http: Provisioning with 'local-exec'...

  aws_s3_bucket.http (local-exec): Executing: ["/bin/sh" "-c" "aws s3 cp
  reverse_shell.exe s3://4a4a8f4331a58e913893a5d58b03221f-redstack --profile
  hacker"]

  aws_s3_bucket.http (local-exec): Completed 12 Bytes/12 Bytes (8 Bytes/s) with
  1 file(s) remaining

  aws_s3_bucket.http (local-exec): upload: ./reverse_shell.exe to
  s3://4a4a8f4331a58e913893a5d58b03221f-redstack/reverse_shell.exe

  aws_s3_bucket.http: Creation complete after 15s
  [id=4a4a8f4331a58e913893a5d58b03221f-redstack]


  Apply complete! Resources: 2 added, 0 changed, 0 destroyed.


  Outputs:


  bucket_domain_name =
  s3://4a4a8f4331a58e913893a5d58b03221f-redstack.s3.amazonaws.com/reverse_shell.exe
created_at: '2019-10-10T18:18:30.572730+00:00'
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

# terraform-apply

## Command

```bash
terraform apply -auto-approve
```

## Description

Applies the Terraform configuration to create or update infrastructure resources in AWS. The -auto-approve flag skips interactive confirmation; use cautiously in production.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -auto-approve | Skips confirmation prompts | No |

## Examples

### Basic Usage

```bash
terraform apply
```

Prompts for approval before applying changes.

### Advanced Usage

```bash
terraform apply -var="region=us-west-2"
```

Applies with variable overrides.

## Expected Output

hacker@kali~$ terraform apply -auto-approve

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_s3_bucket.http will be created

--- CUT ---

aws_s3_bucket.logs: Creating...
aws_s3_bucket.logs: Creation complete after 8s [id=4a4a8f4331a58e913893a5d58b03221f-redstack-site-logs]
aws_s3_bucket.http: Creating...
aws_s3_bucket.http: Still creating... [10s elapsed]
aws_s3_bucket.http: Provisioning with 'local-exec'...
aws_s3_bucket.http (local-exec): Executing: ["/bin/sh" "-c" "aws s3 cp reverse_shell.exe s3://4a4a8f4331a58e913893a5d58b03221f-redstack --profile hacker"]
aws_s3_bucket.http (local-exec): Completed 12 Bytes/12 Bytes (8 Bytes/s) with 1 file(s) remaining
aws_s3_bucket.http (local-exec): upload: ./reverse_shell.exe to s3://4a4a8f4331a58e913893a5d58b03221f-redstack/reverse_shell.exe
aws_s3_bucket.http: Creation complete after 15s [id=4a4a8f4331a58e913893a5d58b03221f-redstack]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

bucket_domain_name = s3://4a4a8f4331a58e913893a5d58b03221f-redstack.s3.amazonaws.com/reverse_shell.exe

## Related

- [[procedures/Terraform-Create-Kali-Linux-EC2-Instance]]
- [[commands/terraform-init]]
