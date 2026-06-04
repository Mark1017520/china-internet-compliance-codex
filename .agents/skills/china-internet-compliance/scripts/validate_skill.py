#!/usr/bin/env python3
from pathlib import Path
import json, sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
errors = []

def require(path, desc):
    if not path.exists():
        errors.append(f'Missing {desc}: {path}')
    return path.exists()

def contains(path, needles, desc):
    if not require(path, desc):
        return
    text = path.read_text(encoding='utf-8')
    for n in needles:
        if n not in text:
            errors.append(f'{desc} lacks required phrase: {n}')

# Core files
require(ROOT/'SKILL.md', 'main skill')
require(REPO/'AGENTS.md', 'repo AGENTS.md')

# v4.0/v4.1/v4.2/v4.3 required files
for rel in [
    'references/SPECIALIST_SKILL_DEEPENING_INDEX.md',
    'commands/COMMAND_EXECUTION_STANDARD.md',
    'commands/COMMAND_INPUT_CONTRACTS.json',
    'commands/COMMAND_ROUTING_MATRIX.md',
    'evals/expected_issues.json',
    'evals/EXPECTED_CASE_MATRIX.md',
    'evals/legal_correctness_rubric.md',
    'evals/risk_identification_benchmark.md',
    'references/SOURCE_INDEX.yaml',
]:
    require(ROOT/rel, rel)

# Specialist skills
specialists = [
 'china-product-compliance','china-data-privacy-compliance','china-ai-algorithm-compliance','china-content-governance','china-advertising-marketing','china-platform-transaction','china-game-virtual-assets','china-payment-fintech-adjacent','china-ip-open-source','china-vendor-contract','china-regulatory-response'
]
skills_dir = ROOT.parent
for slug in specialists:
    p = skills_dir/slug/'SKILL.md'
    contains(p, ['必需输入字段','专项判断树','P0/P1 触发条件','证据材料清单','交叉场景路由','质量门槛'], f'specialist {slug}')
    require(skills_dir/slug/'PLAYBOOK.md', f'playbook {slug}')

# Commands
cmd_dir = ROOT/'commands'
cmds = list(cmd_dir.glob('*.md'))
command_files = [p for p in cmds if p.name not in {'COMMAND_EXECUTION_STANDARD.md','COMMAND_ROUTING_MATRIX.md'}]
if len(command_files) < 15:
    errors.append(f'Expected at least 15 command files, found {len(command_files)}')
for p in command_files:
    contains(p, ['命令契约','必需输入','执行流程','缺失材料处理','质量门槛'], f'command {p.name}')

# Test cases and expected issues
text = (ROOT/'prompts/test_cases.md').read_text(encoding='utf-8') if (ROOT/'prompts/test_cases.md').exists() else ''
case_count = sum(1 for line in text.splitlines() if line.strip()[:2].rstrip('.').isdigit() or line.strip().startswith(tuple(str(i)+'.' for i in range(1,10))))
# robust actual count
import re
case_count = len(re.findall(r'^\d+\.\s', text, flags=re.M))
if case_count < 120:
    errors.append(f'Expected >=120 test cases, found {case_count}')

exp_path = ROOT/'evals/expected_issues.json'
if exp_path.exists():
    data = json.loads(exp_path.read_text(encoding='utf-8'))
    if data.get('case_count', 0) < 120 or len(data.get('cases', [])) < 120:
        errors.append('expected_issues.json must contain >=120 cases')

# Golden examples
ge = list((ROOT/'golden_examples').glob('*.md')) if (ROOT/'golden_examples').exists() else []
if len(ge) < 30:
    errors.append(f'Expected >=30 golden examples, found {len(ge)}')

# Command input contracts
cic = ROOT/'commands/COMMAND_INPUT_CONTRACTS.json'
if cic.exists():
    data = json.loads(cic.read_text(encoding='utf-8'))
    if len(data) < 15:
        errors.append('COMMAND_INPUT_CONTRACTS.json must include >=15 commands')

if errors:
    print('[FAIL] validation failed')
    for e in errors:
        print('-', e)
    sys.exit(1)
print('[OK] china-internet-compliance skill package is valid.')
print(f'[OK] Found {case_count} full-scenario test cases.')
print(f'[OK] Found {len(ge)} golden examples.')
print(f'[OK] Found {len(command_files)} executable command files.')
print(f'[OK] Found {len(specialists)} deepened specialist skills.')
print('[OK] v4.1/v4.2/v4.3 staged enhancement files are present.')
