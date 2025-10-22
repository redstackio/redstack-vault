---
id: 0a8960d1-41ef-4494-8a4c-cad0f0b1eeab
name: Collection
type: tactic
mitre_id: TA0009
mitre_url: null
created_at: '2019-08-28T21:17:19.150471+00:00'
updated_at: '2023-05-29T16:48:53.579491+00:00'
techniques:
- '[[Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]'
- '[[Archive Collected Data|T1560 - Archive Collected Data]]'
- '[[Audio Capture|T1123 - Audio Capture]]'
- '[[Automated Collection|T1119 - Automated Collection]]'
- '[[Clipboard Data|T1115 - Clipboard Data]]'
- '[[Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
- '[[Data from Configuration Repository|T1602 - Data from Configuration Repository]]'
- '[[Data from Information Repositories|T1213 - Data from Information Repositories]]'
- '[[Data from Local System|T1005 - Data from Local System]]'
- '[[Data from Network Shared Drive|T1039 - Data from Network Shared Drive]]'
- '[[Data from Removable Media|T1025 - Data from Removable Media]]'
- '[[Data Staged|T1074 - Data Staged]]'
- '[[Email Collection|T1114 - Email Collection]]'
- '[[Input Capture|T1056 - Input Capture]]'
- '[[Man in the Browser|T1185 - Man in the Browser]]'
- '[[Screen Capture|T1113 - Screen Capture]]'
- '[[Video Capture|T1125 - Video Capture]]'
procedures:
- '[[Active Directory SCCM Loot Inventory and Download]]'
- '[[AWS API Key Enumeration]]'
- '[[AWS Extract Backup to EC2 Instance]]'
- '[[AWS Extract Backup to EC2 Instance]]'
- '[[AWS Fargate Container Credentials Theft]]'
- '[[AWS IAM Policy Information Gathering]]'
- '[[AWS KMS Key Listing]]'
- '[[AWS Managed Policy Version Enumeration]]'
- '[[AWS Managed Policy Version Enumeration]]'
- '[[AWS S3 Bucket Data Exfiltration]]'
- '[[AWS S3 Bucket Data Exfiltration]]'
- '[[AWS S3 Bucket Listing Exploitation]]'
- '[[AWS Userdata Retrieval via Instance Metadata Service]]'
- '[[BigQuery SQL Injection Attack]]'
- '[[Browse an SMB Share]]'
- '[[Cloud Instance Rancher Metadata Retrieval via SSRF]]'
- '[[Cloud Security Assessment and Auditing]]'
- '[[Creating and Importing a CLR Assembly for MSSQL Server]]'
- '[[DirtyCow Kernel Exploit for Linux Privilege Escalation]]'
- '[[Dump a Process''s Memory (PowerShell)]]'
- '[[EBS Snapshot Creation]]'
- '[[Enclosed Alphanumeric Server-Side Request Forgery]]'
- '[[Enumerate a MS Access .mdb Database and Tables]]'
- '[[Enumerate Local Users'' PowerShell History]]'
- '[[Extract E-mails and Attachments from MS .PST Files]]'
- '[[Extracting Database Information using MySQL Union Based Injection]]'
- '[[Find Interesting Strings in a Raw Memory Dump]]'
- '[[Git Repository Dumping with GoGitDumper]]'
- '[[Git Secrets Harvesting with Yar]]'
- '[[Google BigQuery SQL Injection Detection]]'
- '[[GraphQL Data Extraction]]'
- '[[Jinja2 Server Side Template Injection - Dump All Used Classes]]'
- '[[Lessjs Server Side Template Injection via Inline Import]]'
- '[[LFI to RCE via Mail Log File Inclusion]]'
- '[[LFI to RCE via SSH Log File Inclusion]]'
- '[[Linked Database Table Enumeration]]'
- '[[Linux - Privilege Escalation: Looting for Old Passwords]]'
- '[[Linux - Privilege Escalation via Writable /etc/passwd]]'
- '[[Linux Privilege Escalation - Writable Files Escalation]]'
- '[[Log4Shell Environment Variables Exfiltration]]'
- '[[Log4Shell Environment Variables Exfiltration]]'
- '[[Log4Shell Environment Variables Exfiltration]]'
- '[[Mounting EBS Volume to EC2 Linux Instance]]'
- '[[MSSQL Server - Identify Sensitive Information - Get Tables and Column Details]]'
- '[[MSSQL Server Password Retrieval and Cracking]]'
- '[[Netdoc SSRF via URL Scheme]]'
- '[[Network Discovery Responder]]'
- '[[NoSQL Injection via SSJI Exploit]]'
- '[[Open URL Redirection via Injection Parameters]]'
- '[[Oracle SQL List Tables and Columns]]'
- '[[Password Looting from SharePoint and SMB Shares]]'
- '[[Recursively Download Files From an SMB Share]]'
- '[[SAML Injection Authentication Bypass]]'
- '[[SAML Injection for Authentication Bypass and Signature Stripping with Admin NameID]]'
- '[[Search SMB by Filename and Download Matches]]'
- '[[Server-Side Request Forgery on Cloud Instances and HP Helion]]'
- '[[SMB and HTTP Relay Attack]]'
- '[[Snapshot Enumeration]]'
- '[[SQLmap MySQL Database Dump]]'
- '[[SSL MITM Network Discovery with OpenSSL]]'
- '[[SSRF Attack on Alibaba Cloud Instances]]'
- '[[SSRF Exploiting URL Parser Bypass]]'
- '[[SSRF URL for Google Cloud Instances - Add SSH Key]]'
- '[[SSRF URL for Oracle Cloud Instances via AWS Instance Metadata and User Data]]'
- '[[Tabnabbing Link Format Hunting]]'
- '[[Unzip an AES Encrypted Zip Archive (Linux)]]'
- '[[Web Enumeration and Backup File Discovery]]'
- '[[XML External Entity Injection to Disclose HTTP Response]]'
- '[[XML External Entity WAF Bypass via Character Encoding]]'
- '[[XML External Entity (XXE) Injection using Various Tools]]'
- '[[XSLT Injection for File Read and SSRF]]'
- '[[XSS Cookie and Access Token Grabber]]'
- '[[XXE in DTD File Contents Extractor]]'
---

