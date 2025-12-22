---
id: 616c17b8-6744-42d3-aee1-48d35cd89543
name: bash-delete-available-ebs-volumes
type: code
language: Bash
verified: true
created_at: '2020-07-31T04:25:34.141507+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Cloud
tags:
  - AWS
  - automation
  - cleanup
validated: true
---

# bash-delete-available-ebs-volumes

## Code

```bash
for x in $(aws ec2 describe-volumes --filters  Name=status,Values=available  --profile <your_profile_name>|grep VolumeId|awk '{print $2}' | tr ',|"' ' '); do aws ec2 delete-volume --region <region> --volume-id $x; done
```

## Description

This bash script queries all available (unused) EBS volumes in an AWS region and deletes them in a loop. It uses grep and awk to parse the JSON output for VolumeIds. Ideal for automating cleanup of detached volumes to reduce costs and attack surface.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <your_profile_name> | AWS CLI profile name for authentication | default |
| <region> | AWS region to target | us-east-1 |

## Usage

Save as a script (e.g., cleanup-volumes.sh), make executable with `chmod +x cleanup-volumes.sh`, and run `./cleanup-volumes.sh`. Schedule via cron (e.g., `0 2 * * 0 /path/to/script.sh`) for weekly execution. Test in a non-production account first.

## Detection

- CloudTrail logs showing multiple DeleteVolume API calls in sequence.
- Billing alerts for sudden drops in EBS volume count.
- IAM access logs for ec2:DescribeVolumes followed by deletions.

## Related

- [[procedures/aws-delete-ebs-volumes]]
- [[tools/aws-cli]]
