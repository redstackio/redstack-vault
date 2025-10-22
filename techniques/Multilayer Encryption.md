---
id: 56f9a02e-7b67-4b1e-9e6d-18e6812f64e3
name: Multilayer Encryption
type: technique
mitre_id: T1079
mitre_url: null
created_at: '2019-08-28T21:17:24.536562+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
procedures:
- '[[SVG Alert WAF Bypass]]'
---

# Multilayer Encryption

**MITRE ID**: T1079

## Description

An adversary performs C2 communications using multiple layers of encryption, typically (but not exclusively) tunneling a custom encryption scheme within a protocol encryption scheme such as HTTPS or SMTPS.

# Detection

If malware uses Standard Cryptographic Protocol, SSL/TLS inspection can be used to detect command and control traffic within some encrypted communication channels. [7] SSL/TLS inspection does come with certain risks that should be considered before implementing to avoid potential security issues such as incomplete certificate validation. [8] After SSL/TLS inspection, additional cryptographic analysis may be needed to analyze the second layer of encryption.

With Custom Cryptographic Protocol, if malware uses encryption with symmetric keys, it may be possible to obtain the algorithm and key from samples and use them to decode network traffic to detect malware communications signatures. [9]

In general, analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. [6]

# Mitigation

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Use of encryption protocols may make typical network-based C2 detection more difficult due to a reduced ability to signature the traffic. Prior knowledge of adversary C2 infrastructure may be useful for domain and IP address blocking, but will likely not be an effective long-term solution because adversaries can change infrastructure often. [6]

# Footnotes

[1] Fidelis Cybersecurity. (2015, December 16). Fidelis Threat Advisory #1020: Dissecting the Malware Involved in the INOCNATION Campaign. Retrieved March 24, 2016.

[2] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

[3] Blasco, J. (2013, March 21). New Sykipot developments [Blog]. Retrieved November 12, 2014.

[4] Roger Dingledine, Nick Mathewson and Paul Syverson. (2004). Tor: The Second-Generation Onion Router. Retrieved December 21, 2017.

[5] Counter Threat Unit Research Team. (2017, May 18). WCry Ransomware Analysis. Retrieved March 26, 2019.

[6] Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting. Retrieved April 20, 2016.

[7] Butler, M. (2013, November). Finding Hidden Threats by Decrypting SSL. Retrieved April 5, 2016.

[8] Dormann, W. (2015, March 13). The Risks of SSL Inspection. Retrieved April 5, 2016.

[9] Fidelis Cybersecurity. (2015, August 4). Looking at the Sky for a DarkComet. Retrieved April 5, 2016.

## Defense

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Use of encryption protocols may make typical network-based C2 detectio

## Tactics

- [[Command and Control|TA0011 - Command and Control]]

## Related Procedures (1)

- [[SVG Alert WAF Bypass]]
