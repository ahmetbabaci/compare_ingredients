# Ingredient List Comparator
**Written by Lily Gates** 

## Description
This script compares the ingredient lists of two products entered via the command line. It identifies unique ingredients for each product as well as shared or similar ingredients.
* Similar ingredients are defined as those derived from the same base component but appearing in different forms or derivatives (e.g., various Vitamin C compounds or retinol variants).
* For shared ingredients, the script reports their relative position within each product’s ingredient list, including percentile rankings.  

The output includes:  
* A pandas DataFrame showing shared ingredients, their positions, and relative percentiles in both products.
* Visualizations of the shared ingredients through bar graphs, scatter plots, and heat maps.  

## Usage
Run the script from the command line. You will be prompted to input ingredient lists for two products. Enter ingredients as comma-separated values.

```python ingredient_comparison.py```

Then enter ingredients when prompted:

```
Enter ingredients for Product 1: water, glycerin, vitamin C, retinol
Enter ingredients for Product 2: water, hyaluronic acid, vitamin C derivative, retinol acetate
```

The script will output:
* A table showing shared and unique ingredients, along with their relative positions in each product.
* Visualizations comparing the shared ingredients (bar chart, scatter plot, heat map).  

Note: Be sure you have installed the required dependencies before running.

## Required Dependencies
This project requires the following Python libraries:
* numpy — for numerical operations
* pandas — for data manipulation and DataFrame handling
* matplotlib — for creating visualizations such as bar charts and scatter plots
* seaborn — for enhanced statistical data visualization, including heat maps

## Future Seteps
* Develop a GUI and/or web-based interface for easier use.
* Integrate Optical Character Recognition (OCR) to allow input via images of ingredient lists.
