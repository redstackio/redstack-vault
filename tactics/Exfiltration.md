---
id: 1325db3d-4db0-41b0-ab0f-ba17a754aae6
name: Exfiltration
type: tactic
mitre_id: TA0010
mitre_url: null
created_at: '2019-08-28T21:17:35.822702+00:00'
updated_at: '2023-05-29T16:48:53.579491+00:00'
techniques:
- '[[Automated Exfiltration|T1020 - Automated Exfiltration]]'
- '[[Data Compressed|T1002 - Data Compressed]]'
- '[[Data Encrypted|T1022 - Data Encrypted]]'
- '[[Data Transfer Size Limits|T1030 - Data Transfer Size Limits]]'
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
- '[[Exfiltration Over Command and Control Channel|T1041 - Exfiltration Over Command
  and Control Channel]]'
- '[[Exfiltration Over Other Network Medium|T1011 - Exfiltration Over Other Network
  Medium]]'
- '[[Exfiltration Over Physical Medium|T1052 - Exfiltration Over Physical Medium]]'
- '[[Exfiltration Over Web Service|T1567 - Exfiltration Over Web Service]]'
- '[[Scheduled Transfer|T1029 - Scheduled Transfer]]'
- '[[Transfer Data to Cloud Account|T1537 - Transfer Data to Cloud Account]]'
procedures:
- '[[Active Directory SCCM Loot Inventory and Download]]'
- '[[AWS KMS Decrypt Exfiltration]]'
- '[[AWS Private Route to Nat Gateway]]'
- '[[AWS S3 Download by Authenticated User]]'
- '[[AWS S3 Secret Text Retrieval - Public Access Data Exfiltration]]'
- '[[AWS S3 Time-Based URL Exfiltration]]'
- '[[AWS Secrets Manager Credential Exfiltration]]'
- '[[Azure AD Connect PTA Backdoor Installation and Log Retrieval]]'
- '[[Azure Storage Blob Download]]'
- '[[Blind XSS Data Exfiltration]]'
- '[[Blind XXE Data Exfiltration via OOB Attack]]'
- '[[Blind XXE Out-of-Band Data Exfiltration]]'
- '[[Chisel Port Forwarding and SOCKS Proxy Network Pivoting]]'
- '[[Cobalt Strike VPN & Pivots]]'
- '[[Create a Windows SMB Share with PowerShell]]'
- '[[DNS Data Exfiltration with Command Injection]]'
- '[[DNS Poisoning and Credential Dumping via mitm6 Relay Attack]]'
- '[[Download all files from Amazon S3 Bucket]]'
- '[[Download all files from Amazon S3 Bucket]]'
- '[[Download Files and Folders Recursively from FTP]]'
- '[[EBS Volume Attachment]]'
- '[[Exfiltrate Data Using Ping]]'
- '[[File Retrieval via XXE Injection]]'
- '[[GitTools Insecure Source Code Management]]'
- '[[IAM-Based Authentication Data Exfiltration via RDS]]'
- '[[IAM-Based Authentication for RDS MySQL Database]]'
- '[[Kubernetes etcd API Enumeration]]'
- '[[Linux Meterpreter Reverse TCP Shell]]'
- '[[Local DTD Injection in Citrix XenMobile Server]]'
- '[[Mercurial Source Code Extraction with rip-hg.pl]]'
- '[[Meterpreter File Transfer]]'
- '[[Mount a Windows SMB Share with PowerShell (Authenticated)]]'
- '[[MSSQL Out of Band DNS Exfiltration]]'
- '[[MSSQL UNC Path Out-of-Band Data Retrieval]]'
- '[[MYSQL Injection Out-of-Band Data Exfiltration]]'
- '[[MYSQL Injection with Out of Band DNS Exfiltration]]'
- '[[.NET Serialization Tools Exploitation]]'
- '[[Node Deserialization Exploit using Funcster]]'
- '[[Perl Bind Shell]]'
- '[[Portforwarding with Meterpreter]]'
- '[[PostgreSQL Time Based Injection for Database Dump]]'
- '[[PostgreSQL Time Based Table Dump]]'
- '[[Python Pickle Deserialization]]'
- '[[RDS List Instance Details Exfiltration]]'
- '[[RDS Password-based Authentication Data Exfiltration]]'
- '[[Remote File Read via Jinja2 Server-Side Template Injection]]'
- '[[Springboot-Actuator Health Monitoring]]'
- '[[Windows Local DTD and Side Channel Leak to Disclose HTTP Response/File Contents]]'
- '[[XXE Injection in SOAP Messages]]'
- '[[YAML Deserialization in Ruby]]'
- '[[YAML Deserialization via SnakeYAML]]'
---

# Exfiltration

**MITRE ID**: TA0010

## Description

Exfiltration refers to techniques and attributes that result or aid in the adversary removing files and information from a target network. This category also covers locations on a system or network where the adversary may look for information to exfiltrate.

## Techniques

This tactic includes 11 techniques:

- [[Automated Exfiltration|T1020 - Automated Exfiltration]]
- [[Data Compressed|T1002 - Data Compressed]]
- [[Data Encrypted|T1022 - Data Encrypted]]
- [[Data Transfer Size Limits|T1030 - Data Transfer Size Limits]]
- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]
- [[Exfiltration Over Command and Control Channel|T1041 - Exfiltration Over Command and Control Channel]]
- [[Exfiltration Over Other Network Medium|T1011 - Exfiltration Over Other Network Medium]]
- [[Exfiltration Over Physical Medium|T1052 - Exfiltration Over Physical Medium]]
- [[Exfiltration Over Web Service|T1567 - Exfiltration Over Web Service]]
- [[Scheduled Transfer|T1029 - Scheduled Transfer]]
- [[Transfer Data to Cloud Account|T1537 - Transfer Data to Cloud Account]]

## Related Procedures

There are 51 procedures implementing this tactic:

- [[Active Directory SCCM Loot Inventory and Download]]
- [[AWS KMS Decrypt Exfiltration]]
- [[AWS Private Route to Nat Gateway]]
- [[AWS S3 Download by Authenticated User]]
- [[AWS S3 Secret Text Retrieval - Public Access Data Exfiltration]]
- [[AWS S3 Time-Based URL Exfiltration]]
- [[AWS Secrets Manager Credential Exfiltration]]
- [[Azure AD Connect PTA Backdoor Installation and Log Retrieval]]
- [[Azure Storage Blob Download]]
- [[Blind XSS Data Exfiltration]]
- [[Blind XXE Data Exfiltration via OOB Attack]]
- [[Blind XXE Out-of-Band Data Exfiltration]]
- [[Chisel Port Forwarding and SOCKS Proxy Network Pivoting]]
- [[Cobalt Strike VPN & Pivots]]
- [[Create a Windows SMB Share with PowerShell]]
- [[DNS Data Exfiltration with Command Injection]]
- [[DNS Poisoning and Credential Dumping via mitm6 Relay Attack]]
- [[Download all files from Amazon S3 Bucket]]
- [[Download all files from Amazon S3 Bucket]]
- [[Download Files and Folders Recursively from FTP]]

*...and 31 more*
