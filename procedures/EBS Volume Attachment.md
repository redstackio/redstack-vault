---
id: dd3b2a59-92d1-44e5-bece-906ee29519ae
name: EBS Volume Attachment
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.830957+00:00'
updated_at: '2023-04-10T20:20:08.011206+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Data Transfer Size Limits|T1030 - Data Transfer Size Limits]]'
- '[[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute Infrastructure]]'
sub_techniques:
- '[[Create Cloud Instance|T1578.002 - Create Cloud Instance]]'
tags:
- '[[Attaching the volume to an instance]]'
- '[[Elastic Block Store]]'
- '[[Exploitation & Data Exfiltration]]'
commands:
- '[[Attach EBS volume to EC2 instance]]'
---

# EBS Volume Attachment

## Summary

Elastic Block Store (EBS) is a scalable block storage service used by Amazon Web Services (AWS) to provide persistent storage for EC2 instances. The Attach Volume to EC2 Instance command allows users to attach an EBS volume to an EC2 instance. This procedure can be exploited by an attacker to gain 

## Description

# Description

Elastic Block Store (EBS) is a scalable block storage service used by Amazon Web Services (AWS) to provide persistent storage for EC2 instances. The Attach Volume to EC2 Instance command allows users to attach an EBS volume to an EC2 instance. This procedure can be exploited by an attacker to gain access to sensitive data stored on the EBS volume or to exfiltrate data from the volume. By attaching the volume to an instance, the attacker can gain access to the file system and data stored on the volume. This procedure can be used to execute malicious code or to steal sensitive data.

## Requirements

1. Access to AWS console or API

1. Authenticated access to the EC2 instance

1. Permissions to attach EBS volumes to EC2 instances

## Defense

1. Limit permissions to attach EBS volumes to EC2 instances

1. Implement network segmentation to limit access to EBS volumes

1. Monitor EBS volume attachment events for suspicious activity

## Objectives

1. Gain access to sensitive data stored on the EBS volume

1. Exfiltrate data from the EBS volume

# Instructions

1. To attach an Amazon EBS volume to an EC2 instance, use the attach-volume command. This command attaches the specified EBS volume to the specified EC2 instance, exposing the volume using the specified device name.

The attach-volume command requires the following arguments: 

1. volume-id: The ID of the EBS volume to attach. 
2. instance-id: The ID of the EC2 instance to attach the EBS volume to. 
3. device: The device name to expose the EBS volume as on the instance. This can be any valid device name that is not already in use by the instance.

**Command** ([[Attach EBS volume to EC2 instance]]):

```bash
aws ec2 attach-volume --volume-id VolumeID --instance-id InstanceID --device /dev/sdfd -> Can be other value
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Data Transfer Size Limits|T1030 - Data Transfer Size Limits]]
- [[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute Infrastructure]]

### Sub-Techniques

- [[Create Cloud Instance|T1578.002 - Create Cloud Instance]]

## Commands Used

- [[Attach EBS volume to EC2 instance]]

## Tags

- [[Attaching the volume to an instance]]
- [[Elastic Block Store]]
- [[Exploitation & Data Exfiltration]]
