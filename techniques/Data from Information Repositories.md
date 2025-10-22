---
id: 6e1735a9-5c3e-4f7f-a9f7-64e1253acfae
name: Data from Information Repositories
type: technique
mitre_id: T1213
mitre_url: null
created_at: '2019-08-28T21:17:39.592909+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
procedures:
- '[[AWS Fargate Container Credentials Theft]]'
- '[[DirtyCow Kernel Exploit for Linux Privilege Escalation]]'
- '[[Enclosed Alphanumeric Server-Side Request Forgery]]'
- '[[Git Secrets Harvesting with Yar]]'
- '[[GraphQL Data Extraction]]'
- '[[Lessjs Server Side Template Injection via Inline Import]]'
- '[[Linux - Privilege Escalation via Writable /etc/passwd]]'
- '[[Netdoc SSRF via URL Scheme]]'
- '[[Open URL Redirection via Injection Parameters]]'
- '[[SQLmap MySQL Database Dump]]'
- '[[SSRF Attack on Alibaba Cloud Instances]]'
- '[[SSRF Exploiting URL Parser Bypass]]'
- '[[Tabnabbing Link Format Hunting]]'
- '[[XSLT Injection for File Read and SSRF]]'
---

# Data from Information Repositories

**MITRE ID**: T1213

## Description

Adversaries may leverage information repositories to mine valuable information. Information repositories are tools that allow for storage of information, typically to facilitate collaboration or information sharing between users, and can store a wide variety of data that may aid adversaries in further objectives, or direct access to the target information.The following is a brief list of example information that may hold potential value to an adversary and may also be found on an information repository:Policies, procedures, and standardsPhysical / logical network diagramsSystem architecture diagramsTechnical system documentationTesting / development credentialsWork / project schedulesSource code snippetsLinks to network shares and other internal resourcesSpecific common information repositories include:Microsoft SharePointFound in many enterprise networks and often used to store and share significant amounts of documentation.Atlassian ConfluenceOften found in development environments alongside Atlassian JIRA, Confluence is generally used to store development-related documentation.

# Detection

As information repositories generally have a considerably large user base, detection of malicious use can be non-trivial. At minimum, access to information repositories performed by privileged users (for example, Active Directory Domain, Enterprise, or Schema Administrators) should be closely monitored and alerted upon, as these types of accounts should not generally used to access information repositories. If the capability exists, it may be of value to monitor and alert on users that are retrieving and viewing a large number of documents and pages; this behavior may be indicative of programmatic means being used to retrieve all data within the repository. In environments with high-maturity, it may be possible to leverage User-Behavioral Analytics (UBA) platforms to detect and alert on user based anomalies.

The user access logging within Microsoft's SharePoint can be configured to report access to certain pages and documents. [3] The user user access logging within Atlassian's Confluence can also be configured to report access to certain pages and documents through AccessLogFilter. [4] Additional log storage and analysis infrastructure will likely be required for more robust detection capabilities.

# Mitigation

To mitigate adversary access to information repositories for collection:

Develop and publish policies that define acceptable information to be storedAppropriate implementation of access control mechanisms that include both authentication and appropriate authorizationEnforce the principle of least-privilegePeriodic privilege review of accountsMitigate access to Valid Accounts that may be used to access repositories

# Footnotes

[1] Maccaglia, S. (2015, November 4). Evolving Threats: dissection of a CyberEspionage attack. Retrieved April 4, 2018.

[2] Smallridge, R. (2018, March 10). APT15 is alive and strong: An analysis of RoyalCli and RoyalDNS. Retrieved April 4, 2018.

[3] Microsoft. (2017, July 19). Configure audit settings for a site collection. Retrieved April 4, 2018.

[4] Atlassian. (2018, January 9). How to Enable User Access Logging. Retrieved April 4, 2018.

## Defense

To mitigate adversary access to information repositories for collection:

* Develop and publish policies that define acceptable information to be stored
* Appropriate implementation of access control mechanisms that include both authentication and appropr

## Tactics

- [[Collection|TA0009 - Collection]]

## Related Procedures (14)

- [[AWS Fargate Container Credentials Theft]]
- [[DirtyCow Kernel Exploit for Linux Privilege Escalation]]
- [[Enclosed Alphanumeric Server-Side Request Forgery]]
- [[Git Secrets Harvesting with Yar]]
- [[GraphQL Data Extraction]]
- [[Lessjs Server Side Template Injection via Inline Import]]
- [[Linux - Privilege Escalation via Writable /etc/passwd]]
- [[Netdoc SSRF via URL Scheme]]
- [[Open URL Redirection via Injection Parameters]]
- [[SQLmap MySQL Database Dump]]
- [[SSRF Attack on Alibaba Cloud Instances]]
- [[SSRF Exploiting URL Parser Bypass]]
- [[Tabnabbing Link Format Hunting]]
- [[XSLT Injection for File Read and SSRF]]
