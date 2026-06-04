#!/usr/bin/env python3
"""V1.0.2 evaluator for China Internet Compliance Skill outputs.

Usage:
  python evaluate_outputs.py --case TC-001 --output path/to/output.md
  python evaluate_outputs.py --output path/to/output.md

This script does not decide legal correctness by itself. It is a lightweight
structure and keyword/term coverage checker, then produces a review score for
human calibration against the rubrics. Similar meanings may still need manual
review when they do not use the expected terms.
"""
import argparse, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / 'evals' / 'expected_issues.json'

BASE_SECTIONS = {
    'facts': ['事实', '已确认', '假设', '缺失'],
    'scenario': ['场景', '主场景', '交叉'],
    'risk': ['风险', 'P0', 'P1', 'P2', 'P3'],
    'basis': ['依据', '核验', '待核验', '法律', '规则'],
    'evidence': ['证据', '材料', '待确认'],
    'remediation': ['整改', '关闭标准', '责任方'],
    'gate': ['Gate', '上线', '灰度', '阻断', '可复制结论'],
}

def load_expected(case_id=None):
    if not EXPECTED.exists():
        return None
    data = json.loads(EXPECTED.read_text(encoding='utf-8'))
    if not case_id:
        return data
    for c in data.get('cases', []):
        if c.get('case_id') == case_id:
            return c
    return None

def score_text(text, case=None):
    score = 0
    details = []
    for key, terms in BASE_SECTIONS.items():
        hit = any(t.lower() in text.lower() for t in terms)
        if hit: score += 8
        details.append((key, hit))
    # 56 base max
    if case and isinstance(case, dict):
        req = case.get('required_terms', [])
        issues = case.get('expected_issues', [])
        terms = list(dict.fromkeys(req + issues))
        if terms:
            hits = [t for t in terms if t.lower() in text.lower()]
            issue_score = round(34 * len(hits) / len(terms))
            score += issue_score
            details.append(('expected_issue_terms', f'{len(hits)}/{len(terms)}'))
        level = case.get('expected_risk_level')
        if level and level in text:
            score += 10
            details.append(('expected_risk_level', True))
        else:
            details.append(('expected_risk_level', False))
    else:
        score += 20
    return min(score, 100), details

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--case', help='Case id such as TC-001')
    ap.add_argument('--output', required=True, help='Markdown output file')
    args = ap.parse_args()
    text = Path(args.output).read_text(encoding='utf-8')
    case = load_expected(args.case) if args.case else None
    score, details = score_text(text, case)
    print(f'Score: {score}/100')
    for k,v in details:
        print(f'- {k}: {v}')
    if args.case and not case:
        print(f'[WARN] Case {args.case} not found in expected_issues.json')
    if score < 80:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
