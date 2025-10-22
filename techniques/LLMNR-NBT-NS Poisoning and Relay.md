---
id: 91e85e6e-33f2-402e-9720-6f67f92b9f3d
name: LLMNR/NBT-NS Poisoning and Relay
type: technique
mitre_id: T1171
mitre_url: null
created_at: '2019-08-28T21:17:30.760909+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Intercept NTLMv2 Hashes via LLMNR and NetBIOS Requests (Windows)]]'
---

# LLMNR/NBT-NS Poisoning and Relay

**MITRE ID**: T1171

## Description

Link-Local Multicast Name Resolution (LLMNR) and NetBIOS Name Service (NBT-NS) are Microsoft Windows components that serve as alternate methods of host identification. LLMNR is based upon the Domain Name System (DNS) format and allows hosts on the same local link to perform name resolution for other hosts. NBT-NS identifies systems on a local network by their NetBIOS name. [1] [2]Adversaries can spoof an authoritative source for name resolution on a victim network by responding to LLMNR (UDP 5355)/NBT-NS (UDP 137) traffic as if they know the identity of the requested host, effectively poisoning the service so that the victims will communicate with the adversary controlled system. If the requested host belongs to a resource that requires identification/authentication, the username and NTLMv2 hash will then be sent to the adversary controlled system. The adversary can then collect the hash information sent over the wire through tools that monitor the ports for traffic or through Network Sniffing and crack the hashes offline through Brute Force to obtain the plaintext passwords. In some cases where an adversary has access to a system that is in the authentication path between systems or when automated scans that use credentials attempt to authenticate to an adversary controlled system, the NTLMv2 hashes can be intercepted and relayed to access and execute code against a target system. The relay step can happen in conjunction with poisoning but may also be independent of it. [3][4]Several tools exist that can be used to poison name services within local networks such as NBNSpoof, Metasploit, and Responder. [5] [6] [7]

# Detection

Monitor HKLM\Software\Policies\Microsoft\Windows NT\DNSClient for changes to the "EnableMulticast" DWORD value. A value of "0" indicates LLMNR is disabled. [15]

Monitor for traffic on ports UDP 5355 and UDP 137 if LLMNR/NetBIOS is disabled by security policy.

Deploy an LLMNR/NBT-NS spoofing detection tool.[16] Monitoring of Windows event logs for event IDs 4697 and 7045 may help in detecting successful relay techniques.[4]

# Mitigation

Disable LLMNR and NetBIOS in local computer security settings or by group policy if they are not needed within an environment. [13]

Use host-based security software to block LLMNR/NetBIOS traffic. Enabling SMB Signing can stop NTLMv2 relay attacks.[3][4][14]

# Footnotes

[1] Wikipedia. (2016, July 7). Link-Local Multicast Name Resolution. Retrieved November 17, 2017.

[2] Microsoft. (n.d.). NetBIOS Name Resolution. Retrieved November 17, 2017.

[3] Salvati, M. (2017, June 2). Practical guide to NTLM Relaying in 2017 (A.K.A getting a foothold in under 5 minutes). Retrieved February 7, 2019.

[4] Kuehn, E. (2018, April 11). Ever Run a Relay? Why SMB Relays Should Be On Your Mind. Retrieved February 7, 2019.

[5] Nomex. (2014, February 7). NBNSpoof. Retrieved November 17, 2017.

[6] Francois, R. (n.d.). LLMNR Spoofer. Retrieved November 17, 2017.

[7] Gaffie, L. (2016, August 25). Responder. Retrieved November 17, 2017.

[8] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[9] Robertson, K. (2015, April 2). Inveigh: Windows PowerShell ADIDNS/LLMNR/mDNS/NBNS spoofer/man-in-the-middle tool. Retrieved March 11, 2019.

[10] SecureAuth. (n.d.).  Retrieved January 15, 2019.

[11] Nettitude. (2016, June 8). PoshC2: Powershell C2 Server and Implants. Retrieved April 23, 2019.

[12] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

[13] Metcalf, S. (2016, October 21). Securing Windows Workstations: Developing a Secure Baseline. Retrieved November 17, 2017.

[14] Microsoft. (2008, September 10). Using SMB Packet Signing. Retrieved February 7, 2019.

[15] Sternstein, J. (2013, November). Local Network Attacks: LLMNR and NBT-NS Poisoning. Retrieved November 17, 2017.

[16] Robertson, K. (2016, August 28). Conveigh. Retrieved November 17, 2017.

## Defense

Disable LLMNR and NetBIOS in local computer security settings or by group policy if they are not needed within an environment. (Citation: ADSecurity Windows Secure Baseline)

Use host-based security software to block LLMNR/NetBIOS traffic. Enabling SMB Si

## Tactics

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures (1)

- [[Intercept NTLMv2 Hashes via LLMNR and NetBIOS Requests (Windows)]]
