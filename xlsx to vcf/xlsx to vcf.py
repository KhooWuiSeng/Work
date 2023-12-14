#pip install openpyxl
import pandas as pd

required_cols = list(range(1,5))

xlsx = pd.read_excel('xlsx to vcf/NIHMS1501643-supplement-2.xlsx', usecols = required_cols, skiprows = 2)
sorted_xlsx = xlsx.sort_values(by = "position (hg19)").rename(columns = {"chromosome":"CHROM", "position (hg19)":"POS", "reference":"REF", "alt":"ALT"})

#print(sorted_xlsx)

sorted_xlsx['ID'] = "."
sorted_xlsx['QUAL'] = "."
sorted_xlsx['FILTER'] = "."
sorted_xlsx['INFO'] = "."
sorted_xlsx['FORMAT'] = "."

sorted_xlsx = sorted_xlsx[['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT']]

header = """##fileformat=VCFv4.2
##fileDate=20231214
##source=myImputationProgramV3.1
##reference=file:///seq/references/
#CHROM POS ID REF ALT QUAL FILTER INFO
"""

output_vcf = "xlsx to vcf/output.vcf"
with open(output_vcf, 'w') as vcf:
    vcf.write(header)

sorted_xlsx.to_csv(output_vcf, sep="\t", mode='a', index=False)