#!/usr/bin/env python3
"""
Model Context Protocol (MCP) Server for Redstack Vault

Provides structured access to procedures, commands, techniques, and tools
for LLM agents via MCP protocol.

Usage with Claude Desktop:
Add to config.json:
{
  "mcpServers": {
    "redstack": {
      "command": "python3",
      "args": ["/path/to/mcp_server.py"],
      "env": {
        "VAULT_PATH": "/path/to/obsidian-vault/output"
      }
    }
  }
}
"""

import os
import sys
import json
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
import re


@dataclass
class Procedure:
    """Represents a procedure with MITRE mapping."""
    name: str
    tactics: List[str]
    techniques: List[str]
    platforms: List[str]
    verified: bool
    description: str
    commands: List[str]
    file_path: str
    tags: List[str]


@dataclass
class Command:
    """Represents an executable command."""
    name: str
    executor: str
    command: str
    description: str
    platforms: List[str]
    file_path: str


@dataclass
class Technique:
    """Represents a MITRE ATT&CK technique."""
    technique_id: str
    name: str
    tactic: str
    description: str
    procedures: List[str]
    file_path: str


@dataclass
class AttackChain:
    """Represents an attack chain with ordered steps."""
    id: str
    name: str
    description: str
    step_count: int
    procedures: List[str]
    verified: bool
    complexity: str
    execution_time: str
    skill_level: str
    impact_level: str
    tags: List[str]
    file_path: str
    steps: List[Dict]  # Detailed step information


@dataclass
class Tool:
    """Represents a red team tool."""
    id: str
    name: str
    type: str
    description: str
    verified: bool
    file_path: str


@dataclass
class SubTechnique:
    """Represents a MITRE ATT&CK sub-technique."""
    id: str
    mitre_id: str
    name: str
    parent_technique: str
    tactics: List[str]
    description: str
    file_path: str


