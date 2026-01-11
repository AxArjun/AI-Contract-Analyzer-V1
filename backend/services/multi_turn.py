def compliance_followup(compliance_output: str, legal_output: str):
    return f"""
Compliance Findings:
{compliance_output}

Legal Interpretation:
{legal_output}

Question:
Are there legal risks due to compliance gaps? Explain clearly.
"""
