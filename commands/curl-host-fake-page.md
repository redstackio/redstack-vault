---
id: cmd-curl-host-fake-page
data: >-
  echo '<html><body><form method="POST" action="/steal">Username: <input
  name="user"><br>Password: <input type="password" name="pass"><br><input
  type="submit" value="Login"></form></body></html>' > fake.html && python3 -m
  http.server 80 --bind 127.0.0.1
tags:
  - exploit
  - phishing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.945Z'
verified: false
validated: true
submitted: true
---
# Curl Host Fake Page

## Command

```bash
echo '<html><body><form method="POST" action="/steal">Username: <input name="user"><br>Password: <input type="password" name="pass"><br><input type="submit" value="Login"></form></body></html>' > fake.html && python3 -m http.server 80 --bind 127.0.0.1
```

## Description

This command creates a simple HTML phishing page and starts a local HTTP server to host it, simulating impersonation for typosquatting demos.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo ... > fake.html` | Generate fake HTML file | Yes |
| `python3 -m http.server 80` | Start server on port 80 | Yes |
| `--bind 127.0.0.1` | Bind to localhost | No |

## Examples

### Basic Usage

```bash
python3 -m http.server 80
```

### Advanced Usage

```bash
# With custom content
echo 'Custom phishing' > index.html && python3 -m http.server 8080
```

## Expected Output

Server logs: "Serving HTTP on 0.0.0.0 port 80"; access http://localhost/ to see fake form.

## Related

- [[procedures/Demonstrate-Typosquatting-Exploit]]
- [[commands/curl-access-url]]
