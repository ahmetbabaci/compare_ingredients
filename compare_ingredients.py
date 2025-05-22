# -------------------------------------------
#   Comparing Ingredients
#   Written By: Lily Gates
#   May 2025 
# -------------------------------------------

# ===========================================
# Import Libraries and Packages
# ===========================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------
# Prompt User Input for Product Names
# Provide confirmation statement for the newly saved name
# -------------------------------------------

# Input name for `Product 1`
# If no input is given, default is "Product 1"
product_1_name = str(input("\nWhat is the name of Product 1?: ")) or "Product 1"
print(f"Saving Product 1 as: '{product_1_name}'")

# Input name for `Product 2`
# If no input is given, default is "Product 2"
product_2_name = str(input("\nWhat is the name of Product 2?: ")) or "Product 2"
print(f"Saving Product 2 as: '{product_2_name}'")

# -------------------------------------------
# Prompt User Input for Product Ingredients
# Will take in str and return a list that is lowercased
# -------------------------------------------

# Input ingredients for `Product 1`
product_1_ingr_input = str(input(f"\nList the ingredients for {product_1_name} (comma-seperated):\n"))
product_1_ingr_list = product_1_ingr_input.lower().replace(", ", ",").split(",")
print(f"Confirming ingredients for {product_1_name} as:\n{product_1_ingr_list}")

# Input ingredients for `Product 2`
product_2_ingr_input = str(input(f"\nList the ingredients for {product_2_name} (comma-seperated):\n"))
product_2_ingr_list = product_2_ingr_input.lower().replace(", ", ",").split(",")
print(f"Confirming ingredients for {product_2_name} as:\n{product_2_ingr_list}")

# Loading statement
print("==========================================================================")
print(f"Comparing ingredients for {product_1_name} and {product_2_name}")
print("==========================================================================")

# -------------------------------------------
# Returns unique ingredients
# Will take in str and return a list that is lowercased
# -------------------------------------------

unique_ingr_product_1 = list(set(product_1_ingr_list) - set(product_2_ingr_list))
unique_ingr_product_2 = list(set(product_2_ingr_list) - set(product_1_ingr_list))
all_ingredients = set(product_1_ingr_list) | set(product_2_ingr_list)

print(f"ONLY {product_1_name}:\n{unique_ingr_product_1}\n")

print(f"ONLY {product_2_name}:\n{unique_ingr_product_2}")

# -------------------------------------------
# Returns shared ingredients
# -------------------------------------------

print("-----------------------------------------------------")

same_ingr = set(product_1_ingr_list) & set(product_2_ingr_list)

# Return unsorted shared ingredients
print(f"BOTH {product_1_name} and {product_2_name}:\n{list(same_ingr)}")

# -------------------------------------------
# Returns the index and percentile of the shared ingredients
# -------------------------------------------

def get_ingr_stats(ingr_list):
    """
    Returns a dictionary of index and percent location for shared ingredient
    
    Args:
        ingr_list, list of ingredients (e.g., product_1_ingr_list)

    Returns:
        dict with the idx and relative percentile

    """
    stats = {}
    for ingr in same_ingr:
        if ingr in ingr_list:
            idx = ingr_list.index(ingr)
            perct = round(1-(idx / len(ingr_list)), 4)
            stats[ingr] = {"idx": idx, "perct": perct}
    return stats

# Create dictionaries
shared_1 = get_ingr_stats(product_1_ingr_list)
shared_2 = get_ingr_stats(product_2_ingr_list)

# Merge dictionaries into a combined list of rows

# Convert product names to snake_case
product_1_snake = product_1_name.replace(" ", "_").lower()
product_2_snake = product_2_name.replace(" ", "_").lower()

combined = []

