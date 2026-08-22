"""Fail-closed research-integrity policy for F85 climate science."""

REQUIRED_REVIEWS = (
    "problem_reviewed",
    "data_provenance_reviewed",
    "model_assumptions_reviewed",
    "scenario_definition_reviewed",
    "uncertainty_reviewed",
    "attribution_reviewed",
    "reproducibility_reviewed",
    "human_approval",
)

BLOCKED_ACTIONS = {
    "fabricate_evidence",
    "hide_uncertainty",
    "claim_certain_attribution",
    "claim_policy_mandate",
}


def check(context: dict) -> dict:
    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {
            "allowed": False,
            "human_review_required": True,
            "reason": "missing required climate-science review",
            "missing": missing,
        }

    blockers = []
    if context.get("data_provenance_missing"):
        blockers.append("data provenance incomplete")
    if context.get("model_assumption_invalid"):
        blockers.append("model assumption not justified")
    if context.get("scenario_mismatch"):
        blockers.append("scenario definition incompatible with claim")
    if context.get("uncertainty_not_characterized"):
        blockers.append("material uncertainty not characterized")
    if context.get("attribution_overclaim"):
        blockers.append("attribution claim exceeds evidence")
    if context.get("causal_claim_unsupported"):
        blockers.append("causal claim unsupported")
    if context.get("reproducibility_gap"):
        blockers.append("reproducibility gap unresolved")
    if context.get("contradictory_evidence_unresolved"):
        blockers.append("contradictory evidence unresolved")

    return {
        "allowed": not blockers,
        "human_review_required": True,
        "reason": "review complete" if not blockers else "climate-science governance blocker",
        "blockers": blockers,
        "prohibited": sorted(BLOCKED_ACTIONS),
    }
