---
id: c5594224-340c-463c-86fb-c69ba79927cf
name: Terraform Apply
type: command
executor: bash
data: terraform apply -auto-approve
output: "hacker@kali~$ terraform apply -auto-approve\n\nAn execution plan has been\
  \ generated and is shown below.\nResource actions are indicated with the following\
  \ symbols:\n  + create\n\nTerraform will perform the following actions:\n\n  # aws_s3_bucket.http\
  \ will be created\n\n--- CUT ---\n\naws_s3_bucket.logs: Creating...\naws_s3_bucket.logs:\
  \ Creation complete after 8s [id=4a4a8f4331a58e913893a5d58b03221f-redstack-site-logs]\n\
  aws_s3_bucket.http: Creating...\naws_s3_bucket.http: Still creating... [10s elapsed]\n\
  aws_s3_bucket.http: Provisioning with 'local-exec'...\naws_s3_bucket.http (local-exec):\
  \ Executing: [\"/bin/sh\" \"-c\" \"aws s3 cp reverse_shell.exe s3://4a4a8f4331a58e913893a5d58b03221f-redstack\
  \ --profile hacker\"]\naws_s3_bucket.http (local-exec): Completed 12 Bytes/12 Bytes\
  \ (8 Bytes/s) with 1 file(s) remaining\naws_s3_bucket.http (local-exec): upload:\
  \ ./reverse_shell.exe to s3://4a4a8f4331a58e913893a5d58b03221f-redstack/reverse_shell.exe\n\
  aws_s3_bucket.http: Creation complete after 15s [id=4a4a8f4331a58e913893a5d58b03221f-redstack]\n\
  \nApply complete! Resources: 2 added, 0 changed, 0 destroyed.\n\nOutputs:\n\nbucket_domain_name\
  \ = s3://4a4a8f4331a58e913893a5d58b03221f-redstack.s3.amazonaws.com/reverse_shell.exe"
created_at: '2019-10-10T18:18:30.572730+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Terraform Apply

```bash
terraform apply -auto-approve
```

## Expected Output

```
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
```
