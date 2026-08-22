from orchestration.orchestrator import run


def base():
    return {
        "problem_reviewed": True,
        "data_provenance_reviewed": True,
        "model_assumptions_reviewed": True,
        "scenario_definition_reviewed": True,
        "uncertainty_reviewed": True,
        "attribution_reviewed": True,
        "reproducibility_reviewed": True,
        "human_approval": True,
    }


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "human_approval": False}, False),
    ({**base(), "data_provenance_missing": True}, False),
    ({**base(), "model_assumption_invalid": True}, False),
    ({**base(), "scenario_mismatch": True}, False),
    ({**base(), "uncertainty_not_characterized": True}, False),
    ({**base(), "attribution_overclaim": True}, False),
    ({**base(), "causal_claim_unsupported": True}, False),
    ({**base(), "reproducibility_gap": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += run(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
