---
id: proc-create-express-app
tags:
  - express
  - metascraper-integration
type: procedure
tools:
  - '[[tools/express]]'
  - '[[tools/metascraper]]'
  - '[[tools/got]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Node.js
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.504Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Express-App-with-Metascraper

## Summary

This procedure develops a vulnerable Express.js application that uses metascraper to fetch and extract Open Graph metadata from a target URL, then inserts it unsanitized into an HTML response.

## Description

The app fetches http://127.0.0.1:8080/article.html with got, extracts metadata using metascraper, logs it, and serves HTML at /scrap with raw metadata.publisher. This triggers XSS when accessed. Prerequisites: Installed dependencies from previous step; text editor for app.js.

## Requirements

1. Installed metascraper, got, express
2. Node.js project directory
3. Knowledge of Express routing

## Defense

Defensive measures and detection strategies:

- Escape HTML outputs using libraries like node-esapi
- Apply sanitization (e.g., DOMPurify) to all scraped content before insertion
- Use template engines with auto-escaping like Handlebars

## Objectives

1. Integrate metascraper for scraping
2. Create /scrap endpoint for demonstration
3. Ensure unsanitized insertion for exploit

## Instructions

### Step 1: Write the App.js Script

**Context**: Code the Express server to scrape and serve vulnerable metadata.

No command; create app.js:

```javascript
const express = require('express');
const got = require('got');
const metascraper = require('metascraper')();

const app = express();

app.get('/scrap', async (req, res) => {
  try {
    const { body: html, url } = await got('http://127.0.0.1:8080/article.html');
    const metadata = await metascraper({ html, url });
    console.log(metadata);
    res.send(`<html><body><div>Publisher: ${metadata.publisher}</div></body></html>`);
  } catch (err) {
    res.send('Error');
  }
});

app.listen(8888, () => console.log('Example app listening on port 8888!'));
```

> This fetches, scrapes, and inserts raw publisher (which contains the script tag). Log shows extracted metadata.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/express]]
- [[tools/metascraper]]
- [[tools/got]]

## Tags

- [[tools/express]]
- [[metascraper-integration]]
