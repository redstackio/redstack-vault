---
id: 3a251c9b-2dd3-4d33-a51d-44502bf7d901
name: Internal Spearphishing
type: technique
mitre_id: T1534
mitre_url: null
created_at: '2023-04-06T00:31:26.634371+00:00'
updated_at: '2023-04-06T03:56:41.283641+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[AWS EBS Snapshot Volume Creation]]'
- '[[AWS Shadow Admin - Create AWS Glue Development Endpoint]]'
- '[[Cloud Security Assessment and Auditing]]'
- '[[Disable CloudTrail on Specific Regions]]'
- '[[Disabling CloudTrail Trail]]'
- '[[Illicit Consent Grant - User Consent Permissions]]'
- '[[Mounting EBS Volume to EC2 Linux Instance]]'
- '[[Web Cache Deception - Methodology 2: Un-keyed Input Cache Poisoning]]'
---

# Internal Spearphishing

**MITRE ID**: T1534

## Description

Adversaries may use internal spearphishing to gain access to additional information or exploit other users within the same organization after they already have access to accounts or systems within the environment. Internal spearphishing is multi-staged campaign where an email account is owned either by controlling the user's device with previously installed malware or by compromising the account credentials of the user. Adversaries attempt to take advantage of a trusted internal account to increase the likelihood of tricking the target into falling for the phish attempt.(Citation: Trend Micro When Phishing Starts from the Inside 2017)

Adversaries may leverage [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001) or [Spearphishing Link](https://attack.mitre.org/techniques/T1566/002) as part of internal spearphishing to deliver a payload or redirect to an external site to capture credentials through [Input Capture](https://attack.mitre.org/techniques/T1056) on sites that mimic email login interfaces.

There have been notable incidents where internal spearphishing has been used. The Eye Pyramid campaign used phishing emails with malicious attachments for lateral movement between victims, compromising nearly 18,000 email accounts in the process.(Citation: Trend Micro When Phishing Starts from the Inside 2017) The Syrian Electronic Army (SEA) compromised email accounts at the Financial Times (FT) to steal additional account credentials. Once FT learned of the campaign and began warning employees of the threat, the SEA sent phishing emails mimicking the Financial Times IT department and were able to compromise even more users.(Citation: THE FINANCIAL TIMES LTD 2019.)

## Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures (8)

- [[AWS EBS Snapshot Volume Creation]]
- [[AWS Shadow Admin - Create AWS Glue Development Endpoint]]
- [[Cloud Security Assessment and Auditing]]
- [[Disable CloudTrail on Specific Regions]]
- [[Disabling CloudTrail Trail]]
- [[Illicit Consent Grant - User Consent Permissions]]
- [[Mounting EBS Volume to EC2 Linux Instance]]
- [[Web Cache Deception - Methodology 2: Un-keyed Input Cache Poisoning]]
