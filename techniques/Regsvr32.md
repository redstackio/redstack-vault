---
id: 30e64424-98a4-4e41-bbee-d9e9d2a876cc
name: Regsvr32
type: technique
mitre_id: T1117
mitre_url: null
created_at: '2019-08-28T21:17:41.760633+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[Akamai WAF Bypass via Prompt User Input]]'
- '[[Automatic Sanitization Bypass in Angular and AngularJS]]'
- '[[CSP Bypass via XSS Injection]]'
- '[[Linux Privilege Escalation - Writable Files Escalation]]'
- '[[ObjectDataProvider JSON.NET Deserialization RCE]]'
- '[[Phar Deserialization Attack]]'
- '[[PHP Deserialization with Monolog/RCE1 and Swiftmailer/FW1 Gadgets]]'
- '[[SAML Injection for Authentication Bypass and Signature Stripping with Admin NameID]]'
- '[[Windows Download and Execute via Regsvr32]]'
---

# Regsvr32

**MITRE ID**: T1117

## Description

Regsvr32.exe is a command-line program used to register and unregister object linking and embedding controls, including dynamic link libraries (DLLs), on Windows systems. Regsvr32.exe can be used to execute arbitrary binaries. [1]Adversaries may take advantage of this functionality to proxy execution of code to avoid triggering security tools that may not monitor execution of, and modules loaded by, the regsvr32.exe process because of whitelists or false positives from Windows using regsvr32.exe for normal operations. Regsvr32.exe is also a Microsoft signed binary.Regsvr32.exe can also be used to specifically bypass process whitelisting using functionality to load COM scriptlets to execute DLLs under user permissions. Since regsvr32.exe is network and proxy aware, the scripts can be loaded by passing a uniform resource locator (URL) to file on an external Web server as an argument during invocation. This method makes no changes to the Registry as the COM object is not actually registered, only executed. [2] This variation of the technique is often referred to as a "Squiblydoo" attack and has been used in campaigns targeting governments. [3] [4]Regsvr32.exe can also be leveraged to register a COM Object used to establish Persistence via Component Object Model Hijacking. [3]

# Detection

Use process monitoring to monitor the execution and arguments of regsvr32.exe. Compare recent invocations of regsvr32.exe with prior history of known good arguments and loaded files to determine anomalous and potentially adversarial activity. Command arguments used before and after the regsvr32.exe invocation may also be useful in determining the origin and purpose of the script or DLL being loaded. [3]

# Mitigation

Microsoft's Enhanced Mitigation Experience Toolkit (EMET) Attack Surface Reduction (ASR) feature can be used to block regsvr32.exe from being used to bypass whitelisting. [20]

# Footnotes

[1] Microsoft. (2015, August 14). How to use the Regsvr32 tool and troubleshoot Regsvr32 error messages. Retrieved June 22, 2016.

[2] Smith, C. (2016, April 19). Bypass Application Whitelisting Script Protections - Regsvr32.exe & COM Scriptlets (.sct files). Retrieved June 30, 2017.

[3] Nolen, R. et al.. (2016, April 28). Threat Advisory: “Squiblydoo” Continues Trend of Attackers Using Native OS Tools to “Live off the Land”. Retrieved April 9, 2018.

[4] Anubhav, A., Kizhakkinan, D. (2017, February 22). Spear Phishing Techniques Used in Attacks Targeting the Mongolian Government. Retrieved February 24, 2017.

[5] Ahl, I. (2017, June 06). Privileges and Credentials: Phished at the Request of Counsel. Retrieved May 17, 2018.

[6] Carr, N.. (2017, May 14). Cyber Espionage is Alive and Well: APT32 and the Threat to Global Corporations. Retrieved June 18, 2017.

[7] Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.

[8] Dumont, R. (2019, March 20). Fake or Fake: Keeping up with OceanLotus decoys. Retrieved April 1, 2019.

[9] Salem, E. (2019, February 13). ASTAROTH MALWARE USES LEGITIMATE OS AND ANTIVIRUS PROCESSES TO STEAL PASSWORDS AND PERSONAL DATA. Retrieved April 17, 2019.

[10] Svajcer, V. (2018, July 31). Multiple Cobalt Personality Disorder. Retrieved September 5, 2018.

[11] Gorelik, M. (2018, October 08). Cobalt Group 2.0. Retrieved November 5, 2018.

[12] Giagone, R., Bermejo, L., and Yarochkin, F. (2017, November 20). Cobalt Strikes Again: Spam Runs Use Macros and CVE-2017-8759 Exploit Against Russian Banks. Retrieved March 7, 2019.

[13] RSA Incident Response. (2014, January). RSA Incident Response Emerging Threat Profile: Shell Crew. Retrieved January 14, 2016.

[14] Fidelis Threat Research Team. (2016, May 2). Turbo Twist: Two 64-bit Derusbi Strains Converge. Retrieved August 16, 2018.

[15] Fidelis Cybersecurity. (2015, December 16). Fidelis Threat Advisory #1020: Dissecting the Malware Involved in the INOCNATION Campaign. Retrieved March 24, 2016.

[16] Magius, J., et al. (2017, July 19). Koadic. Retrieved June 18, 2018.

[17] Axel F, Pierre T. (2017, October 16). Leviathan: Espionage actor spearphishes maritime and defense targets. Retrieved February 15, 2018.

[18] Lee, B., Falcone, R. (2019, January 18). DarkHydrus delivers new Trojan that can use Google Drive for C2 communications. Retrieved April 17, 2019.

[19] Xiao, C. (2018, September 17). Xbash Combines Botnet, Ransomware, Coinmining in Worm that Targets Linux and Windows. Retrieved November 14, 2018.

[20] National Security Agency. (2016, May 4). Secure Host Baseline EMET. Retrieved June 22, 2016.

## Defense

Microsoft's Enhanced Mitigation Experience Toolkit (EMET) Attack Surface Reduction (ASR) feature can be used to block regsvr32.exe from being used to bypass whitelisting. (Citation: Secure Host Baseline EMET)

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

## Related Procedures (9)

- [[Akamai WAF Bypass via Prompt User Input]]
- [[Automatic Sanitization Bypass in Angular and AngularJS]]
- [[CSP Bypass via XSS Injection]]
- [[Linux Privilege Escalation - Writable Files Escalation]]
- [[ObjectDataProvider JSON.NET Deserialization RCE]]
- [[Phar Deserialization Attack]]
- [[PHP Deserialization with Monolog/RCE1 and Swiftmailer/FW1 Gadgets]]
- [[SAML Injection for Authentication Bypass and Signature Stripping with Admin NameID]]
- [[Windows Download and Execute via Regsvr32]]
