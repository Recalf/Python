import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

output = r"C:\Users\touto\Desktop\webscr\Results\1\finish3.csv"

options = webdriver.ChromeOptions()


# https://www.trekbikes.com/fr/fr_FR/v%C3%A9los/v%C3%A9los-hybrides/v%C3%A9los-hybrides-%C3%A0-assistance-%C3%A9lectrique/verve/verve-1/p/29110/
# https://www.trekbikes.com/fr/fr_FR/v%C3%A9los/v%C3%A9los-hybrides/v%C3%A9los-hybrides-%C3%A0-assistance-%C3%A9lectrique/verve/verve-4-lowstep/p/40519/?colorCode=grey
# https://www.trekbikes.com/fr/fr_FR/v%C3%A9los/v%C3%A9los-hybrides/v%C3%A9los-hybrides-%C3%A0-assistance-%C3%A9lectrique/verve/verve-5/p/41026/?colorCode=grey

while True:
    a = input("Do you want to continue: ")
    if a.lower() == "no":
        break

    url = input(r"Insert the URL: ")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    

    taillex = driver.find_element(By.CSS_SELECTOR, r"#SizingComponent > div > div:nth-child(1) > div > table").get_attribute('outerHTML')
    geox = driver.find_element(By.CSS_SELECTOR, r"#sizing-table").get_attribute('outerHTML')
    product_name = driver.find_element(By.CSS_SELECTOR, r"#data-product-details-header > h1").text

    df1 = pd.read_html(taillex)[0] # taille
    df2 = pd.read_html(geox)[0] # geo
    

    driver.quit()

    pd.DataFrame([[product_name], [url]]).to_csv(output, mode="a", index=False, header=False, encoding="utf-8")

    # GEO
    def geo(tab):
        columns = ["A — Tube de selle","C — Longueur du tube douille","E — Tube supérieur efficient","M — Portée du cadre","N — Hauteur du tube de direction / boîtier"]
        return tab[columns]

    # tailles
    pd.DataFrame([["---Sizes---"]]).to_csv(output, mode="a", index=False, header=False, encoding="utf-8")
    df1.to_csv(output,mode="a",index=False,encoding="utf-8")
    
    
    
    # geo
    geresu = geo(df2)
    pd.DataFrame([["---Geo---"]]).to_csv(output, mode="a", index=False, header=False, encoding="utf-8")
    geresu.to_csv(output,mode="a",index=False,encoding="utf-8")
    pd.DataFrame([["---End of Product---"]]).to_csv(output, mode="a", index=False, header=False, encoding="utf-8")

    
df_new = pd.read_csv(output)
GFG = pd.ExcelWriter(r"C:\Users\touto\Desktop\webscr\Results\1\finish2.xlsx")
df_new.to_excel(GFG, index=False)
    
