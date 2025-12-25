<div align="center">

# 🔴 Redstack Vault

### *The Offensive Security Knowledge Programmatic Dataset*

**A structured, queryable, AI-ready dataset of 15,125+ real-world attack procedures**

[![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK%20v14-red?style=for-the-badge&logo=minutemailer&logoColor=white)](https://attack.mitre.org/)
[![Obsidian](https://img.shields.io/badge/Obsidian-v1.4+-7C3AED?style=for-the-badge&logo=obsidian&logoColor=white)](https://obsidian.md)
[![MCP Protocol](https://img.shields.io/badge/MCP-Enabled-00A67E?style=for-the-badge&logo=anthropic&logoColor=white)](https://modelcontextprotocol.io/)


[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Markdown](https://img.shields.io/badge/Markdown-33K%20Files-000000?style=flat-square&logo=markdown)]()
[![YAML](https://img.shields.io/badge/YAML-Structured-CB171E?style=flat-square&logo=yaml)]()
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)]()

[🚀 Quick Start](#-quick-start) • [📖 Documentation](#-documentation) • [🎯 Use Cases](#-use-cases) • [🤝 Contributing](#-contributing)

</div>

---

## 🎯 What is Redstack Vault?

Redstack Vault transforms offensive security knowledge into a **living knowledge graph**. Instead of scattered notes, blog posts, and cheat sheets, you get a unified, interconnected dataset where every technique, tool, and procedure is linked, tagged, and mapped to the MITRE ATT&CK framework.

**Think of it as:** *Obsidian vault meets MITRE ATT&CK meets your penetration testing playbook—with AI superpowers.*

### ⚡ Core Value

- **🔗 Graph-Native Architecture**: Every entity (procedures, tools, techniques) is bidirectionally linked through WikiLinks, creating a traversable knowledge graph
- **🤖 AI-First Design**: Built-in MCP server for Claude, RAG-ready structured content, semantic search capabilities
- **📊 MITRE ATT&CK Synchronized**: Complete mapping of 18 tactics, 337 techniques, 380+ sub-techniques with real-world procedures
- **⚡ Execution-Ready**: 15,139 procedures, 8,314 executable commands, 1,062 code snippets, copy-paste ready for engagements
- **🔍 Multi-Dimensional Access**: Query by tactic, technique, platform, tool, or semantic meaning
- **📈 Living Dataset**: Structured YAML frontmatter on every file enables programmatic analysis and extensibility

---

## 🌟 Why Redstack Vault?

### The Problem We Solve

Security professionals face a critical challenge: **knowledge fragmentation**. Attack techniques are scattered across:
- 📝 Personal notes that aren't searchable
- 🌐 Blog posts that disappear or become outdated
- 📚 PDFs and books that aren't queryable
- 💬 Forum threads with incomplete context
- 🧠 Mental models that can't be shared

### Our Solution

**Redstack Vault** provides:

✅ **Centralized Knowledge Graph** — All offensive techniques in one interconnected system  
✅ **Programmatic Access** — Query, filter, and integrate via APIs, MCP, or semantic search  
✅ **Standardized Schema** — Every entry follows consistent YAML + Markdown structure  
✅ **MITRE ATT&CK Native** — Complete framework integration for threat modeling  
✅ **AI-Enhanced Workflow** — RAG, ML training, semantic search, and LLM integration  
✅ **Open Ecosystem** — Extend with your own procedures, integrate with your tools  

---

## 📊 By The Numbers

<div align="center">

| 📁 Category | 📈 Count | 🎯 Purpose |
|------------|----------|------------|
| **Procedures** | 15,139 | Step-by-step attack procedures |
| **Commands** | 8,314 | Executable CLI commands |
| **Attack Chains** | 4,718 | Multi-stage attack sequences |
| **Tags** | 1,909 | Categorical navigation |
| **Tools** | 1,767 | Red team tool documentation |
| **Images** | 1,392 | Screenshots and diagrams |
| **Code Snippets** | 1,062 | Bash, Python, PowerShell scripts |
| **Sub-Techniques** | 380 | Platform-specific variants |
| **Techniques** | 335 | MITRE ATT&CK techniques |
| **Tactics** | 18 | MITRE ATT&CK tactics |

**Total: 33,684+ markdown files with structured data**

</div>

---

## 🎯 Use Cases

### 🔴 Red Team Operations

Plan and execute offensive engagements with confidence:

- **Attack Planning**: Browse by MITRE ATT&CK tactics to design multi-stage operations
- **Tool Discovery**: Find alternative tools when primary options are blocked or detected
- **Technique Research**: Deep-dive into 15,139 documented procedures with real-world context
- **Chain Building**: Leverage pre-built attack chains or create custom sequences
- **Operational Notes**: Copy-paste ready commands and scripts for immediate execution

### 🔍 Penetration Testing

Streamline your testing workflow:

- **Quick Reference**: Access 8,314 commands organized by context
- **Platform-Specific**: Filter by Windows, Linux, macOS, Cloud, Web, or Network targets
- **Execution Ready**: Every command tested and documented with prerequisites
- **Methodology**: Follow structured procedures from reconnaissance to post-exploitation
- **Reporting**: MITRE ATT&CK mappings for professional assessment reports

### 🛡️ Blue Team & Detection Engineering

Understand the adversary to build better defenses:

- **Threat Modeling**: Map attacker TTPs to your environment using MITRE ATT&CK
- **Detection Rules**: Build SIEM/EDR rules based on documented attack procedures
- **Threat Emulation**: Replicate real-world attacks in controlled environments
- **Purple Teaming**: Bridge offensive and defensive teams with shared taxonomy
- **Intelligence Analysis**: Track tool usage, technique evolution, and emerging TTPs

### 🤖 AI/ML & Research Applications

**Retrieval-Augmented Generation (RAG)**
- Pre-structured for vector embeddings and semantic search
- YAML frontmatter enables metadata filtering
- Link graph provides contextual relationships
- 33,000+ training examples for fine-tuning

**Machine Learning Training**
- Malware classification datasets from code snippets
- Command detection model training data
- Attack sequence prediction from chains
- Technique recommendation systems

**Knowledge Graph Analytics**
- Graph database ingestion (Neo4j, Amazon Neptune)
- Technique clustering and pattern analysis
- Tool-to-technique relationship mapping
- Coverage gap identification

**Semantic Search & Chatbots**
- MCP server for Claude Desktop integration
- LangChain/LlamaIndex compatible structure
- Natural language query: *"How do I escalate privileges on Windows without touching disk?"*
- Context-aware responses with source attribution

### 📚 Security Education & Training

- **Capture The Flag (CTF)**: Reference library for techniques and tools
- **Certification Prep**: OSCP, OSEP, PNPT, CEH study material
- **Course Development**: Structured curriculum with hands-on procedures
- **Research**: Academic analysis of offensive techniques and tool capabilities

---

## 🏗️ Architecture & Features

### Graph-Native Knowledge Structure

Every entity in Redstack Vault is a node in a knowledge graph:

```
┌─────────────┐         ┌──────────────┐         ┌─────────────┐
│   TACTICS   │────────▶│  TECHNIQUES  │────────▶│SUB-TECHNIQUES│
│    (18)     │         │    (337)     │         │   (380+)     │
└──────┬──────┘         └──────┬───────┘         └──────┬──────┘
       │                       │                        │
       │    ┌──────────────────┴──────────────┐         │
       │    │                                 │         │
       ▼    ▼                                 ▼         ▼
    ┌──────────────┐                   ┌──────────────┐
    │  PROCEDURES  │◀───────────────────│    TOOLS     │
    │   (15,139)   │                   │   (1,767)    │
    └──────┬───────┘                   └──────┬───────┘
           │                                  │
           ▼                                  ▼
    ┌──────────────┐                   ┌──────────────┐
    │   COMMANDS   │                   │     TAGS     │
    │   (8,314)    │                   │   (1,909)    │
    └──────────────┘                   └──────────────┘
```

### 🎯 MITRE ATT&CK Integration

Complete framework coverage:

| Tactic ID | Name | Coverage | Description |
|-----------|------|----------|-------------|
| TA0043 | Reconnaissance | ✅ Full | Pre-attack intel gathering |
| TA0042 | Resource Development | ✅ Full | Building attack infrastructure |
| TA0001 | Initial Access | ✅ Full | Entry vectors into target systems |
| TA0002 | Execution | ✅ Full | Running malicious code |
| TA0003 | Persistence | ✅ Full | Maintaining foothold |
| TA0004 | Privilege Escalation | ✅ Full | Gaining elevated permissions |
| TA0005 | Defense Evasion | ✅ Full | Avoiding detection |
| TA0006 | Credential Access | ✅ Full | Credential theft techniques |
| TA0007 | Discovery | ✅ Full | Environment reconnaissance |
| TA0008 | Lateral Movement | ✅ Full | Network traversal methods |
| TA0009 | Collection | ✅ Full | Data gathering |
| TA0010 | Exfiltration | ✅ Full | Data extraction |
| TA0011 | Command & Control | ✅ Full | C2 communications |
| TA0040 | Impact | ✅ Full | Destructive actions |

### 🔑 Key Features

**📋 Standardized Schema**
- YAML frontmatter on every file (UUID, timestamps, metadata)
- Consistent Markdown structure across all content types
- Bidirectional WikiLinks for graph traversal
- Platform tags (Windows, Linux, macOS, Cloud, Web, Network)

**🔍 Multi-Dimensional Navigation**
- Browse by MITRE ATT&CK Tactic → Technique → Procedure
- Filter by target Platform (7 categories)
- Search by Tool (1,767 documented)
- Explore by Tag (1,909 categorical)
- Traverse via knowledge graph relationships

**🤖 AI/LLM Integration**
- **MCP Server**: Claude Desktop native integration
- **RAG-Ready**: Structured content for vector embeddings
- **Semantic Search**: Natural language queries via SSE endpoint
- **Dataview Queries**: Dynamic filtering and statistics

**⛓️ Attack Chain System**
- 4,718 pre-built multi-stage attack sequences
- Complexity ratings and skill level requirements
- Execution time estimates
- Complete MITRE ATT&CK technique coverage per chain

---

## 📂 Repository Structure

```bash
redstack-vault/
├── 📁 procedures/          # 15,139 step-by-step attack procedures
│   ├── Kerberoasting.md
│   ├── DCSync Attack.md
│   └── Pass-the-Hash.md
│
├── 💻 commands/            # 8,314 executable CLI commands
│   ├── mimikatz-sekurlsa.md
│   ├── bloodhound-python.md
│   └── crackmapexec-smb.md
│
├── ⛓️ attack-chains/       # 4,718 multi-stage attack sequences
│   ├── Kerberoast to DCSync.md
│   ├── GitHub Token to Cloud Compromise.md
│   └── Web Shell to Domain Admin.md
│
├── 🏷️ tags/                # 1,909 categorical tags
├── 🛠️ tools/               # 1,767 red team tool documentation
│   ├── Metasploit.md
│   ├── BloodHound.md
│   └── Cobalt Strike.md
│
├── 📝 codes/               # 1,062 code snippets (Bash, Python, PowerShell)
│   ├── reverse-shells/
│   ├── enumeration-scripts/
│   └── exploitation/
│
├── 🔹 sub-techniques/      # 380 sub-technique variations
├── 🛡️ techniques/          # 335 MITRE ATT&CK techniques (T1001-T1659)
├── 🎯 tactics/             # 18 MITRE ATT&CK tactics (TA0001-TA0043)
│
├── 🖥️ Platforms/           # Platform-specific browsing
│   ├── Windows.md         # Most comprehensive coverage
│   ├── Linux.md
│   ├── macOS.md
│   ├── Cloud.md           # AWS, Azure, GCP
│   └── Web.md
│
├── 📚 _assets/
│   ├── templates/         # Templater templates for content creation
│   └── images/            # 1,392 screenshots & diagrams
│
├── 🤖 .mcp-server/         # Model Context Protocol server
│   ├── mcp_server.py      # Main MCP server implementation
│   ├── mcp_server_sse.py  # SSE endpoint for semantic search
│   └── start.sh           # Server startup script
│
├── .obsidian/           # Obsidian vault configuration
├── Dashboard.md         # Main navigation dashboard
└── MITRE-Framework.md   # ATT&CK framework overview
```

---

## 🔑 File Schema

Every file follows a standardized YAML + Markdown structure for programmatic access:

```yaml path=null start=null
---
id: 550e8400-e29b-41d4-a716-446655440000      # UUID for unique identification
name: Kerberoasting                            # Human-readable name
type: procedure                                # Entity type
verified: true                                 # Validation status
created_at: 2024-01-15T10:30:00Z              # Creation timestamp
updated_at: 2024-03-22T14:45:00Z              # Last update timestamp

# MITRE ATT&CK Mappings (WikiLinks)
tactics:
  - "[[Credential Access|TA0006 - Credential Access]]"
techniques:
  - "[[Steal or Forge Kerberos Tickets|T1558]]"
sub_techniques:
  - "[[T1558.003 - Kerberoasting]]"

# Categorization
platforms:
  - "[[Windows]]"
tools:
  - "[[Rubeus]]"
  - "[[Impacket]]"
commands:
  - "[[GetUserSPNs.py]]"
tags:
  - "[[Active Directory]]"
  - "[[Credential Theft]]"
---

# Kerberoasting

## Summary
Kerberoasting exploits Kerberos TGS tickets to extract service account credentials...

## Description
[Detailed technical explanation with context]

## Requirements
- Valid domain credentials
- Network access to Domain Controller
- Tools: Rubeus, Impacket, or PowerView

## Instructions
### Step 1: Enumerate SPNs
[Detailed procedure steps...]
```

---

## 🚀 Quick Start

### Prerequisites

- **[Obsidian](https://obsidian.md)** v1.4.0+ (free)
- **Git** for cloning
- **Python 3.10+** (optional, for MCP server)

### Installation

```bash path=null start=null
# Clone the repository
git clone https://github.com/redstackio/redstack-vault.git
cd redstack-vault

# Open in Obsidian
# Option 1: Obsidian → "Open folder as vault" → Select redstack-vault/
# Option 2: CLI (macOS)
open -a Obsidian .

# Option 3: CLI (Linux)
obsidian .
```

### 🎉 First Steps

1. **Open Dashboard.md** - Your central navigation hub
2. **Explore by MITRE ATT&CK** - Browse tactics/techniques/procedures
3. **Search** - Use Cmd/Ctrl+O for quick file search
4. **Graph View** - Cmd/Ctrl+G to visualize connections

### 🔌 Recommended Obsidian Plugins

Install these community plugins for the best experience:

- **Dataview** - Dynamic queries and statistics (essential)
- **Templater** - Content creation templates
- **Omnisearch** - Full-text search
- **Tag Wrangler** - Tag management
- **Excalidraw** - Attack flow diagrams

---

## 🤖 MCP Server (AI Integration)

Redstack Vault includes a **Model Context Protocol (MCP)** server for seamless AI/LLM integration.

### 🔧 Available Tools

| Tool | Description |
|------|-------------|
| `get_attack_chain_with_commands()` | Retrieve complete attack chain with all commands |
| `list_attack_chains()` | Browse available attack chains |
| `search_attack_chains()` | Filter by tool/technique/platform |
| `find_commands_by_tool()` | Find commands for specific tools |
| `find_commands_by_capability()` | Semantic search for capabilities |
| `find_attack_chains_by_tool()` | Chains using a specific tool |
| `list_available_tools()` | Full tool inventory |
| `search_procedures()` | Search by tactic/technique/platform |
| `get_vault_stats()` | Content statistics |

### 🟣 Claude Desktop Integration

1. Install Python dependencies:

```bash path=null start=null
cd .mcp-server
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2. Add to your Claude Desktop config:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json path=null start=null
{
  "mcpServers": {
    "redstack-vault": {
      "command": "python",
      "args": ["/absolute/path/to/redstack-vault/.mcp-server/mcp_server.py"]
    }
  }
}
```

3. Restart Claude Desktop

4. Ask Claude: *"List all Windows privilege escalation procedures"* or *"Show me the DCSync attack chain"*

### 🔍 Other RAG Integrations

**LangChain**
```python path=null start=null
from langchain.document_loaders import ObsidianLoader

loader = ObsidianLoader("/path/to/redstack-vault")
docs = loader.load()
```

**LlamaIndex**
```python path=null start=null
from llama_index import SimpleDirectoryReader

reader = SimpleDirectoryReader("/path/to/redstack-vault")
documents = reader.load_data()
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 📝 Adding New Content

1. **Fork the repository**
2. **Use templates** from `_assets/templates/` for consistency:
   - `procedure.md` - Attack procedures
   - `command.md` - CLI commands
   - `tool.md` - Tool documentation
   - `attack-chain.md` - Multi-stage attacks
   - `technique.md` - MITRE techniques
3. **Follow the schema**:
   - Include YAML frontmatter with UUID
   - Link to relevant tactics/techniques/tools using WikiLinks
   - Add platform tags
   - Include verification status
4. **Submit a Pull Request** with:
   - Clear description of additions
   - MITRE ATT&CK mappings (if applicable)
   - Verification/testing notes

### ✅ Contribution Guidelines

- **Quality over quantity**: Verified procedures preferred
- **Cite sources**: Link to original research/blogs when applicable
- **No illegal content**: Only techniques for authorized testing
- **Maintain consistency**: Follow existing file structure
- **Test before submitting**: Verify procedures work as documented

### 💬 Community

- **Issues**: Bug reports and feature requests
- **Discussions**: Share use cases and integrations
- **Pull Requests**: Code and content contributions welcome

---

## ⚠️ Disclaimer

> **FOR AUTHORIZED SECURITY TESTING ONLY**

This knowledge base contains offensive security techniques and should only be used for:

✅ **Authorized Activities**
- Penetration testing engagements with written authorization
- Red team operations within defined scope
- Security research and academic study
- Capture The Flag (CTF) competitions
- Defensive security and threat modeling
- Personal lab environments you own

❌ **Prohibited Activities**
- Unauthorized access to computer systems (illegal in most jurisdictions)
- Attacking systems without explicit written permission
- Using techniques for malicious purposes
- Violating terms of service or acceptable use policies

### Legal Notice

- **Unauthorized computer access is illegal** under laws including the Computer Fraud and Abuse Act (CFAA) in the US and similar legislation worldwide
- **The authors and contributors are not responsible** for misuse of this information
- **Always follow responsible disclosure** practices when discovering vulnerabilities
- **Obtain proper authorization** before testing any system you do not own

*Use responsibly. Stay legal. Be ethical.*

---

## 📚 Documentation

- **[Dashboard.md](Dashboard.md)** - Main navigation hub
- **[MITRE-Framework.md](MITRE-Framework.md)** - ATT&CK framework overview
- **[Platforms/](Platforms/)** - Platform-specific documentation
- **[.mcp-server/README.md](.mcp-server/README.md)** - MCP server setup guide

---

## 🔗 Related Projects

- **[MITRE ATT&CK](https://attack.mitre.org/)** - The framework that powers our taxonomy
- **[Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)** - Small, portable detection tests
- **[LOLBAS Project](https://lolbas-project.github.io/)** - Living Off The Land Binaries
- **[GTFOBins](https://gtfobins.github.io/)** - Unix binaries for privilege escalation
- **[WADComs](https://wadcoms.github.io/)** - Windows/AD command cheat sheet

---

## ⭐ Star History

If you find Redstack Vault useful, please consider starring the repository!

---

---

<div align="center">

### 🔴 Redstack Vault

**Built with ❤️ by the security community, for the security community**

*"The quieter you become, the more you are able to hear."*

🌐 [Website](https://redstack.io) • 🐦 [Twitter](https://x.com/redstackio)

© 2025 RedStack Labs Corp.

</div>