# Collection

**MITRE ID**: TA0009

## Description

Collection consists of techniques used to identify and gather information, such as sensitive files, from a target network prior to exfiltration. This category also covers locations on a system or network where the adversary may look for information to exfiltrate.

## Techniques

This tactic includes 17 techniques:

- [[Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]
- [[Archive Collected Data|T1560 - Archive Collected Data]]
- [[Audio Capture|T1123 - Audio Capture]]
- [[Automated Collection|T1119 - Automated Collection]]
- [[Clipboard Data|T1115 - Clipboard Data]]
- [[Data from Cloud Storage|T1530 - Data from Cloud Storage]]
- [[Data from Configuration Repository|T1602 - Data from Configuration Repository]]
- [[Data from Information Repositories|T1213 - Data from Information Repositories]]
- [[Data from Local System|T1005 - Data from Local System]]
- [[Data from Network Shared Drive|T1039 - Data from Network Shared Drive]]
- [[Data from Removable Media|T1025 - Data from Removable Media]]
- [[Data Staged|T1074 - Data Staged]]
- [[Email Collection|T1114 - Email Collection]]
- [[Input Capture|T1056 - Input Capture]]
- [[Man in the Browser|T1185 - Man in the Browser]]
- [[Screen Capture|T1113 - Screen Capture]]
- [[Video Capture|T1125 - Video Capture]]

## Related Procedures

There are 73 procedures implementing this tactic:

- [[Active Directory SCCM Loot Inventory and Download]]
- [[AWS API Key Enumeration]]
- [[AWS Extract Backup to EC2 Instance]]
- [[AWS Extract Backup to EC2 Instance]]
- [[AWS Fargate Container Credentials Theft]]
- [[AWS IAM Policy Information Gathering]]
- [[AWS KMS Key Listing]]
- [[AWS Managed Policy Version Enumeration]]
- [[AWS Managed Policy Version Enumeration]]
- [[AWS S3 Bucket Data Exfiltration]]
- [[AWS S3 Bucket Data Exfiltration]]
- [[AWS S3 Bucket Listing Exploitation]]
- [[AWS Userdata Retrieval via Instance Metadata Service]]
- [[BigQuery SQL Injection Attack]]
- [[Browse an SMB Share]]
- [[Cloud Instance Rancher Metadata Retrieval via SSRF]]
- [[Cloud Security Assessment and Auditing]]
- [[Creating and Importing a CLR Assembly for MSSQL Server]]
- [[DirtyCow Kernel Exploit for Linux Privilege Escalation]]
- [[Dump a Process's Memory (PowerShell)]]

*...and 53 more*
