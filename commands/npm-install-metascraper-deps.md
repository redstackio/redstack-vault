---
id: cmd-npm-install-metascraper
data: npm install metascraper got express
tags:
  - npm
  - install
type: command
output: Installation logs and confirmation of packages added to node_modules
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.489Z'
verified: false
validated: true
submitted: true
---
# npm-install-metascraper-deps

## Command

```bash
npm install metascraper got express
```

## Description

Installs the metascraper library (vulnerable to XSS), got for HTTP requests, and express for web serving in a Node.js project. Use during setup to prepare the exploitation environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| metascraper | Scraping library for metadata | Yes |
| got | HTTP client | Yes |
| express | Web framework | Yes |

## Examples

### Basic Usage

```bash
npm install metascraper got express
```

### Advanced Usage

```bash
npm install metascraper@latest got express --save
```

## Expected Output

Logs like 'added 50 packages from 30 contributors and audited 100 packages in 5s'. Packages appear in node_modules and package.json.

## Related

- [[Related Procedure: Install-Metascraper-and-Dependencies]]
