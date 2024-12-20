import pandas as pd
import pytrec_eval

#True Duplicate Bug reports for Cgeo Zero Shot
cgeo_dup ={
    "BR7905": {"BR9879": 1},#
    "BR8515": {"BR8043": 1},#
    "BR11218": {"BR11846":1},#
    "BR11566": {"BR11568":1, "BR11557":1,},#
    "BR11568":{"BR11566":1, "BR11557":1,},#
    "BR11846":{"BR11218":1},#
    "BR12760": {"BR12587": 1},
}

#Duplicate Bug reports for Cgeo Zero Shot
cgeo_zshot ={
    "BR7905": {"BR8515": 0.62, "BR11218": 0.8, "BR11566": 0.7, "BR11568": 0.85, "BR11846":0.6, "BR12760": 0.6, "BR9879": 0.77},
    "BR8515": {"BR7905": 0.62, "BR11218": 0.67, "BR11566": 0.87, "BR11568":0.49, "BR11846":0.8,	"BR12760":0.67, "BR8043": 0.67},
    "BR11218": {"BR7905":0.8, "BR8515": 0.67, "BR11566": 0.86, "BR11568": 0.6, "BR11846":0.82, "BR12760":0.63},
    "BR11566": {"BR7905":0.7, "BR8515":0.87, "BR11218":0.86, "BR11568":0.73, "BR11846":0.85, "BR12760":0.82, "BR11557": 0.41},
    "BR11568":{"BR7905":0.85, "BR8515":0.49, "BR11218":0.6, "BR11566":0.73, "BR11846":0.62, "BR12760": 0.58, "BR11557": 0.86},
    "BR11846":{"BR7905":0.6,	"BR8515":0.8, "BR11218":0.82,	"BR11566":0.85, "BR11568":0.62, "BR12760":0.8},
    "BR12760": {"BR7905":0.6, "BR8515":0.67, "BR11218":0.63,	"BR11566":0.82,	"BR11568":0.58,	"BR11846":0.8, "BR12587": 0.65},
}

#Duplicate Bug reports for Cgeo One Shot
cgeo_oshot ={
    "BR7905": {"BR8515": 0.7, "BR11218": 0.62, "BR11566": 0.62, "BR11568": 0.58, "BR11846":0.82, "BR12760": 0.6, "BR9879": 0.8},
    "BR8515": {"BR7905": 0.7, "BR11218": 0.82, "BR11566": 0.55, "BR11568":0.5, "BR11846":0.48,	"BR12760":0.63, "BR8043": 0.8},
    "BR11218": {"BR7905":0.62, "BR8515": 0.82, "BR11566": 0.57, "BR11568": 0.73, "BR11846":0.72, "BR12760":0.67},
    "BR11566": {"BR7905":0.62, "BR8515":0.55,	"BR11218":0.57,	"BR11568":0.78,	"BR11846":0.67,	"BR12760":0.65, "BR11557": 0.87},
    "BR11568":{"BR7905":0.58, "BR8515":0.5,	"BR11218":0.73, "BR11566":0.78, "BR11846":0.5, "BR12760": 0.58, "BR11557": 0.73},
    "BR11846":{"BR7905":0.82,	"BR8515":0.48, "BR11218":0.72,	"BR11566":0.67, "BR11568":0.5, "BR12760":0.38},
    "BR12760": {"BR7905":0.6, "BR8515":0.63, "BR11218":0.67,	"BR11566":0.65,	"BR11568":0.58,	"BR11846":0.38, "BR12587": 0.78}
}

#Bug reports for ? ?
similarity_matrix_large = {
    "BR1264": {"BR772": 0.1, "BR1149": 0.3, "BR1257": 0.1, "BR418": 0.98},
    "BR450": {"BR772": 0.1, "BR1149": 0.3, "BR1257": 0.1, "BR418": 0.2,"BR1264":0.56},
    "BR772": {"BR450": 0.1, "BR1149": 0.6, "BR1257": 0, "BR418": 0,"BR1264":0.23},
    "BR1149": {"BR450": 0.3, "BR772": 0.6, "BR1257": 0.77, "418": 0.52,"BR1264":0.12},
    "BR1257": {"BR450": 0.1, "BR772": 0, "BR1149": 0.77, "BR418": 0.44,"BR1264":0},
    "BR418": {"BR450": 0.2, "BR772": 0, "BR1149": 0.52, "BR1257": 0.44,"BR1264":0.6},
}


def calculate_map_and_mrr_for_query(scores, true_duplicates):
    ##Uses a premade library to get the map metrics
    evaluator = pytrec_eval.RelevanceEvaluator(true_duplicates, {'map_cut.4'})
    results = evaluator.evaluate(scores)
    results = pd.DataFrame.from_dict(results, orient="index").reset_index() #Will be easier to add the mrr if in the form of a Pandas data frame. 
    results.rename(columns={"index": "Query"}, inplace=True)
    results.rename(columns={"map_cut_4": "MAP"}, inplace=True)

    #The library does not have mrr, so here is my method
    results["MRR"] = 0
    # row = 0
    # for key, _ in true_duplicates.items():
    #     #If there is only one value the MAP and MRR will be the same
    #     if len(true_duplicates[key].items()) == 1:
    #         results.loc[row, "MRR"] = results.at[row, "MAP"]
    #         print(results.loc[row])
    #     else:
    #         sorted_scores = sorted(true_duplicates[key], key=lambda x: x[1], reverse=True)
    #         for i, (bug, _) in enumerate(sorted_scores, start=1):
    #             if bug in true_duplicates[key].keys():  # Assuming scores > 0 are relevant
    #                 results.loc[row, "MRR"] = 1/row
    #                 break
    #     row += 1
    results.loc[len(results)] = ['Avg', results['MAP'].mean(), results['MRR'].mean()]

    return results

#?
# Calculating MRR and MAP for each query
# Convert results to a DataFrame for easier visualization
df_zresults = calculate_map_and_mrr_for_query(cgeo_zshot, cgeo_dup)

df_oresults = calculate_map_and_mrr_for_query(cgeo_oshot, cgeo_dup)

print("MRR and MAP Results for Bug Report Similarity Table:")
print(df_zresults)
print(df_oresults)

# Optional: Save the results to a CSV file for further reference
df_zresults.to_csv("cgeo_zshot_mrr_map_results.csv", index=False)
df_oresults.to_csv("cgeo_oshot_mrr_map_results.csv", index=False)
#Figure out MRR 
#Average