class RedstackVault:
    """Interface to Redstack TTP vault."""
    
    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        self._procedures: Dict[str, Procedure] = {}
        self._commands: Dict[str, Command] = {}
        self._techniques: Dict[str, Technique] = {}
        self._sub_techniques: Dict[str, SubTechnique] = {}
        self._attack_chains: Dict[str, AttackChain] = {}
        self._tools: Dict[str, Tool] = {}
        self._tools_index: Dict[str, List[str]] = {}  # tool -> command names
        self._load_vault()
    
    def _extract_frontmatter(self, content: str) -> tuple[Optional[Dict], str]:
        """Extract YAML frontmatter."""
        if not content.startswith('---'):
            return None, content
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            return None, content
        
        try:
            frontmatter = yaml.safe_load(parts[1])
            body = parts[2].strip()
            return frontmatter, body
        except:
            return None, content
    
    def _load_procedures(self):
        """Load all procedures from vault."""
        proc_dir = self.vault_path / 'procedures'
        if not proc_dir.exists():
            return
        
        for file_path in proc_dir.rglob('*.md'):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                fm, body = self._extract_frontmatter(content)
                if not fm:
                    continue
                
                # Extract commands from body
                commands = re.findall(r'```(?:bash|powershell|cmd)\n(.*?)\n```', body, re.DOTALL)
                
                proc = Procedure(
                    name=fm.get('name', file_path.stem),
                    tactics=fm.get('tactics', []),
                    techniques=fm.get('techniques', []),
                    platforms=fm.get('platforms', []),
                    verified=fm.get('verified', False),
                    description=fm.get('description', ''),
                    commands=commands,
                    file_path=str(file_path.relative_to(self.vault_path)),
                    tags=fm.get('tags', [])
                )
                
                self._procedures[proc.name] = proc
                
            except Exception as e:
                print(f"Error loading procedure {file_path}: {e}", file=sys.stderr)
    
    def _load_commands(self):
        """Load all commands from vault."""
        cmd_dir = self.vault_path / 'commands'
        if not cmd_dir.exists():
            return
        
        for file_path in cmd_dir.rglob('*.md'):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                fm, body = self._extract_frontmatter(content)
                if not fm:
                    continue
                
                # Extract command from body
                cmd_match = re.search(r'```(?:bash|powershell|cmd)\n(.*?)\n```', body, re.DOTALL)
                command_text = cmd_match.group(1) if cmd_match else ''
                
                cmd = Command(
                    name=fm.get('name', file_path.stem),
                    executor=fm.get('executor', 'bash'),
                    command=command_text,
                    description=fm.get('description', ''),
                    platforms=fm.get('platforms', []),
                    file_path=str(file_path.relative_to(self.vault_path))
                )
                
                self._commands[cmd.name] = cmd
                
            except Exception as e:
                print(f"Error loading command {file_path}: {e}", file=sys.stderr)
    
    def _load_techniques(self):
        """Load MITRE techniques from vault."""
        tech_dir = self.vault_path / 'techniques'
        if not tech_dir.exists():
            return
        
        for file_path in tech_dir.rglob('*.md'):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                fm, body = self._extract_frontmatter(content)
                if not fm:
                    continue
                
                tech = Technique(
                    technique_id=fm.get('mitre_id', ''),  # Use mitre_id from frontmatter
                    name=fm.get('name', file_path.stem),
                    tactic=fm.get('tactic', ''),
                    description=fm.get('description', ''),
                    procedures=fm.get('procedures', []),
                    file_path=str(file_path.relative_to(self.vault_path))
                )
                
                if tech.technique_id:  # Only add if has valid ID
                    self._techniques[tech.technique_id] = tech
                
            except Exception as e:
                print(f"Error loading technique {file_path}: {e}", file=sys.stderr)
    
    def _load_sub_techniques(self):
        """Load MITRE sub-techniques from vault."""
        subtech_dir = self.vault_path / 'sub-techniques'
        if not subtech_dir.exists():
            return
        
        for file_path in subtech_dir.rglob('*.md'):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                fm, body = self._extract_frontmatter(content)
                if not fm:
                    continue
                
                subtech = SubTechnique(
                    id=fm.get('id', ''),
                    mitre_id=fm.get('mitre_id', ''),
                    name=fm.get('name', file_path.stem),
                    parent_technique=fm.get('parent_technique', ''),
                    tactics=fm.get('tactics', []),
                    description=body[:500] if body else '',  # First 500 chars
                    file_path=str(file_path.relative_to(self.vault_path))
                )
                
                self._sub_techniques[subtech.mitre_id] = subtech
                
            except Exception as e:
                print(f"Error loading sub-technique {file_path}: {e}", file=sys.stderr)
    
    def _load_tools(self):
        """Load tools from vault."""
        tools_dir = self.vault_path / 'tools'
        if not tools_dir.exists():
            return
        
        for file_path in tools_dir.rglob('*.md'):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                fm, body = self._extract_frontmatter(content)
                if not fm:
                    continue
                
                tool = Tool(
                    id=fm.get('id', ''),
                    name=fm.get('name', file_path.stem),
                    type=fm.get('type', 'tool'),
                    description=body[:500] if body else '',  # First 500 chars
                    verified=fm.get('verified', False),
                    file_path=str(file_path.relative_to(self.vault_path))
                )
                
                self._tools[tool.name.lower()] = tool
                
            except Exception as e:
                print(f"Error loading tool {file_path}: {e}", file=sys.stderr)
    
    def _load_attack_chains(self):
        """Load attack chains from vault."""
        chain_dir = self.vault_path / 'attack-chains'
        if not chain_dir.exists():
            return
        
        for file_path in chain_dir.rglob('*.md'):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                fm, body = self._extract_frontmatter(content)
                if not fm or fm.get('type') != 'attack_chain':
                    continue
                
                # Parse steps from body
                steps = []
                step_pattern = r'### \*\*\[Step (\d+)\]\*\* (.+?)\n\n(?:.*?)\*\*Procedure:\*\* \[\[(.+?)\]\](?:.*?)\n\n> 📝 \*\*Objective:\*\* (.+?)\n'
                for match in re.finditer(step_pattern, body, re.DOTALL):
                    steps.append({
                        'step_number': int(match.group(1)),
                        'name': match.group(2).strip(),
                        'procedure': match.group(3).strip(),
                        'objective': match.group(4).strip()
                    })
                
                # Extract metadata from body
                complexity = 'Unknown'
                execution_time = 'Unknown'
                skill_level = 'Unknown'
                impact_level = 'Unknown'
                
                if '**Complexity**' in body:
                    complexity_match = re.search(r'\*\*Complexity\*\* \| (.+?) \|', body)
                    if complexity_match:
                        complexity = complexity_match.group(1).strip()
                
                if '**Execution Time**' in body:
                    time_match = re.search(r'\*\*Execution Time\*\* \| (.+?) \|', body)
                    if time_match:
                        execution_time = time_match.group(1).strip()
                
                if '**Skill Level**' in body:
                    skill_match = re.search(r'\*\*Skill Level\*\* \| (.+?) \|', body)
                    if skill_match:
                        skill_level = skill_match.group(1).strip()
                
                if '**Impact Level**' in body:
                    impact_match = re.search(r'\*\*Impact Level\*\* \| (.+?) \|', body)
                    if impact_match:
                        impact_level = impact_match.group(1).strip()
                
                chain = AttackChain(
                    id=fm.get('id', ''),
                    name=fm.get('name', file_path.stem),
                    description=fm.get('description', ''),
                    step_count=fm.get('step_count', len(steps)),
                    procedures=fm.get('procedures', []),
                    verified=fm.get('verified', False),
                    complexity=complexity,
                    execution_time=execution_time,
                    skill_level=skill_level,
                    impact_level=impact_level,
                    tags=fm.get('tags', []),
                    file_path=str(file_path.relative_to(self.vault_path)),
                    steps=steps
                )
                
                self._attack_chains[chain.name] = chain
                
            except Exception as e:
                print(f"Error loading attack chain {file_path}: {e}", file=sys.stderr)
    
    def _build_tools_index(self):
        """Build index of tools to commands."""
        for cmd_name, cmd in self._commands.items():
            # Extract tool names from command name and description
            tools = set()
            
            # Common tools to index
            tool_keywords = [
                'mimikatz', 'rubeus', 'bloodhound', 'sharphound', 'impacket',
                'nmap', 'metasploit', 'msfvenom', 'sqlmap', 'john', 'hashcat',
                'crackmapexec', 'evil-winrm', 'powershell', 'powerview',
                'responder', 'burp', 'nikto', 'gobuster', 'ffuf', 'hydra',
                'medusa', 'ncrack', 'wpscan', 'searchsploit', 'exploit-db',
                'nc', 'netcat', 'curl', 'wget', 'ssh', 'rdp', 'smb', 'ftp',
                'kerberos', 'ldap', 'winrm', 'psexec', 'wmic', 'reg', 'sc'
            ]
            
            text = f"{cmd.name} {cmd.description} {cmd.command}".lower()
            
            for tool in tool_keywords:
                if tool in text:
                    tools.add(tool)
            
            for tool in tools:
                if tool not in self._tools_index:
                    self._tools_index[tool] = []
                self._tools_index[tool].append(cmd_name)
    
    def _load_vault(self):
        """Load all vault data."""
        self._load_procedures()
        self._load_commands()
        self._load_techniques()
        self._load_sub_techniques()
        self._load_tools()
        self._load_attack_chains()
        self._build_tools_index()
    
    # Public API for MCP
    
    def get_procedure(self, name: str) -> Optional[Dict]:
        """Get procedure by name."""
        proc = self._procedures.get(name)
        return asdict(proc) if proc else None
    
    def search_procedures(self, **filters) -> List[Dict]:
        """Search procedures with filters.
        
        Supported filters:
        - tactic: MITRE tactic
        - technique: MITRE technique
        - platform: Target platform
        - verified: Verification status
        - tag: Tag value
        """
        results = []
        
        for proc in self._procedures.values():
            match = True
            
            if 'tactic' in filters and filters['tactic'] not in proc.tactics:
                match = False
            if 'technique' in filters and filters['technique'] not in proc.techniques:
                match = False
            if 'platform' in filters and filters['platform'] not in proc.platforms:
                match = False
            if 'verified' in filters and proc.verified != filters['verified']:
                match = False
            if 'tag' in filters and filters['tag'] not in proc.tags:
                match = False
            
            if match:
                results.append(asdict(proc))
        
        return results
    
    def text_search_procedures(self, query: str, limit: int = 20) -> List[Dict]:
        """Text search procedures across name, description, tags, tactics, techniques.
        
        Args:
            query: Search text (case-insensitive)
            limit: Maximum number of results
        
        Returns:
            List of matching procedures, scored and sorted by relevance
        """
        query_lower = query.lower()
        query_terms = query_lower.split()
        
        def score_procedure(proc):
            """Score procedure relevance."""
            score = 0
            
            # Build searchable text
            name_lower = proc.name.lower()
            desc_lower = proc.description.lower()
            tags_text = ' '.join(proc.tags).lower()
            tactics_text = ' '.join(proc.tactics).lower()
            techniques_text = ' '.join(proc.techniques).lower()
            
            # Exact match in name - highest priority
            if query_lower in name_lower:
                score += 100
            
            # Match in description
            if query_lower in desc_lower:
                score += 50
            
            # Match in tags
            for tag in proc.tags:
                if query_lower in tag.lower():
                    score += 30
            
            # Match in tactics
            if query_lower in tactics_text:
                score += 20
            
            # Match in techniques
            if query_lower in techniques_text:
                score += 20
            
            # Match individual terms
            combined_text = f"{name_lower} {desc_lower} {tags_text} {tactics_text} {techniques_text}"
            for term in query_terms:
                if len(term) >= 2 and term in combined_text:
                    score += 10
            
            return score
        
        # Score all procedures
        scored = [(proc, score_procedure(proc)) for proc in self._procedures.values()]
        
        # Filter out zero scores and sort
        results = [asdict(proc) for proc, score in scored if score > 0]
        results.sort(key=lambda p: score_procedure(self._procedures[p['name']]), reverse=True)
        
        return results[:limit]
    
    def get_command(self, name: str) -> Optional[Dict]:
        """Get command by name."""
        cmd = self._commands.get(name)
        return asdict(cmd) if cmd else None
    
    def search_commands(self, query: str = '', platform: str = '') -> List[Dict]:
        """Search commands by keyword or platform."""
        results = []
        
        for cmd in self._commands.values():
            match = True
            
            if query and query.lower() not in cmd.name.lower() and query.lower() not in cmd.command.lower():
                match = False
            if platform and platform not in cmd.platforms:
                match = False
            
            if match:
                results.append(asdict(cmd))
        
        return results
    
    def get_technique(self, technique_id: str) -> Optional[Dict]:
        """Get MITRE technique by ID."""
        tech = self._techniques.get(technique_id)
        return asdict(tech) if tech else None
    
    def list_tactics(self) -> List[str]:
        """List all MITRE tactics in vault."""
        tactics = set()
        for proc in self._procedures.values():
            tactics.update(proc.tactics)
        return sorted(list(tactics))
    
    def list_platforms(self) -> List[str]:
        """List all supported platforms."""
        platforms = set()
        for proc in self._procedures.values():
            platforms.update(proc.platforms)
        return sorted(list(platforms))
    
    def get_stats(self) -> Dict[str, int]:
        """Get vault statistics."""
        return {
            'procedures': len(self._procedures),
            'commands': len(self._commands),
            'techniques': len(self._techniques),
            'sub_techniques': len(self._sub_techniques),
            'tools': len(self._tools),
            'attack_chains': len(self._attack_chains),
            'verified_procedures': sum(1 for p in self._procedures.values() if p.verified),
            'verified_chains': sum(1 for c in self._attack_chains.values() if c.verified),
            'tactics': len(self.list_tactics()),
            'platforms': len(self.list_platforms())
        }
    
    # NEW: Attack Chain Methods
    
    def get_attack_chain(self, name: str) -> Optional[Dict]:
        """Get attack chain by name."""
        chain = self._attack_chains.get(name)
        return asdict(chain) if chain else None
    
    def get_attack_chain_with_commands(self, name: str) -> Optional[Dict]:
        """Get attack chain with all commands for Kali MCP execution.
        
        Returns attack chain with expanded commands ready for execution.
        Format optimized for Kali Linux MCP integration.
        """
        chain = self._attack_chains.get(name)
        if not chain:
            return None
        
        chain_data = asdict(chain)
        expanded_steps = []
        
        for step in chain.steps:
            proc_name = step['procedure']
            
            # Get procedure and its commands
            proc = self._procedures.get(proc_name)
            if proc:
                step_data = {
                    'step_number': step['step_number'],
                    'name': step['name'],
                    'procedure': proc_name,
                    'objective': step['objective'],
                    'commands': [],
                    'platforms': proc.platforms,
                    'tactics': proc.tactics,
                    'techniques': proc.techniques
                }
                
                # Add all commands from procedure
                for cmd_text in proc.commands:
                    step_data['commands'].append({
                        'command': cmd_text,
                        'executor': self._guess_executor(cmd_text),
                        'description': proc.description
                    })
                
                expanded_steps.append(step_data)
        
        chain_data['expanded_steps'] = expanded_steps
        chain_data['total_commands'] = sum(len(s['commands']) for s in expanded_steps)
        
        return chain_data
    
    def _guess_executor(self, command: str) -> str:
        """Guess command executor from command content."""
        cmd_lower = command.lower()
        
        if any(ps in cmd_lower for ps in ['powershell', 'invoke-', 'get-', 'new-', 'set-', '$', 'iex']):
            return 'powershell'
        elif any(win in cmd_lower for win in ['cmd.exe', 'reg.exe', 'sc.exe', 'net.exe']):
            return 'cmd'
        elif command.startswith('#!/'):
            if 'python' in command:
                return 'python'
            elif 'bash' in command:
                return 'bash'
        
        return 'bash'  # Default to bash for Linux
    
    def search_attack_chains(self, **filters) -> List[Dict]:
        """Search attack chains with filters.
        
        Supported filters:
        - query: Text search in name/description/tags
        - verified: Only verified chains
        - skill_level: Skill level required
        - impact_level: Impact level
        - complexity: Complexity level
        """
        results = []
        
        for chain in self._attack_chains.values():
            match = True
            
            if 'query' in filters:
                query = filters['query'].lower()
                searchable = f"{chain.name} {chain.description} {' '.join(chain.tags)}".lower()
                if query not in searchable:
                    match = False
            
            if 'verified' in filters and chain.verified != filters['verified']:
                match = False
            
            if 'skill_level' in filters and filters['skill_level'].lower() not in chain.skill_level.lower():
                match = False
            
            if 'impact_level' in filters and filters['impact_level'].lower() not in chain.impact_level.lower():
                match = False
            
            if 'complexity' in filters and filters['complexity'].lower() not in chain.complexity.lower():
                match = False
            
            if match:
                results.append(asdict(chain))
        
        return results
    
    def list_attack_chains(self) -> List[str]:
        """List all attack chain names."""
        return sorted(list(self._attack_chains.keys()))
    
    # NEW: Command Discovery Methods
    
    def find_commands_by_tool(self, tool_name: str) -> List[Dict]:
        """Find all commands that use a specific tool.
        
        Args:
            tool_name: Tool name (e.g., 'mimikatz', 'nmap', 'metasploit')
        
        Returns:
            List of commands with full details
        """
        tool_lower = tool_name.lower()
        cmd_names = self._tools_index.get(tool_lower, [])
        
        results = []
        for cmd_name in cmd_names:
            cmd = self._commands.get(cmd_name)
            if cmd:
                results.append(asdict(cmd))
        
        return results
    
    def find_commands_by_capability(self, capability: str, platform: str = '') -> List[Dict]:
        """Find commands by what they can do (semantic search).
        
        Args:
            capability: What you want to do (e.g., 'dump credentials', 'scan ports', 'escalate privileges')
            platform: Optional platform filter
        
        Returns:
            List of matching commands
        """
        capability_lower = capability.lower()
        results = []
        
        for cmd in self._commands.values():
            # Search in name, description, and command text
            searchable = f"{cmd.name} {cmd.description} {cmd.command}".lower()
            
            # Platform filter
            if platform and platform not in cmd.platforms:
                continue
            
            # Capability match
            if capability_lower in searchable:
                results.append(asdict(cmd))
        
        # Sort by relevance (simple: count occurrences)
        results.sort(
            key=lambda x: f"{x['name']} {x['description']} {x['command']}".lower().count(capability_lower),
            reverse=True
        )
        
        return results
    
    def find_attack_chains_by_tool(self, tool_name: str) -> List[Dict]:
        """Find attack chains that use a specific tool.
        
        Args:
            tool_name: Tool name to search for
        
        Returns:
            List of attack chains that use this tool
        """
        tool_lower = tool_name.lower()
        results = []
        
        for chain in self._attack_chains.values():
            # Check if any procedure in the chain uses this tool
            uses_tool = False
            
            for proc_name in chain.procedures:
                # Remove wiki-link markers
                clean_name = proc_name.replace('[[', '').replace(']]', '')
                proc = self._procedures.get(clean_name)
                
                if proc:
                    # Check commands in procedure
                    for cmd_text in proc.commands:
                        if tool_lower in cmd_text.lower():
                            uses_tool = True
                            break
                
                if uses_tool:
                    break
            
            if uses_tool:
                results.append(asdict(chain))
        
        return results
    
    def find_attack_chains_by_capability(self, capability: str) -> List[Dict]:
        """Find attack chains by what they accomplish.
        
        Args:
            capability: What you want to accomplish (e.g., 'domain admin', 'privilege escalation')
        
        Returns:
            List of matching attack chains
        """
        capability_lower = capability.lower()
        results = []
        
        for chain in self._attack_chains.values():
            searchable = f"{chain.name} {chain.description} {' '.join(chain.tags)}".lower()
            
            if capability_lower in searchable:
                results.append(asdict(chain))
        
        return results
    
    def list_available_tools(self) -> List[str]:
        """List all indexed tools."""
        return sorted(list(self._tools_index.keys()))


