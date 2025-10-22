---
id: a23b6d42-9d7c-4895-bc6c-1a3cbe15d8e5
name: Data Obfuscation
type: technique
mitre_id: T1001
mitre_url: null
created_at: '2019-08-28T21:17:25.604344+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
procedures:
- '[[Creating Files with Zero-Width Spaces]]'
- '[[CRLF Filter Bypass with UTF-8 Encoding]]'
- '[[CRLF Filter Bypass with UTF-8 Encoding]]'
- '[[CRLF Filter Bypass with UTF-8 Encoding]]'
- '[[DB2 Injection - Select Nth Char Extraction]]'
- '[[Embed a File In an Image Using Steghide]]'
- '[[Exotic Payloads for Bypassing Email Filters]]'
- '[[Extract a Hidden File In an Image Using Steghide]]'
- '[[MYSQL Error Based - UpdateXML function Data Extraction]]'
- '[[MYSQL Union Based Injection to Extract Data from Users Table]]'
- '[[Out Of Band XPATH Injection]]'
- '[[PostgreSQL Time Based Table Dump]]'
- '[[TE Header Obfuscation]]'
- '[[XXE Injection in SOAP Messages]]'
---

# Data Obfuscation

**MITRE ID**: T1001

## Description

Command and control (C2) communications are hidden (but not necessarily encrypted) in an attempt to make the content more difficult to discover or decipher and to make the communication less conspicuous and hide commands from being seen. This encompasses many methods, such as adding junk data to protocol traffic, using steganography, commingling legitimate traffic with C2 communications traffic, or using a non-standard data encoding system, such as a modified Base64 encoding for the message body of an HTTP request.

# Detection

Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. [21]

# Mitigation

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools. [21]

# Footnotes

[1] FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.

[2] Novetta. (n.d.). Operation SMN: Axiom Threat Actor Group Report. Retrieved November 12, 2014.

[3] Symantec Security Response. (2014, July 7). Dragonfly: Cyberespionage Attacks Against Energy Suppliers. Retrieved April 8, 2016.

[4] FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved May 1, 2015.

[5] Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.

[6] US-CERT. (2017, December 13). Malware Analysis Report (MAR) - 10135536-B. Retrieved July 17, 2018.

[7] Yadav, A., et al. (2017, August 31). Cobian RAT – A backdoored RAT. Retrieved November 13, 2018.

[8] Chen, J. and Hsieh, M. (2017, November 7). REDBALDKNIGHT/BRONZE BUTLER’s Daserf Backdoor Now Using Steganography. Retrieved December 27, 2017.

[9] ESET. (2016, October). En Route with Sednit - Part 3: A Mysterious Downloader. Retrieved November 21, 2016.

[10] Symantec Security Response. (2011, November). W32.Duqu: The precursor to the next Stuxnet. Retrieved September 17, 2015.

[11] Falcone, R. and Miller-Osborn, J.. (2016, January 24). Scarlet Mimic: Years-Long Espionage Campaign Targets Minority Activists. Retrieved February 10, 2016.

[12] Reynolds, J.. (2016, September 14). H1N1: Technical analysis reveals new capabilities – part 2. Retrieved September 26, 2016.

[13] FireEye Labs. (2015, July). HAMMERTOSS: Stealthy Tactics Define a Russian Cyber Threat Group. Retrieved September 17, 2015.

[14] US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.

[15] Moran, N., & Villeneuve, N. (2013, August 12). Survival of the Fittest: New York Times Attackers Evolve Quickly [Blog]. Retrieved November 12, 2014.

[16] SecureWorks. (2013). The Lifecycle of Peer-to-Peer (Gameover) ZeuS. Retrieved August 19, 2015.

[17] Lee, B., Falcone, R. (2018, July 25). OilRig Targets Technology Service Provider and Government Agency with QUADAGENT. Retrieved August 9, 2018.

[18] Falcone, R., et al. (2018, July 27). New Threat Actor Group DarkHydrus Targets Middle East Government. Retrieved August 2, 2018.

[19] Axel F. (2017, April 27). APT Targets Financial Analysts with CVE-2017-0199. Retrieved February 15, 2018.

[20] Huss, D., et al. (2017, February 2). Oops, they did it again: APT Targets Russia and Belarus with ZeroT and PlugX. Retrieved April 5, 2018.

[21] Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting. Retrieved April 20, 2016.

## Defense

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be

## Tactics

- [[Command and Control|TA0011 - Command and Control]]

## Related Procedures (14)

- [[Creating Files with Zero-Width Spaces]]
- [[CRLF Filter Bypass with UTF-8 Encoding]]
- [[CRLF Filter Bypass with UTF-8 Encoding]]
- [[CRLF Filter Bypass with UTF-8 Encoding]]
- [[DB2 Injection - Select Nth Char Extraction]]
- [[Embed a File In an Image Using Steghide]]
- [[Exotic Payloads for Bypassing Email Filters]]
- [[Extract a Hidden File In an Image Using Steghide]]
- [[MYSQL Error Based - UpdateXML function Data Extraction]]
- [[MYSQL Union Based Injection to Extract Data from Users Table]]
- [[Out Of Band XPATH Injection]]
- [[PostgreSQL Time Based Table Dump]]
- [[TE Header Obfuscation]]
- [[XXE Injection in SOAP Messages]]
