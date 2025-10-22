---
id: ff91a479-cfdc-46c5-9e48-79b18ef595a9
name: Data Encoding
type: technique
mitre_id: T1132
mitre_url: null
created_at: '2019-08-28T21:17:43.485987+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
procedures:
- '[[AWS Secrets Manager Credential Exfiltration]]'
- '[[Cobalt Strike Team Server Installation and Execution]]'
- '[[CRLF Filter Bypass with UTF-8 Encoding]]'
- '[[CRLF Filter Bypass with UTF-8 Encoding]]'
- '[[CRLF Filter Bypass with UTF-8 Encoding]]'
- '[[Double URL encoded Directory Traversal]]'
- '[[Exotic Payloads for Bypassing Dot Filters in XSS Attacks]]'
- '[[Filter Bypass using Katakana Library]]'
- '[[JavaScript Alert WAF Bypass]]'
- '[[Malicious HLS playlist inside an AVI video]]'
- '[[MSSQL Out of Band DNS Exfiltration]]'
- '[[Out Of Band XPATH Injection]]'
- '[[Polyglot Command Injection for DNS Data Exfiltration]]'
- '[[PostgreSQL Time Based Table Dump]]'
- '[[Reflected XSS Attack Prevention]]'
- '[[SMB Beacon Payload with Command Line Interactions]]'
- '[[XXE Denial of Service via YAML Attack]]'
- '[[XXE File Retrieval with PHP Wrapper]]'
- '[[XXE in DOCX Files]]'
- '[[XXE Injection in SOAP Messages]]'
---

# Data Encoding

**MITRE ID**: T1132

## Description

Command and control (C2) information is encoded using a standard data encoding system. Use of data encoding may be to adhere to existing protocol specifications and includes use of ASCII, Unicode, Base64,  MIME, UTF-8, or other binary-to-text and character encoding systems. [1] [2] Some data encoding systems may also result in data compression, such as gzip.

# Detection

Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. [35]

# Mitigation

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools. [35]

# Footnotes

[1] Wikipedia. (2016, December 26). Binary-to-text encoding. Retrieved March 1, 2017.

[2] Wikipedia. (2017, February 19). Character Encoding. Retrieved March 1, 2017.

[3] Kaspersky Lab's Global Research and Analysis Team. (2015, December 4). Sofacy APT hits high profile targets with updated toolset. Retrieved December 10, 2015.

[4] Grunzweig, J., Lee, B. (2016, January 22). New Attacks Linked to C0d0so0 Group. Retrieved August 2, 2018.

[5] Ackerman, G., et al. (2018, December 21). OVERRULED: Containing a Potentially Destructive Adversary. Retrieved January 17, 2019.

[6] Doaty, J., Garrett, P.. (2018, September 10). We’re Seeing a Resurgence of the Demonic Astaroth WMIC Trojan. Retrieved April 17, 2019.

[7] Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.

[8] Levene, B. et al.. (2018, March 7). Patchwork Continues to Deliver BADNEWS to the Indian Subcontinent. Retrieved March 31, 2018.

[9] Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.

[10] Sherstobitoff, R. (2018, March 08). Hidden Cobra Targets Turkish Financial Sector With New Bankshot Implant. Retrieved May 18, 2018.

[11] Counter Threat Unit Research Team. (2017, October 12). BRONZE BUTLER Targets Japanese Enterprises. Retrieved January 4, 2018.

[12] Villeneuve, N., Bennett, J. T., Moran, N., Haq, T., Scott, M., & Geers, K. (2014). OPERATION “KE3CHANG”: Targeted Attacks Against Ministries of Foreign Affairs. Retrieved November 12, 2014.

[13] FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.

[14] Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.

[15] Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.

[16] M.Léveillé, M.. (2014, February 21). An In-depth Analysis of Linux/Ebury. Retrieved April 19, 2019.

[17] Falcone, R., et al.. (2015, June 16). Operation Lotus Blossom. Retrieved February 15, 2016.

[18] Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.

[19] Unit 42. (2017, December 15). Unit 42 Playbook Viewer. Retrieved December 20, 2017.

[20] Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.

[21] Sherstobitoff, R. (2018, February 12). Lazarus Resurfaces, Targets Global Banks and Bitcoin Users. Retrieved February 19, 2018.

[22] Anomali Labs. (2018, December 6). Pulling Linux Rabbit/Rabbot Malware Out of a Hat. Retrieved March 4, 2019.

[23] Gross, J. (2016, February 23). Operation Dust Storm. Retrieved September 19, 2017.

[24] Sherstobitoff, R., Malhotra, A. (2018, October 18). ‘Operation Oceansalt’ Attacks South Korea, U.S., and Canada With Source Code From Chinese Hacker Group. Retrieved November 30, 2018.

[25] Kaspersky Lab's Global Research & Analysis Team. (2018, October 15). Octopus-infested seas of Central Asia. Retrieved November 14, 2018.

[26] Lee, B., Falcone, R. (2018, February 23). OopsIE! OilRig Uses ThreeDollars to Deliver New Trojan. Retrieved July 16, 2018.

[27] Cymmetria. (2016). Unveiling Patchwork - The Copy-Paste APT. Retrieved August 3, 2016.

[28] Grunzweig, J., et al. (2016, May 24). New Wekby Attacks Use DNS Requests As Command and Control Mechanism. Retrieved August 17, 2016.

[29] Lancaster, T.. (2017, November 14). Muddying the Water: Targeted Attacks in the Middle East. Retrieved March 15, 2018.

[30] Sardiwal, M, et al. (2017, December 7). New Targeted Attack in the Middle East by APT34, a Suspected Iranian Threat Group, Using CVE-2017-11882 Exploit. Retrieved December 20, 2017.

[31] Cherepanov, A.. (2016, May 17). Operation Groundbait: Analysis of a surveillance toolkit. Retrieved May 18, 2016.

[32] Grunzweig, J.. (2015, July 14). Unit 42 Technical Analysis: Seaduke. Retrieved August 3, 2016.

[33] Check Point Research. (2019, February 4). SpeakUp: A New Undetected Backdoor Linux Trojan. Retrieved April 17, 2019.

[34] US-CERT. (2017, November 01). Malware Analysis Report (MAR) - 10135536-D. Retrieved July 16, 2018.

[35] Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting. Retrieved April 20, 2016.

## Defense

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be

## Tactics

- [[Command and Control|TA0011 - Command and Control]]

## Related Procedures (20)

- [[AWS Secrets Manager Credential Exfiltration]]
- [[Cobalt Strike Team Server Installation and Execution]]
- [[CRLF Filter Bypass with UTF-8 Encoding]]
- [[CRLF Filter Bypass with UTF-8 Encoding]]
- [[CRLF Filter Bypass with UTF-8 Encoding]]
- [[Double URL encoded Directory Traversal]]
- [[Exotic Payloads for Bypassing Dot Filters in XSS Attacks]]
- [[Filter Bypass using Katakana Library]]
- [[JavaScript Alert WAF Bypass]]
- [[Malicious HLS playlist inside an AVI video]]
- [[MSSQL Out of Band DNS Exfiltration]]
- [[Out Of Band XPATH Injection]]
- [[Polyglot Command Injection for DNS Data Exfiltration]]
- [[PostgreSQL Time Based Table Dump]]
- [[Reflected XSS Attack Prevention]]
- [[SMB Beacon Payload with Command Line Interactions]]
- [[XXE Denial of Service via YAML Attack]]
- [[XXE File Retrieval with PHP Wrapper]]
- [[XXE in DOCX Files]]
- [[XXE Injection in SOAP Messages]]
