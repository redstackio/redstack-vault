---
id: a8e46090-f914-404d-95f1-bbcfb70b8a54
name: Supply Chain Compromise
type: technique
mitre_id: T1195
mitre_url: null
created_at: '2019-08-28T21:17:29.766991+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
procedures:
- '[[MSSQL List Tables]]'
- '[[MYSQL Injection - Current Queries]]'
---

# Supply Chain Compromise

**MITRE ID**: T1195

## Description

Supply chain compromise is the manipulation of products or product delivery mechanisms prior to receipt by a final consumer for the purpose of data or system compromise. Supply chain compromise can take place at any stage of the supply chain including:Manipulation of development toolsManipulation of a development environmentManipulation of source code repositories (public or private)Manipulation of source code in open-source dependenciesManipulation of software update/distribution mechanismsCompromised/infected system images (multiple cases of removable media infected at the factory)Replacement of legitimate software with modified versionsSales of modified/counterfeit products to legitimate distributorsShipment interdictionWhile supply chain compromise can impact any component of hardware or software, attackers looking to gain execution have often focused on malicious additions to legitimate software in software distribution or update channels. [1] [2] [3] Targeting may be specific to a desired victim set [4] or malicious software may be distributed to a broad set of consumers but only move on to additional tactics on specific victims. [1] [3] Popular open source projects that are used as dependencies in many applications may also be targeted as a means to add malicious code to users of the dependency. [5]

# Detection

Use verification of distributed binaries through hash checking or other integrity checking mechanisms. Scan downloads for malicious signatures and attempt to test software and updates prior to deployment while taking note of potential suspicious activity. Perform physical inspection of hardware to look for potential tampering.

# Mitigation

Apply supply chain risk management (SCRM) practices and procedures [11], such as supply chain analysis and appropriate risk management, throughout the life-cycle of a system.

Leverage established software development lifecycle (SDLC) practices [12]: 

Uniquely Identify Supply Chain Elements, Processes, and ActorsLimit Access and Exposure within the Supply ChainEstablish and Maintain the Provenance of Elements, Processes, Tools, and DataShare Information within Strict LimitsPerform SCRM Awareness and TrainingUse Defensive Design for Systems, Elements, and ProcessesPerform Continuous Integrator ReviewStrengthen Delivery MechanismsAssure Sustainment Activities and ProcessesManage Disposal and Final Disposition Activities throughout the System or Element Life Cycle

A patch management process should be implemented to check unused dependencies, unmaintained and/or previously vulnerable dependencies, unnecessary features, components, files, and documentation. Continuous monitoring of vulnerability sources and the use of automatic and manual code review tools should also be implemented as well. [13]

# Footnotes

[1] Avast Threat Intelligence Team. (2018, March 8). New investigations into the CCleaner incident point to a possible third stage that had keylogger capacities. Retrieved March 15, 2018.

[2] Windows Defender Research. (2018, March 7). Behavior monitoring combined with machine learning spoils a massive Dofoil coin mining campaign. Retrieved March 20, 2018.

[3] Command Five Pty Ltd. (2011, September). SK Hack by an Advanced Persistent Threat. Retrieved April 6, 2018.

[4] O'Gorman, G., and McDonald, G.. (2012, September 6). The Elderwood Project. Retrieved February 15, 2018.

[5] Trendmicro. (2018, November 29). Hacker Infects Node.js Package to Steal from Bitcoin Wallets. Retrieved April 10, 2019.

[6] Brumaghin, E. et al. (2017, September 18). CCleanup: A Vast Number of Machines at Risk. Retrieved March 9, 2018.

[7] Rosenberg, J. (2017, September 20). Evidence Aurora Operation Still Active: Supply Chain Attack Through CCleaner. Retrieved February 13, 2018.

[8] Chiu, A. (2016, June 27). New Ransomware Variant "Nyetya" Compromises Systems Worldwide. Retrieved March 26, 2019.

[9] US-CERT. (2017, July 1). Alert (TA17-181A): Petya Ransomware. Retrieved March 15, 2019.

[10] Maynor, D., Nikolic, A., Olney, M., and Younan, Y. (2017, July 5). The MeDoc Connection. Retrieved March 26, 2019.

[11] The MITRE Corporation. (2014). MITRE Systems Engineering Guide. Retrieved April 6, 2018.

[12] Boyens, J,. Et al.. (2002, October). Notional Supply Chain Risk Management Practices for Federal Information Systems. Retrieved April 6, 2018.

[13] OWASP. (2017, April 16). OWASP Top 10 2017 - The Ten Most Critical Web Application Security Risks. Retrieved February 12, 2019.

## Defense

Apply supply chain risk management (SCRM) practices and procedures (Citation: MITRE SE Guide 2014), such as supply chain analysis and appropriate risk management, throughout the life-cycle of a system.

Leverage established software development lifecycle 

## Tactics

- [[Initial Access|TA0001 - Initial Access]]

## Related Procedures (2)

- [[MSSQL List Tables]]
- [[MYSQL Injection - Current Queries]]
