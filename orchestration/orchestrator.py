from AGENTS.data_agent import run as data
from AGENTS.modeling_agent import run as modeling
from AGENTS.problem_agent import run as problem
from AGENTS.reviewer_agent import run as reviewer
from AGENTS.uncertainty_agent import run as uncertainty
from safety.policy import check


def run(context: dict) -> dict:
    """Run the climate-science pipeline and apply fail-closed governance."""
    outputs = [
        problem(context),
        data(context),
        modeling(context),
        uncertainty(context),
        reviewer(context),
    ]
    governance = check(context)
    return {
        "system": "F85",
        "outputs": outputs,
        "governance": governance,
        "release_allowed": governance["allowed"],
        "human_review_required": True,
        "autonomous_scientific_authority": False,
        "autonomous_policy_authority": False,
    }
