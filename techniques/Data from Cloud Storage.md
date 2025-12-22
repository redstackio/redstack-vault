---
id: 2c78770a-6dd1-4bf3-8c8b-f21515baa8b0
name: Data from Cloud Storage
type: technique
mitre_id: T1530
mitre_url: null
created_at: '2023-04-06T00:31:25.866939+00:00'
updated_at: '2023-04-06T03:56:38.806818+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
procedures:
- '[[AWS-API-Key-Enumeration]]'
- '[[AWS-Extract-EBS-Backup-to-EC2-Instance]]'
- '[[AWS-Extract-EBS-Backup-to-EC2-Instance]]'
- '[[Describe-AWS-KMS-Key]]'
- '[[Enumerate-AWS-IAM-Managed-Policy-Versions]]'
- '[[Enumerate-AWS-IAM-Managed-Policy-Versions]]'
- '[[Exfiltrate-AWS-S3-Data-via-EC2-SSRF]]'
- '[[Exfiltrate-AWS-S3-Data-via-EC2-SSRF]]'
- '[[List-Contents-of-Misconfigured-AWS-S3-Bucket]]'
- '[[Retrieve-AWS-EC2-User-Data-via-Instance-Metadata-Service]]'
- '[[Cloud-Instance-Rancher-Metadata-Retrieval-via-SSRF]]'
- '[[aws-cloud-security-assessment-and-auditing]]'
- '[[SQL-Injection-in-Google-BigQuery-for-Data-Exfiltration]]'
- '[[Mount-EBS-Volume-to-EC2-Linux-Instance]]'
- '[[Exploit-SSRF-to-Retrieve-AWS-Instance-Metadata]]'
- '[[Enumerate-AWS-EBS-Snapshots]]'
- '[[Exploit-SSRF-to-Add-SSH-Key-to-GCP-Instance]]'
- '[[Exploit-SSRF-to-Retrieve-AWS-Instance-Metadata]]'
- '[[Web-Enumeration-and-Backup-File-Discovery]]'
---

# Data from Cloud Storage

**MITRE ID**: T1530

## Description

Adversaries may access data from improperly secured cloud storage.

Many cloud service providers offer solutions for online data object storage such as Amazon S3, Azure Storage, and Google Cloud Storage. These solutions differ from other storage solutions (such as SQL or Elasticsearch) in that there is no overarching application. Data from these solutions can be retrieved directly using the cloud provider's APIs. 

In other cases, SaaS application providers such as Slack, Confluence, and Salesforce also provide cloud storage solutions as a peripheral use case of their platform. These cloud objects can be extracted directly from their associated application.(Citation: EA Hacked via Slack - June 2021)(Citation: SecureWorld - How Secure Is Your Slack Channel - Dec 2021)(Citation: HackerNews - 3 SaaS App Cyber Attacks - April 2022)(Citation: Dark Clouds_Usenix_Mulazzani_08_2011)

Adversaries may collect sensitive data from these cloud storage solutions. Providers typically offer security guides to help end users configure systems, though misconfigurations are a common problem.(Citation: Amazon S3 Security, 2019)(Citation: Microsoft Azure Storage Security, 2019)(Citation: Google Cloud Storage Best Practices, 2019) There have been numerous incidents where cloud storage has been improperly secured, typically by unintentionally allowing public access to unauthenticated users, overly-broad access by all users, or even access for any anonymous person outside the control of the Identity Access Management system without even needing basic user permissions.

This open access may expose various types of sensitive data, such as credit cards, personally identifiable information, or medical records.(Citation: Trend Micro S3 Exposed PII, 2017)(Citation: Wired Magecart S3 Buckets, 2019)(Citation: HIPAA Journal S3 Breach, 2017)(Citation: Rclone-mega-extortion_05_2021)

Adversaries may also obtain then abuse leaked credentials from source repositories, logs, or other means as a way to gain access to cloud storage objects.



## Tactics

- [[Collection|TA0009 - Collection]]

## Related Procedures (19)

- [[AWS-API-Key-Enumeration]]
- [[AWS-Extract-EBS-Backup-to-EC2-Instance]]
- [[AWS-Extract-EBS-Backup-to-EC2-Instance]]
- [[Describe-AWS-KMS-Key]]
- [[Enumerate-AWS-IAM-Managed-Policy-Versions]]
- [[Enumerate-AWS-IAM-Managed-Policy-Versions]]
- [[Exfiltrate-AWS-S3-Data-via-EC2-SSRF]]
- [[Exfiltrate-AWS-S3-Data-via-EC2-SSRF]]
- [[List-Contents-of-Misconfigured-AWS-S3-Bucket]]
- [[Retrieve-AWS-EC2-User-Data-via-Instance-Metadata-Service]]
- [[Cloud-Instance-Rancher-Metadata-Retrieval-via-SSRF]]
- [[aws-cloud-security-assessment-and-auditing]]
- [[SQL-Injection-in-Google-BigQuery-for-Data-Exfiltration]]
- [[Mount-EBS-Volume-to-EC2-Linux-Instance]]
- [[Exploit-SSRF-to-Retrieve-AWS-Instance-Metadata]]
- [[Enumerate-AWS-EBS-Snapshots]]
- [[Exploit-SSRF-to-Add-SSH-Key-to-GCP-Instance]]
- [[Exploit-SSRF-to-Retrieve-AWS-Instance-Metadata]]
- [[Web-Enumeration-and-Backup-File-Discovery]]


