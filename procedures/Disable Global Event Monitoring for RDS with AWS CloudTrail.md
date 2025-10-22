---
id: 1cfb27e7-1525-4a31-9728-46f3cfc9631f
name: Disable Global Event Monitoring for RDS with AWS CloudTrail
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.161052+00:00'
updated_at: '2023-04-10T20:20:25.379104+00:00'
tags:
- '[[CloudTrail]]'
- '[[Disable monitoring of events from global events]]'
- '[[RDS - Relational Database Service]]'
- '[[Useful Commands]]'
commands:
- '[[Update CloudTrail]]'
---

# Disable Global Event Monitoring for RDS with AWS CloudTrail

## Summary

This procedure aims to disable monitoring of events from global events for RDS with AWS CloudTrail. This can be useful for an attacker to evade detection and cover their tracks. By disabling this monitoring, an attacker can perform malicious actions on the RDS instance without being detected by the

## Description

# Description

This procedure aims to disable monitoring of events from global events for RDS with AWS CloudTrail. This can be useful for an attacker to evade detection and cover their tracks. By disabling this monitoring, an attacker can perform malicious actions on the RDS instance without being detected by the security team. From a technical standpoint, this procedure involves updating the AWS CloudTrail configuration to disable global event monitoring. From a business perspective, this procedure can help organizations protect their sensitive data and prevent unauthorized access to their RDS instances.

## Requirements

1. AWS CloudTrail configured for RDS monitoring

1. Access to AWS CloudTrail configuration

## Defense

1. Regularly review CloudTrail logs for any suspicious activity

1. Implement least privilege access control for AWS CloudTrail configuration

1. Enable CloudTrail multi-region logging to ensure visibility across all regions

## Objectives

1. Disable monitoring of events from global events for RDS with AWS CloudTrail

1. Evade detection and cover attacker's tracks

# Instructions

1. To update the configuration of an AWS CloudTrail, use the following command:

**Code**: [[aws cloudtrail update-trail --name example_trail -]]

> This command updates the configuration of an existing AWS CloudTrail. The `--name` option specifies the name of the trail to be updated. The `--no-include-global-service-event` option disables the inclusion of global service events in the trail. By default, global service events are included in the trail, but this can be disabled by setting this option to `true`. Other options can be used to update other aspects of the trail configuration, such as the S3 bucket where the trail logs are stored, or the CloudWatch Logs group where the trail logs are delivered. Refer to the AWS documentation for more information on the available options.

**Command** ([[Update CloudTrail]]):

```bash
aws cloudtrail update-trail --name example_trail --no-include-global-service-event
```

## Commands Used

- [[Update CloudTrail]]

## Tags

- [[CloudTrail]]
- [[Disable monitoring of events from global events]]
- [[RDS - Relational Database Service]]
- [[Useful Commands]]
