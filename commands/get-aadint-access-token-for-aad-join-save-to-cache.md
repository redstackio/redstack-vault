---
id: 39f92cd3-a23d-4aed-98a0-daf37257282a
name: get-aadint-access-token-for-aad-join-save-to-cache
type: command
executor: powershell
data: Get-AADIntAccessTokenForAADJoin -SaveToCache
output: null
created_at: '2023-04-06T03:56:15.982472+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - azure
  - aad
  - token
verified: true
validated: true
---

# get-aadint-access-token-for-aad-join-save-to-cache

## Command

```powershell
Get-AADIntAccessTokenForAADJoin -SaveToCache
```

## Description

This command retrieves an OAuth access token for Azure AD device join operations using the AADInternals module and saves it to the module's internal cache for reuse in subsequent commands.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -SaveToCache | Stores the token in cache for session persistence | Yes |

## Examples

### Basic Usage

```powershell
Get-AADIntAccessTokenForAADJoin -SaveToCache
```

## Expected Output

Token acquired and saved to cache. Output may include:
```
AccessToken : eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik...
TokenType : Bearer
ExpiresOn : 2023-10-01T12:00:00Z
```

## Related

- [[procedures/Bypass-Azure-Conditional-Access-via-Fake-Device-Join]]
- [[tools/AADInternals]]
