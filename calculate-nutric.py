# Calculate modified NUTRIC score (without consideration of IL-6)
# 02/2018 / Arne Peine

# 1. Required Variables and explanations

# Age (age): expects integer
# APACHE II score (apache): expects integer (can be calculated with APACHEII calculator)
# SOFA score (sofa): expects integer
# Number of comorbidities (comorbidities): expects integer
# Days from hospital to ICU-admission (daystoicu) (0<1, >=1): expects integer

# 2. Functions:
# in_range() checks whether a value is in range
# calculate_single_scores() calculates a single score, e.g. calculate_single_scores(22, "age")
# calculate_nutric() calculates full nutric score, e.g. calculate_nutric(44,28,12,1,2)


def in_range (lowerlimit, upperlimit, value):
    return lowerlimit <= value <= upperlimit
       
def calculate_single_scores (value, selector):
    
    if selector is "age":
        value_ranges = ([0,49,0],[50,74,1],[75,120,2])
    elif selector is "apache":
        value_ranges = ([0,14,0],[15,19,1],[20,28,2],[28,100,3])
    elif selector is "sofa":
        value_ranges = ([0,5,0],[6,9,1],[10,20,2])
    elif selector is "comorbidities":
        value_ranges = ([0,1,0],[2,200,1])
    elif selector is "daystoicu":
        value_ranges = ([0,0,0],[1,100,1])
    else:
        value_ranges = 0
    for value_range in value_ranges:
        if in_range(value_range[0], value_range[1], value):
            return int(value_range[2])

def calculate_nutric(age,apache,sofa,comorbidities,daystoicu):
    args = list(locals().values())
    list_of_scores = []
    selectors = list(reversed(["age","apache","sofa","comorbidities","daystoicu"]))
    for arg, selector in zip(args, selectors):
        #print(selector, arg) uncomment for validation
        result = calculate_single_scores(arg, selector)
        list_of_scores.append(result)
    return(sum(list_of_scores))

calculate_nutric(44,28,12,1,2)
