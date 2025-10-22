---
id: cd1b027b-19d3-4292-842e-f7a5fe718c9e
name: Disabling CloudTrail Trail
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.135138+00:00'
updated_at: '2023-04-10T20:20:25.021858+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Internal Spearphishing|T1534 - Internal Spearphishing]]'
tags:
- '[[CloudTrail]]'
- '[[Disabling CloudTrail]]'
- '[[RDS - Relational Database Service]]'
- '[[Userful Commands]]'
commands:
- '[[Delete AWS CloudTrail example_trail]]'
---

# Disabling CloudTrail Trail

## Summary

Disabling CloudTrail can be used as a defense evasion technique by an attacker to hide their activities from security monitoring tools. CloudTrail is a service that records AWS API calls and can be used to detect suspicious or malicious activity. By disabling CloudTrail logging, an attacker can avo

## Description

# Description

Disabling CloudTrail can be used as a defense evasion technique by an attacker to hide their activities from security monitoring tools. CloudTrail is a service that records AWS API calls and can be used to detect suspicious or malicious activity. By disabling CloudTrail logging, an attacker can avoid detection and make it more difficult for defenders to identify and respond to their actions.

To disable CloudTrail logging, an attacker can use the 'Delete AWS CloudTrail Trail' command. This will remove the CloudTrail trail and stop all logging of AWS API calls.

Disabling CloudTrail logging can be valuable for an attacker because it allows them to operate undetected and avoid triggering alerts that could lead to their discovery.

## Requirements

1. Access to an AWS account with permissions to delete CloudTrail trails

## Defense

1. Monitor CloudTrail logs for suspicious activity, and investigate any gaps in logging

1. Enable CloudTrail log file validation to ensure the integrity of log files

1. Restrict access to the CloudTrail service and trails to only authorized users and roles

## Objectives

1. Disable CloudTrail logging to avoid detection and operate undetected

# Instructions

1. To delete an AWS CloudTrail trail, run the following command:

**Code**: [[aws cloudtrail delete-trail --name example_trail -]]

> This command will delete the CloudTrail trail with the name 'example_trail'. The '--profile' flag is optional and is used to specify the name of the AWS CLI profile to use. If this flag is not used, the default profile will be used.

Note: Deleting a trail will permanently delete all of the trail's log files and cannot be undone. Make sure you have exported any logs you need before deleting a trail.

**Command** ([[Delete AWS CloudTrail example_trail]]):

```bash
aws cloudtrail delete-trail --name example_trail --profile name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Internal Spearphishing|T1534 - Internal Spearphishing]]

## Commands Used

- [[Delete AWS CloudTrail example_trail]]

## Tags

- [[CloudTrail]]
- [[Disabling CloudTrail]]
- [[RDS - Relational Database Service]]
- [[Userful Commands]]
