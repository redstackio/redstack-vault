---
id: 8aeb90e0-ffbb-434c-9ba4-4e11cb6668a9
name: Impair Defenses
type: technique
mitre_id: T1562
mitre_url: null
created_at: '2023-04-06T00:31:25.964736+00:00'
updated_at: '2023-04-06T03:56:27.660180+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Disable Script Logging and Clear Signatures]]'
- '[[Windows - Disable Antivirus and Security (Elastic Agent and Cortex XDR)]]'
---

# Impair Defenses

**MITRE ID**: T1562

## Description

Adversaries may maliciously modify components of a victim environment in order to hinder or disable defensive mechanisms. This not only involves impairing preventative defenses, such as firewalls and anti-virus, but also detection capabilities that defenders can use to audit activity and identify malicious behavior. This may also span both native defenses as well as supplemental capabilities installed by users and administrators.

Adversaries could also target event aggregation and analysis mechanisms, or otherwise disrupt these procedures by altering other system components.

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures (2)

- [[Disable Script Logging and Clear Signatures]]
- [[Windows - Disable Antivirus and Security (Elastic Agent and Cortex XDR)]]
