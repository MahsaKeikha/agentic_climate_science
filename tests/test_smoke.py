from orchestration.orchestrator import run


def valid_context():
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


def test_pipeline_requires_human_review_and_has_no_autonomous_authority():
    result = run(valid_context())
    assert result["system"] == "F85"
    assert result["human_review_required"] is True
    assert result["autonomous_scientific_authority"] is False
    assert result["autonomous_policy_authority"] is False


def test_complete_review_can_release_analysis():
    assert run(valid_context())["release_allowed"] is True


def test_missing_human_approval_fails_closed():
    context = valid_context()
    context["human_approval"] = False
    assert run(context)["release_allowed"] is False


def test_missing_data_provenance_blocks_release():
    context = valid_context()
    context["data_provenance_missing"] = True
    assert run(context)["release_allowed"] is False


def test_invalid_model_assumption_blocks_release():
    context = valid_context()
    context["model_assumption_invalid"] = True
    assert run(context)["release_allowed"] is False


def test_uncharacterized_uncertainty_blocks_release():
    context = valid_context()
    context["uncertainty_not_characterized"] = True
    assert run(context)["release_allowed"] is False


def test_attribution_overclaim_blocks_release():
    context = valid_context()
    context["attribution_overclaim"] = True
    assert run(context)["release_allowed"] is False


def test_reproducibility_gap_blocks_release():
    context = valid_context()
    context["reproducibility_gap"] = True
    assert run(context)["release_allowed"] is False
