---
id: 2ba66783-e947-476c-86d9-ff23b28868b6
name: assetfinder-enumerate-subdomains
type: command
executor: bash
data: assetfinder $_DOMAIN
output: null
created_at: '2020-07-24T17:11:30.473048+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - dns
verified: true
validated: true
---

# assetfinder-enumerate-subdomains

## Command

```bash
assetfinder $_DOMAIN
```

## Description

This command uses the assetfinder tool to passively enumerate subdomains for a specified domain by querying public sources such as certificate transparency logs, search engines, and threat intelligence feeds. It is ideal for initial reconnaissance to map a domain's attack surface without generating detectable traffic to the target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | The target domain name (e.g., owasp.com) to enumerate subdomains for | Yes |

## Examples

### Basic Usage

```bash
assetfinder owasp.com
```

This runs the enumeration and outputs subdomains to the console.

### Advanced Usage

```bash
assetfinder owasp.com > subdomains.txt
```

Redirects output to a file for further processing or piping to other tools like httpx for liveliness checks.

## Expected Output

A list of discovered subdomains, one per line. For example:

```
www.owasp.com
mail.owasp.com
api.owasp.com
blog.owasp.com
```

Success is indicated by a list of subdomains (potentially empty for obscure domains, but typically includes several for well-known ones). No errors should appear if the tool is properly installed and internet access is available.

## Related

- [[procedures/Enumerate-Subdomains-Using-Assetfinder]]
- [[tools/Assetfinder]]