for ingr in same_ingr:
    combined.append({
        "ingredient": ingr,
        f"{product_1_snake}_idx": shared_1[ingr]["idx"],
        f"{product_1_snake}_perct": shared_1[ingr]["perct"],
        f"{product_2_snake}_idx": shared_2[ingr]["idx"],
        f"{product_2_snake}_perct": shared_2[ingr]["perct"],
    })

# Create final combined dataframe
df_combined = pd.DataFrame(combined).sort_values(by=f"{product_1_snake}_idx").reset_index(drop=True)

print(f"\n'{product_1_name}' and '{product_2_name}'\nIndex and Relative Percentile of Shared Ingredients\n")
print(df_combined)


# ===========================================
# Creating Visualizationsfor Results
# ===========================================

# Loading statement
print("==========================================================================")
print(f"Creating visualizations for {product_1_name} and {product_2_name}")
print("==========================================================================")

# ---- Horizontal Bar Chart ----
plt.figure(figsize=(10, 5))
bar_width = 0.4
y_positions = range(len(df_combined))

plt.barh(
    [y - bar_width/2 for y in y_positions], 
    df_combined[f"{product_1_snake}_perct"], 
    height=bar_width, 
    label=product_1_name, 
    color='skyblue'
)
plt.barh(
    [y + bar_width/2 for y in y_positions], 
    df_combined[f"{product_2_snake}_perct"], 
    height=bar_width, 
    label=product_2_name, 
    color='lightcoral'
)

plt.yticks(ticks=y_positions, labels=df_combined["ingredient"])
plt.xlabel("Relative Position in Ingredient List (1 = Top)")
plt.title("Shared Ingredients Bar Chart")
plt.gca().invert_yaxis()
plt.legend()
plt.tight_layout()
plt.show()

# ---- Vertical Bar Chart ----

plt.figure(figsize=(10, 5))
bar_width = 0.4
x_positions = range(len(df_combined))

plt.bar(
    [x - bar_width/2 for x in x_positions], 
    df_combined[f"{product_1_snake}_perct"], 
    width=bar_width, 
    label=product_1_name, 
    color='skyblue'
)
plt.bar(
    [x + bar_width/2 for x in x_positions], 
    df_combined[f"{product_2_snake}_perct"], 
    width=bar_width, 
    label=product_2_name, 
    color='lightcoral'
)

plt.xticks(ticks=x_positions, labels=df_combined["ingredient"], rotation=45, ha='right')
plt.ylabel("Relative Position in Ingredient List (1 = Top)")
plt.title("Shared Ingredients Bar Chart")
plt.legend()
plt.tight_layout()
plt.show()

# ---- Scatter Plot ----
plt.figure(figsize=(6, 6))
plt.scatter(
    df_combined[f"{product_1_snake}_perct"], 
    df_combined[f"{product_2_snake}_perct"], 
    color='navy'
)

for i, row in df_combined.iterrows():
    plt.text(
        row[f"{product_1_snake}_perct"], 
        row[f"{product_2_snake}_perct"], 
        row["ingredient"], 
        fontsize=9, 
        ha='right'
    )

plt.xlabel(f"{product_1_name} (Percentile)")
plt.ylabel(f"{product_2_name} (Percentile)")
plt.title("Relative Percentile of Shared Ingredients")

plt.grid(False, which='major')
plt.grid(False, which='minor')
plt.tight_layout()
plt.show()

# ---- Heatmap ----
heat_df = df_combined.set_index("ingredient")[
    [f"{product_1_snake}_perct", f"{product_2_snake}_perct"]
]

plt.figure(figsize=(6, 4))
sns.heatmap(heat_df, annot=True, cmap="YlGnBu", cbar_kws={"label": "Relative Position"})

plt.xlabel(f"Product")
plt.ylabel(f"Ingredient")

plt.title("Relative Percentile of Shared Ingredients")
plt.tight_layout()
plt.show()

# TODO
# - Refine data visualizations
# - Save the dataframe as CSV and save all data visualizations
# - Create folders for the output files
# - Create confirmation print statement for path that files are saved