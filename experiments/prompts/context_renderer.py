#!/usr/bin/env python3
"""Render an organisation context (YAML) as a structured "interview output"
profile usable as the {context_narrative} placeholder.

The output is intentionally formatted as elicited fields under thematic
headers (not free narrative), so a system prompt that defaults to interview
behaviour can detect that all expected information has already been
collected and switch to rapid-policy mode.
"""

from __future__ import annotations
import sys
from pathlib import Path
import yaml


def _bullet(items, prefix: str = "- ") -> str:
    return "\n".join(f"{prefix}{i}" for i in (items or []) if i)


def render_hospital(ctx: dict) -> str:
    org = ctx["organisation"]
    it = ctx["it_posture"]
    res = ctx["resources"]
    reg = ctx["regulatory"]
    threats = ctx["threats_top"]
    cstr = ctx["constraints"]
    sys_list = ", ".join(it["clinical_systems"])

    return f"""### Organisation type and governance
- **Type**: small public hospital (province-level, generalist)
- **Country**: Italy
- **Governance**: {org['governance']}
- **Operating hours**: clinical services 24/7
- **Wards / units**: {", ".join(org['wards'])}

### Size and staffing
- **Total staff**: {org['staff_total']}
  - clinical: {org['staff_breakdown']['clinical']}
  - administrative: {org['staff_breakdown']['administrative']}
  - technical/facility: {org['staff_breakdown']['technical_facility']}
- **Beds**: {org['beds']}
- **Workstations**: {it['endpoint_estate']['workstations']} (of which {it['endpoint_estate']['legacy_windows']} are legacy Windows on clinical kiosks)
- **Mobile devices**: {it['endpoint_estate']['mobile']} (point-of-care)

### IT and security posture
- **CISO**: not in place
- **Internal IT staff**: {it['it_staff_internal_fte']} FTE
- **Outsourcing**: {it['msp_outsourced']} (managed services contract with external MSP)
- **Identity**: {it['identity']}
- **Network**: {it['network']['perimeter']}; segmentation: {it['network']['segmentation']}
- **Clinical systems**: {sys_list}
- **Backups**: {it['backups']}
- **Detection**: {it['detection']}
- **Incident response**: {it['incident_response']}

### Resource envelope
- **Cybersecurity budget**: {res['cybersecurity_budget_eur_year']:,} EUR/year ({res['cybersecurity_budget_band']})
- **Training**: {res['training_hours_per_staff_year']} hours/staff/year
- **External consulting**: {res['external_consulting_eur_year']:,} EUR/year

### Regulatory regime
- **Applicable frameworks**:
{_bullet(reg['applicable_frameworks'])}
- **Recommended (not yet certified)**:
{_bullet(reg['recommended_frameworks'])}
- **Data categories processed**: {", ".join(reg['data_categories'])}

### Threat profile (top threats)
{_bullet(threats)}

### Operational constraints
- **Business continuity**: {cstr['business_continuity']}
- **Patient safety priority**: {cstr['patient_safety_priority']}
- **Procurement**: {cstr['procurement']}
- **Clinical staff turnover**: {cstr['staff_turnover_clinical']}
- **Working language**: Italian (policy itself in English)
"""


def render_military(ctx: dict) -> str:
    org = ctx["organisation"]
    it = ctx["it_posture"]
    res = ctx["resources"]
    reg = ctx["regulatory"]
    threats = ctx["threats_top"]
    cstr = ctx["constraints"]
    domains_block = "\n".join(
        f"  - {d['name']}: classification {d['classification']}, use: {d['use']}"
        for d in it["network_domains"]
    )

    return f"""### Organisation type and governance
- **Type**: medium multinational military detachment
- **Command authority**: {org['command_authority']}
- **Host nation**: {org['host_nation']}
- **Framework nation**: {org['framework_nation']}
- **Mission set**:
{_bullet(org['mission'], prefix='  - ')}

### Size and staffing
- **Total personnel**: {org['personnel_total']}
  - military active: {org['personnel_breakdown']['military_active']}
  - civilian NATO staff: {org['personnel_breakdown']['civilian_NATO_staff']}
  - cleared contractors: {org['personnel_breakdown']['contractors']}
- **Workstations classified**: {it['endpoint_estate']['workstations_classified']}
- **Workstations unclassified**: {it['endpoint_estate']['workstations_unclass']}

### IT and security posture
- **Information security lead**: {it['ciso_equivalent']}
- **Security staff (FTE)**: {it['security_staff_fte']}
- **Network domains**:
{domains_block}
- **Cross-domain solutions**: {it['cross_domain_solutions']}
- **COMSEC**: {it['comsec']}
- **Identity**: {it['identity']}
- **TEMPEST zoning**: {it['endpoint_estate']['tempest_zoned_areas']}
- **Detection**: {it['detection']}
- **Incident response**: {it['incident_response']}
- **Supply chain**: {it['supply_chain']}

### Resource envelope
- **Cybersecurity budget**: {res['cybersecurity_budget_band']}
- **Training**: {res['training_hours_per_staff_year']} hours/staff/year
- **Exercises per year**: {res['exercises_per_year']}
- **Red-team engagements per year**: {res['red_team_engagements_per_year']}

### Regulatory regime
- **NATO frameworks**:
{_bullet(reg['applicable_frameworks_nato'], prefix='  - ')}
- **Host-nation frameworks**:
{_bullet(reg['applicable_frameworks_host_nation'], prefix='  - ')}
- **Coalition frameworks**:
{_bullet(reg['applicable_frameworks_coalition'], prefix='  - ')}
- **Civilian-overlay references**:
{_bullet(reg['recommended_frameworks_civilian_overlay'], prefix='  - ')}
- **Classification regimes**:
{_bullet(reg['classification_regimes'], prefix='  - ')}

### Threat profile (top threats)
{_bullet(threats)}

### Operational constraints
- **Classification handling**: {cstr['classification_handling']}
- **Need-to-know**: {cstr['need_to_know']}
- **Dual-key procedures**: {cstr['dual_key_procedures']}
- **COMSEC chain of custody**: {cstr['chain_of_custody_comsec']}
- **Host-nation sovereignty**: {cstr['host_nation_sovereignty']}
- **Working language**: English
"""


RENDERERS = {
    "ctx-H": render_hospital,
    "ctx-M": render_military,
}


def render(yaml_path: Path) -> str:
    ctx = yaml.safe_load(Path(yaml_path).read_text())
    fn = RENDERERS.get(ctx["id"])
    if not fn:
        raise SystemExit(f"No renderer for context id {ctx['id']!r}")
    return fn(ctx)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <context.yaml>", file=sys.stderr)
        sys.exit(2)
    print(render(Path(sys.argv[1])))
