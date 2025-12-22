---
id: cmd-uuid-1
data: npm init -y && npm install react react-dom react-marked-markdown@1.4.6 marked
tags:
  - install
  - npm
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:07.842Z'
verified: false
validated: true
submitted: true
---
---

# npm-install-react-marked-markdown

## Command

```bash
npm init -y && npm install react react-dom react-marked-markdown@1.4.6 marked
```

## Description

Initializes a new npm project and installs the vulnerable react-marked-markdown module along with React dependencies for testing the XSS vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `init -y` | Automatically creates package.json without prompts | Yes |
| `install` | Installs specified packages | Yes |
| `react-marked-markdown@1.4.6` | Pins to vulnerable version | Yes |

## Examples

### Basic Usage

```bash
npm init -y && npm install react react-dom react-marked-markdown@1.4.6 marked
```

### Advanced Usage

```bash
npm install react-marked-markdown@1.4.6 --save-dev
```

## Expected Output

Terminal output showing "added 5 packages in X seconds" and creation of node_modules directory.

## Related

- [[Related Procedure: Setup-React-App-for-Vulnerability-Testing]]

