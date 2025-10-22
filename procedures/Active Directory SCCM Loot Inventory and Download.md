---
id: 64a3024f-f4ab-457f-83f2-688c74ccac6d
name: Active Directory SCCM Loot Inventory and Download
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.280384+00:00'
updated_at: '2023-04-10T20:36:07.097511+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Data from Local System|T1005 - Data from Local System]]'
- '[[Exfiltration Over Command and Control Channel|T1041 - Exfiltration Over Command
  and Control Channel]]'
- '[[Network Share Discovery|T1135 - Network Share Discovery]]'
tags:
- '[[Active Directory Attacks]]'
- '[[SCCM Shares]]'
commands:
- '[[Download MigApp.xml]]'
- '[[Download MSI extension files]]'
- '[[Download SCCM inventory]]'
---

# Active Directory SCCM Loot Inventory and Download

## Summary

This attack involves exploiting SCCM shares in Active Directory to loot inventory and download sensitive information. SCCM shares are used for software distribution and inventory collection, and can contain sensitive information such as software licenses, system configurations, and user data. Attac

## Description

# Description

This attack involves exploiting SCCM shares in Active Directory to loot inventory and download sensitive information. SCCM shares are used for software distribution and inventory collection, and can contain sensitive information such as software licenses, system configurations, and user data. Attackers can use this information for further attacks or to sell on the black market. To execute this attack, the attacker will first discover SCCM shares within the network. They will then use a tool to download the inventory of the share and exfiltrate the sensitive information. 

From a technical perspective, this attack involves using a tool to access the SCCM share and enumerate the inventory. The attacker will then use a tool to download the inventory and exfiltrate it to a command and control server. 

From a business value perspective, this attack can have severe consequences for an organization. The stolen information can be used for further attacks or sold on the black market. The organization can suffer reputational damage and financial losses. It is important to secure SCCM shares to prevent this type of attack.

## Requirements

1. Access to the network

1. Access to SCCM shares

1. Tool for accessing and downloading SCCM inventory

## Defense

1. Ensure SCCM shares are properly secured with restricted access and strong authentication

1. Monitor network for suspicious activity and access to SCCM shares

1. Encrypt sensitive information stored in SCCM shares

## Objectives

1. Loot inventory from SCCM shares

1. Download sensitive information

1. Exfiltrate data to a command and control server

# Instructions

1. Run the Invoke-CMLootInventory command to generate an inventory of files available for download from SCCM. Then, run the Invoke-CMLootDownload command to download selected files. Use the -SingleFile parameter to download a specific file and the -InventoryFile parameter to download multiple files listed in an inventory file.

**Code**: [[Invoke-CMLootInventory -SCCMHost sccm01.domain.loc]]

> -SCCMHost: Specifies the hostname of the SCCM server.
-Outfile: Specifies the name and path of the output file for the inventory.
-SingleFile: Specifies the path of a single file to download.
-InventoryFile: Specifies the path of the inventory file to download multiple files.
-Extension: Specifies the file extension of the files to download.

**Command** ([[Download SCCM inventory]]):

```bash
Invoke-CMLootInventory -SCCMHost sccm01.domain.local -Outfile sccmfiles.txt
```

**Command** ([[Download MigApp.xml]]):

```bash
Invoke-CMLootDownload -SingleFile \\sccm\SCCMContentLib$\DataLib\SC100001.1\x86\MigApp.xml
```

**Command** ([[Download MSI extension files]]):

```bash
Invoke-CMLootDownload -InventoryFile .\sccmfiles.txt -Extension msi
```

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Discovery|TA0007 - Discovery]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Data from Local System|T1005 - Data from Local System]]
- [[Exfiltration Over Command and Control Channel|T1041 - Exfiltration Over Command and Control Channel]]
- [[Network Share Discovery|T1135 - Network Share Discovery]]

## Commands Used

- [[Download MigApp.xml]]
- [[Download MSI extension files]]
- [[Download SCCM inventory]]

## Tags

- [[Active Directory Attacks]]
- [[SCCM Shares]]
