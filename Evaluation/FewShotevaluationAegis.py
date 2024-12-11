import pandas as pd
# Similarity matrix for the given table
similarity_matrix_large = {
    "BR1264": {"BR772": 0.1, "BR1149": 0.3, "BR1257": 0.1, "BR418": 0.98},
    "BR450": {"BR772": 0.1, "BR1149": 0.3, "BR1257": 0.1, "BR418": 0.2,"BR1264":0.56},
    "BR772": {"BR450": 0.1, "BR1149": 0.6, "BR1257": 0, "BR418": 0,"BR1264":0.23},
    "BR1149": {"BR450": 0.3, "BR772": 0.6, "BR1257": 0.77, "418": 0.52,"BR1264":0.12},
    "BR1257": {"BR450": 0.1, "BR772": 0, "BR1149": 0.77, "BR418": 0.44,"BR1264":0},
    "BR418": {"BR450": 0.2, "BR772": 0, "BR1149": 0.52, "BR1257": 0.44,"BR1264":0.6},
}

# Function to calculate MRR for a single query
def calculate_mrr_for_query(scores):
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for i, (_, score) in enumerate(sorted_scores, start=1):
        if score > 0:  # Assuming scores > 0 are relevant
            return 1 / i
    return 0

# Function to calculate MAP for a single query
def calculate_map_for_query(scores):
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    relevant_count = 0
    precision_sum = 0
    for i, (_, score) in enumerate(sorted_scores, start=1):
        if score > 0:  # Assuming scores > 0 are relevant
            relevant_count += 1
            precision_sum += relevant_count / i
    return precision_sum / len(sorted_scores) if sorted_scores else 0

# Calculating MRR and MAP for each query
results_large = {}
for query, scores in similarity_matrix_large.items():
    mrr = calculate_mrr_for_query(scores)
    map_score = calculate_map_for_query(scores)
    results_large[query] = {"MRR": round(mrr, 2), "MAP": round(map_score, 2)}

# Convert results to a DataFrame for easier visualization
df_results_large = pd.DataFrame.from_dict(results_large, orient="index").reset_index()
df_results_large.rename(columns={"index": "Query"}, inplace=True)

df_results_large
print("MRR and MAP Results for Bug Report Similarity Table:")
print(df_results_large)

# Optional: Save the results to a CSV file for further reference
df_results_large.to_csv("mrr_map_results.csv", index=False)
