---
id: 4eaa3962-ea95-4149-9250-fa7a43179228
name: Rc.common
type: technique
mitre_id: T1163
mitre_url: null
created_at: '2019-08-28T21:17:31.289841+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# Rc.common

**MITRE ID**: T1163

## Description

During the boot process, macOS executes source /etc/rc.common, which is a shell script containing various utility functions. This file also defines routines for processing command-line arguments and for gathering system settings, and is thus recommended to include in the start of Startup Item Scripts [1]. In macOS and OS X, this is now a deprecated technique in favor of launch agents and launch daemons, but is currently still used.Adversaries can use the rc.common file as a way to hide code for persistence that will execute on each reboot as the root user [2].

# Detection

The /etc/rc.common file can be monitored to detect changes from the company policy. Monitor process execution resulting from the rc.common script for unusual or unknown applications or behavior.

# Mitigation

Limit privileges of user accounts so only authorized users can edit the rc.common file.

# Footnotes

[1] Apple. (2016, September 13). Startup Items. Retrieved July 11, 2017.

[2] Patrick Wardle. (2014, September). Methods of Malware Persistence on Mac OS X. Retrieved July 5, 2017.

[3] Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.

## Defense

Limit privileges of user accounts so only authorized users can edit the rc.common file.

## Tactics

- [[Persistence|TA0003 - Persistence]]
