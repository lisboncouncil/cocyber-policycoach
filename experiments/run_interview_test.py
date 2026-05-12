#!/usr/bin/env python3
"""PolicyCoach interview test — 6 sessions, duplicate question detection.

Per ogni sessione:
- invia "hello" come primo messaggio
- risponde alle domande del server usando Claude Haiku come answer generator
- rileva domande duplicate (similarità >= 0.75)
- su duplicato: ripete la stessa risposta, logga [DUPLICATE]
- su tripla ripetizione: logga [ERROR] e interrompe la sessione
- termina quando il server produce una policy (output lungo / con headers)

Output: results/interview_test_YYYYMMDD_HHMMSS.log
"""
from __future__ import annotations
import json
import uuid
import time
import re
import difflib
import requests
import anthropic
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
SERVER = "http://localhost:5050"
SIMILARITY_THRESHOLD = 0.75
MAX_SAME_QUESTION = 3       # stop on 3rd occurrence (tripla ripetizione)
MAX_TURNS = 25              # safety cap per sessione
POLICY_LEN_THRESHOLD = 800  # chars — sopra questo è policy, non domanda
ANSWER_MODEL = "claude-haiku-4-5-20251001"

ROOT = Path(__file__).resolve().parent
RESULTS_DIR = ROOT / "results"
SECRETS = Path("/Users/erreclaudea/erre-claudia/secrets")
ANTHROPIC_KEY = (SECRETS / "anthropic_api_key_clodia_5").read_text().strip()

