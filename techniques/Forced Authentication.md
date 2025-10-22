---
id: dec333d6-1f00-4246-bf96-7a18f4d93ee8
name: Forced Authentication
type: technique
mitre_id: T1187
mitre_url: null
created_at: '2019-08-28T21:17:42.799774+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
---

# Forced Authentication

**MITRE ID**: T1187

## Description

The Server Message Block (SMB) protocol is commonly used in Windows networks for authentication and communication between systems for access to resources and file sharing. When a Windows system attempts to connect to an SMB resource it will automatically attempt to authenticate and send credential information for the current user to the remote system. [1] This behavior is typical in enterprise environments so that users do not need to enter credentials to access network resources. Web Distributed Authoring and Versioning (WebDAV) is typically used by Windows systems as a backup protocol when SMB is blocked or fails. WebDAV is an extension of HTTP and will typically operate over TCP ports 80 and 443. [2] [3]Adversaries may take advantage of this behavior to gain access to user account hashes through forced SMB authentication. An adversary can send an attachment to a user through spearphishing that contains a resource link to an external server controlled by the adversary (i.e. Template Injection), or place a specially crafted file on navigation path for privileged accounts (e.g. .SCF file placed on desktop) or on a publicly accessible share to be accessed by victim(s). When the user's system accesses the untrusted resource it will attempt authentication and send information including the user's hashed credentials over SMB to the adversary controlled server. [4] With access to the credential hash, an adversary can perform off-line Brute Force cracking to gain access to plaintext credentials, or reuse it for Pass the Hash. [5]There are several different ways this can occur. [6] Some specifics from in-the-wild use include:A spearphishing attachment containing a document with a resource that is automatically loaded when the document is opened (i.e. Template Injection). The document can include, for example, a request similar to file[:]//[remote address]/Normal.dotm to trigger the SMB request. [7]A modified .LNK or .SCF file with the icon filename pointing to an external reference such as \[remote address]\pic.png that will force the system to load the resource when the icon is rendered to repeatedly gather credentials. [7]

# Detection

Monitor for SMB traffic on TCP ports 139, 445 and UDP port 137 and WebDAV traffic attempting to exit the network to unknown external systems. If attempts are detected, then investigate endpoint data sources to find the root cause.

Monitor creation and modification of .LNK, .SCF, or any other files on systems and within virtual environments that contain resources that point to external network resources as these could be used to gather credentials when the files are rendered. [7]

# Mitigation

Block SMB  traffic from exiting an enterprise network with egress filtering or by blocking TCP ports 139, 445 and UDP port 137. Filter or block WebDAV protocol traffic from exiting the network. If access to external resources over SMB and WebDAV is necessary, then traffic should be tightly limited with whitelisting. [10] [7]

For internal traffic, monitor the workstation-to-workstation unusual (vs. baseline) SMB traffic. For many networks there should not be any, but it depends on how systems on the network are configured and where resources are located.

Use strong passwords to increase the difficulty of credential hashes from being cracked if they are obtained.

# Footnotes

[1] Wikipedia. (2017, December 16). Server Message Block. Retrieved December 21, 2017.

[2] Stevens, D. (2017, November 13). WebDAV Traffic To Malicious Sites. Retrieved December 21, 2017.

[3] Microsoft. (n.d.). Managing WebDAV Security (IIS 6.0). Retrieved December 21, 2017.

[4] Dunning, J. (2016, August 1). Hashjacking. Retrieved December 21, 2017.

[5] Cylance. (2015, April 13). Redirect to SMB. Retrieved December 21, 2017.

[6] Malith, O. (2017, March 24). Places of Interest in Stealing NetNTLM Hashes. Retrieved January 26, 2018.

[7] US-CERT. (2017, October 20). Alert (TA17-293A): Advanced Persistent Threat Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved November 2, 2017.

[8] Falcone, R. (2018, August 07). DarkHydrus Uses Phishery to Harvest Credentials in the Middle East. Retrieved August 10, 2018.

[9] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[10] US-CERT. (2017, March 16). SMB Security Best Practices. Retrieved December 21, 2017.

## Defense

Block SMB  traffic from exiting an enterprise network with egress filtering or by blocking TCP ports 139, 445 and UDP port 137. Filter or block WebDAV protocol traffic from exiting the network. If access to external resources over SMB and WebDAV is necess

## Tactics

- [[Credential Access|TA0006 - Credential Access]]
