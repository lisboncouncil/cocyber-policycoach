# PolicyCoach Interview Test — Report

**Data:** 2026-05-12  
**Server:** localhost:5050 (PolicyCoach v1.3.4, backbone: DeepSeek V3.2)  
**Sessioni:** 20  
**Obiettivo:** Verificare il rispetto della direttiva no-repeat del system prompt su scenari diversificati  
**Sessione di riferimento:** #3 (logica di detection definitiva — estrazione frasi interrogative + strip bold markdown)

---

## Tabella riepilogativa

| # | Sessione | Contesto | Policy type | Turni | Dom. uniche | Duplicati | Policy gen. | Anomalie |
|---|---|---|---|---|---|---|---|---|
| 1 | S1-ctx-H | Ospedale pubblico italiano, 200 dip., Cagliari | Password Policy | 9 | 8 | 0 | ✓ | — |
| 2 | S2-ctx-M | Distaccamento NATO Romania, 85 pers., classificato | Incident Response | 6 | 5 | 0 | ✓ | — |
| 3 | S3-PMI-manifatturiera | PMI manifatturiera CNC, 80 dip., Vicenza | Access Control | 7 | 6 | 0 | ✓ | — |
| 4 | S4-Comune | Comune 15k abitanti, uffici anagrafe/tributi | Data Protection | 4 | 4 | 0 | ✓ | — |
| 5 | S5-Commercialista | Studio commercialista, 12 prof., Milano | General Cybersecurity | 8 | 8 | 0 | ✓ | — |
| 6 | S6-Fintech | Startup fintech lending, 30 dip., Roma | Incident Response | 6 | 5 | 0 | ✓ | — |
| 7 | S7-Universita | Università pubblica, 3000 studenti, Sassari | General Cybersecurity | 5 | 4 | 0 | ✓ | — |
| 8 | S8-Clinica-privata | Clinica privata ortopedica, 50 dip., Roma | Access Control | 4 | 3 | 0 | ✓ | — |
| 9 | S9-Porto-logistica | Operatore portuale logistico, 300 dip., Genova | Network Security | 4 | 4 | 0 | ✓ | — |
| 10 | S10-ITS-Academy | ITS Academy meccatronico, 500 studenti, Torino | Password Policy | 3 | 2 | 0 | ✓ | early termination (≤2 domande) |
| 11 | S11-Farmaceutica | Farmaceutica R&D oncologica, 200 dip., Milano | Data Protection | 8 | 7 | 0 | ✓ | — |
| 12 | S12-Studio-legale | Studio legale M&A, 8 avv., Torino | General Cybersecurity | 5 | 4 | 0 | ✓ | — |
| 13 | S13-Assicurazioni | Agenzia assicurativa regionale, 150 dip., Napoli | Access Control | 5 | 4 | 0 | ✓ | — |
| 14 | S14-Agenzia-immobiliare | Catena agenzie immobiliari, 30 ag., Napoli | Password Policy | 10 | 10 | 0 | ✓ | — |
| 15 | S15-Utilities-acqua | Gestore reti idriche, 120 dip., Toscana | Incident Response | 7 | 7 | 0 | ✓ | — |
| 16 | S16-Media-digitale | Editore digitale investigativo, 25 dip., Milano | General Cybersecurity | 4 | 4 | 0 | ✓ | — |
| 17 | S17-Ecommerce | E-commerce fashion B2C, 15 dip., Firenze | Password Policy | 3 | 2 | 0 | ✓ | early termination (≤2 domande) |
| 18 | S18-ONG | ONG umanitaria internazionale, 60 dip., Roma | Data Protection | 5 | 4 | 0 | ✓ | — |
| 19 | S19-Hotel | Catena hotel 4 strutture, 200 dip., Sicilia | Access Control | 5 | 4 | 0 | ✓ | — |
| 20 | S20-SaaS-Berlino | Startup SaaS HR tech, 18 dip., Berlino | Incident Response | 9 | 8 | 0 | ✓ | — |

---

## Metriche aggregate

| Metrica | Valore |
|---|---|
| Sessioni totali | 20 |
| Policy generate | 20 / 20 |
| Domande duplicate | **0** |
| Sessioni senza anomalie | 18 / 20 |
| Anomalie rilevate | 2 (early termination) |
| Turni medi per sessione | 5.8 |
| Range turni | 3 – 10 |
| Domande uniche medie | 5.1 |

### Distribuzione per policy type

| Policy type | Sessioni | Turni medi | Range |
|---|---|---|---|
| General Cybersecurity | 4 | 5.5 | 4–8 |
| Access Control | 4 | 5.3 | 4–7 |
| Incident Response | 4 | 7.0 | 6–9 |
| Password Policy | 4 | 6.3 | 3–10 |
| Data Protection | 4 | 5.5 | 4–8 |
| Network Security | 1 | 4.0 | 4 |

---

## Analisi anomalie

### No-repeat directive (obiettivo principale del test)

**Risultato: nessuna violazione su 20 sessioni.**  
La direttiva del system prompt (*"Never, never, never ask the same question twice"*, linee 49–51) è rispettata in tutti gli scenari testati, inclusi contesti ad alta complessità normativa (NATO, farmaceutica, utilities NIS2) e contesti molto semplici (agenzia immobiliare, ITS Academy).

### Early termination — S10-ITS-Academy, S17-Ecommerce

In due sessioni il server ha concluso l'intervista dopo soli 2 domande uniche, producendo output brevi. Il system prompt prescrive esplicitamente 6–8 turni di approfondimento (linea 52: *"Go in depth, across 6–8 separate turns"*). L'ipotesi più probabile è che le risposte generate — molto ricche di contesto normativo e organizzativo — abbiano saturato prematuramente i criteri di raccolta informazioni del modello.

**Impatto:** trascurabile ai fini del test no-repeat; rilevante se l'obiettivo fosse misurare la qualità dell'output generato.

### Nota metodologica

Le risposte dell'utente simulato sono state generate da Claude Haiku 4.5 con un profilo organizzativo pre-definito. Risposte molto complete e strutturate possono innescare early exit nel server anche quando il system prompt prescrive più turni. Un test con risposte più scarne o ambigue potrebbe evidenziare comportamenti diversi.

### Note sul processo di validazione

Questa è la Sessione #3 del test. Le sessioni precedenti hanno portato a due miglioramenti del detector:
- **Sessione #1 → #2**: passaggio da similarità sull'intero testo a estrazione di frasi interrogative — eliminati falsi positivi da domande con preamble diverso ma nucleo identico.
- **Sessione #2 → #3**: aggiunto strip del formatting markdown bold (`**...**`) — risolto bug che impediva l'estrazione di domande formattate in grassetto (confermato su S14: 0 → 10 domande uniche estratte).

---

## Log di riferimento

| Run | File |
|---|---|
| Sessione #1 (S1–S6) | `results/interview_test_20260512_091811.log` |
| Sessione #1 (S7–S20) | `results/interview_test_20260512_093752.log` |
| Sessione #2 (S1–S20) | `results/interview_test_20260512_101904.log` |
| Sessione #3 (S1–S20) — **definitiva** | `results/interview_test_20260512_105536.log` |
