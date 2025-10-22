---
id: 4320bb80-9024-49b4-96e0-53857d89ae70
name: AMSI Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-01-10T04:07:21.816219+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Windows
tags:
- '[[anti-malware]]'
- '[[Defense Bypass]]'
---

# AMSI Bypass

## Summary

AMSI (Windows Anti-Malware Scan Interface) is a security feature in the Windows operating system that allows applications and services to request scanning of data by an installed anti-malware product. AMSI provides a standard interface that enables anti-malware products to integrate with applicatio

## Description

# Description

AMSI (Windows Anti-Malware Scan Interface) is a security feature in the Windows operating system that allows applications and services to request scanning of data by an installed anti-malware product. AMSI provides a standard interface that enables anti-malware products to integrate with applications and scripts, and it enables applications and scripts to request a scan of data from an installed anti-malware product. AMSI can be used to scan data in memory, on disk, or in transmission, and it can be used to scan data in a variety of formats including text, scripts, and binary files. It is designed to be extensible, so that it can support new formats and scanning scenarios as they are introduced. AMSI is available on Windows 10 and Windows Server 2016 and later, and it is used by a variety of applications and services in Windows including Microsoft Office, PowerShell, and the Windows Defender antivirus. By providing a standard interface for anti-malware products to integrate with applications and scripts, AMSI helps to improve the security of Windows by enabling real-time scanning of potentially malicious data, and it can also help to reduce the burden on anti-malware products by allowing them to scan data in a more targeted and efficient manner.

# Instructions

1. To bypass AMSI run the following script in powershell

**Code**: [[$ierku = @"
using System;
using System.Runtime.I]]

## Troubleshooting

If the following output is received from the above command, try a different AMSI bypass. The target may also be alerted by this error.

**Code**: [[At line:1 char:1
+ sET-ItEM ( 'V'+'aR' +  'IA' + ]]

## Platforms

- Windows

## Tags

- [[anti-malware]]
- [[Defense Bypass]]
