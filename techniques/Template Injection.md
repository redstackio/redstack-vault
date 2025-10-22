---
id: d5c88f99-6557-4912-ac61-cb39ffd6fb41
name: Template Injection
type: technique
mitre_id: T1221
mitre_url: null
created_at: '2019-08-28T21:17:33.539815+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Admin Site URL Leak via Server Side Template Injection in Django Templates]]'
- '[[ASP.NET Razor Basic Injection with Addition Command]]'
- '[[Blind XXE Data Exfiltration with DTD and PHP Filter]]'
- '[[DB2 Injection - Find Tables From Column Name]]'
- '[[DB2 Injection - List Tables]]'
- '[[DB2 List DBA Accounts Procedure]]'
- '[[Freemarker Code Execution]]'
- '[[Freemarker Sandbox Bypass Remote Code Execution]]'
- '[[Gopher Server-Side Request Forgery via SMTP Spoofing Attack]]'
- '[[GraphQL Injection using Mutations to Steal Credentials and Add Users]]'
- '[[GraphQL Projection Data Extraction]]'
- '[[GraphQL SQL Injection Exploitation]]'
- '[[Groovy Sandbox Bypass for Server Side Template Injection]]'
- '[[Groovy Server Side Template Injection with Command Execution]]'
- '[[Java Server Side Template Injection for Retrieving /etc/passwd]]'
- '[[Java Server Side Template Injection - Retrieve System Environment Variables]]'
- '[[Java Velocity Server Side Template Injection]]'
- '[[Jinja2 Filter Bypass for Server Side Template Injection]]'
- '[[Jinja2 RCE via Server Side Template Injection]]'
- '[[Jinja2 Server Side Template Injection Debugging]]'
- '[[Jinja2 SSTI Remote Code Execution via subprocess.Popen]]'
- '[[Jinjava Uppercase String and Request Object Injection]]'
- '[[Lessjs Command Execution via Server Side Template Injection]]'
- '[[MYSQL Union Based Column Enumeration]]'
- '[[Oracle SQL Injection - User and Version Information Retrieval]]'
- '[[Pebble Server Side Template Injection - Code Execution]]'
- '[[Phishing Word Document Injection]]'
- '[[Remote Template Injection via Malicious Macro and Attachment]]'
- '[[Safe Script Tag Injection via Django Templates]]'
- '[[SAML Injection for Authentication Bypass and XML External Entity Attacks]]'
- '[[Server Side Template Injection Detection]]'
- '[[Server Side Template Injection - Django Templates - Admin Credentials Leak]]'
- '[[Server Side Template Injection - Freemarker Read File]]'
- '[[Server Side Template Injection - Groovy File Manipulation]]'
- '[[Server Side Template Injection - Java Basic Injection using Java ClassLoader
  and Resource Retrieval]]'
- '[[Server Side Template Injection using Jade/Codepen to execute commands and list
  system users]]'
- '[[Server Side Template Injection using Plates]]'
- '[[Server Side Template Injection with Debug Information Leak]]'
- '[[Server Side Template Injection with Django Templates using Burp Payload Calculation]]'
- '[[Server Side Template Injection with Groovy - Basic Injection - Multiplication
  Result]]'
- '[[Server Side Template Injection with Groovy HTTP Request]]'
- '[[Server Side Template Injection with Java Spring]]'
- '[[Server Side Template Injection with Less.js Plugins]]'
- '[[Server Side Template Injection with patTemplate]]'
- '[[Server Side Template Injection with Pebble - Basic Injection using Convert String
  to Uppercase]]'
- '[[Server Side Template Injection with tplmap and SSTImap]]'
- '[[Twig Template Injection - Arbitrary File Reading]]'
- '[[XML External Entity Injection Detection and Mitigation]]'
- '[[XXE File Retrieval with PHP Wrapper]]'
- '[[XXE in DOCX Files]]'
---

# Template Injection

**MITRE ID**: T1221

## Description

Microsoft’s Open Office XML (OOXML) specification defines an XML-based format for Office documents (.docx, xlsx, .pptx) to replace older binary formats (.doc, .xls, .ppt). OOXML files are packed together ZIP archives compromised of various XML files, referred to as parts, containing properties that collectively define how a document is rendered. [1]Properties within parts may reference shared public resources accessed via online URLs. For example, template properties reference a file, serving as a pre-formatted document blueprint, that is fetched when the document is loaded.Adversaries may abuse this technology to initially conceal malicious code to be executed via documents (i.e. Scripting). Template references injected into a document may enable malicious payloads to be fetched and executed when the document is loaded. [2] These documents can be delivered via other techniques such as Spearphishing Attachment and/or Taint Shared Content and may evade static detections since no typical indicators (VBA macro, script, etc.) are present until after the malicious payload is fetched. [3] Examples have been seen in the wild where template injection was used to load malicious code containing an exploit. [4]This technique may also enable Forced Authentication by injecting a SMB/HTTPS (or other credential prompting) URL and triggering an authentication attempt. [5] [6] [7]

