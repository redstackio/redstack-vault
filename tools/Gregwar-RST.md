---
url: 'https://github.com/Gregwar/RST'
tags:
  - rst-parser
  - php-library
  - lfi-vulnerable
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.091Z'
id: 242769b6-59be-4d4e-918f-e28982460752
validated: true
submitted: true
---
# Gregwar-RST

**Status**: Unverified

## Overview

Gregwar/RST is a PHP library for parsing reStructuredText (RST) markup into HTML, commonly used in documentation systems like Airship CMS. In security testing, it's analyzed for vulnerabilities such as LFI via its unrestricted include directive.

## Description

The library provides a Parser class that processes RST directives, including 'include' which fetches and embeds external files. Lacking path validation, it enables path traversal attacks to disclose local files. It's integrated via Composer in PHP projects for rendering user-generated docs.

## Features

- Feature 1: Full RST directive support, including include for file embedding
- Feature 2: HTML output generation from RST source
- Feature 3: Extensible parser for custom directives

## Installation

### Requirements

- PHP 5.3+
- Composer

### Install Commands

```bash
composer require gregwar/rst
```

## Basic Usage

```bash
php -r "require 'vendor/autoload.php'; use Gregwar\RST\Parser; echo (new Parser())->parse('Hello *world*');",
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Primarily class-based; no CLI flags

## Examples

### Example 1: Basic Usage

```php
$parser = new Parser();
echo $parser->parse('*Test*');
```

### Example 2: Advanced Usage

```php
$parser = new Parser();
echo $parser->parse('.. include:: file.txt');
```

> Includes and renders file.txt.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor Composer logs for gregwar/rst installation
- Scan for Parser.php includes in web apps
- Detect anomalous file reads during RST parsing

## Related Procedures


## Related Tools

- [[php]]

## References

- Official documentation: https://github.com/Gregwar/RST
- Related resources: RST spec at docutils.sourceforge.net
