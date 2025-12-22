---
id: 03bf48b2-c806-48a7-bfa6-513e8346e9d7
name: bash-delete-available-ebs-volumes-with-profile
type: code
language: Bash
verified: true
created_at: '2020-07-31T04:25:34.141661+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Cloud
tags:
  - AWS
  - automation
  - cleanup
  - multi-account
validated: true
---

# bash-delete-available-ebs-volumes-with-profile

## Code

```bash
for x in $(aws ec2 describe-volumes --filters  Name=status,Values=available  --profile <your_profile_name>|grep VolumeId|awk '{print $2}' | tr ',|"' ' '); do aws ec2 delete-volume --region <region> --volume-id $x --profile <your_profile_name>; done
```

## Description

This bash script deletes all available EBS volumes using a specified AWS CLI profile for both querying and deletion actions. It ensures operations are scoped to the correct account in multi-account environments, parsing VolumeIds with grep and awk.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <your_profile_name> | AWS CLI profile name for authentication | prod-profile |
| <region> | AWS region to target | us-west-2 |

## Usage

Save as a script, execute with `./script.sh`, or integrate into CI/CD pipelines for post-test cleanup. The profile parameter isolates actions to specific credentials.

## Detection

- CloudTrail events with profile-specific API calls for DescribeVolumes and DeleteVolume.
- GuardDuty findings on unusual volume deletion patterns.
- Config changes in volume inventory post-execution.

## Related

- [[procedures/aws-delete-ebs-volumes]]
- [[tools/aws-cli]]