# ---------------------------------------------------------------------------
# Session profiles
# ---------------------------------------------------------------------------
SESSIONS = [
    {
        "id": "S1-ctx-H",
        "policy_type": "Password Policy",
        "context_desc": "Ospedale pubblico italiano ~200 dipendenti, Cagliari",
        "profile": {
            "organisation": "Ospedale Regionale di Cagliari",
            "sector": "sanità pubblica",
            "country": "Italia",
            "employees": 200,
            "revenues_eur": "budget pubblico ~12M€/anno",
            "it_maturity": "media — sistemi EHR legacy (Dedalus), rete piatta, AD on-prem",
            "regulations": "GDPR, NIS2, normativa sanitaria italiana (d.lgs 196/2003 aggiornato)",
            "governance": "Direttore Sanitario, CIO, RSPP, nessun CISO dedicato",
            "current_policy": "nessuna password policy formale, linee guida informali",
            "cloud": "nessun cloud, solo on-premise",
            "special_notes": "dati sanitari sensibili (art. 9 GDPR), accesso da reparti 24/7",
        },
    },
    {
        "id": "S2-ctx-M",
        "policy_type": "Incident Response Policy",
        "context_desc": "Distaccamento NATO in Romania, classificato",
        "profile": {
            "organisation": "NATO Forward Presence Detachment — Romania",
            "sector": "difesa / militare",
            "country": "Romania (base multinazionale NATO)",
            "employees": 85,
            "it_maturity": "alta — rete classificata separata da internet, COMSEC officer",
            "regulations": "NATO Information Security Policy (C-M(2002)49), GDPR per dati personali non classificati",
            "governance": "Commanding Officer, COMSEC Officer, J6 (IT Officer)",
            "current_policy": "procedure NATO standard esistenti, necessità di policy IR locale adattata",
            "cloud": "nessun cloud pubblico, sistemi NATO SECRET e NATO RESTRICTED",
            "special_notes": "gestione incidenti su rete classificata, procedure escalation a NATO HQ",
        },
    },
    {
        "id": "S3-PMI-manifatturiera",
        "policy_type": "Access Control Policy",
        "context_desc": "PMI manifatturiera veneta 80 dipendenti, ISO 27001 in progress",
        "profile": {
            "organisation": "Metalmeccanica Bortolotti Srl",
            "sector": "manifattura — lavorazione metalli CNC",
            "country": "Italia (Vicenza)",
            "employees": 80,
            "revenues_eur": "~8M€/anno",
            "it_maturity": "bassa-media — ERP SAP Business One, workstation Windows 11, NAS Synology",
            "regulations": "GDPR (dati dipendenti/clienti), normativa sulla sicurezza sul lavoro",
            "governance": "Titolare/AD, Responsabile IT part-time esternalizzato, nessun DPO interno",
            "current_policy": "nessuna access control policy formale, account condivisi in produzione",
            "cloud": "Microsoft 365 Business per email e Office, resto on-premise",
            "iso27001_status": "gap analysis completata, certificazione prevista entro 12 mesi",
            "special_notes": "accesso remoto tecnici manutentori CNC (VPN), OT/IT separati fisicamente",
        },
    },
    {
        "id": "S4-Comune",
        "policy_type": "Data Protection Policy",
        "context_desc": "Comune italiano 15.000 abitanti, uffici anagrafe e tributi",
        "profile": {
            "organisation": "Comune di San Vito al Tagliamento",
            "sector": "pubblica amministrazione locale",
            "country": "Italia (Friuli-Venezia Giulia)",
            "employees": 42,
            "budget_it": "~80.000€/anno",
            "it_maturity": "bassa — sistemi applicativi in SaaS (Maggioli, TeamSystem), PC Windows 10",
            "regulations": "GDPR, Codice Privacy italiano, Linee Guida AGID, CAD",
            "governance": "Sindaco, Segretario Comunale, Responsabile Informatico (geometra con funzioni IT), RPD esterno",
            "current_policy": "registro dei trattamenti esistente, nessuna DPP formale",
            "cloud": "SaaS applicativi comunali (Maggioli Cloud), email PEC su Aruba",
            "special_notes": "trattamento dati anagrafici, tributari, assistenziali; accesso da sportello fisico e remoto",
        },
    },
    {
        "id": "S5-Commercialista",
        "policy_type": "General Cybersecurity Policy",
        "context_desc": "Studio commercialista 12 professionisti, dati fiscali clienti",
        "profile": {
            "organisation": "Studio Tributario Associato Ferretti & Partners",
            "sector": "servizi professionali — consulenza fiscale e tributaria",
            "country": "Italia (Milano)",
            "employees": 12,
            "revenues_eur": "~1.2M€/anno",
            "it_maturity": "media — gestionale Zucchetti, firma digitale, fatturazione elettronica SDI",
            "regulations": "GDPR (dati fiscali clienti persone fisiche e giuridiche), normativa antiriciclaggio (d.lgs 231/2007)",
            "governance": "Partner responsabile, nessun IT dedicato, consulente esterno occasionale",
            "current_policy": "solo policy privacy per clienti, nessuna cybersecurity policy",
            "cloud": "Microsoft 365, Dropbox Business per condivisione documenti con clienti",
            "special_notes": "dati reddituali, patrimoniali e societari di ~450 clienti; accesso remoto soci da casa",
        },
    },
    {
        "id": "S6-Fintech",
        "policy_type": "Incident Response Policy",
        "context_desc": "Startup fintech 30 dipendenti, operazioni cloud AWS EU",
        "profile": {
            "organisation": "Credix SRL — piattaforma lending B2B",
            "sector": "fintech — credito alle imprese (invoice financing)",
            "country": "Italia (Roma), operazioni EU",
            "employees": 30,
            "revenues_eur": "~2M€/anno ARR, funding Series A 4M€",
            "it_maturity": "alta — cloud-native AWS eu-west-1, microservizi, DevOps maturo",
            "regulations": "GDPR, PSD2, normativa Banca d'Italia per operatori finanziari, DORA (in preparazione)",
            "governance": "CTO, Head of Security (part-time), DPO esterno",
            "current_policy": "runbook tecnici per outage, nessuna IR policy formale per incidenti di sicurezza",
            "cloud": "AWS (ECS, RDS Aurora, S3, CloudTrail), Datadog per monitoring",
            "special_notes": "dati finanziari PMI clienti, SLA 99.9% uptime, notifica incidenti Banca d'Italia obbligatoria entro 4h",
        },
    },
    # ---- nuovi 14 scenari ----
    {
        "id": "S7-Universita",
        "policy_type": "General Cybersecurity Policy",
        "context_desc": "Università italiana 3000 studenti, ricerca e didattica",
        "profile": {
            "organisation": "Università degli Studi di Sassari",
            "sector": "istruzione superiore e ricerca pubblica",
            "country": "Italia (Sardegna)",
            "students": 3000,
            "employees": 450,
            "revenues_eur": "budget MIUR ~35M€/anno",
            "it_maturity": "media — rete campus fisico, VPN studenti, HPC cluster per ricerca, Google Workspace",
            "regulations": "GDPR, normativa PA (CAD, AGID), accordi H2020/Horizon Europa su gestione dati ricerca",
            "governance": "Rettore, Direttore Generale, CIO, RPD designato, nessun CISO dedicato",
            "current_policy": "policy d'uso accettabile (AUP) obsoleta, nessuna cybersecurity policy strutturata",
            "cloud": "Google Workspace per email istituzionale, OneDrive per ricercatori, server on-campus",
            "special_notes": "utenti molto eterogenei (studenti, docenti, ricercatori), frequente BYOD, progetto NIS2 compliance in corso",
        },
    },
    {
        "id": "S8-Clinica-privata",
        "policy_type": "Access Control Policy",
        "context_desc": "Clinica privata specialistica ortopedica, 50 dipendenti, Roma",
        "profile": {
            "organisation": "Clinica Ortopedica Villa Aurelia Srl",
            "sector": "sanità privata — clinica specialistica",
            "country": "Italia (Roma)",
            "employees": 50,
            "revenues_eur": "~4.5M€/anno",
            "it_maturity": "bassa — software gestionale Athena, cartelle cliniche elettroniche parziali, PC non aggiornati",
            "regulations": "GDPR (dati sanitari art. 9), normativa regionale Lazio, accreditamento SSN",
            "governance": "Direttore Sanitario, Amministratore, nessun responsabile IT interno",
            "current_policy": "nessuna access control policy, account condivisi tra infermieri per turno",
            "cloud": "nessun cloud, NAS locale per backup immagini radiologiche (DICOM)",
            "special_notes": "immagini RX/RM in formato DICOM, accesso medici da studio privato esterno via TeamViewer, dati pazienti minori",
        },
    },
    {
        "id": "S9-Porto-logistica",
        "policy_type": "Network Security Policy",
        "context_desc": "Operatore logistico portuale, Genova, 300 dipendenti",
        "profile": {
            "organisation": "Genovaport Logistics SpA",
            "sector": "logistica e trasporto merci — terminal portuale",
            "country": "Italia (Genova)",
            "employees": 300,
            "revenues_eur": "~28M€/anno",
            "it_maturity": "media — TOS (Terminal Operating System) proprietario, OT su gru e sistemi di movimentazione, rete IT/OT parzialmente convergente",
            "regulations": "GDPR, NIS2 (operatore infrastruttura critica), Codice della Navigazione, normativa doganale ADM",
            "governance": "CEO, IT Manager, nessun CISO, accordi con autorità portuale",
            "current_policy": "segmentazione IT/OT documentata parzialmente, nessuna network security policy formale",
            "cloud": "SAP S/4HANA in cloud Azure EU per ERP, TOS on-premise, sistemi OT isolati",
            "special_notes": "infrastruttura critica NIS2, rischio cyberattacchi su sistemi di movimentazione container, accessi operatori portuali terzi",
        },
    },
    {
        "id": "S10-ITS-Academy",
        "policy_type": "Password Policy",
        "context_desc": "ITS Academy (istituto tecnico superiore), 500 studenti, Torino",
        "profile": {
            "organisation": "ITS Academy Meccatronico Piemonte",
            "sector": "istruzione tecnica superiore (ITS)",
            "country": "Italia (Torino)",
            "students": 500,
            "employees": 40,
            "it_maturity": "bassa-media — laboratori CAD/CAM, Microsoft 365 Education, Moodle LMS",
            "regulations": "GDPR (dati minori di età per alcuni corsi), normativa MIUR per ITS, accordi aziendali per tirocini",
            "governance": "Direttore, Referente IT (docente con incarico aggiuntivo), nessun DPO interno",
            "current_policy": "nessuna password policy, account studenti con password default, admin condiviso tra docenti",
            "cloud": "Microsoft 365 Education, Teams per didattica, SharePoint per materiali",
            "special_notes": "account studenti creati da aziende partner per tirocinio, dati minori in alcuni corsi, accesso laboratori 6:00-22:00",
        },
    },
    {
        "id": "S11-Farmaceutica",
        "policy_type": "Data Protection Policy",
        "context_desc": "Azienda farmaceutica R&D, 200 dipendenti, Milano, dati clinici",
        "profile": {
            "organisation": "BioNovaMed Srl",
            "sector": "farmaceutica — ricerca e sviluppo farmaci oncologici",
            "country": "Italia (Milano), collaborazioni EU e USA",
            "employees": 200,
            "revenues_eur": "~18M€/anno + grant ricerca",
            "it_maturity": "alta — sistemi LIMS (Laboratory Information Management System), ELN (Electronic Lab Notebook), pipeline bioinformatica",
            "regulations": "GDPR (dati sperimentazioni cliniche), FDA 21 CFR Part 11 (per trial clinici con partner USA), GCP (Good Clinical Practice), EMA",
            "governance": "CEO, CTO, Data Protection Officer, Quality Assurance Manager, IT Security Lead",
            "current_policy": "DPP parziale per sperimentazioni cliniche, non copre dati genomici e biobank",
            "cloud": "AWS us-east-1 per bioinformatica (non EU — da regolarizzare), Azure EU per Office e collaborazione",
            "special_notes": "dati genomici di pazienti in sperimentazioni cliniche, accordi di trasferimento dati con CRO USA, audit EMA ogni 2 anni",
        },
    },
    {
        "id": "S12-Studio-legale",
        "policy_type": "General Cybersecurity Policy",
        "context_desc": "Studio legale 8 avvocati, Torino, clientela corporate",
        "profile": {
            "organisation": "Studio Legale Associato Martinelli Riva & Partners",
            "sector": "servizi legali — diritto societario e M&A",
            "country": "Italia (Torino)",
            "employees": 8,
            "revenues_eur": "~900k€/anno",
            "it_maturity": "bassa — Microsoft 365, NAS per archivio atti, DocuSign per firme",
            "regulations": "GDPR (dati clienti e fascicoli processuali), normativa antiriciclaggio avvocati (d.lgs 231/2007), segreto professionale forense",
            "governance": "Socio fondatore responsabile, nessun IT interno, supporto esterno saltuario",
            "current_policy": "nessuna policy formale, procedure di riservatezza solo in forma contrattuale con clienti",
            "cloud": "Microsoft 365 Business Premium, iManage Work per gestione documenti (cloud)",
            "special_notes": "dati M&A estremamente sensibili (offerte, due diligence pre-closing), accesso da casa soci senza MFA, target frequente di spear phishing",
        },
    },
    {
        "id": "S13-Assicurazioni",
        "policy_type": "Access Control Policy",
        "context_desc": "Agenzia assicurativa regionale, 150 dipendenti, Napoli",
        "profile": {
            "organisation": "Sud Italia Assicurazioni SpA — Agenzia Campania",
            "sector": "assicurazioni — ramo danni e vita",
            "country": "Italia (Napoli e provincia)",
            "employees": 150,
            "revenues_eur": "~22M€ premi raccolti/anno",
            "it_maturity": "media — gestionale ANIA-compliant, portale agenti web, CRM Salesforce",
            "regulations": "GDPR, IVASS (normativa vigilanza assicurativa), Solvency II, DORA (in preparazione)",
            "governance": "Direttore Generale, Responsabile Compliance, IT Manager, nessun CISO",
            "current_policy": "access control gestito da policy IVASS generica, non aggiornata alle best practice",
            "cloud": "Salesforce CRM, gestionale on-premise datacenter co-located Napoli",
            "special_notes": "rete di 45 agenti esterni con accesso CRM da dispositivi personali, dati polizze e sinistri (art. 9 GDPR per dati salute), audit IVASS annuale",
        },
    },
    {
        "id": "S14-Agenzia-immobiliare",
        "policy_type": "Password Policy",
        "context_desc": "Catena agenzie immobiliari 30 agenti, Napoli-Caserta",
        "profile": {
            "organisation": "Gruppo Vesuvio Immobiliare — rete 4 agenzie",
            "sector": "servizi immobiliari — compravendita e locazione",
            "country": "Italia (Napoli, Caserta)",
            "employees": 30,
            "revenues_eur": "~1.8M€/anno provvigioni",
            "it_maturity": "molto bassa — CRM Immobiliare.it, WhatsApp per comunicazioni interne, email personali miste a professionali",
            "regulations": "GDPR (dati acquirenti/locatari), normativa antiriciclaggio agenti immobiliari",
            "governance": "Titolare, nessuna figura IT, gestione informatica fai-da-te",
            "current_policy": "nessuna, password comunicate via WhatsApp, account condivisi",
            "cloud": "Google Workspace gratuito, Immobiliare.it CRM SaaS",
            "special_notes": "trattamento dati anagrafici e reddituali per antiriciclaggio, foto e documenti clienti su Google Drive non strutturato, recente violazione account email",
        },
    },
    {
        "id": "S15-Utilities-acqua",
        "policy_type": "Incident Response Policy",
        "context_desc": "Gestore reti idriche municipale, 120 dipendenti, Toscana",
        "profile": {
            "organisation": "Acque Toscane SpA — gestore servizio idrico integrato",
            "sector": "utilities — distribuzione acqua potabile e fognatura",
            "country": "Italia (Toscana, 8 comuni serviti)",
            "employees": 120,
            "revenues_eur": "~14M€/anno tariffa regolata ARERA",
            "it_maturity": "media — SCADA per telemetria impianti, GIS per rete idrica, ERP SAP",
            "regulations": "GDPR, NIS2 (infrastruttura critica — settore acqua), ARERA, autorizzazione AIA ambientale",
            "governance": "Direttore Generale, Responsabile Tecnico, IT Coordinator, nessun CISO",
            "current_policy": "piano emergenza operativo per guasti, nessuna IR policy per incidenti cyber",
            "cloud": "nessun cloud, SCADA on-premise, VPN per accesso remoto tecnici campo",
            "special_notes": "sistemi SCADA collegati a Internet per telemetria (rischio elevato), obbligo notifica incidenti NIS2 entro 24h, recenti attacchi ransomware a utilities idriche europee",
        },
    },
    {
        "id": "S16-Media-digitale",
        "policy_type": "General Cybersecurity Policy",
        "context_desc": "Editore digitale indipendente, 25 dipendenti, Milano",
        "profile": {
            "organisation": "Nexus Media Srl — testata giornalistica digitale",
            "sector": "media digitale — giornalismo investigativo e tecnologia",
            "country": "Italia (Milano)",
            "employees": 25,
            "revenues_eur": "~1.4M€/anno (abbonamenti + advertising)",
            "it_maturity": "media — WordPress VIP, Slack, Google Workspace, CMS proprietario",
            "regulations": "GDPR (dati abbonati e fonti confidenziali), normativa editoria digitale, protezione delle fonti (art. 200 c.p.p.)",
            "governance": "Direttore Editoriale, CTO, nessun responsabile security dedicato",
            "current_policy": "nessuna formale, linee guida informali per protezione fonti",
            "cloud": "Google Workspace, WordPress VIP (cloud), AWS S3 per archivio multimediale",
            "special_notes": "protezione fonti giornalistiche confidenziali (rischio intercettazione), target di hacking sponsorizzato da stati per inchieste politiche, redattori in smartworking da paesi esteri",
        },
    },
    {
        "id": "S17-Ecommerce",
        "policy_type": "Password Policy",
        "context_desc": "E-commerce abbigliamento online, 15 dipendenti, PMI",
        "profile": {
            "organisation": "ModaViva Srl — e-commerce fashion B2C",
            "sector": "commercio al dettaglio — abbigliamento e accessori online",
            "country": "Italia (Firenze), vendite EU",
            "employees": 15,
            "revenues_eur": "~2.8M€/anno (200k ordini/anno)",
            "it_maturity": "media — Shopify Plus, Stripe pagamenti, Klaviyo email marketing, Warehouse Management System",
            "regulations": "GDPR (dati acquirenti EU), PCI-DSS livello 3 (via Stripe), normativa consumer rights EU",
            "governance": "Fondatore/CEO, Operations Manager, IT gestito da agenzia esterna",
            "current_policy": "nessuna password policy, MFA attivo su Shopify admin ma non su altri sistemi",
            "cloud": "Shopify Plus SaaS, Google Workspace, Slack, warehouse integration via API",
            "special_notes": "dati carta di credito gestiti via Stripe (out of scope PCI), ma dati personali 80k clienti EU in Klaviyo, accesso supplier estero (Bangladesh) al WMS",
        },
    },
    {
        "id": "S18-ONG",
        "policy_type": "Data Protection Policy",
        "context_desc": "ONG internazionale umanitaria, ufficio IT Roma, 60 dipendenti",
        "profile": {
            "organisation": "MedAid International — organizzazione umanitaria medica",
            "sector": "ONG — assistenza medica in zone di conflitto",
            "country": "Italia (sede legale Roma), operazioni Africa e Medioriente",
            "employees": 60,
            "volunteers_field": 200,
            "revenues_eur": "~8M€/anno (donazioni e grants EU)",
            "it_maturity": "media-bassa — Salesforce CRM per donatori, sistemi medici sul campo non connessi, comunicazioni sicure con Signal/ProtonMail",
            "regulations": "GDPR (dati donatori EU), normative locali paesi di operazione, principi umanitari MSF (Do No Harm per dati beneficiari)",
            "governance": "Direttore, Responsabile IT, DPO esterno, nessun CISO",
            "current_policy": "privacy policy donatori presente, nessuna data protection policy per dati beneficiari sul campo",
            "cloud": "Salesforce EU, Google Workspace nonprofit, ProtonMail per comunicazioni sensibili",
            "special_notes": "dati beneficiari vulnerabili (rifugiati, pazienti in zone di guerra) — violazione può mettere a rischio vite umane, target di APT per intelligence su movimenti migratori",
        },
    },
    {
        "id": "S19-Hotel",
        "policy_type": "Access Control Policy",
        "context_desc": "Piccola catena hotel 4 strutture, 200 dipendenti, Sicilia",
        "profile": {
            "organisation": "Etna Hospitality Group Srl — 4 hotel 3-4 stelle",
            "sector": "ospitalità — hotellerie e turismo",
            "country": "Italia (Catania, Siracusa, Taormina, Palermo)",
            "employees": 200,
            "revenues_eur": "~9M€/anno",
            "it_maturity": "bassa — PMS (Property Management System) Protel, WiFi guest aperta, terminali POS per pagamenti",
            "regulations": "GDPR (dati ospiti), PCI-DSS per pagamenti con carta, normativa turismo regionale",
            "governance": "General Manager, IT Coordinator part-time, nessun responsabile security",
            "current_policy": "nessuna access control policy, account admin PMS condiviso tra 4 strutture",
            "cloud": "Protel PMS on-premise in ogni struttura, booking.com e Expedia API, Google Workspace",
            "special_notes": "account admin PMS unico per tutte le strutture (rischio critico), WiFi ospiti su stessa rete del PMS, accesso remoto fornitori manutenzione PMS non controllato",
        },
    },
    {
        "id": "S20-SaaS-Berlino",
        "policy_type": "Incident Response Policy",
        "context_desc": "Startup SaaS B2B HR tech, 18 dipendenti, Berlino",
        "profile": {
            "organisation": "PeopleSync GmbH — piattaforma HR analytics SaaS",
            "sector": "HR tech — analytics e people management per PMI",
            "country": "Germania (Berlino), clienti EU",
            "employees": 18,
            "revenues_eur": "~800k€ ARR, seed round 1.5M€",
            "it_maturity": "alta — cloud-native GCP europe-west3 (Frankfurt), CI/CD GitHub Actions, monitoraggio Grafana",
            "regulations": "GDPR (dati dipendenti clienti — categoria sensibile), BDSG (Bundesdatenschutzgesetz tedesco), BAG per accordi lavorativi",
            "governance": "CEO/CTO (stessa persona), part-time Security Engineer, DPO esterno",
            "current_policy": "runbook tecnici Confluence, nessuna IR policy formale, nessun playbook per data breach",
            "cloud": "GCP europe-west3, GitHub, Datadog, Intercom per customer support",
            "special_notes": "tratta dati HR di ~15k dipendenti di clienti EU (dati salario, performance, assenteismo), obbligo GDPR notifica breach entro 72h, due clienti enterprise con SLA 99.95%",
        },
    },
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def extract_questions(text: str) -> list[str]:
    """Extract interrogative sentences from a server message.

    Strips HTML comments, markdown bold formatting, and parenthetical examples,
    then splits on sentence boundaries and returns only sentences ending with '?'.
    """
    clean = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    clean = re.sub(r'\*\*([^*]+)\*\*', r'\1', clean)  # strip **bold** markdown
    clean = re.sub(r'\([^)]*\?[^)]*\)', '', clean)    # remove (parenthetical questions)
    # Split on sentence-ending punctuation followed by whitespace/newline
    sentences = re.split(r'(?<=[.?!])\s+', clean.strip())
    return [s.strip() for s in sentences if s.strip().endswith('?')]


def question_similarity(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, a.lower().strip(), b.lower().strip()).ratio()


def find_duplicate(new_msg: str, asked_questions: list[str]) -> str | None:
    """Compare the interrogative sentences of new_msg against all previously
    asked interrogative sentences.  Returns the matching previous question
    sentence if a duplicate is found, otherwise None.
    """
    new_qs = extract_questions(new_msg)
    if not new_qs:
        return None
    for prev_q in asked_questions:
        for nq in new_qs:
            if question_similarity(nq, prev_q) >= SIMILARITY_THRESHOLD:
                return prev_q
    return None


def is_policy_output(text: str) -> bool:
    """Heuristic: policy docs are long and/or contain markdown headers."""
    has_header = any(line.startswith(("# ", "## ", "### ")) for line in text.splitlines())
    return len(text) >= POLICY_LEN_THRESHOLD or has_header


def generate_answer(question: str, profile: dict, client: anthropic.Anthropic) -> str:
    context_str = "\n".join(f"  {k}: {v}" for k, v in profile.items())
    resp = client.messages.create(
        model=ANSWER_MODEL,
        max_tokens=200,
        messages=[{
            "role": "user",
            "content": (
                "You are being interviewed by a cybersecurity consultant to generate a "
                "cybersecurity policy document for your organisation.\n\n"
                f"Your organisation profile:\n{context_str}\n\n"
                f"Interviewer's question: {question}\n\n"
                "Answer briefly and naturally (1-3 sentences). Be specific to your "
                "organisation. Do not add preamble or meta-commentary."
            ),
        }],
    )
    return resp.content[0].text.strip()


def chat(message: str, session_id: str) -> dict:
    resp = requests.post(
        f"{SERVER}/conversation",
        json={"message": message, "sessionId": session_id},
        timeout=180,
    )
    resp.raise_for_status()
    return resp.json()


# ---------------------------------------------------------------------------
# Single session runner
# ---------------------------------------------------------------------------

def run_session(session: dict, log_lines: list[str], client: anthropic.Anthropic) -> bool:
    sid = str(uuid.uuid4())
    ts = lambda: datetime.now().strftime("%H:%M:%S")

    def log(msg: str, tag: str = ""):
        tag_str = f"[{tag}]" if tag else ""
        line = f"[{ts()}]{tag_str} {msg}"
        log_lines.append(line)
        print(line)

    log("=" * 70, "")
    log(f"SESSION {session['id']} | Policy: {session['policy_type']}", "SESSION")
    log(f"Context: {session['context_desc']}", "CTX")
    log(f"sessionId: {sid}", "SID")
    log("=" * 70, "")

    asked_questions: list[str] = []
    question_occurrences: dict[str, int] = {}   # canonical_q -> count
    prev_answers: dict[str, str] = {}            # canonical_q -> answer given
    policy_generated = False
    current_message = "hello"

    for turn in range(1, MAX_TURNS + 1):
        log(f"[TURN {turn}][USER] {current_message}", "SEND")

        try:
            data = chat(current_message, sid)
        except Exception as exc:
            log(f"Request error: {exc}", "ERROR")
            break

        server_text: str = data.get("answer", "").strip()
        display = server_text[:800] + ("…" if len(server_text) > 800 else "")
        log(f"[TURN {turn}][SERVER] {display}", "RECV")

        if is_policy_output(server_text):
            log(f"Policy generated — {len(server_text)} chars.", "DONE")
            policy_generated = True
            break

        # --- duplicate detection ---
        canonical = find_duplicate(server_text, asked_questions)

        if canonical is not None:
            count = question_occurrences.get(canonical, 1) + 1
            question_occurrences[canonical] = count
            sim = question_similarity(server_text[-120:], canonical)
            log(
                f"DUPLICATE QUESTION (occurrence #{count}, sim={sim:.2f}): "
                f"'{canonical[:80]}' re-asked as: '{server_text[:80]}'",
                "DUPLICATE",
            )
            if count >= MAX_SAME_QUESTION:
                log(
                    f"TRIPLE REPETITION — stopping session. "
                    f"Original Q: {canonical[:100]}",
                    "ERROR",
                )
                break
            # repeat same answer
            current_message = prev_answers.get(canonical, "I already answered that.")
            log(f"[REPEATED ANSWER] {current_message[:80]}", "INFO")
        else:
            # Register all interrogative sentences from this message
            new_qs = extract_questions(server_text)
            for nq in new_qs:
                asked_questions.append(nq)
                question_occurrences[nq] = 1
            prev_answers[server_text] = None  # placeholder until answer generated
            answer = generate_answer(server_text, session["profile"], client)
            for nq in new_qs:
                prev_answers[nq] = answer
            current_message = answer

        time.sleep(0.5)

    else:
        log(f"MAX_TURNS ({MAX_TURNS}) reached without policy generation.", "WARN")

    log(
        f"SESSION END | turns={turn} | unique_questions={len(asked_questions)} | "
        f"duplicates={sum(1 for v in question_occurrences.values() if v > 1)} | "
        f"policy_generated={policy_generated}",
        "SUMMARY",
    )
    return policy_generated


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--execute", action="store_true")
    ap.add_argument("--sessions", nargs="*", help="Session IDs to run (default: all)")
    args = ap.parse_args()

    sessions_to_run = SESSIONS
    if args.sessions:
        sessions_to_run = [s for s in SESSIONS if s["id"] in args.sessions]

    print(f"Sessions: {[s['id'] for s in sessions_to_run]}  "
          f"[{'EXECUTE' if args.execute else 'dry-run'}]")

    if not args.execute:
        for s in sessions_to_run:
            print(f"  [DRY] {s['id']} — {s['policy_type']} — {s['context_desc']}")
        return 0

    client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    log_path = RESULTS_DIR / f"interview_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    all_lines: list[str] = [
        f"PolicyCoach Interview Test — {datetime.now().isoformat()}",
        f"Server: {SERVER}",
        f"Similarity threshold: {SIMILARITY_THRESHOLD}",
        f"Max turns/session: {MAX_TURNS}",
        "",
    ]

    results = []
    for session in sessions_to_run:
        session_lines: list[str] = []
        ok = run_session(session, session_lines, client)
        all_lines.extend(session_lines)
        all_lines.append("")
        results.append({"id": session["id"], "policy_generated": ok})
        time.sleep(1)

    all_lines.append("=" * 70)
    all_lines.append("FINAL SUMMARY")
    for r in results:
        status = "OK" if r["policy_generated"] else "FAIL/INCOMPLETE"
        all_lines.append(f"  {r['id']}: {status}")

    log_path.write_text("\n".join(all_lines))
    print(f"\nLog written to {log_path}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
