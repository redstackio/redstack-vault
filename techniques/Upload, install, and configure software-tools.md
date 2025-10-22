---
id: 9332aac5-f2c1-4873-b308-4b9c140fc3db
name: Upload, install, and configure software/tools
type: technique
mitre_id: T1362
mitre_url: null
created_at: '2019-12-18T23:58:08.378845+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Stage Capabilities|TA0026 - Stage Capabilities]]'
procedures:
- '[[Provision S3 Website and Upload Payload]]'
- '[[Terraform Create Kali Linux EC2 Instance]]'
- '[[Update /etc/hosts with IP and Hostname]]'
---

# Upload, install, and configure software/tools

**MITRE ID**: T1362

## Description

An adversary may stage software and tools for use during later stages of an attack. The software and tools may be placed on systems legitimately in use by the adversary or may be placed on previously compromised infrastructure.

# Detection

**Detectable by Common Defenses (Yes/No/Partial): **No

**Explanation: **Infrastructure is (typically) outside of control/visibility of defender and as such as tools are staged for specific campaigns, it will not be observable to those being attacked.

# Difficulty for the Adversary

**Easy for the Adversary (Yes/No): **Yes

**Explanation: **Adversary has control of the infrastructure and will likely be able to add/remove tools to infrastructure, whether acquired via hacking or standard computer acquisition (e.g., [https://aws.amazon.com AWS], VPS providers).

# References

1. Mandiant. (n.d.). APT1: Exposing One of China’s Cyber Espionage Units. Retrieved March 5, 2017.

1. GReAT. (2013, January 17). “Red October”. Detailed Malware Description 4. Second Stage of Attack. Retrieved March 7, 2017.

## Tactics

- [[Stage Capabilities|TA0026 - Stage Capabilities]]

## Related Procedures (3)

- [[Provision S3 Website and Upload Payload]]
- [[Terraform Create Kali Linux EC2 Instance]]
- [[Update /etc/hosts with IP and Hostname]]
