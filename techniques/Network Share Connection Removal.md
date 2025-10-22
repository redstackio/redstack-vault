---
id: 9e4141f9-96d5-4568-9902-d93e32115ec2
name: Network Share Connection Removal
type: technique
mitre_id: T1126
mitre_url: null
created_at: '2019-08-28T21:17:46.492610+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Network Share Connection Removal

**MITRE ID**: T1126

## Description

Windows shared drive and Windows Admin Shares connections can be removed when no longer needed. Net is an example utility that can be used to remove network share connections with the net use \system\share /delete command. [1]Adversaries may remove share connections that are no longer useful in order to clean up traces of their operation.

# Detection

Network share connections may be common depending on how an network environment is used. Monitor command-line invocation of net use commands associated with establishing and removing remote shares over SMB, including following best practices for detection of Windows Admin Shares. SMB traffic between systems may also be captured and decoded to look for related network share session and file transfer activity. Windows authentication logs are also useful in determining when authenticated network shares are established and by which account, and can be used to correlate network share activity to other events to investigate potentially malicious activity.

# Mitigation

Follow best practices for mitigation of activity related to establishing Windows Admin Shares. 

Identify unnecessary system utilities or potentially malicious software that may be used to leverage network shares, and audit and/or block them by using whitelisting [3] tools, like AppLocker, [4] [5] or Software Restriction Policies [6] where appropriate. [7]

# Footnotes

[1] Microsoft. (n.d.). Net Use. Retrieved November 25, 2016.

[2] Counter Threat Unit Research Team. (2017, June 27). BRONZE UNION Cyberespionage Persists Despite Disclosures. Retrieved July 13, 2017.

[3] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[4] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[5] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[6] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[7] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Follow best practices for mitigation of activity related to establishing [Windows Admin Shares](https://attack.mitre.org/techniques/T1077). 

Identify unnecessary system utilities or potentially malicious software that may be used to leverage network shar

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
