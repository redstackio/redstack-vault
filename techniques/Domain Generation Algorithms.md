---
id: 8fe7b0a4-e2eb-468f-b8f2-6bc0a863380b
name: Domain Generation Algorithms
type: technique
mitre_id: T1483
mitre_url: null
created_at: '2019-08-28T21:17:47.477764+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
procedures:
- '[[AdminCount Abuse]]'
- '[[Azure Reconnaissance]]'
- '[[Golden Certificate Domain Persistence]]'
---

# Domain Generation Algorithms

**MITRE ID**: T1483

## Description

Adversaries may make use of Domain Generation Algorithms (DGAs) to dynamically identify a destination for command and control traffic rather than relying on a list of static IP addresses or domains. This has the advantage of making it much harder for defenders block, track, or take over the command and control channel, as there potentially could be thousands of domains that malware can check for instructions.[1][2][3]DGAs can take the form of apparently random or "gibberish" strings (ex: istgmxdejdnxuyla.ru) when they construct domain names by generating each letter. Alternatively, some DGAs employ whole words as the unit by concatenating words together instead of letters (ex: cityjulydish.net). Many DGAs are time-based, generating a different domain for each time period (hourly, daily, monthly, etc). Others incorporate a seed value as well to make predicting future domains more difficult for defenders.[1][2][4][5]Adversaries may use DGAs for the purpose of Fallback Channels. When contact is lost with the primary command and control server malware may employ a DGA as a means to reestablishing command and control.[4][6][7]

# Detection

Detecting dynamically generated domains can be challenging due to the number of different DGA algorithms, constantly evolving malware families, and the increasing complexity of the algorithms. There is a myriad of approaches for detecting a pseudo-randomly generated domain name, including using frequency analysis, Markov chains, entropy, proportion of dictionary words, ratio of vowels to other characters, and more.[12] CDN domains may trigger these detections due to the format of their domain names. In addition to detecting a DGA domain based on the name, another more general approach for detecting a suspicious domain is to check for recently registered names or for rarely visited domains.

Machine learning approaches to detecting DGA domains have been developed and have seen success in applications. One approach is to use N-Gram methods to determine a randomness score for strings used in the domain name. If the randomness score is high, and the domains are not whitelisted (CDN, etc), then it may be determined if a domain or related to a legitimate host or DGA.[13] Another approach is to use deep learning to classify domains as DGA-generated.[14]

# Mitigation

This technique may be difficult to mitigate since the domains can be registered just before they are used, and disposed shortly after. Malware researchers can reverse-engineer malware variants that use DGAs and determine future domains that the malware will attempt to contact, but this is a time and resource intensive effort.[1][10] Malware is also increasingly incorporating seed values that can be unique for each instance, which would then need to be determined to extract future generated domains. In some cases, the seed that a particular sample uses can be extracted from DNS traffic.[5] Even so, there can be thousands of possible domains generated per day; this makes it impractical for defenders to preemptively register all possible C2 domains due to the cost. In some cases a local DNS sinkhole may be used to help prevent DGA-based command and control at a reduced cost.

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific protocol used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools. [11]

# Footnotes

[1] Sternfeld, U. (2016). Dissecting Domain Generation Algorithms: Eight Real World DGA Variants. Retrieved February 18, 2019.

[2] Scarfo, A. (2016, October 10). Domain Generation Algorithms – Why so effective?. Retrieved February 18, 2019.

[3] Unit 42. (2019, February 7). Threat Brief: Understanding Domain Generation Algorithms (DGA). Retrieved February 19, 2019.

[4] Brumaghin, E. et al. (2017, September 18). CCleanup: A Vast Number of Machines at Risk. Retrieved March 9, 2018.

[5] Liu, H. and Yuzifovich, Y. (2018, January 9). A Death Match of Domain Generation Algorithms. Retrieved February 18, 2019.

[6] Dunwoody, M.. (2017, April 3). Dissecting One of APT29’s Fileless WMI and PowerShell Backdoors (POSHSPY). Retrieved April 5, 2017.

[7] ESET. (2017, December 21). Sednit update: How Fancy Bear Spent the Year. Retrieved February 18, 2019.

[8] Sardiwal, M, et al. (2017, December 7). New Targeted Attack in the Middle East by APT34, a Suspected Iranian Threat Group, Using CVE-2017-11882 Exploit. Retrieved December 20, 2017.

[9] M.Léveillé, M.. (2014, February 21). An In-depth Analysis of Linux/Ebury. Retrieved April 19, 2019.

[10] Kasza, A. (2015, February 18). Using Algorithms to Brute Force Algorithms. Retrieved February 18, 2019.

[11] Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting. Retrieved April 20, 2016.

[12] Jacobs, J. (2014, October 2). Building a DGA Classifier: Part 2, Feature Engineering. Retrieved February 18, 2019.

[13] Chen, L., Wang, T.. (2017, May 5). Detecting Algorithmically Generated Domains Using Data Visualization and N-Grams Methods . Retrieved April 26, 2019.

[14] Ahuja, A., Anderson, H., Grant, D., Woodbridge, J.. (2016, November 2). Predicting Domain Generation Algorithms with Long Short-Term Memory Networks. Retrieved April 26, 2019.

## Defense

This technique may be difficult to mitigate since the domains can be registered just before they are used, and disposed shortly after. Malware researchers can reverse-engineer malware variants that use DGAs and determine future domains that the malware wi

## Tactics

- [[Command and Control|TA0011 - Command and Control]]

## Related Procedures (3)

- [[AdminCount Abuse]]
- [[Azure Reconnaissance]]
- [[Golden Certificate Domain Persistence]]
