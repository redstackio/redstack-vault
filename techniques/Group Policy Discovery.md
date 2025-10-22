---
id: ab1a8a59-1ccc-4cfd-a979-8839a5e53be9
name: Group Policy Discovery
type: technique
mitre_id: T1615
mitre_url: null
created_at: '2023-04-06T00:31:25.647495+00:00'
updated_at: '2023-04-06T00:31:27.793016+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
---

# Group Policy Discovery

**MITRE ID**: T1615

## Description

Adversaries may gather information on Group Policy settings to identify paths for privilege escalation, security measures applied within a domain, and to discover patterns in domain objects that can be manipulated or used to blend in the environment. Group Policy allows for centralized management of user and computer settings in Active Directory (AD). Group policy objects (GPOs) are containers for group policy settings made up of files stored within a predicable network path <code>\<DOMAIN>\SYSVOL\<DOMAIN>\Policies\</code>.(Citation: TechNet Group Policy Basics)(Citation: ADSecurity GPO Persistence 2016)

Adversaries may use commands such as <code>gpresult</code> or various publicly available PowerShell functions, such as <code>Get-DomainGPO</code> and <code>Get-DomainGPOLocalGroup</code>, to gather information on Group Policy settings.(Citation: Microsoft gpresult)(Citation: Github PowerShell Empire) Adversaries may use this information to shape follow-on behaviors, including determining potential attack paths within the target network as well as opportunities to manipulate Group Policy settings (i.e. [Domain Policy Modification](https://attack.mitre.org/techniques/T1484)) for their benefit.

## Tactics

- [[Discovery|TA0007 - Discovery]]
