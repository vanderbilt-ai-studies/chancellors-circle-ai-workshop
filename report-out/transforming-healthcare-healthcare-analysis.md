# Transforming healthcare: Healthcare analysis

**Table:** Transforming healthcare
**Industry:** Healthcare
**Approach(es):** Research planning (individual draft, not a table exercise)
**Date:** 2026-10-16
**Horizon:** Three to five years

> **Status:** This is a research plan drafted by one person, not the reviewed product of a table discussion. No literature search was run, so it contains no verified sources. Sections 2 and 6 are marked as gaps rather than filled in.

## Summary

This draft outlines a research plan for a Medicare-scale patient digital twin that would link beneficiary claims to genomic data to support predictive diagnosis and preventive care. Its central correction is that genomic data cannot be meaningfully de-identified, because a genome is itself an identifier; the plan therefore substitutes governed access inside a secure enclave for anonymization. It proposes four phases across thirty-six months: data governance and legal review, privacy-preserving linkage to consented genomic cohorts, one disease-specific twin validated prospectively, and a pragmatic trial of the preventive action the twin triggers. No literature survey was run, so every empirical claim here is an unverified hypothesis rather than a finding.

## 1. The change we investigated

Whether a Medicare-scale digital twin integrating claims with genomic data could become predictive of future diagnosis and preventive care within three to five years. Our initial expectation was not recorded, because this was drafted as an individual research plan rather than a table exercise.

## 2. What we found happening already

No evidence was collected. The literature survey was stopped before any search ran, so this report contains no source-backed findings and no citations. This is an evidence gap, not a null result.

## 3. A plausible future and its assumptions

Phase 1 (months 0–6): CMS data use agreement via ResDAC, IRB review, Common Rule and GINA analysis, one cohort and one outcome defined. Phase 2 (6–12): link Medicare Parts A/B/D to consented genomic cohorts using privacy-preserving record linkage, reporting linkage rates by race, ancestry and dual-eligible status. Phase 3 (12–24): build one disease-specific twin rather than an all-patient system, validating retrospectively then prospectively and reporting calibration per subgroup instead of pooled AUC. Phase 4 (24–36): a pragmatic trial of the care action the twin triggers, because prediction is not prevention. This assumes Medicare claims hold no genomic data of their own, which is why linkage to consented cohorts is required, and it assumes HIPAA Expert Determination rather than Safe Harbor. It fails if consent at that scale is unobtainable, or if linkage rates differ so sharply by subgroup that the twin encodes care access rather than disease.

## 4. What people and organizations would still contribute

Consent, governance and enclave administration; clinical judgment about which predictions warrant action; subgroup fairness review. One implication for a new graduate: the scarce skill here is data governance under HIPAA and the Common Rule, not model fitting.

## 5. Our biggest disagreement or uncertainty

The de-identification premise. Re-identification from genotype combined with quasi-identifiers is understood to be a well-established result in the privacy literature, so "de-identify the genomes" is not an achievable control, and re-identification liability survives any de-identification claim. A second uncertainty: polygenic scores are understood to underperform in non-European ancestries, which could make the twin least accurate for the beneficiaries with the least access. Both claims need verification against sources before use.

## 6. What changed in our thinking

Not collected. No table discussion took place, so no before-and-after reflection exists. Marked missing rather than invented.

Report-out: We explored whether a Medicare digital twin could link claims and genomic data to predict and prevent disease. We were surprised by how completely the de-identification premise fails for genomic data. Our biggest uncertainty is whether consented, representative linkage is achievable at Medicare scale.
