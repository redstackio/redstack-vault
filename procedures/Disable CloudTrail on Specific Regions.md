---
id: 1d6c6b4c-eec8-4822-a999-2eaf2539bdb6
name: Disable CloudTrail on Specific Regions
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.184238+00:00'
updated_at: '2023-04-10T20:20:22.167592+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Internal Spearphishing|T1534 - Internal Spearphishing]]'
tags:
- '[[CloudTrail]]'
- '[[Disable CloudTrail on specific regions]]'
- '[[RDS - Relational Database Service]]'
- '[[Userful Commands]]'
commands:
- '[[Update CloudTrail for example_trail in eu-west region without including global
  service events and not multi-region]]'
---

# Disable CloudTrail on Specific Regions

## Summary

Disabling CloudTrail on specific regions can be useful for attackers trying to hide their tracks. By disabling CloudTrail, attackers can avoid detection and prevent security teams from seeing what actions they have taken. From a technical standpoint, disabling CloudTrail can be done using the 'Upda

## Description

# Description

Disabling CloudTrail on specific regions can be useful for attackers trying to hide their tracks. By disabling CloudTrail, attackers can avoid detection and prevent security teams from seeing what actions they have taken. From a technical standpoint, disabling CloudTrail can be done using the 'Update CloudTrail' command. This procedure can be used by attackers to cover their tracks and maintain persistence within a compromised environment. From a business perspective, disabling CloudTrail can lead to a loss of visibility and control over AWS resources, potentially leading to data breaches and compliance issues.

## Requirements

1. AWS credentials with permissions to modify CloudTrail configuration

## Defense

1. Regularly review CloudTrail logs for any suspicious activity

1. Enable CloudTrail on all regions and log all events

1. Implement least privilege access control to prevent unauthorized access to AWS resources

## Objectives

1. Disable CloudTrail on specific regions to avoid detection

1. Maintain persistence within a compromised environment

# Instructions

1. The `aws cloudtrail update-trail` command is used to update an existing CloudTrail trail with new settings. The `--name` option specifies the name of the trail to update. The `--no-include-global-service-event` option specifies that global service events should not be included in the trail. The `--no-is-multi-region` option specifies that the trail should not be a multi-region trail. The `--region` option specifies the region of the trail to update.

**Code**: [[aws cloudtrail update-trail --name example_trail -]]

> The `aws cloudtrail update-trail` command is used to update an existing CloudTrail trail with new settings. The `--name` option specifies the name of the trail to update. The `--no-include-global-service-event` option specifies that global service events should not be included in the trail. The `--no-is-multi-region` option specifies that the trail should not be a multi-region trail. The `--region` option specifies the region of the trail to update. The `--name` option is required. The `--no-include-global-service-event` and `--no-is-multi-region` options are optional and default to `false`. The `--region` option is also optional and defaults to the current region of the AWS CLI configuration.

**Command** ([[Update CloudTrail for example_trail in eu-west region without including global service events and not multi-region]]):

```bash
aws cloudtrail update-trail --name example_trail --no-include-global-service-event --no-is-multi-region --region=eu-west
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Internal Spearphishing|T1534 - Internal Spearphishing]]

## Commands Used

- [[Update CloudTrail for example_trail in eu-west region without including global service events and not multi-region]]

## Tags

- [[CloudTrail]]
- [[Disable CloudTrail on specific regions]]
- [[RDS - Relational Database Service]]
- [[Userful Commands]]
