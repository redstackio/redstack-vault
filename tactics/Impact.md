---
id: eea7033c-5b1a-447d-8c42-1de63dad9649
name: Impact
type: tactic
mitre_id: TA0040
mitre_url: null
created_at: '2019-08-28T21:17:34.857247+00:00'
updated_at: '2023-05-29T16:48:53.579491+00:00'
techniques:
- '[[Account Access Removal|T1531 - Account Access Removal]]'
- '[[Data Destruction|T1485 - Data Destruction]]'
- '[[Data Encrypted for Impact|T1486 - Data Encrypted for Impact]]'
- '[[Data Manipulation|T1565 - Data Manipulation]]'
- '[[Defacement|T1491 - Defacement]]'
- '[[Disk Content Wipe|T1488 - Disk Content Wipe]]'
- '[[Disk Structure Wipe|T1487 - Disk Structure Wipe]]'
- '[[Disk Wipe|T1561 - Disk Wipe]]'
- '[[Endpoint Denial of Service|T1499 - Endpoint Denial of Service]]'
- '[[Firmware Corruption|T1495 - Firmware Corruption]]'
- '[[Inhibit System Recovery|T1490 - Inhibit System Recovery]]'
- '[[Network Denial of Service|T1498 - Network Denial of Service]]'
- '[[Resource Hijacking|T1496 - Resource Hijacking]]'
- '[[Runtime Data Manipulation|T1494 - Runtime Data Manipulation]]'
- '[[Service Stop|T1489 - Service Stop]]'
- '[[Stored Data Manipulation|T1492 - Stored Data Manipulation]]'
- '[[System Shutdown/Reboot|T1529 - System Shutdown/Reboot]]'
- '[[Transmitted Data Manipulation|T1493 - Transmitted Data Manipulation]]'
procedures:
- '[[Abusing Backup Operators Group for Sensitive File Access]]'
- '[[Abusing coredumps and core_pattern in Docker containers]]'
- '[[Abusing DNSAdmins Group to Change DNS Service DLL]]'
- '[[Abusing Group Policy Objects with StandIn to Manage Local Administrators and
  User Rights]]'
- '[[Abusing Shadow Copies for Privilege Escalation]]'
- '[[Active Directory Account Enumeration using CrackMapExec]]'
- '[[Active Directory User Enumeration]]'
- '[[AWS Delete EBS Volumes]]'
- '[[AWS Delete File from S3 Bucket]]'
- '[[Billion Laugh Attack to Perform Denial of Service using XML External Entity]]'
- '[[Copying EC2 Instances using AMI Image in AWS]]'
- '[[Docker Security Assessment]]'
- '[[Exploiting .NET BinaryFormatter Deserialization]]'
- '[[HTTP/2 Request Smuggling]]'
- '[[Jinja2 Config Information Extraction]]'
- '[[Lessjs Server Side Template Injection via Inline Import]]'
- '[[Linux - Docker Privilege Escalation]]'
- '[[Race Condition Turbo Intruder Attack]]'
- '[[SQL Injection WAF Bypass]]'
- '[[SSRF for AWS Metadata and User Data Commands]]'
- '[[SSRF URL for Google Cloud Instances - Add SSH Key]]'
- '[[Subdomain CSRF Attack]]'
- '[[Subdomain CSRF Attack]]'
- '[[XML Billion Laughs Attack with Delayed Interpretation]]'
---

# Impact

**MITRE ID**: TA0040

## Description

The Impact tactic represents techniques whose primary objective directly reduces the availability or integrity of a system, service, or network; including manipulation of data to impact a business or operational process. These techniques may represent an adversary's end goal, or provide cover for a breach of confidentiality.

## Techniques

This tactic includes 18 techniques:

- [[Account Access Removal|T1531 - Account Access Removal]]
- [[Data Destruction|T1485 - Data Destruction]]
- [[Data Encrypted for Impact|T1486 - Data Encrypted for Impact]]
- [[Data Manipulation|T1565 - Data Manipulation]]
- [[Defacement|T1491 - Defacement]]
- [[Disk Content Wipe|T1488 - Disk Content Wipe]]
- [[Disk Structure Wipe|T1487 - Disk Structure Wipe]]
- [[Disk Wipe|T1561 - Disk Wipe]]
- [[Endpoint Denial of Service|T1499 - Endpoint Denial of Service]]
- [[Firmware Corruption|T1495 - Firmware Corruption]]
- [[Inhibit System Recovery|T1490 - Inhibit System Recovery]]
- [[Network Denial of Service|T1498 - Network Denial of Service]]
- [[Resource Hijacking|T1496 - Resource Hijacking]]
- [[Runtime Data Manipulation|T1494 - Runtime Data Manipulation]]
- [[Service Stop|T1489 - Service Stop]]
- [[Stored Data Manipulation|T1492 - Stored Data Manipulation]]
- [[System Shutdown/Reboot|T1529 - System Shutdown/Reboot]]
- [[Transmitted Data Manipulation|T1493 - Transmitted Data Manipulation]]

## Related Procedures

There are 24 procedures implementing this tactic:

- [[Abusing Backup Operators Group for Sensitive File Access]]
- [[Abusing coredumps and core_pattern in Docker containers]]
- [[Abusing DNSAdmins Group to Change DNS Service DLL]]
- [[Abusing Group Policy Objects with StandIn to Manage Local Administrators and User Rights]]
- [[Abusing Shadow Copies for Privilege Escalation]]
- [[Active Directory Account Enumeration using CrackMapExec]]
- [[Active Directory User Enumeration]]
- [[AWS Delete EBS Volumes]]
- [[AWS Delete File from S3 Bucket]]
- [[Billion Laugh Attack to Perform Denial of Service using XML External Entity]]
- [[Copying EC2 Instances using AMI Image in AWS]]
- [[Docker Security Assessment]]
- [[Exploiting .NET BinaryFormatter Deserialization]]
- [[HTTP/2 Request Smuggling]]
- [[Jinja2 Config Information Extraction]]
- [[Lessjs Server Side Template Injection via Inline Import]]
- [[Linux - Docker Privilege Escalation]]
- [[Race Condition Turbo Intruder Attack]]
- [[SQL Injection WAF Bypass]]
- [[SSRF for AWS Metadata and User Data Commands]]

*...and 4 more*
