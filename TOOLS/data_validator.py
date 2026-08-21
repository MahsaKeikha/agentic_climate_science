def run(payload:dict)->dict:return {"valid":isinstance(payload,dict) and bool(payload),"payload":payload}
