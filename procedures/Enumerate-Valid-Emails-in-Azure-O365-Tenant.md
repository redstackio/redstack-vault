---
id: e70cde78-e6f7-45a9-b86f-28bf0c31f26a
name: Enumerate-Valid-Emails-in-Azure-O365-Tenant
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:14.829481+00:00'
updated_at: '2023-05-28T04:04:53.093358+00:00'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - '[[techniques/Active Scanning|T1595 - Active Scanning]]'
  - >-
    [[techniques/Search Open Websites/Domains|T1593 - Search Open
    Websites/Domains]]
sub_techniques: []
platforms:
  - Cloud
tags:
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Email]]'
  - '[[tags/Enumerate valid emails]]'
  - '[[tags/Enumeration]]'
  - '[[tags/o365]]'
  - '[[tags/Office 365]]'
commands:
  - '[[commands/run-o365creeper-validate-emails]]'
tools:
  - '[[tools/o365creeper]]'
validated: true
---

# Enumerate Valid Emails in Azure O365 Tenant

## Summary

This procedure uses the o365creeper tool to validate a list of potential email addresses against an Azure Office 365 tenant, identifying which ones are active and valid. It is primarily used in reconnaissance phases to map out user accounts for targeted phishing or further enumeration attacks.

## Description

Email enumeration in Azure O365 involves querying the tenant's Active Directory to check the existence and validity of email addresses without requiring authentication. Attackers typically start with a list of guessed or harvested emails (e.g., from public sources like LinkedIn or company directories) and use tools like o365creeper to send validation requests. The tool leverages methods such as SMTP checks or API probes to determine if an email is associated with the tenant. Valid emails indicate real user accounts, enabling spear-phishing campaigns or social engineering. This technique exploits the lack of strict rate limiting or validation controls in many O365 configurations, though tenants with lockout policies (default 10 attempts, 1-minute lock) can slow down automated scans. The target environment is cloud-based Azure AD, requiring no initial access but potentially triggering alerts if monitored.

## Requirements

1. A text file containing a list of potential email addresses (e.g., emails.txt), one per line, formatted as user@tenant.onmicrosoft.com.
2. The o365creeper tool installed and configured.
3. Python 2.7 environment (as the tool uses legacy Python paths).
4. Network access to the internet for querying O365 endpoints.

## Defense

Defensive measures and detection strategies:

- Implement email validation measures like SPF, DKIM, and DMARC to obscure valid email patterns.
- Enable multi-factor authentication (MFA) on all O365 accounts to prevent credential-based follow-on attacks.
- Regularly monitor Azure Active Directory sign-in logs and audit logs for unusual validation attempts or failed logins.
- Use Azure AD Identity Protection to detect anomalous reconnaissance activity.
- Configure conditional access policies to block suspicious IP ranges or automate lockouts for enumeration patterns.

## Objectives

1. Identify valid email addresses associated with an Azure O365 tenant.
2. Gather information for spear-phishing campaigns targeting real users.
3. Identify potential targets for further attacks, such as credential harvesting.

## Instructions

### Step 1: Prepare the Email List

**Context**: Create or obtain a file with potential email addresses to test against the target tenant. Replace <TENANT NAME> with the actual tenant identifier (e.g., contoso.onmicrosoft.com). This step ensures the input is formatted correctly for the tool.

Use a text editor to compile the list, ensuring one email per line without duplicates.

### Step 2: Run the Validation Using o365creeper

**Context**: Execute the o365creeper script to validate the emails. The tool will check each address and output VALID or INVALID statuses, writing valid ones to a specified output file. Be aware of the O365 lockout policy: after 10 failed attempts, accounts lock for 1 minute, so pace scans if needed.

**Command** ([[commands/run-o365creeper-validate-emails]]):
```bash
C:\Python27\python.exe C:\Tools\o365creeper\o365creeper.py -f C:\Tools\emails.txt -o C:\Tools\validemails.txt
```

> This command runs the Python script with the input file (-f) containing emails and outputs valid ones to validemails.txt (-o). Expected output includes a console log of each email's status, such as:
>
> admin@<TENANT NAME>.onmicrosoft.com   - VALID
> noob@<TENANT NAME>.onmicrosoft.com    - INVALID
> jeff@<TENANT NAME>.onmicrosoft.com    - VALID
> payroll@<TENANT NAME>.onmicrosoft.com - INVALID
>
> Review validemails.txt for the list of confirmed active accounts. If errors occur (e.g., path issues), verify Python and tool installation.
