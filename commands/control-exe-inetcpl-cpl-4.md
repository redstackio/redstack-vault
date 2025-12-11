---
data: 'control.exe inetcpl.cpl,,4'
tags:
  - windows
  - proxy
type: command
executor: bash
platforms:
  - Windows
id: fb2c4e9e-ad64-440b-8a24-02bf02070bab
created_at: '2025-12-11T03:47:56.468Z'
updated_at: '2025-12-11T03:47:56.468Z'
verified: false
validated: true
submitted: true
---
# control-exe-inetcpl-cpl-4

## Command

```bash
control.exe inetcpl.cpl,,4
```

## Description

Opens the Windows Internet Properties dialog to the Connections tab for configuring proxy settings, used to set up Burp Suite proxy.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `inetcpl.cpl,,4` | Opens the specific tab for LAN settings | Yes |

## Examples

### Basic Usage

```bash
control.exe inetcpl.cpl,,4
```

## Expected Output

Internet Properties window opens to Connections tab.

## Related

- [[procedures/Proxy-Application-Traffic-for-Inspection]]
- [[tools/Burp-Suite]]
