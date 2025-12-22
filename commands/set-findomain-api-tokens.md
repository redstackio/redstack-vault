---
id: 93f1f557-3a11-4044-8cf9-8ab6811b6c75
name: set-findomain-api-tokens
type: command
executor: bash
data: |-
  export findomain_spyse_token="YourSpyseAccessToken"
  export findomain_virustotal_token="YourVirusTotalAccessToken"
  export findomain_fb_token="YourFacebookAccessToken"
output: null
created_at: '2023-04-06T03:56:25.542052+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - configuration
  - api
verified: true
validated: true
---

# set-findomain-api-tokens

## Command

```bash
export findomain_spyse_token="YourSpyseAccessToken"
export findomain_virustotal_token="YourVirusTotalAccessToken"
export findomain_fb_token="YourFacebookAccessToken"
```

## Description

This command sets environment variables for Findomain's API tokens, enabling access to passive intelligence sources like Spyse, VirusTotal, and Facebook CT logs for enhanced subdomain discovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| findomain_spyse_token | Spyse API access token | Optional (for Spyse source) |
| findomain_virustotal_token | VirusTotal API key | Optional (for VT source) |
| findomain_fb_token | Facebook Graph API token | Optional (for CT logs) |

## Examples

### Basic Usage

```bash
export findomain_spyse_token="abc123def456"
export findomain_virustotal_token="ghi789jkl012"
export findomain_fb_token="mno345pqr678"
```

### Persistent in Shell Profile

Add to ~/.bashrc:
```bash
export findomain_spyse_token="YourSpyseAccessToken"
```

## Expected Output

No output. Verify with 'echo $findomain_spyse_token' showing the token value. Tokens persist for the session; unset with 'unset VAR'.

## Related

- [[procedures/Subdomain-Enumeration-with-Findomain]]
- [[commands/run-findomain-enumerate-subdomains]]
