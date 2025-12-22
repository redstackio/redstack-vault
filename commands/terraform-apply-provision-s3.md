---
id: c5594224-340c-463c-86fb-c69ba79927cf
name: terraform-apply-provision-s3
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
  - macOS
tags:
  - infrastructure
  - aws
  - s3
verified: true
validated: true
---

# terraform-apply-provision-s3

## Command

```bash
terraform apply -auto-approve
```

## Description

Applies the Terraform configuration to create or update infrastructure, such as S3 buckets for website hosting and logging, including uploading a payload file via AWS CLI provisioner. The -auto-approve flag skips interactive confirmation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -auto-approve | Skips confirmation prompts for apply | Yes |

## Examples

### Basic Usage

```bash
terraform apply -auto-approve
```

Provisions resources defined in main.tf using variables from terraform.tfvars.

### Advanced Usage

```bash
terraform apply -var="site_name=customsite" -auto-approve
```

Overrides variables at runtime for custom configurations.

## Expected Output

Terraform shows a plan summary, then creates resources like S3 buckets, executes the upload provisioner, and outputs the bucket domain name with payload path upon completion (e.g., "Apply complete! Resources: 2 added").

## Related

- [[commands/terraform-initialize-project]]
- [[procedures/Provision-AWS-S3-Website-and-Upload-Payload]]
