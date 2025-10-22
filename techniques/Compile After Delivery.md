---
id: 5e49ef3b-4cf3-4fd9-8335-a7e2f0dc04fe
name: Compile After Delivery
type: technique
mitre_id: T1500
mitre_url: null
created_at: '2019-08-28T21:17:27.034728+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[C Reverse Shell]]'
---

# Compile After Delivery

**MITRE ID**: T1500

## Description

Adversaries may attempt to make payloads difficult to discover and analyze by delivering files to victims as uncompiled code. Similar to Obfuscated Files or Information, text-based source code files may subvert analysis and scrutiny from protections targeting executables/binaries. These payloads will need to be compiled before execution; typically via native utilities such as csc.exe or GCC/MinGW.[1]Source code payloads may also be encrypted, encoded, and/or embedded within other files, such as those delivered as a Spearphishing Attachment. Payloads may also be delivered in formats unrecognizable and inherently benign to the native OS (ex: EXEs on macOS/Linux) before later being (re)compiled into a proper executable binary with a bundled compiler and execution framework.[2]

# Detection

Monitor the execution file paths and command-line arguments for common compilers, such as csc.exe and GCC/MinGW, and correlate with other suspicious behavior to reduce false positives from normal user and administrator behavior. The compilation of payloads may also generate file creation and/or file write events. Look for non-native binary formats and cross-platform compiler and execution frameworks like Mono and determine if they have a legitimate purpose on the system.[2] Typically these should only be used in specific and limited cases, like for software development.

# Mitigation

This type of technique cannot be easily mitigated with preventive controls or patched since it is based on the abuse of operating system design features. For example, blocking all file compilation may have unintended side effects, such as preventing legitimate OS frameworks and code development mechanisms from operating properly. Consider removing compilers if not needed, otherwise efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identifying subsequent malicious behavior.

Identify unnecessary system utilities or potentially malicious software that may be used to decrypt, deobfuscate, decode, and compile files or information, and audit and/or block them by using whitelisting [4] tools, like AppLocker, [5] [6] or Software Restriction Policies [7] where appropriate. [8]

# Footnotes

[1] ClearSky Cyber Security. (2018, November). MuddyWater Operations in Lebanon and Oman: Using an Israeli compromised domain for a two-stage campaign. Retrieved November 29, 2018.

[2] Trend Micro. (2019, February 11). Windows App Runs on Mac, Downloads Info Stealer and Adware. Retrieved April 25, 2019.

[3] Grunzweig, J.. (2017, April 20). Cardinal RAT Active for Over Two Years. Retrieved December 8, 2018.

[4] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[5] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[6] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[7] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[8] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

This type of technique cannot be easily mitigated with preventive controls or patched since it is based on the abuse of operating system design features. For example, blocking all file compilation may have unintended side effects, such as preventing legit

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures (1)

- [[C Reverse Shell]]