class MCPServer:
    """MCP Server implementation."""
    
    def __init__(self, vault: RedstackVault):
        self.vault = vault
    
    def handle_request(self, request: Dict) -> Dict:
        """Handle MCP request."""
        method = request.get('method')
        params = request.get('params', {})
        
        try:
            if method == 'get_procedure':
                result = self.vault.get_procedure(params.get('name'))
            elif method == 'search_procedures':
                result = self.vault.search_procedures(**params)
            elif method == 'get_command':
                result = self.vault.get_command(params.get('name'))
            elif method == 'search_commands':
                result = self.vault.search_commands(
                    query=params.get('query', ''),
                    platform=params.get('platform', '')
                )
            elif method == 'get_technique':
                result = self.vault.get_technique(params.get('technique_id'))
            elif method == 'list_tactics':
                result = self.vault.list_tactics()
            elif method == 'list_platforms':
                result = self.vault.list_platforms()
            elif method == 'get_stats':
                result = self.vault.get_stats()
            
            # Attack Chain Methods
            elif method == 'get_attack_chain':
                result = self.vault.get_attack_chain(params.get('name'))
            elif method == 'get_attack_chain_with_commands':
                result = self.vault.get_attack_chain_with_commands(params.get('name'))
            elif method == 'search_attack_chains':
                result = self.vault.search_attack_chains(**params)
            elif method == 'list_attack_chains':
                result = self.vault.list_attack_chains()
            
            # Command Discovery Methods
            elif method == 'find_commands_by_tool':
                result = self.vault.find_commands_by_tool(params.get('tool_name'))
            elif method == 'find_commands_by_capability':
                result = self.vault.find_commands_by_capability(
                    params.get('capability'),
                    params.get('platform', '')
                )
            elif method == 'find_attack_chains_by_tool':
                result = self.vault.find_attack_chains_by_tool(params.get('tool_name'))
            elif method == 'find_attack_chains_by_capability':
                result = self.vault.find_attack_chains_by_capability(params.get('capability'))
            elif method == 'list_available_tools':
                result = self.vault.list_available_tools()
            
            else:
                return {'error': f'Unknown method: {method}'}
            
            return {'result': result}
            
        except Exception as e:
            return {'error': str(e)}
    
    def run(self):
        """Run MCP server (stdio mode)."""
        for line in sys.stdin:
            try:
                request = json.loads(line)
                response = self.handle_request(request)
                print(json.dumps(response), flush=True)
            except Exception as e:
                print(json.dumps({'error': str(e)}), flush=True)


