---
id: 422611b6-e1c2-4aa0-b77d-cc1f666b8be9
name: >-
  Request-Certificate-on-Behalf-of-User-via-Misconfigured-Enrollment-Agent-Templates
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:05.826186+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Persistence]]'
techniques:
  - '[[Application Access Token]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Active Directory Certificate Services]]'
  - '[[tags/ESC3 - Misconfigured Enrollment Agent Templates]]'
commands:
  - '[[commands/certipy-request-certificate-basic]]'
  - '[[commands/certipy-request-certificate-on-behalf-of-user]]'
platforms:
  - Windows
  - Active Directory
tools:
  - '[[tools/Certipy]]'
validated: true
---

# Request-Certificate-on-Behalf-of-User-via-Misconfigured-Enrollment-Agent-Templates

## Summary

This procedure exploits misconfigured Enrollment Agent Templates in Active Directory Certificate Services (ADCS) to request certificates on behalf of other users, bypassing standard access controls. By leveraging an Enrollment Agent certificate, an attacker can impersonate privileged users, enabling privilege escalation, lateral movement, or persistence without direct authentication.

## Description

In ADCS environments, Enrollment Agent Templates allow authorized users to request certificates for other principals. If misconfigured (e.g., ESC3 vulnerability), low-privileged users can enroll an Enrollment Agent certificate and use it to issue certificates for high-privileged accounts like domain administrators. This technique abuses the certificate enrollment process to obtain authentication material that can be used for further attacks, such as Kerberos authentication or remote access. It targets Windows domains with vulnerable CA configurations and requires domain user credentials for initial access.

## Requirements

1. Domain user credentials with access to the CA.
2. Installed Certipy tool on a Linux or Windows system with network access to the domain.
3. Knowledge of the CA name, template names (e.g., 'ESC3' or 'User'), and domain details.
4. The target CA must have misconfigured Enrollment Agent Templates allowing unauthorized enrollment.

## Defense

- Restrict Enrollment Agent Template permissions to only necessary principals and require approval for requests.
- Monitor ADCS event logs (e.g., Event ID 4886 for certificate enrollments) for anomalous requests, especially on-behalf-of scenarios.
- Implement certificate template auditing and use tools like BloodHound to identify misconfigurations.
- Enforce least privilege on CA roles and regularly review template ACLs.

## Objectives

1. Enroll an Enrollment Agent certificate using a vulnerable template.
2. Use the Enrollment Agent certificate to request a user certificate on behalf of a target account.
3. Obtain a PFX file containing the certificate and private key for impersonation.

## Instructions

### Step 1: Request Basic Enrollment Agent Certificate

**Context**: First, enroll a basic Enrollment Agent certificate using a misconfigured template like 'ESC3' to gain the ability to request certificates for others. This step authenticates with your low-privileged user credentials.

**Command** ([[commands/certipy-request-certificate-basic]]):
```bash
certipy req '$_DOMAIN/$_USERNAME:$_PASSWORD@$_CA_SERVER' -ca '$_CA_NAME' -template '$_TEMPLATE'
```

> This command submits a certificate request to the specified CA using the given template. Replace placeholders with actual values (e.g., domain 'corp.local', username 'john', password 'Passw0rd!', CA server 'ca.corp.local', CA name 'corp-CA', template 'ESC3'). The command generates and saves a PFX file with the certificate and private key.

### Step 2: Request Certificate on Behalf of Target User

**Context**: Using the Enrollment Agent certificate from Step 1, request a certificate for a target user (e.g., a domain admin) via the 'on-behalf-of' option. This impersonates the target without their credentials, exploiting the misconfiguration.

**Command** ([[commands/certipy-request-certificate-on-behalf-of-user]]):
```bash
certipy req '$_DOMAIN/$_USERNAME:$_PASSWORD@$_CA_SERVER' -ca '$_CA_NAME' -template '$_TEMPLATE' -on-behalf-of '$_TARGET_USER' -pfx '$_OUTPUT_FILE.pfx'
```

> Authenticate with the original user credentials and specify the Enrollment Agent PFX from Step 1 implicitly via the tool's session. The '-on-behalf-of' flag targets the privileged user (e.g., 'corp\administrator'). Upon success, a new PFX file is saved for the target user, which can be used for authentication (e.g., with Rubeus or PassTheCert).
