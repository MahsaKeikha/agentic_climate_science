from AGENTS.problem_agent import run as problem
from AGENTS.data_agent import run as data
from AGENTS.modeling_agent import run as modeling
from AGENTS.uncertainty_agent import run as uncertainty
from AGENTS.reviewer_agent import run as reviewer

def run(context:dict)->dict:
    return {"system":"F85","outputs":[problem(context),data(context),modeling(context),uncertainty(context),reviewer(context)],"human_review_required":True}
