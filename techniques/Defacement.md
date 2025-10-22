---
id: 1ea1323f-74f1-4f9a-b9af-684b3778a7df
name: Defacement
type: technique
mitre_id: T1491
mitre_url: null
created_at: '2019-08-28T21:17:44.112120+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
---

# Defacement

**MITRE ID**: T1491

## Description

Adversaries may modify visual content available internally or externally to an enterprise network. Reasons for Defacement include delivering messaging, intimidation, or claiming (possibly false) credit for an intrusion. InternalAn adversary may deface systems internal to an organization in an attempt to intimidate or mislead users. This may take the form of modifications to internal websites, or directly to user systems with the replacement of the desktop wallpaper.[1] Disturbing or offensive images may be used as a part of Defacement in order to cause user discomfort, or to pressure compliance with accompanying messages. While internally defacing systems exposes an adversary's presence, it often takes place after other intrusion goals have been accomplished.[2]ExternalWebsites are a common victim of defacement; often targeted by adversary and hacktivist groups in order to push a political message or spread propaganda.[3][4][5] Defacement may be used as a catalyst to trigger events, or as a response to actions taken by an organization or government. Similarly, website defacement may also be used as setup, or a precursor, for future attacks such as Drive-by Compromise.[6]

# Detection

Monitor internal and external websites for unplanned content changes. Monitor application logs for abnormal behavior that may indicate attempted or successful exploitation. Use deep packet inspection to look for artifacts of common exploit traffic, such as SQL injection. Web Application Firewalls may detect improper inputs attempting exploitation.

# Mitigation

Implementing best practices for websites such as defending against Exploit Public-Facing Application [7]. Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data. (Ready.gov IT DRP) Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery.

# Footnotes

[1] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.

[2] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Destructive Malware Report. Retrieved March 2, 2016.

[3] FireEye. (n.d.). Retrieved April 19, 2019.

[4] Kevin Mandia. (2017, March 30). Prepared Statement of Kevin Mandia, CEO of FireEye, Inc. before the United States Senate Select Committee on Intelligence. Retrieved April 19, 2019.

[5] Andy. (2018, May 12). ‘Anonymous’ Hackers Deface Russian Govt. Site to Protest Web-Blocking (NSFW). Retrieved April 19, 2019.

[6] Marco Balduzzi, Ryan Flores, Lion Gu, Federico Maggi, Vincenzo Ciancaglini, Roel Reyes, Akira Urano. (n.d.). A Deep Dive into Defacement: How Geopolitical Events Trigger Web Attacks. Retrieved April 19, 2019.

[7] OWASP. (2017, April 16). OWASP Top 10 2017 - The Ten Most Critical Web Application Security Risks. Retrieved February 12, 2019.

## Defense

Implementing best practices for websites such as defending against [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190) (Citation: OWASP Top 10 2017). Consider implementing IT disaster recovery plans that contain procedures for t

## Tactics

- [[Impact|TA0040 - Impact]]
