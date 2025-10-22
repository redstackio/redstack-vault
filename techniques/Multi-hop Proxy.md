---
id: 1c677d43-0ddd-4d3d-937d-9588dbac4c2f
name: Multi-hop Proxy
type: technique
mitre_id: T1188
mitre_url: null
created_at: '2019-08-28T21:17:40.604058+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
procedures:
- '[[Backdoored Docker Image Creation]]'
---

# Multi-hop Proxy

**MITRE ID**: T1188

## Description

To disguise the source of malicious traffic, adversaries may chain together multiple proxies. Typically, a defender will be able to identify the last proxy traffic traversed before it enters their network; the defender may or may not be able to identify any previous proxies before the last-hop proxy. This technique makes identifying the original source of the malicious traffic even more difficult by requiring the defender to trace malicious traffic through several proxies to identify its source.

# Detection

When observing use of Multi-hop proxies, network data from the actual command and control servers could allow correlating incoming and outgoing flows to trace malicious traffic back to its source. Multi-hop proxies can also be detected by alerting on traffic to known anonymity networks (such as Tor) or known adversary infrastructure that uses this technique.

# Mitigation

Traffic to known anonymity networks and C2 infrastructure can be blocked through the use of network black and white lists. It should be noted that this kind of blocking may be circumvented by other techniques like Domain Fronting.

# Footnotes

[1] Dunwoody, M. and Carr, N.. (2016, September 27). No Easy Breach DerbyCon 2016. Retrieved October 4, 2016.

[2] Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.

[3] Vengerik, B. et al.. (2014, December 5). Hacking the Street? FIN4 Likely Playing the Market. Retrieved December 17, 2018.

[4] Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.

[5] Patrick Wardle. (2017, January 1). Mac Malware of 2016. Retrieved September 21, 2018.

[6] Roger Dingledine, Nick Mathewson and Paul Syverson. (2004). Tor: The Second-Generation Onion Router. Retrieved December 21, 2017.

[7] Counter Threat Unit Research Team. (2017, May 18). WCry Ransomware Analysis. Retrieved March 26, 2019.

## Defense

Traffic to known anonymity networks and C2 infrastructure can be blocked through the use of network black and white lists. It should be noted that this kind of blocking may be circumvented by other techniques like [Domain Fronting](https://attack.mitre.or

## Tactics

- [[Command and Control|TA0011 - Command and Control]]

## Related Procedures (1)

- [[Backdoored Docker Image Creation]]
