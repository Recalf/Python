from Modules.Captcha import *
# 'Captcha' module is just my  that can even solve captcha v2 or v1 without using any subscription like 2captcha to be able
# to do it + other basic measures to not get detected as a bot when using the scraper 


url = r"https://www.practicematch.com/physicians/jobs/"
brws(url)


# turn page funct
def turn():
    
    next = driver.find_elements(By.CLASS_NAME, "page-item")
    next = next[-1].find_element(By.TAG_NAME,'a').get_attribute("href")
    driver.get(next)
    sleep(1)




# filters
countries = ['Alaska','Maryland'] 
filter = 'Remote'


col = ["Facility & Adress", "Contact & Information"]



for k in range(len(countries)):
    urls = []
    df = pd.DataFrame(columns=col)

    # clear the filters
    try:
        clear = driver.find_element(By.CSS_SELECTOR, '#contentDiv > div > div.selected-criteria-panel.fade.show.alert-dismissible.bg-light.p-2.mb-3.row.d-block.scrollable.border > div > a')
        clear = clear.get_attribute('href')
        driver.get(clear)
    except NSEE:
        pass

    driver.find_element(By.ID, "button-states").click()
    sleep(0.25)
    driver.find_element(By.XPATH, f"//*[contains(text(), '{countries[k]}')]").click()
    sleep(0.6)

    # job type

    driver.find_element(By.ID, "button-employmenttype").click()
    sleep(0.3)
    driver.find_element(By.XPATH, f"//*[contains(text(), '{filter}')]").click()
    sleep(0.5)

    while True:

        print(k)
        elems = driver.find_elements(By.CLASS_NAME, "col-lg-9")
        for elem in elems:
            ls = []
            sleep(0.4)
            urlo = elem.find_element(By.TAG_NAME, "a").get_attribute("href")
            urls.append(urlo)
            driver.get(urlo)

            # now scrape the data

            #fac and adress / location
            try:
                facadress_element = driver.find_element(By.CSS_SELECTOR, "#pm-physicians-site > div.container-fluid.pb-0.mx-0.px-0 > section.container-fluid.pt-0.px-0.px-lg-5 > section:nth-child(5) > div > div.col-md-4.smaller-column-style > div:nth-child(1) > ul")
                facadress = facadress_element.text.strip() #without split("\n"), so that you assign the whole thing into 1 block in the row (facadress has \n in each line)
                ls.append(facadress)
            except NSEE:
                ls.append(None)
            # success
            
            #contact
            try:
                lis = []
                try:
                    ele = driver.find_element(By.CLASS_NAME, "card-title")
                    ele = ele.text.strip()
                    lis.append(ele)
                    
                except NSEE:
                    pass
                
                # part 2
                
                contlist = driver.find_elements(By.CSS_SELECTOR, '#contact-info > div > div > div > ul > li')
                if len(contlist) > 1:
                    for i in range(len(contlist) - 1):
                        lis.append(contlist[i].text.strip().replace("\n"," "))
                
                # email
                email = contlist[-1].find_element(By.TAG_NAME,"a").get_attribute("href").replace("mailto:","").split("?")[0]
                lis.append(email)
                
                lis = "\n".join(lis)
                
                ls.append(lis)  
            except NSEE:
                ls.append(None)
            #sucess
            


            
            df.loc[len(df)] = ls
            

            driver.back()
            sleep(1)

        # turn page
        try:
            turn()
        except:
            print(k)
            break

    
    df.index = urls
    print(fr"C:\Users\touto\Desktop\webscr\Project in work\exc{k}.csv") 

    df.to_csv(fr"C:\Users\touto\Desktop\webscr\Project in work\exc{k}.csv")
    df.to_excel(fr"C:\Users\touto\Desktop\webscr\Project in work\exc{k}.xlsx")


    # turning page to the next one till the end




