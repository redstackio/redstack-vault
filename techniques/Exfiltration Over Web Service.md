---
id: 8d9d1eed-8645-4d5a-b88e-ac2f980749cd
name: Exfiltration Over Web Service
type: technique
mitre_id: T1567
mitre_url: null
created_at: '2023-04-06T00:31:25.988916+00:00'
updated_at: '2023-04-06T03:56:05.652738+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
procedures:
- '[[DNS Poisoning and Credential Dumping via mitm6 Relay Attack]]'
---

# Exfiltration Over Web Service

**MITRE ID**: T1567

## Description

Adversaries may use an existing, legitimate external Web service to exfiltrate data rather than their primary command and control channel. Popular Web services acting as an exfiltration mechanism may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to compromise. Firewall rules may also already exist to permit traffic to these services.

Web service providers also commonly use SSL/TLS encryption, giving adversaries an added level of protection.

## Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

## Related Procedures (1)

- [[DNS Poisoning and Credential Dumping via mitm6 Relay Attack]]