# Detection

Analyze process behavior to determine if an Office application is performing actions, such as opening network connections, reading files, spawning abnormal child processes (ex: PowerShell), or other suspicious actions that could relate to post-compromise behavior.

# Mitigation

Consider disabling Microsoft Office macros/active content to prevent the execution of malicious payloads in documents [13], though this setting may not mitigate the Forced Authentication use for this technique.

Because this technique involves user interaction on the endpoint, it's difficult to fully mitigate. However, there are potential mitigations including training users to identify social engineering techniques and spearphishing emails. Network/Host intrusion prevention systems, antivirus, and detonation chambers can be employed to prevent documents from fetching and/or executing malicious payloads. [5]

# Footnotes

[1] Microsoft. (2014, July 9). Introducing the Office (2007) Open XML File Formats. Retrieved July 20, 2018.

[2] Wiltse, B.. (2018, November 7). Template Injection Attacks - Bypassing Security Controls by Living off the Land. Retrieved April 10, 2019.

[3] Hawkins, J. (2018, July 18). Executing Macros From a DOCX With Remote Template Injection. Retrieved October 12, 2018.

[4] Segura, J. (2017, October 13). Decoy Microsoft Word document delivers malware through a RAT. Retrieved July 21, 2018.

[5] Intel_Acquisition_Team. (2018, March 1). Credential Harvesting and Malicious File Delivery using Microsoft Office Template Injection. Retrieved July 20, 2018.

[6] Baird, S. et al.. (2017, July 7). Attack on Critical Infrastructure Leverages Template Injection. Retrieved July 21, 2018.

[7] Hanson, R. (2016, September 24). phishery. Retrieved July 21, 2018.

[8] Lee, B., Falcone, R. (2018, December 12). Dear Joohn: The Sofacy Group’s Global Campaign. Retrieved April 19, 2019.

[9] Falcone, R. (2018, August 07). DarkHydrus Uses Phishery to Harvest Credentials in the Middle East. Retrieved August 10, 2018.

[10] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[11] US-CERT. (2017, October 20). Alert (TA17-293A): Advanced Persistent Threat Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved November 2, 2017.

[12] Ray, V. (2016, November 22). Tropic Trooper Targets Taiwanese Government and Fossil Fuel Provider With Poison Ivy. Retrieved November 9, 2018.

[13] Microsoft. (n.d.). Enable or disable macros in Office files. Retrieved September 13, 2018.

## Defense

Consider disabling Microsoft Office macros/active content to prevent the execution of malicious payloads in documents (Citation: Microsoft Disable Macros), though this setting may not mitigate the [Forced Authentication](https://attack.mitre.org/technique

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures (50)

- [[Admin Site URL Leak via Server Side Template Injection in Django Templates]]
- [[ASP.NET Razor Basic Injection with Addition Command]]
- [[Blind XXE Data Exfiltration with DTD and PHP Filter]]
- [[DB2 Injection - Find Tables From Column Name]]
- [[DB2 Injection - List Tables]]
- [[DB2 List DBA Accounts Procedure]]
- [[Freemarker Code Execution]]
- [[Freemarker Sandbox Bypass Remote Code Execution]]
- [[Gopher Server-Side Request Forgery via SMTP Spoofing Attack]]
- [[GraphQL Injection using Mutations to Steal Credentials and Add Users]]
- [[GraphQL Projection Data Extraction]]
- [[GraphQL SQL Injection Exploitation]]
- [[Groovy Sandbox Bypass for Server Side Template Injection]]
- [[Groovy Server Side Template Injection with Command Execution]]
- [[Java Server Side Template Injection for Retrieving /etc/passwd]]
- [[Java Server Side Template Injection - Retrieve System Environment Variables]]
- [[Java Velocity Server Side Template Injection]]
- [[Jinja2 Filter Bypass for Server Side Template Injection]]
- [[Jinja2 RCE via Server Side Template Injection]]
- [[Jinja2 Server Side Template Injection Debugging]]

*...and 30 more*
