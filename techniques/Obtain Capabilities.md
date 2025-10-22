---
id: 740300a0-b040-424d-8f8a-b24f9c175a34
name: Obtain Capabilities
type: technique
mitre_id: T1588
mitre_url: null
created_at: '2023-04-06T00:31:26.957355+00:00'
updated_at: '2023-04-06T03:56:37.979880+00:00'
tactics:
- '[[Resource Development|TA0042 - Resource Development]]'
procedures:
- '[[Gopher SMTP Email Spoofing via SSRF]]'
---

# Obtain Capabilities

**MITRE ID**: T1588

## Description

Adversaries may buy and/or steal capabilities that can be used during targeting. Rather than developing their own capabilities in-house, adversaries may purchase, freely download, or steal them. Activities may include the acquisition of malware, software (including licenses), exploits, certificates, and information relating to vulnerabilities. Adversaries may obtain capabilities to support their operations throughout numerous phases of the adversary lifecycle.

In addition to downloading free malware, software, and exploits from the internet, adversaries may purchase these capabilities from third-party entities. Third-party entities can include technology companies that specialize in malware and exploits, criminal marketplaces, or from individuals.(Citation: NationsBuying)(Citation: PegasusCitizenLab)

In addition to purchasing capabilities, adversaries may steal capabilities from third-party entities (including other adversaries). This can include stealing software licenses, malware, SSL/TLS and code-signing certificates, or raiding closed databases of vulnerabilities or exploits.(Citation: DiginotarCompromise)

## Tactics

- [[Resource Development|TA0042 - Resource Development]]

## Related Procedures (1)

- [[Gopher SMTP Email Spoofing via SSRF]]
