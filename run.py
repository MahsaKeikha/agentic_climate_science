from orchestration.orchestrator import run

REFERENCE_CONTEXT = {
    "objective": "climate science research review",
    "problem_reviewed": True,
    "data_provenance_reviewed": True,
    "model_assumptions_reviewed": True,
    "scenario_definition_reviewed": True,
    "uncertainty_reviewed": True,
    "attribution_reviewed": True,
    "reproducibility_reviewed": True,
    "human_approval": True,
}

if __name__ == "__main__":
    print(run(REFERENCE_CONTEXT))
