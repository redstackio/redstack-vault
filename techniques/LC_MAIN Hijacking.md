---
id: 2e56d430-144c-461f-8987-3bf4ba8fd242
name: LC_MAIN Hijacking
type: technique
mitre_id: T1149
mitre_url: null
created_at: '2019-08-28T21:17:40.926608+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# LC_MAIN Hijacking

**MITRE ID**: T1149

## Description

As of OS X 10.8, mach-O binaries introduced a new header called LC_MAIN that points to the binary’s entry point for execution. Previously, there were two headers to achieve this same effect: LC_THREAD and LC_UNIXTHREAD  [1]. The entry point for a binary can be hijacked so that initial execution flows to a malicious addition (either another section or a code cave) and then goes back to the initial entry point so that the victim doesn’t know anything was different  [2]. By modifying a binary in this way, application whitelisting can be bypassed because the file name or application path is still the same.

# Detection

Determining the original entry point for a binary is difficult, but checksum and signature verification is very possible. Modifying the LC_MAIN entry point or adding in an additional LC_MAIN entry point invalidates the signature for the file and can be detected. Collect running process information and compare against known applications to look for suspicious behavior.

# Mitigation

Enforce valid digital signatures for signed code on all applications and only trust applications with signatures from trusted parties.

# Footnotes

[1] Bit9 + Carbon Black Threat Research Team. (2015). 2015: The Most Prolific Year in History for OS X Malware. Retrieved July 8, 2017.

[2] Patrick Wardle. (2014, September). Methods of Malware Persistence on Mac OS X. Retrieved July 5, 2017.

## Defense

Enforce valid digital signatures for signed code on all applications and only trust applications with signatures from trusted parties.

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
