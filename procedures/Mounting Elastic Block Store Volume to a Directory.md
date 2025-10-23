---
id: a11baa3b-8d0c-4d39-92fc-902391d0b7eb
name: Mounting Elastic Block Store Volume to a Directory
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.856825+00:00'
updated_at: '2023-04-10T20:20:57.615194+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute Infrastructure]]'
tags:
- '[[Elastic Block Store]]'
- '[[Exploitation & Data Exfiltration]]'
- '[[Mounting the volume]]'
commands:
- '[[Mount Device to Directory]]'
---

# Mounting Elastic Block Store Volume to a Directory

## Summary

Mounting an Elastic Block Store (EBS) volume to a directory is a common task for system administrators. Attackers can also leverage this functionality to persistently store and exfiltrate data from a compromised system. By mounting an EBS volume to a directory, an attacker can maintain access to st

## Description

# Description

Mounting an Elastic Block Store (EBS) volume to a directory is a common task for system administrators. Attackers can also leverage this functionality to persistently store and exfiltrate data from a compromised system. By mounting an EBS volume to a directory, an attacker can maintain access to stolen data even if the original system is taken offline. This technique can be used in conjunction with other tactics, such as drive-by compromise, to establish persistence and maintain access to a target environment.

From a technical perspective, mounting an EBS volume is a straightforward process that involves attaching a volume to an EC2 instance and then mounting it to a directory. Once the volume is mounted, an attacker can use it to store and exfiltrate data. From a business perspective, this technique can lead to data theft, intellectual property theft, and reputational damage.


 

## Requirements

1. Access to an EC2 instance

1. Authentication credentials with sufficient permissions to mount an EBS volume

 

## Defense

1. Implement least privilege access controls to limit the ability to mount EBS volumes

1. Monitor for unusual EBS volume activity, such as unexpected mounts or high volume of data being transferred

1. Regularly review and audit EBS volume usage to ensure that it aligns with business requirements

 

## Objectives

1. Establish persistence on a compromised system

1. Maintain access to stolen data even if the original system is taken offline

 

# Instructions

1. To mount a device to a directory, use the 'mount' command with the following syntax: 

sudo mount /dev/device_name /mount_point

Replace 'device_name' with the name of the device you want to mount and 'mount_point' with the directory where you want to mount it.

 

The 'mount' command is used to mount a file system or device to a directory in the file system. This allows you to access the contents of the device through the directory. The 'sudo' command is used to run the 'mount' command with root privileges, which is required to mount a device. The '/dev/sdfd' argument specifies the device you want to mount, and the '/directory' argument specifies the directory where you want to mount it.



**Command** ([[Mount Device to Directory]]):

```bash
sudo mount /dev/sdfd /directory
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute Infrastructure]]

## Commands Used

- [[Mount Device to Directory]]

## Tags

- [[Elastic Block Store]]
- [[Exploitation & Data Exfiltration]]
- [[Mounting the volume]]


