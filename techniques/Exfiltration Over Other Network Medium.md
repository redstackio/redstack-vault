---
id: b4a9c355-75f8-406d-9d55-4801e4167126
name: Exfiltration Over Other Network Medium
type: technique
mitre_id: T1011
mitre_url: null
created_at: '2019-08-28T21:17:35.473480+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
procedures:
- '[[AWS Private Route to Nat Gateway]]'
---

# Exfiltration Over Other Network Medium

**MITRE ID**: T1011

## Description

Exfiltration could occur over a different network medium than the command and control channel. If the command and control network is a wired Internet connection, the exfiltration may occur, for example, over a WiFi connection, modem, cellular data connection, Bluetooth, or another radio frequency (RF) channel. Adversaries could choose to do this if they have sufficient access or proximity, and the connection might not be secured or defended as well as the primary Internet-connected channel because it is not routed through the same enterprise network.

# Detection

Processes utilizing the network that do not normally have network communication or have never been seen before. Processes that normally require user-driven events to access the network (for example, a mouse click or key press) but access the network without such may be malicious.

Monitor for and investigate changes to host adapter settings, such as addition and/or replication of communication interfaces.

# Mitigation

Ensure host-based sensors maintain visibility into usage of all network adapters and prevent the creation of new ones where possible. [2] [3]

# Footnotes

[1] Symantec Security Response. (2012, May 31). Flamer: A Recipe for Bluetoothache. Retrieved February 25, 2017.

[2] Microsoft. (2009, February 9). Disabling Bluetooth and Infrared Beaming. Retrieved July 26, 2018.

[3] Schauland, D. (2009, February 24). Configuring Wireless settings via Group Policy. Retrieved July 26, 2018.

## Defense

Ensure host-based sensors maintain visibility into usage of all network adapters and prevent the creation of new ones where possible. (Citation: Microsoft GPO Bluetooth FEB 2009) (Citation: TechRepublic Wireless GPO FEB 2009)

## Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

## Related Procedures (1)

- [[AWS Private Route to Nat Gateway]]