def main():
    vault_path = os.getenv('VAULT_PATH', 'output/')
    
    if not Path(vault_path).exists():
        print(f"Error: Vault path not found: {vault_path}", file=sys.stderr)
        sys.exit(1)
    
    vault = RedstackVault(vault_path)
    server = MCPServer(vault)
    
    # Print available methods to stderr (won't interfere with MCP protocol)
    print("Redstack MCP Server initialized", file=sys.stderr)
    print(f"Vault: {vault_path}", file=sys.stderr)
    print(f"Stats: {vault.get_stats()}", file=sys.stderr)
    print("\n=== CORE METHODS ===", file=sys.stderr)
    print("  - get_procedure(name)", file=sys.stderr)
    print("  - search_procedures(tactic, technique, platform, verified, tag)", file=sys.stderr)
    print("  - get_command(name)", file=sys.stderr)
    print("  - search_commands(query, platform)", file=sys.stderr)
    print("  - get_technique(technique_id)", file=sys.stderr)
    print("  - list_tactics()", file=sys.stderr)
    print("  - list_platforms()", file=sys.stderr)
    print("  - get_stats()", file=sys.stderr)
    print("\n=== ATTACK CHAIN METHODS (NEW) ===", file=sys.stderr)
    print("  - get_attack_chain(name)", file=sys.stderr)
    print("  - get_attack_chain_with_commands(name)  # Kali MCP ready", file=sys.stderr)
    print("  - search_attack_chains(query, verified, skill_level, impact_level, complexity)", file=sys.stderr)
    print("  - list_attack_chains()", file=sys.stderr)
    print("  - find_attack_chains_by_tool(tool_name)", file=sys.stderr)
    print("  - find_attack_chains_by_capability(capability)", file=sys.stderr)
    print("\n=== COMMAND DISCOVERY METHODS (NEW) ===", file=sys.stderr)
    print("  - find_commands_by_tool(tool_name)", file=sys.stderr)
    print("  - find_commands_by_capability(capability, platform)", file=sys.stderr)
    print("  - list_available_tools()", file=sys.stderr)
    print("\nListening for requests...\n", file=sys.stderr)
    
    server.run()


if __name__ == '__main__':
    main()
