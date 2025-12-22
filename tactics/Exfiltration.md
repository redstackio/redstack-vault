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
- '[[Active-Directory-SCCM-Loot-Inventory-and-Download]]'
- '[[AWS-KMS-Decrypt-Exfiltration]]'
- '[[Configure-Private-Subnet-Route-to-NAT-Gateway]]'
- '[[AWS-S3-Download-by-Authenticated-User]]'
- '[[aws-s3-secret-text-retrieval-public-access-data-exfiltration]]'
- '[[Generate-AWS-S3-Pre-Signed-URL-for-Exfiltration]]'
- '[[AWS-Secrets-Manager-Credential-Exfiltration]]'
- '[[Install-Azure-AD-Connect-PTA-Backdoor-and-Retrieve-Logs]]'
- '[[Download-Azure-Storage-Blob]]'
- '[[Blind-XSS-Data-Exfiltration]]'
- '[[Blind-XXE-Data-Exfiltration-via-OOB-Attack]]'
- '[[Blind-XXE-Out-of-Band-Data-Exfiltration]]'
- '[[chisel-port-forwarding-and-socks-proxy-network-pivoting]]'
- '[[Establish-VPN-Like-Connection-and-Pivot-Using-Cobalt-Strike]]'
- '[[Create-Windows-SMB-Share-with-PowerShell]]'
- '[[DNS-Data-Exfiltration-via-Command-Injection]]'
- '[[dns-poisoning-and-credential-dumping-via-mitm6-relay-attack]]'
- '[[Download-All-Files-from-Misconfigured-S3-Bucket]]'
- '[[Download-All-Files-from-Misconfigured-S3-Bucket]]'
- '[[Download-Files-Recursively-from-FTP]]'
- '[[Attach-EBS-Volume-to-EC2-Instance]]'
- '[[Exfiltrate-Data-Using-Ping]]'
- '[[File-Retrieval-via-XXE-Injection]]'
- '[[Exploit-Insecure-Git-Repository-with-GitTools]]'
- '[[IAM-Based-Authentication-Data-Exfiltration-via-RDS]]'
- '[[IAM-Authentication-for-RDS-MySQL-Database]]'
- '[[Kubernetes-Etcd-API-Enumeration]]'
- '[[Establish-Linux-Meterpreter-Reverse-TCP-Shell]]'
- '[[Local-DTD-Injection-in-Citrix-XenMobile-Server]]'
- '[[mercurial-source-code-extraction-with-rip-hg-pl]]'
- '[[Meterpreter-File-Transfer]]'
- '[[Mount-Windows-SMB-Share-with-PowerShell-Authenticated]]'
- '[[mssql-out-of-band-dns-exfiltration]]'
- '[[MSSQL-UNC-Path-Out-of-Band-Data-Retrieval]]'
- '[[MySQL-Injection-Out-of-Band-Data-Exfiltration]]'
- '[[MySQL-SQL-Injection-for-Out-of-Band-DNS-Exfiltration]]'
- '[[.NET Serialization Tools Exploitation]]'
- '[[Node-Deserialization-Exploit-using-Funcster]]'
- '[[Create-Perl-Bind-Shell]]'
- '[[Meterpreter-Port-Forwarding-Setup]]'
- '[[PostgreSQL-Time-Based-Blind-Injection-for-Database-Dump]]'
- '[[PostgreSQL-Time-Based-Blind-SQL-Injection-for-Table-Dump]]'
- '[[Exploit-Python-Pickle-Deserialization-for-RCE]]'
- '[[List-AWS-RDS-DB-Instances-for-Exfiltration]]'
- '[[Exfiltrate-Data-from-AWS-RDS-via-Password-Authentication]]'
- '[[Remote-File-Read-via-Jinja2-SSTI]]'
- '[[Enumerate-Spring-Boot-Actuator-Health-Endpoint]]'
- '[[Windows Local DTD and Side Channel Leak to Disclose HTTP Response/File Contents]]'
- '[[XXE-Injection-in-SOAP-Messages]]'
- '[[Exploit-YAML-Deserialization-in-Ruby-for-RCE]]'
- '[[Exploit-YAML-Deserialization-with-SnakeYAML]]'
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

- [[Active-Directory-SCCM-Loot-Inventory-and-Download]]
- [[AWS-KMS-Decrypt-Exfiltration]]
- [[Configure-Private-Subnet-Route-to-NAT-Gateway]]
- [[AWS-S3-Download-by-Authenticated-User]]
- [[aws-s3-secret-text-retrieval-public-access-data-exfiltration]]
- [[Generate-AWS-S3-Pre-Signed-URL-for-Exfiltration]]
- [[AWS-Secrets-Manager-Credential-Exfiltration]]
- [[Install-Azure-AD-Connect-PTA-Backdoor-and-Retrieve-Logs]]
- [[Download-Azure-Storage-Blob]]
- [[Blind-XSS-Data-Exfiltration]]
- [[Blind-XXE-Data-Exfiltration-via-OOB-Attack]]
- [[Blind-XXE-Out-of-Band-Data-Exfiltration]]
- [[chisel-port-forwarding-and-socks-proxy-network-pivoting]]
- [[Establish-VPN-Like-Connection-and-Pivot-Using-Cobalt-Strike]]
- [[Create-Windows-SMB-Share-with-PowerShell]]
- [[DNS-Data-Exfiltration-via-Command-Injection]]
- [[dns-poisoning-and-credential-dumping-via-mitm6-relay-attack]]
- [[Download-All-Files-from-Misconfigured-S3-Bucket]]
- [[Download-All-Files-from-Misconfigured-S3-Bucket]]
- [[Download-Files-Recursively-from-FTP]]

*...and 31 more*


