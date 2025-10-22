---
id: c6232f93-fd7b-46e1-913e-81b4b91268c6
name: Execution Guardrails
type: technique
mitre_id: T1480
mitre_url: null
created_at: '2019-08-28T21:17:41.228277+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Execution Guardrails

**MITRE ID**: T1480

## Description

Execution guardrails constrain execution or actions based on adversary supplied environment specific conditions that are expected to be present on the target. Guardrails ensure that a payload only executes against an intended target and reduces collateral damage from an adversary’s campaign.[1] Values an adversary can provide about a target system or environment to use as guardrails may include specific network share names, attached physical devices, files, joined Active Directory (AD) domains, and local/external IP addresses.Environmental keying is one type of guardrail that includes cryptographic techniques for deriving encryption/decryption keys from specific types of values in a given computing environment.[2] Values can be derived from target-specific elements and used to generate a decryption key for an encrypted payload. Target-specific values can be derived from specific network shares, physical devices, software/software versions, files, joined AD domains, system time, and local/external IP addresses.[3][4][5][6][7] By generating the decryption keys from target-specific environmental values, environmental keying can make sandbox detection, anti-virus detection, crowdsourcing of information, and reverse engineering difficult.[3][7] These difficulties can slow down the incident response process and help adversaries hide their tactics, techniques, and procedures (TTPs).Similar to Obfuscated Files or Information, adversaries may use guardrails and environmental keying to help protect their TTPs and evade detection. For example, environmental keying may be used to deliver an encrypted payload to the target that will use target-specific values to decrypt the payload before execution.[3][5][6][7][8] By utilizing target-specific values to decrypt the payload the adversary can avoid packaging the decryption key with the payload or sending it over a potentially monitored network connection. Depending on the technique for gathering target-specific values, reverse engineering of the encrypted payload can be exceptionally difficult.[3] In general, guardrails can be used to prevent exposure of capabilities in environments that are not intended to be compromised or operated within. This use of guardrails is distinct from typical Virtualization/Sandbox Evasion where a decision can be made not to further engage because the value conditions specified by the adversary are meant to be target specific and not such that they could occur in any environment.

# Detection

Detecting the action of environmental keying may be difficult depending on the implementation. Monitoring for suspicious processes being spawned that gather a variety of system information or perform other forms of Discovery, especially in a short period of time, may aid in detection.

# Mitigation

This technique likely should not be mitigated with preventative controls because it may protect unintended targets from being compromised. If targeted, efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identifying subsequent malicious behavior if compromised.

# Footnotes

[1] Shoorbajee, Z. (2018, June 1). Playing nice? FireEye CEO says U.S. malware is more restrained than adversaries'. Retrieved January 17, 2019.

[2] Riordan, J., Schneier, B. (1998, June 18). Environmental Key Generation towards Clueless Agents. Retrieved January 18, 2019.

[3] Kaspersky Lab. (2012, August). Gauss: Abnormal Distribution. Retrieved January 17, 2019.

[4] Kafeine. (2016, December 13). Home Routers Under Attack via Malvertising on Windows, Android Devices. Retrieved January 16, 2019.

[5] Song, C., et al. (2012, August 7). Impeding Automated Malware Analysis with Environment-sensitive Malware. Retrieved January 18, 2019.

[6] Warren, R. (2017, August 8). Smuggling HTA files in Internet Explorer/Edge. Retrieved January 16, 2019.

[7] Morrow, T., Pitts, J. (2016, October 28). Genetic Malware: Designing Payloads for Specific Targets. Retrieved January 18, 2019.

[8] Warren, R. (2017, August 2). Demiguise: virginkey.js. Retrieved January 17, 2019.

[9] Ackerman, G., et al. (2018, December 21). OVERRULED: Containing a Potentially Destructive Adversary. Retrieved January 17, 2019.

[10] Kaspersky Lab's Global Research and Analysis Team. (2015, February). Equation Group: Questions and Answers. Retrieved December 21, 2015.

## Defense

This technique likely should not be mitigated with preventative controls because it may protect unintended targets from being compromised. If targeted, efforts should be focused on preventing adversary tools from running earlier in the chain of activity a

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
