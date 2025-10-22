---
id: e36769eb-0095-4808-9e9f-99502e238617
name: Input Prompt
type: technique
mitre_id: T1141
mitre_url: null
created_at: '2019-08-28T21:17:24.450154+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
---

# Input Prompt

**MITRE ID**: T1141

## Description

When programs are executed that need additional privileges than are present in the current user context, it is common for the operating system to prompt the user for proper credentials to authorize the elevated privileges for the task (ex: Bypass User Account Control).Adversaries may mimic this functionality to prompt users for credentials with a seemingly legitimate prompt for a number of reasons that mimic normal usage, such as a fake installer requiring additional access or a fake malware removal suite.[1] This type of prompt can be used to collect credentials via various languages such as AppleScript[2][3] and PowerShell[2][4].

# Detection

Monitor process execution for unusual programs as well as malicious instances of Scripting that could be used to prompt users for credentials.

Inspect and scrutinize input prompts for indicators of illegitimacy, such as non-traditional banners, text, timing, and/or sources.

# Mitigation

This technique exploits users' tendencies to always supply credentials when prompted, which makes it very difficult to mitigate. Use user training as a way to bring awareness and raise suspicion for potentially malicious events (ex: Office documents prompting for credentials).

# Footnotes

[1] Sergei Shevchenko. (2015, June 4). New Mac OS Malware Exploits Mackeeper. Retrieved July 3, 2017.

[2] Foss, G. (2014, October 3). Do You Trust Your Computer?. Retrieved December 17, 2018.

[3] Marc-Etienne M.Leveille. (2016, July 6). New OSX/Keydnap malware is hungry for credentials. Retrieved July 3, 2017.

[4] Nelson, M. (2015, January 21). Phishing for Credentials: If you want it, just ask!. Retrieved December 17, 2018.

[5] Pantig, J. (2018, July 30). OSX.Calisto. Retrieved September 7, 2018.

[6] Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.

[7] Vengerik, B. et al.. (2014, December 5). Hacking the Street? FIN4 Likely Playing the Market. Retrieved December 17, 2018.

[8] Vengerik, B. & Dennesen, K.. (2014, December 5). Hacking the Street?  FIN4 Likely Playing the Market. Retrieved January 15, 2019.

[9] Patrick Wardle. (2017, January 1). Mac Malware of 2016. Retrieved September 21, 2018.

## Defense

This technique exploits users' tendencies to always supply credentials when prompted, which makes it very difficult to mitigate. Use user training as a way to bring awareness and raise suspicion for potentially malicious events (ex: Office documents promp

## Tactics

- [[Credential Access|TA0006 - Credential Access]]
