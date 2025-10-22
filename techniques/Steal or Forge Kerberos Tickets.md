---
id: bbb32155-8d5a-478d-b3f3-ba4ba2f99c0b
name: Steal or Forge Kerberos Tickets
type: technique
mitre_id: T1558
mitre_url: null
created_at: '2023-04-06T00:31:25.980033+00:00'
updated_at: '2023-04-06T03:56:31.622631+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Active Directory ACL Abuse via Kerberoasting and AS-REP Roasting]]'
- '[[Active Directory Assessment and Privilege Escalation]]'
- '[[CCACHE Ticket Reuse from Keyring with Tickey]]'
- '[[CCACHE Ticket Reuse from Keytab]]'
- '[[CCACHE Ticket Reuse from /tmp]]'
- '[[Golden Certificate Domain Persistence]]'
- '[[Golden Ticket Attack with Mimikatz]]'
- '[[Golden Ticket Creation via Kerberos Purge]]'
- '[[HTML GET CSRF Payload with User Interaction]]'
- '[[HTML GET CSRF Payload with User Interaction]]'
- '[[Kerberos AS-REP Roasting Attack]]'
- '[[Kerberos Bronze Bit Attack]]'
- '[[Kerberos Bronze Bit Attack Procedure]]'
- '[[Kerberos Clock Synchronization Attack]]'
- '[[Kerberos Clock Synchronization Attack]]'
- '[[Kerberos Constrained Delegation - Impersonation on Resource]]'
- '[[Kerberos S4U2self Privilege Escalation]]'
- '[[Kerberos Unconstrained Delegation with SpoolService Abuse]]'
- '[[Kerberos Unconstrained Delegation with SpoolService Abuse]]'
- '[[NTLM Reflection SMB Relay Attack]]'
- '[[OAuth Token Theft via Redirect URI]]'
- '[[Pass-the-Golden-Ticket Attack using Meterpreter]]'
- '[[Pass-the-Ticket with Silver Tickets]]'
- '[[RODC Key List Extraction and Golden Ticket Creation]]'
- '[[samAccountName Spoofing Attack]]'
- '[[User Certificate and TGT Persistence via Domain Request]]'
---

# Steal or Forge Kerberos Tickets

**MITRE ID**: T1558

## Description

Adversaries may attempt to subvert Kerberos authentication by stealing or forging Kerberos tickets to enable [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003). Kerberos is an authentication protocol widely used in modern Windows domain environments. In Kerberos environments, referred to as “realms”, there are three basic participants: client, service, and Key Distribution Center (KDC).(Citation: ADSecurity Kerberos Ring Decoder) Clients request access to a service and through the exchange of Kerberos tickets, originating from KDC, they are granted access after having successfully authenticated. The KDC is responsible for both authentication and ticket granting.  Adversaries may attempt to abuse Kerberos by stealing tickets or forging tickets to enable unauthorized access.

On Windows, the built-in <code>klist</code> utility can be used to list and analyze cached Kerberos tickets.(Citation: Microsoft Klist)

Linux systems on Active Directory domains store Kerberos credentials locally in the credential cache file referred to as the "ccache". The credentials are stored in the ccache file while they remain valid and generally while a user's session lasts.(Citation: MIT ccache) On modern Redhat Enterprise Linux systems, and derivative distributions, the System Security Services Daemon (SSSD) handles Kerberos tickets. By default SSSD maintains a copy of the ticket database that can be found in <code>/var/lib/sss/secrets/secrets.ldb</code> as well as the corresponding key located in <code>/var/lib/sss/secrets/.secrets.mkey</code>. Both files require root access to read. If an adversary is able to access the database and key, the credential cache Kerberos blob can be extracted and converted into a usable Kerberos ccache file that adversaries may use for [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003). The ccache file may also be converted into a Windows format using tools such as Kekeo.(Citation: Linux Kerberos Tickets)(Citation: Brining MimiKatz to Unix)(Citation: Kekeo)

Kerberos tickets on macOS are stored in a standard ccache format, similar to Linux. By default, access to these ccache entries is federated through the KCM daemon process via the Mach RPC protocol, which uses the caller's environment to determine access. The storage location for these ccache entries is influenced by the <code>/etc/krb5.conf</code> configuration file and the <code>KRB5CCNAME</code> environment variable which can specify to save them to disk or keep them protected via the KCM daemon. Users can interact with ticket storage using <code>kinit</code>, <code>klist</code>, <code>ktutil</code>, and <code>kcc</code> built-in binaries or via Apple's native Kerberos framework. Adversaries can use open source tools to interact with the ccache files directly or to use the Kerberos framework to call lower-level APIs for extracting the user's TGT or Service Tickets.(Citation: SpectorOps Bifrost Kerberos macOS 2019)(Citation: macOS kerberos framework MIT)

## Tactics

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures (26)

- [[Active Directory ACL Abuse via Kerberoasting and AS-REP Roasting]]
- [[Active Directory Assessment and Privilege Escalation]]
- [[CCACHE Ticket Reuse from Keyring with Tickey]]
- [[CCACHE Ticket Reuse from Keytab]]
- [[CCACHE Ticket Reuse from /tmp]]
- [[Golden Certificate Domain Persistence]]
- [[Golden Ticket Attack with Mimikatz]]
- [[Golden Ticket Creation via Kerberos Purge]]
- [[HTML GET CSRF Payload with User Interaction]]
- [[HTML GET CSRF Payload with User Interaction]]
- [[Kerberos AS-REP Roasting Attack]]
- [[Kerberos Bronze Bit Attack]]
- [[Kerberos Bronze Bit Attack Procedure]]
- [[Kerberos Clock Synchronization Attack]]
- [[Kerberos Clock Synchronization Attack]]
- [[Kerberos Constrained Delegation - Impersonation on Resource]]
- [[Kerberos S4U2self Privilege Escalation]]
- [[Kerberos Unconstrained Delegation with SpoolService Abuse]]
- [[Kerberos Unconstrained Delegation with SpoolService Abuse]]
- [[NTLM Reflection SMB Relay Attack]]

*...and 6 more*
