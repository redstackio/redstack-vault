---
id: ae6e0ed5-2bb5-4109-b4d4-9c6a25f95101
name: Two-Factor Authentication Interception
type: technique
mitre_id: T1111
mitre_url: null
created_at: '2019-08-28T21:17:43.184294+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[2FA Bypass via Response Manipulation]]'
- '[[2FA Bypass with Array of OTPs]]'
- '[[Dictionary Hash Cracking with Hashcat]]'
- '[[GraphQL SQL Injection Exploitation]]'
---

# Two-Factor Authentication Interception

**MITRE ID**: T1111

## Description

Use of two- or multifactor authentication is recommended and provides a higher level of security than user names and passwords alone, but organizations should be aware of techniques that could be used to intercept and bypass these security mechanisms. Adversaries may target authentication mechanisms, such as smart cards, to gain access to systems, services, and network resources.If a smart card is used for two-factor authentication (2FA), then a keylogger will need to be used to obtain the password associated with a smart card during normal use. With both an inserted card and access to the smart card password, an adversary can connect to a network resource using the infected system to proxy the authentication with the inserted hardware token. [1]Adversaries may also employ a keylogger to similarly target other hardware tokens, such as RSA SecurID. Capturing token input (including a user's personal identification code) may provide temporary access (i.e. replay the one-time passcode until the next value rollover) as well as possibly enabling adversaries to reliably predict future authentication values (given access to both the algorithm and any seed values used to generate appended temporary codes). [2]Other methods of 2FA may be intercepted and used by an adversary to authenticate. It is common for one-time codes to be sent via out-of-band communications (email, SMS). If the device and/or service is not secured, then it may be vulnerable to interception. Although primarily focused on by cyber criminals, these authentication mechanisms have been targeted by advanced actors. [3]

# Detection

Detecting use of proxied smart card connections by an adversary may be difficult because it requires the token to be inserted into a system; thus it is more likely to be in use by a legitimate user and blend in with other network behavior.

Similar to Input Capture, keylogging activity can take various forms but can may be detected via installation of a driver, setting a hook, or usage of particular API calls associated with polling to intercept keystrokes.

# Mitigation

Remove smart cards when not in use. Protect devices and services used to transmit and receive out-of-band codes.

Identify and block potentially malicious software that may be used to intercept 2FA credentials on a system by using whitelisting [5] tools, like AppLocker, [6] [7] or Software Restriction Policies [8] where appropriate. [9]

# Footnotes

[1] Mandiant. (2011, January 27). Mandiant M-Trends 2011. Retrieved January 10, 2016.

[2] Jackson, William. (2011, June 7). RSA confirms its tokens used in Lockheed hack. Retrieved September 24, 2018.

[3] Sancho, D., Hacquebord, F., Link, R. (2014, July 22). Finding Holes Operation Emmental. Retrieved February 9, 2016.

[4] Blasco, J. (2012, January 12). Sykipot variant hijacks DOD and Windows smart cards. Retrieved January 10, 2016.

[5] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[6] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[7] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[8] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[9] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Remove smart cards when not in use. Protect devices and services used to transmit and receive out-of-band codes.

Identify and block potentially malicious software that may be used to intercept 2FA credentials on a system by using whitelisting (Citation: 

## Tactics

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures (4)

- [[2FA Bypass via Response Manipulation]]
- [[2FA Bypass with Array of OTPs]]
- [[Dictionary Hash Cracking with Hashcat]]
- [[GraphQL SQL Injection Exploitation]]
