---
id: a08e445c-6ff3-412c-83c8-4b8f30d47c5e
name: SID-History Injection
type: technique
mitre_id: T1178
mitre_url: null
created_at: '2019-08-28T21:17:41.193882+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# SID-History Injection

**MITRE ID**: T1178

## Description

The Windows security identifier (SID) is a unique value that identifies a user or group account. SIDs are used by Windows security in both security descriptors and access tokens. [1] An account can hold additional SIDs in the SID-History Active Directory attribute [2], allowing inter-operable account migration between domains (e.g., all values in SID-History are included in access tokens).Adversaries may use this mechanism for privilege escalation. With Domain Administrator (or equivalent) rights, harvested or well-known SID values [3] may be inserted into SID-History to enable impersonation of arbitrary users/groups such as Enterprise Administrators. This manipulation may result in elevated access to local resources and/or access to otherwise inaccessible domains via lateral movement techniques such as Remote Services, Windows Admin Shares, or Windows Remote Management.

# Detection

Examine data in user’s SID-History attributes using the PowerShell Get-ADUser Cmdlet [10], especially users who have SID-History values from the same domain. [11]

Monitor Account Management events on Domain Controllers for successful and failed changes to SID-History. [11]  [12]

Monitor Windows API calls to the DsAddSidHistory function. [12]

# Mitigation

Clean up SID-History attributes after legitimate account migration is complete.

Consider applying SID Filtering to interforest trusts, such as forest trusts and external trusts, to exclude SID-History from requests to access domain resources. SID Filtering ensures that any authentication requests over a trust only contain SIDs of security principals from the trusted domain (i.e. preventing the trusted domain from claiming a user has membership in groups outside of the domain).

SID Filtering of forest trusts is enabled by default, but may have been disabled in some cases to allow a child domain to transitively access forest trusts. SID Filtering of external trusts is automatically enabled on all created external trusts using Server 2003 or later domain controllers. [7] [8] However note that SID Filtering is not automatically applied to legacy trusts or may have been deliberately disabled to allow inter-domain access to resources.

SID Filtering can be applied by: [9]

Disabling SIDHistory on forest trusts using the netdom tool (netdom trust  /domain: /EnableSIDHistory:no on the domain controller). Applying SID Filter Quarantining to external trusts using the netdom tool (netdom trust  /domain: /quarantine:yes on the domain controller)Applying SID Filtering to domain trusts within a single forest is not recommended as it is an unsupported configuration and can cause breaking changes. [9] [6] If a domain within a forest is untrustworthy then it should not be a member of the forest. In this situation it is necessary to first split the trusted and untrusted domains into separate forests where SID Filtering can be applied to an interforest trust.

# Footnotes

[1] Microsoft. (n.d.). Security Identifiers. Retrieved November 30, 2017.

[2] Microsoft. (n.d.). Active Directory Schema - SID-History attribute. Retrieved November 30, 2017.

[3] Microsoft. (2017, June 23). Well-known security identifiers in Windows operating systems. Retrieved November 30, 2017.

[4] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[5] Metcalf, S. (2015, November 13). Unofficial Guide to Mimikatz & Command Reference. Retrieved December 23, 2015.

[6] Metcalf, S. (2015, August 7). Kerberos Golden Tickets are Now More Golden. Retrieved December 1, 2017.

[7] Microsoft. (2014, November 19). Security Considerations for Trusts. Retrieved November 30, 2017.

[8] Microsoft. (n.d.). Configuring SID Filter Quarantining on External Trusts. Retrieved November 30, 2017.

[9] Microsoft. (2012, September 11). Command-Line Reference - Netdom Trust. Retrieved November 30, 2017.

[10] Microsoft. (n.d.). Active Directory Cmdlets - Get-ADUser. Retrieved November 30, 2017.

[11] Metcalf, S. (2015, September 19). Sneaky Active Directory Persistence #14: SID History. Retrieved November 30, 2017.

[12] Microsoft. (n.d.). Using DsAddSidHistory. Retrieved November 30, 2017.

## Defense

Clean up SID-History attributes after legitimate account migration is complete.

Consider applying SID Filtering to interforest trusts, such as forest trusts and external trusts, to exclude SID-History from requests to access domain resources. SID Filteri

## Tactics

- [[Privilege Escalation|TA0004 - Privilege Escalation]]
