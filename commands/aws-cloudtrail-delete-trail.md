---
id: 856c2cfc-fb71-4dc1-a5ed-c725c6cc25ea
name: aws-cloudtrail-delete-trail
type: command
executor: bash
data: aws cloudtrail delete-trail --name $_TRAIL_NAME --profile $_PROFILE_NAME
output: null
created_at: '2023-04-06T03:56:09.750143+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - cloud
  - defense-evasion
verified: true
validated: true
---

# aws-cloudtrail-delete-trail

## Command

```bash
aws cloudtrail delete-trail --name $_TRAIL_NAME --profile $_PROFILE_NAME
```

## Description

This command deletes an existing AWS CloudTrail trail, permanently stopping the logging of API events associated with it. Use this during defense evasion to eliminate audit trails in an AWS account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --name $_TRAIL_NAME | The name of the CloudTrail trail to delete (e.g., cloudgoat_trail) | Yes |
| --profile $_PROFILE_NAME | The AWS CLI profile containing credentials with cloudtrail:DeleteTrail permission (e.g., administrator) | Yes |

## Examples

### Basic Usage

```bash
aws cloudtrail delete-trail --name cloudgoat_trail --profile administrator
```

### With Confirmation Prompt (if interactive)

The command may prompt for confirmation; pipe 'yes' if automating: echo 'yes' | aws cloudtrail delete-trail --name my-trail --profile default

## Expected Output

Successful execution returns:

{
    "Name": "cloudgoat_trail",
    "DeletionStatus": "Deleting trail"
}

Errors include "AccessDeniedException" if permissions are insufficient or "TrailNotFoundException" if the trail does not exist.

## Related

- [[procedures/Disable-CloudTrail-on-AWS]]
- [[commands/aws-cloudtrail-describe-trails]] (for enumeration prior to deletion)
