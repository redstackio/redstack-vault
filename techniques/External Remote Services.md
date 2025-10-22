---
id: 7992c680-cf86-4bc4-a97b-1accc1d849d8
name: External Remote Services
type: technique
mitre_id: T1133
mitre_url: null
created_at: '2019-08-28T21:17:41.057512+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[Cloud Instance SSRF through OpenStack Metadata URL]]'
- '[[CORS Misconfiguration Exploitation: Origin Reflection]]'
- '[[CORS Misconfiguration Exploitation: Origin Reflection]]'
- '[[CORS Misconfiguration Exploitation: Origin Reflection]]'
- '[[CORS Misconfiguration Exploitation: Origin Reflection]]'
- '[[Gopher SMTP Email Spoofing via SSRF]]'
- '[[Metasploit Multiple Transports Payload Generator]]'
- '[[Octal IP Format Server-Side Request Forgery]]'
- '[[RDS Enumeration - Listing Subnets by VPC-id]]'
- '[[SCF and URL File Attack Against Writable Share Procedure]]'
- '[[Socat Bind Shell]]'
- '[[SQLite Boolean-Based Order By Injection]]'
- '[[SSRF via SFTP URL Scheme]]'
- '[[SSRF via XXE Injection]]'
---

# External Remote Services

**MITRE ID**: T1133

## Description

Remote services such as VPNs, Citrix, and other access mechanisms allow users to connect to internal enterprise network resources from external locations. There are often remote service gateways that manage connections and credential authentication for these services. Services such as Windows Remote Management can also be used externally.Adversaries may use remote services to initially access and/or persist within a network. [1] Access to Valid Accounts to use the service is often a requirement, which could be obtained through credential pharming or by obtaining the credentials from users after compromising the enterprise network. Access to remote services may be used as part of Redundant Access during an operation.

# Detection

Follow best practices for detecting adversary use of Valid Accounts for authenticating to remote services. Collect authentication logs and analyze for unusual access patterns, windows of activity, and access outside of normal business hours.

# Mitigation

Limit access to remote services through centrally managed concentrators such as VPNs and other managed remote access systems. Deny direct remote access to internal systems through uses of network proxies, gateways, and firewalls as appropriate. Disable or block services such as Windows Remote Management can be used externally. Use strong two-factor or multi-factor authentication for remote service accounts to mitigate an adversary's ability to leverage stolen credentials, but be aware of Two-Factor Authentication Interception techniques for some two-factor authentication implementations.

# Footnotes

[1] Adair, S. (2015, October 7). Virtual Private Keylogging: Cisco Web VPNs Leveraged for Access and Persistence. Retrieved March 20, 2017.

[2] Adair, S. (2017, February 17). Detecting and Responding to Advanced Threats within Exchange Environments. Retrieved March 20, 2017.

[3] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[4] US-CERT. (2017, October 20). Alert (TA17-293A): Advanced Persistent Threat Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved November 2, 2017.

[5] Scavella, T. and Rifki, A. (2017, July 20). Are you Ready to Respond? (Webinar). Retrieved October 4, 2017.

[6] Higgins, K. (2015, October 13). Prolific Cybercrime Gang Favors Legit Login Credentials. Retrieved October 4, 2017.

[7] Bromiley, M. and Lewis, P. (2016, October 7). Attacking the Hospitality and Gaming Industries: Tracking an Attacker Around the World in 7 Years. Retrieved October 6, 2017.

[8] Smallridge, R. (2018, March 10). APT15 is alive and strong: An analysis of RoyalCli and RoyalDNS. Retrieved April 4, 2018.

[9] McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.

[10] Davis, S. and Caban, D. (2017, December 19). APT34 - New Targeted Attack in the Middle East. Retrieved December 20, 2017.

[11] Miller, S, et al. (2019, April 10). TRITON Actor TTP Profile, Custom Attack Tools, Detections, and ATT&CK Mapping. Retrieved April 16, 2019.

[12] Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, August 5). Threat Group-3390 Targets Organizations for Cyberespionage. Retrieved August 18, 2018.

## Defense

Limit access to remote services through centrally managed concentrators such as VPNs and other managed remote access systems. Deny direct remote access to internal systems through the use of network proxies, gateways, and firewalls. Disable or block remot

## Tactics

- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]

## Related Procedures (14)

- [[Cloud Instance SSRF through OpenStack Metadata URL]]
- [[CORS Misconfiguration Exploitation: Origin Reflection]]
- [[CORS Misconfiguration Exploitation: Origin Reflection]]
- [[CORS Misconfiguration Exploitation: Origin Reflection]]
- [[CORS Misconfiguration Exploitation: Origin Reflection]]
- [[Gopher SMTP Email Spoofing via SSRF]]
- [[Metasploit Multiple Transports Payload Generator]]
- [[Octal IP Format Server-Side Request Forgery]]
- [[RDS Enumeration - Listing Subnets by VPC-id]]
- [[SCF and URL File Attack Against Writable Share Procedure]]
- [[Socat Bind Shell]]
- [[SQLite Boolean-Based Order By Injection]]
- [[SSRF via SFTP URL Scheme]]
- [[SSRF via XXE Injection]]
