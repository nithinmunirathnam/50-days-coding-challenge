policy_ids = [101, 102, 103, 104, 105, 106]
claim_amounts = [5000, 15000, 7000, 20000, 3000, 12000]
claim_status = ["Approved", "Rejected", "Approved", "Approved", "Rejected", "Approved"]
customer_age = [25, 45, 35, 50, 23, 40]

total_approved = sum(
    claim_amounts[i] for i in range(len(claim_status)) if claim_status[i] == "Approved"
)
print("Total Approved Claim Amount:", total_approved)

rejected_count = claim_status.count("Rejected")
print("Rejected Claims:", rejected_count)

print("High Value Policy IDs:")
for i in range(len(claim_amounts)):
    if claim_amounts[i] > 10000:
        print(policy_ids[i])

approved_ages = [
    customer_age[i] for i in range(len(claim_status)) if claim_status[i] == "Approved"
]
avg_age = sum(approved_ages) / len(approved_ages)
print("Average Age (Approved):", avg_age)

risk_category = []
for age in customer_age:
    if age < 30:
        risk_category.append("Low Risk")
    elif 30 <= age <= 45:
        risk_category.append("Medium Risk")
    else:
        risk_category.append("High Risk")

print("Risk Categories:", risk_category)
