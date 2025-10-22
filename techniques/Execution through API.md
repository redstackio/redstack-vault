---
id: 9502daa9-e0b6-48c4-831a-8ecc1b30c41b
name: Execution through API
type: technique
mitre_id: T1106
mitre_url: null
created_at: '2019-08-28T21:17:44.668354+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[AWS Lambda Function Invocation]]'
- '[[AWS Lambda Role Privilege Escalation]]'
- '[[AWS Metadata Information Retrieval]]'
- '[[Azure VM RunCommand Execution]]'
- '[[Kubernetes API Request Simulation]]'
- '[[Linux Privilege Escalation - Writable Files Escalation]]'
- '[[MYSQL UDF Command Execution via lib_mysqludf_sys.so]]'
- '[[Oracle SQL and Java Command Execution]]'
- '[[Rundll32 Download and Execute via WebDAV and Remote Script Execution]]'
- '[[Windows - Privilege Escalation via Operating System Information Gathering]]'
---

# Execution through API

**MITRE ID**: T1106

## Description

Adversary tools may directly use the Windows application programming interface (API) to execute binaries. Functions such as the Windows API CreateProcess will allow programs and scripts to start other processes with proper path and argument parameters. [1]Additional Windows API calls that can be used to execute binaries include: [2]CreateProcessA() and CreateProcessW(),CreateProcessAsUserA() and CreateProcessAsUserW(),CreateProcessInternalA() and CreateProcessInternalW(),CreateProcessWithLogonW(), CreateProcessWithTokenW(),LoadLibraryA() and LoadLibraryW(),LoadLibraryExA() and LoadLibraryExW(),LoadModule(),LoadPackagedLibrary(),WinExec(),ShellExecuteA() and ShellExecuteW(),ShellExecuteExA() and ShellExecuteExW()

# Detection

Monitoring API calls may generate a significant amount of data and may not be directly useful for defense unless collected under specific circumstances, since benign use of Windows API functions such as CreateProcess are common and difficult to distinguish from malicious behavior. Correlation of other events with behavior surrounding API function calls using API monitoring will provide additional context to an event that may assist in determining if it is due to malicious behavior. Correlation of activity by process lineage by process ID may be sufficient.

# Mitigation

Mitigating specific API calls will likely have unintended side effects, such as preventing legitimate software from operating properly. Efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identifying subsequent malicious behavior. Audit and/or block potentially malicious software by using whitelisting [19] tools, like AppLocker, [20] [21] or Software Restriction Policies [22] where appropriate. [23]

# Footnotes

[1] Microsoft. (n.d.). CreateProcess function. Retrieved December 5, 2014.

[2] Kanthak, S. (2017). Application Verifier Provider. Retrieved February 13, 2017.

[3] Bitdefender. (2015, December). APT28 Under the Scope. Retrieved February 23, 2017.

[4] Mercer, W., Rascagneres, P. (2018, January 16). Korea In The Crosshairs. Retrieved May 21, 2018.

[5] Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.

[6] Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.

[7] Sherstobitoff, R. (2018, March 08). Hidden Cobra Targets Turkish Financial Sector With New Bankshot Implant. Retrieved May 18, 2018.

[8] Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.

[9] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[10] Falcone, R., et al. (2018, August 02). The Gorgon Group: Slithering Between Nation State and Cybercrime. Retrieved August 7, 2018.

[11] ASERT Team. (2018, April 04). Innaput Actors Utilize Remote Access Trojan Since 2016, Presumably Targeting Victim Files. Retrieved July 9, 2018.

[12] ESET, et al. (2018, January). Diplomats in Eastern Europe bitten by a Turla mosquito. Retrieved July 3, 2018.

[13] Vasilenko, R. (2013, December 17). An Analysis of PlugX Malware. Retrieved November 24, 2015.

[14] Ivanov, A. et al.. (2018, May 7). SynAck targeted ransomware uses the Doppelgänging technique. Retrieved May 22, 2018.

[15] Bettencourt, J. (2018, May 7). Kaspersky Lab finds new variant of SynAck ransomware using sophisticated Doppelgänging technique. Retrieved May 24, 2018.

[16] Salinas, M., Holguin, J. (2017, June). Evolution of Trickbot. Retrieved July 31, 2018.

[17] US-CERT. (2017, November 01). Malware Analysis Report (MAR) - 10135536-D. Retrieved July 16, 2018.

[18] Robert Falcone. (2017, February 14). XAgentOSX: Sofacy's Xagent macOS Tool. Retrieved July 12, 2017.

[19] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[20] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[21] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[22] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[23] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Mitigating specific API calls will likely have unintended side effects, such as preventing legitimate software from operating properly. Efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identifyin

## Tactics

- [[Execution|TA0002 - Execution]]

## Related Procedures (10)

- [[AWS Lambda Function Invocation]]
- [[AWS Lambda Role Privilege Escalation]]
- [[AWS Metadata Information Retrieval]]
- [[Azure VM RunCommand Execution]]
- [[Kubernetes API Request Simulation]]
- [[Linux Privilege Escalation - Writable Files Escalation]]
- [[MYSQL UDF Command Execution via lib_mysqludf_sys.so]]
- [[Oracle SQL and Java Command Execution]]
- [[Rundll32 Download and Execute via WebDAV and Remote Script Execution]]
- [[Windows - Privilege Escalation via Operating System Information Gathering]]
