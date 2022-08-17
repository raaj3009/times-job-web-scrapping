#                            TIMESJOB-WEB-SCRAPPING-PROJECT                         #


def project_web_scrap():            # made fuction for easily access or reuse this code.

    base_url='https://www.timesjobs.com/candidate/job-search.html?from=submit&searchType=Home_Search&luceneResultSize=25&postWeek=60&cboPresFuncArea=35&pDate=Y&sequence='
    
    ''' this is a main url of website for scrapping data'''

    common_url='&startPage=1'  # this is common page url

    all_urls=[]

    for item in range(1,41):
        all_urls.append(base_url+str(item)+common_url) 

        #print(all_urls)
        
        '''fetched 40 links of page, one page has 25 jobs (40*25=1000) as per requirement.'''
        

    import requests

    '''requests useed for extract data from website'''

    from bs4 import BeautifulSoup

    '''beatifulsoup to understand HTML code for python'''

    all_fetched_data=[]   # list created for store list of dictionary data

    for url in all_urls:
        all_source_data=requests.get(url).text    # fetched data from website.
        #print(all_source_data)

        all_soup_data=BeautifulSoup(all_source_data,'lxml')   # converted data in beautifullsoup which understand python.
        #print(all_soup_data)

        all_pages_data=all_soup_data.find_all('li',class_=('clearfix job-bx wht-shd-bx'))   # tags of HTML which contain job detail.
        #print(all_pages_data)
        
        for val in all_pages_data:

            #1]
            job_title=val.find('h2').text   #fetched jobs title,
            job_title=job_title.lstrip()    #it contain all jobs title.
            #print(job_title)
            
            #2]
            company_name=val.find('h3',class_='joblist-comp-name').text    # fetched comapany name,
            companyname=company_name.lstrip().split()[0]                   # it contain all company name.
            #print(companyname)
            
            #3]
            experience=val.find('li').text                      # fetched experience,
            experience1=experience.replace('card_travel','')    # it contain experience.
            #print(experience1)

            #4]
            location=val.find('span').text       # fetched location,
            location1=location.lstrip()          # it contain location.
            #print(location1)

            #5]
            job_discription=val.find('ul',class_='list-job-dtl clearfix').text   # fetched job description,
            jobdescription=job_discription.splitlines()[3:4]                     # it contain job description.
            jobdescription=','.join(jobdescription)    
            #print(jobdescription)                            

            #6]
            key_skill=val.find('span',class_='srp-skills').text         # fetched key skill,
            keyskill=key_skill.lstrip().splitlines()[0:1]               # it contain key skill.
            keyskill=(','.join(keyskill))   
            #print(keyskill)  

            #7]
            job_link=val.find('a')['href']              # fetched job details link,
            #print(job_link)                            # it contain job details links.

            dict_data={
                'Job Title': job_title,
                'Company Name': companyname,
                'Experience': experience1,
                'Location': location1,
                'Job Description': jobdescription,
                'Key Skills': keyskill,
                'Job Detail Link': job_link
            }                              

            #print(dict_data)              

            all_fetched_data.append(dict_data)          # contain all list of data.

            #print(all_fetched_data)           
            
            
    import pandas as pd

    '''for the help of pandas convert data into excel-sheet.'''

    df1=pd.DataFrame(all_fetched_data)                # contain all frame data

    #print(df1)

    df1.to_excel('project_scrapp_data.xlsx')                # excel-sheet of 1000 jobs details.


project_web_scrap()


#                                            END                                              #


    

    















