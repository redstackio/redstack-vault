---
id: 51803bb8-456c-4478-b57f-f8f62e5df6fa
name: AWS Delete EBS Volumes
type: procedure
verified: false
submitted: false
created_at: '2020-07-31T04:25:34.168246+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
techniques:
- '[[Data Destruction|T1485 - Data Destruction]]'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[Deleting a Volume]]'
---

# AWS Delete EBS Volumes

## Summary

You will probably never need to delete an EBS volume on a pentest, but a client might ask you to delete a target "TEST" EBS Volume so here you are. We also included scripts for SecDevOps to automate the deletion of unused volumes, we recommend doing this on a cronjob to keep old volumes cleaned up 

## Description

# Description

You will probably never need to delete an EBS volume on a pentest, but a client might ask you to delete a target "TEST" EBS Volume so here you are.

We also included scripts for SecDevOps to automate the deletion of unused volumes, we recommend doing this on a cronjob to keep old volumes cleaned up from the attack surface.

# Instructions

1. Delete an EBS volume using the volume ID and Region



**Command** ([[Deleting a Volume]]):

```bash
aws ec2 delete-volume --region $AWS_REGION --volume-id $AWS_VOLUME_ID

```







2. (Optional) Deleting Unused Volumes.



**Code**: [[
for x in $(aws ec2 describe-volumes --filters  Na]]





3. (Optional) Deleteing unused volumes with a specific AWS Profile



**Code**: [[
for x in $(aws ec2 describe-volumes --filters  Na]]





## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Impact|TA0040 - Impact]]

### Techniques

- [[Data Destruction|T1485 - Data Destruction]]

## Commands Used

- [[Deleting a Volume]]

## Tags

- [[AWS]]
- [[Cloud]]


