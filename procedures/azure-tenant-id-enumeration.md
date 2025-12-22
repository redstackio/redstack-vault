---
id: 24504543-c4ab-4c7c-9579-ce03e4dbce58
name: Azure Tenant ID Enumeration
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.066249+00:00'
updated_at: '2023-05-23T17:03:22.734578+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques: []
platforms:
  - Cloud
tags:
  - '[[tags/Active Directory Federation Services]]'
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Enumerate manually]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Tenant ID]]'
commands:
  - '[[commands/curl-azure-get-user-realm-info]]'
  - '[[commands/curl-azure-get-tenant-realm-info]]'
  - '[[commands/powershell-get-azuread-tenant-detail]]'
  - '[[commands/curl-azure-openid-config]]'
tools: []
validated: true
---

# Azure Tenant ID Enumeration

## Summary

This procedure outlines the manual enumeration of an Azure Active Directory (Azure AD) or Office 365 (O365) tenant ID and federation settings using publicly accessible endpoints. It allows attackers or security testers to identify the tenant structure, federation status with external identity providers, and key identifiers without authenticated access, aiding in reconnaissance for targeted attacks.

## Description

Azure Tenant ID Enumeration involves querying Microsoft login endpoints to retrieve details about an Azure AD/O365 environment, such as the unique Tenant ID and whether the tenant is federated (e.g., with Active Directory Federation Services). This technique is useful in the discovery phase of an attack to map the target's cloud identity infrastructure, reveal users, groups, and potential weak points like misconfigured federation. The process uses simple HTTP requests to endpoints like getuserrealm.srf and OpenID configuration, which do not require authentication but rely on known domain or email information. Success provides foundational intelligence for further actions like phishing or privilege escalation planning. From a defensive standpoint, it highlights the need to monitor for anomalous queries to these endpoints.

## Requirements

1. A known email address or domain associated with the target Azure AD/O365 tenant (e.g., user@target.com).
2. A suspected tenant name (e.g., target.onmicrosoft.com), often derived from public sources like domain registration.
3. Network access to the internet and ability to make HTTPS requests (no special privileges needed).
4. Tools like curl or PowerShell for executing requests (curl is cross-platform; PowerShell requires AzureAD module for one variant).

## Defense

- Implement multi-factor authentication (MFA) for all Azure AD/O365 users to limit impact from discovered credentials.
- Monitor Azure AD sign-in logs and Microsoft Entra ID audit logs for suspicious queries to login endpoints or unusual federation checks.
- Use Azure AD Identity Protection to detect and alert on reconnaissance activities, including anomalous IP-based access to discovery endpoints.
- Regularly review and secure federation settings, ensuring only trusted identity providers are configured and disabling unnecessary federation if not required.

## Objectives

1. Identify the Tenant ID and federation status for the target Azure AD/O365 environment.
2. Gather preliminary information on the tenant's structure, including potential users and groups.
3. Enable planning for more targeted attacks, such as credential harvesting or lateral movement within the cloud environment.

## Instructions

### Step 1: Check User Realm and Federation Status

**Context**: Begin by validating if the tenant exists and is federated using a known user email. This step queries the getuserrealm endpoint to retrieve XML data indicating the authentication method (e.g., federated vs. managed) and realm details. If federated, it reveals the identity provider URL.

**Command** ([[commands/curl-azure-get-user-realm-info]]):
```bash
curl "https://login.microsoftonline.com/getuserrealm.srf?login=<USER>@<DOMAIN>&xml=1"
```

> Replace <USER> with a known username (e.g., admin) and <DOMAIN> with the target domain (e.g., target.com). This returns XML with NameIDPolicy, federation metadata, and auth URL. If the tenant is federated, look for <FederationMetadata> elements; otherwise, it indicates a managed (cloud-only) tenant.

### Step 2: Check Tenant Realm and Federation Status

**Context**: Use the suspected tenant's onmicrosoft.com domain to confirm overall tenant federation without a specific user. This complements Step 1 and helps verify the tenant name if uncertain.

**Command** ([[commands/curl-azure-get-tenant-realm-info]]):
```bash
curl "https://login.microsoftonline.com/getuserrealm.srf?login=root@<TENANT-NAME>.onmicrosoft.com&xml=1"
```

> Replace <TENANT-NAME> with the suspected tenant name (e.g., target). Expected output is similar XML to Step 1, confirming federation status at the tenant level. Success is indicated by a valid <UserRealm> response without errors like 'tenant not found'.

### Step 3: Retrieve Tenant ID via PowerShell

**Context**: If the AzureAD PowerShell module is available (common in Windows environments with Azure tools), use it to directly fetch tenant details including the Tenant ID. This requires the module but no authentication for basic details in some contexts; otherwise, fall back to HTTP methods.

**Command** ([[commands/powershell-get-azuread-tenant-detail]]):
```powershell
Get-AzureADTenantDetail
```

> Run in PowerShell after importing the AzureAD module (Install-Module AzureAD if needed). This outputs tenant properties like ObjectId (Tenant ID), DisplayName, and VerifiedDomains. If unauthenticated, it may prompt for login; use generic creds if testing.

### Step 4: Retrieve Tenant ID via OpenID Configuration

**Context**: As an alternative or confirmatory step, query the OpenID Connect discovery endpoint using curl. This works without PowerShell and directly exposes the Tenant ID in the issuer URL.

**Command** ([[commands/curl-azure-openid-config]]):
```bash
curl "https://login.microsoftonline.com/<DOMAIN>/.well-known/openid-configuration"
OR
curl "https://login.microsoftonline.com/<TENANT-NAME>.onmicrosoft.com/.well-known/openid-configuration"
```

> Replace <DOMAIN> or <TENANT-NAME> as appropriate. The JSON response includes 'issuer' with the full Tenant ID (e.g., https://sts.windows.net/{tenant-id}/). Parse the JSON for 'token_endpoint' or 'issuer' to extract the GUID-formatted Tenant ID.
