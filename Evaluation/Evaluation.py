import pandas as pd
import pytrec_eval

#True Duplicate Bug reports for Cgeo
cgeo_dup ={
    "BR7905": {"BR9879": 1},
    "BR8515": {"BR8043": 1},
    "BR11218": {"BR11846":1},
    "BR11566": {"BR11568":1, "BR11557":1,},
    "BR11568":{"BR11566":1, "BR11557":1,},
    "BR11846":{"BR11218":1},
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

#True Duplicate Bug reports for Aegis
aegis_dup ={
    "BR450": {"BR418": 1},
    "BR772": {"BR749": 1},
    "BR1149": {"BR842": 1, "BR1142": 1},
    "BR1257": {"BR411": 1, "BR737": 1, "BR999": 1, "BR1246": 1},
    "BR1268": {"BR1049": 1}
}

#Duplicate Bug reports for Aegis Zero Shot
aegis_zshot = {
    "BR450": {"BR772": 0.1,	"BR1149":0.3, "BR1257":0.1,	"BR1268":0.2, "BR418": 0.91},
    "BR772": {"BR450": 0.1,	"BR1149":0.6, "BR1257":0, "BR1268":0, "BR749": 0.77},
    "BR1149": {"BR450": 0.3, "BR772":0.6, "BR1257": 0.77, "BR1268": 0.52, "BR842": 0.925, "BR1142": 0.9166},
    "BR1257": {"BR450": 0.1, "BR772": 0, "BR1149": .77, "BR1268": 0.44, "BR411": 0.83, "BR737": 0.82, "BR999": 0.06, "BR1246": 0},
    "BR1268": {"BR450": 0.2, "BR772": 0, "BR1149": 0.52, "BR1257":0.44, "BR1049": 0.3}
}

#Duplicate Bug reports for Aegis One Shot
aegis_oshot = {
    "BR450": {"BR772": 0.1,	"BR1149":0.3, "BR1257":0.1,	"BR1268":0.2, "BR418": 0.99},
    "BR772": {"BR450": 0.1,	"BR1149":0.6, "BR1257":0, "BR1268":0, "BR749": 0.82},
    "BR1149": {"BR450": 0.3, "BR772":0.6, "BR1257": 0.66, "BR1268": 0.32, "BR842": 0.91, "BR1142": 0.91},
    "BR1257": {"BR450": 0.1, "BR772": 0, "BR1149": 0.66, "BR1268": 0.44, "BR411": 0.83, "BR737": 0.72, "BR999": 0.89, "BR1246": 0.9},
    "BR1268": {"BR450": 0.2, "BR772": 0, "BR1149": 0.32, "BR1257":0.44, "BR1049": 0.4}
}
#True Duplicate Bug reports for collect
collect_dup ={
    "BR996": {"BR995": 1},
    "BR1906": {"1262": 1},
    "BR1977": {"BR1914": 1},
    "BR2052": {"BR1914": 1, "BR1977": 1}
}

#Duplicate Bug reports for collect Zero Shot
collect_zshot = {
    "BR996":{"BR1906": 0.55, "BR1977":	0.52, "BR2052": 0.77, "BR995": 0.25},
    "BR1906": {"BR996": 0.55, "BR1977": 0.55, "BR2052": 0.23, "1262": 0.96},
    "BR1977": {"BR996": 0.52, "BR1906":0.55, "BR2052":0.62, "BR1914": 0.55},
    "BR2052": {"BR996":0.77, "BR1906": 0.23, "BR1977": 0.62, "BR1914": 0.55, "BR1977": 0.55}
}

#Duplicate Bug reports for collect One Shot
collect_oshot = {
    "BR996":{"BR1906": 0.55, "BR1977":	0.17, "BR2052": 0.72, "BR995": 34},
    "BR1906": {"BR996": 0.55, "BR1977": 0.66, "BR2052": 0.22, "1262": 0.67},
    "BR1977": {"BR996": 0.17, "BR1906":0.66, "BR2052":0.33, "BR1914": 0.52},
    "BR2052": {"BR996":0.72, "BR1906": 0.22, "BR1977": 0.33, "BR1914": 0.62, "BR1977": 0.8}
}
#True Duplicate Bug reports for RetroMusic
rm_dup ={
    "BR1467": {"BR1049": 1},
    "BR1592": {"BR1495": 1}
}

#Duplicate Bug reports for RetroMusic Zero Shot
rm_zshot = {
    "BR1467": {"BR1264": 0.8, "BR1592": 0.55, "BR1049": 1},
    "BR1592": {"BR1264": 0, "BR1467": 0.55, "BR1495": 0.9}
}

#Duplicate Bug reports for RetroMusic One Shot
rm_oshot = {
    "BR1467": {"BR1264": 0.8, "BR1592": 0.36, "BR1049": 0.7},
    "BR1592": {"BR1264": 0, "BR1467": 0.36, "BR1495": 0.92}
}

#Add new duplicate bug reports here in the same format as duplicat, one shot, and zero shot.

def calculate_map_and_mrr_for_query(scores, true_duplicates):
    ##Uses a premade library to get the map metrics
    evaluator = pytrec_eval.RelevanceEvaluator(true_duplicates, {'map_cut.10'})
    results = evaluator.evaluate(scores)
    results = pd.DataFrame.from_dict(results, orient="index").reset_index() #Will be easier to add the mrr if in the form of a Pandas data frame. 
    results.rename(columns={"index": "Query"}, inplace=True)
    results.rename(columns={"map_cut_10": "MAP"}, inplace=True)

    #The library does not have mrr, so here is my method
    results["MRR"] = 0
    #Goes through each Bug Report
    for key in set(true_duplicates.keys()):
        #If there is only one value the MAP and MRR will be the same
        if len(true_duplicates[key]) == 1:
            results.loc[results["Query"] == key, "MRR"] = results.loc[results["Query"] == key, "MAP"]
        #If there are multipe, it finds the first occurence.
        else:
            #Sorts the scores for the BR
            sorted_scores = sorted(scores[key].items(), key=lambda x: x[1], reverse=True)
            #Goes through each score and sees if it is a duplicate. If so, it stops the search and puts the MRR as the 1/current iteration (or i)
            for i, (bug,_) in enumerate(sorted_scores, start=1):
                if bug in true_duplicates[key].keys():  
                    results.loc[results["Query"] == key, "MRR"] = 1/i
                    break

    #Puts a final column stating the averages for the MAP and MRR        
    results.loc[len(results)] = ['Avg', results['MAP'].mean(), results['MRR'].mean()]

    return results

# Calculating MRR and MAP for Cgeo
cgeo_zresults = calculate_map_and_mrr_for_query(cgeo_zshot, cgeo_dup)

cgeo_oresults = calculate_map_and_mrr_for_query(cgeo_oshot, cgeo_dup)

#Prints Results
print("MRR and MAP Results for CGEO:")
print("Zero Shot:")
print(cgeo_zresults)
print("One Shot:")
print(cgeo_oresults)

#Saves to CSV
cgeo_zresults.to_csv("cgeo_zshot_mrr_map_results.csv", index=False)
cgeo_oresults.to_csv("cgeo_oshot_mrr_map_results.csv", index=False)

# Calculating MRR and MAP for Aegis
aegis_zresults = calculate_map_and_mrr_for_query(aegis_zshot, aegis_dup)

aegis_oresults = calculate_map_and_mrr_for_query(aegis_oshot, aegis_dup)

#Print Results
print("MRR and MAP Results for Aegis:")
print("Zero Shot:")
print(aegis_zresults)
print("One Shot:")
print(aegis_oresults)

# Save to CSV
aegis_zresults.to_csv("aegis_zshot_mrr_map_results.csv", index=False)
aegis_oresults.to_csv("aegis_oshot_mrr_map_results.csv", index=False)

# Calculating MRR and MAP Collect
collect_zresults = calculate_map_and_mrr_for_query(collect_zshot, collect_dup)

collect_oresults = calculate_map_and_mrr_for_query(collect_oshot, collect_dup)

#Print Results
print("MRR and MAP Results for Collect:")
print("Zero Shot:")
print(collect_zresults)
print("One Shot:")
print(collect_oresults)

# Save to CSV
collect_zresults.to_csv("collect_zshot_mrr_map_results.csv", index=False)
collect_oresults.to_csv("collect_oshot_mrr_map_results.csv", index=False)

# Calculating MRR and MAP for Retro Music
rm_zresults = calculate_map_and_mrr_for_query(rm_zshot, rm_dup)

rm_oresults = calculate_map_and_mrr_for_query(rm_oshot, rm_dup)

#Print results
print("MRR and MAP Results for Retro Music:")
print("Zero Shot:")
print(rm_zresults)
print("One Shot:")
print(rm_oresults)

# Save to CSV
rm_zresults.to_csv("rm_zshot_mrr_map_results.csv", index=False)
rm_oresults.to_csv("rm_oshot_mrr_map_results.csv", index=False)

#Copy the calculating MRR and MAP lines to do the evaluation. After one can print the results or save them to CSV.
