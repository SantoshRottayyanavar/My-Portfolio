import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_pdf_viewer import pdf_viewer
import pandas as pd
from st_social_media_links import SocialMediaIcons
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="SantoshRottayyanavar", layout="wide", page_icon="👨🏻‍💼")

page_bg_image = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://img.freepik.com/free-vector/minimalist-background-with-geometric-shapes_91008-271.jpg?t=st=1733761857~exp=1733765457~hmac=087815752da786420a0a523482f57106ee3483a8f048307f115291b5732332e2&w=1380");
background-size: cover;
Abackground-color: #ffffff10;
backdrop-filter: blur(50px); 
}          

[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}
</style>"""

st.markdown(page_bg_image, unsafe_allow_html=True)





#Removing Hamburger/Deploy option in web app
st.markdown("""
<style>
.st-emotion-cache-147n6fk.ef3psqc6
{
   visibility : hidden;
}
.st-emotion-cache-125megu.ef3psqc5
{
    visibility : hidden;
}          
</style>            
""", unsafe_allow_html=True)

col1, col2 = st.columns([1,2])

with col1:
 st.markdown("### Santosh")

with col2:
  choice = option_menu(
     menu_title = None,
     options = ["Home", "About", "Experience", "Resume", "Contact"],
     icons= ["house-door", "search-heart-fill", "file-person", "pencil-square", "telephone-outbound-fill"],
     menu_icon = "cast",
     default_index=0,
     orientation="horizontal")  
st.write("---")   
     
if choice == "Home":    
    st.write("")
    intro, image = st.columns([10,4])
    intro.markdown("<H2 style = 'text-align: center;'>Hi, </h2>", unsafe_allow_html=True)
    intro.markdown("<H2 style = 'text-align: center;'>I'm Santosh Rottayyanavar </h2>", unsafe_allow_html=True)
    intro.markdown("<H4 style = 'text-align: center;'><em>A Data Analyst</em></h4>", unsafe_allow_html=True)
    intro.markdown("<H5 style = 'text-align: center;'>Help discovering insights from data to make better and informed business decisions.</h5>", unsafe_allow_html=True)

    image.image("Santosh Photo.png")
    st.write("")
    st.write("---") 
    st.write("")

    collect, clean, explore, modelling   = st.columns(4)
    
    collect.markdown("#### :basket: Collect")
    collect.write("Data collection is my systematic approach to gathering information from various sources to create a comprehensive dataset for analysis and informed decision-making.")
    
    clean.markdown("#### :broom: clean")
    clean.write("Data cleaning is my process of identifying and correcting errors and inconsistencies in datasets to ensure their accuracy and reliability for analysis.")

    explore.markdown("#### :telescope: Explore")
    explore.write("Data exploration is an essential part of my workflow, where I analyze and visualize datasets to understand their structure, patterns, and relationships, guiding further analysis.")
    
    modelling.markdown("#### :snowflake: Modelling")
    modelling.write("Data modeling is my process of creating a conceptual representation of data structures and relationships, defining data types and interactions, and establishing rules to organize data effectively for analysis and efficient querying in databases.")

    visualize, interpretation, report  = st.columns(3)
    
    visualize.markdown("#### :bar_chart: Visualize")
    visualize.write("Data visualization involves my creation of visual formats, such as charts and dashboards, to represent data and communicate insights clearly, making complex information more accessible for decision-making.")

    interpretation.markdown("#### :brain: Interpretation")
    interpretation.write("Data interpretation is my process of analyzing and making sense of data to draw meaningful conclusions and translate findings into actionable insights for decision-making.")
    
    report.markdown("#### :bookmark_tabs: Report")
    report.write("Reporting is my process of organizing and presenting data and analysis results in a structured format to communicate insights and recommendations effectively to stakeholders.")

    st.write("")
    st.write("---") 
    st.write("")

elif choice == "About":
      st.write("")
      st.markdown("### Inspired by the Data and Coding")
      st.text("""Inspired by the Data and coding which can be used to analyse with many functionalities and make better and benificial decisions. experiments and works to make it easier for people to understand the code and use data effectively. primarily uses python to explore the Data and coding.
             
               worked at Amer UID Smart Services, Dubai. As Junior Data Analyst over a year of experience explored various facets of data helping the management to make better and efficient decisions.""")
      st.write("---")

      
      with st.expander("Certifications"):
        col1, col2 = st.columns(2)
        with col1:
            panel = st.container(height=580, border=True)
            with panel:
                st.image("IBM_Certification.jpg", caption="Data Visualization")
        
        with col2:
            panel = st.container(height=780, border=True)
            with panel:
                st.image("MeriSKILL.jpg", caption="Data Analyst")
        
        col3, col4 = st.columns(2)
        with col3:
            panel = st.container(height=780, border=True)
            with panel:
                st.image("AI Variant.jpg", caption="Data Analytics")

        with col4:
            panel = st.container(height=780, border=True)   
            with panel:
                st.image("Excelr.jpg", caption="Data Analyst Certification")     
     
      with st.expander("Education"):
          st.markdown("#### :book: Education")
          st.text("""Graduated in Computer Application from the Karnataka Univercity, Dharwad - India.
                  Completed PU in Commerce from R L S COMP PU College, Dharwad.""")

      with st.expander("Skills"):
          st.markdown("#### :wrench: Skills")
          st.write("- Languages :  English (Professional), Kannada (Native), Hindi (Proficient)")
          st.write("- Programming :  Python (Professional), SQL (Professional)")        
          st.write("- Libraries/Frameworks :  Pandas, Matplotlib, Seaborn, Streamlit")
          st.write("- Tools :  VS Code, PyCharm, Jupyter, Google colab, MySQL, SQL Server, Git & Github")          
          st.write("- Visualization Tools :  Tableau (professional), Power BI (professional)")
    

elif choice == "Experience":
     st.write("")
     st.markdown("##### Internships")
     st.markdown("###### Company Name: AI Variant")
     st.write("AI Variant is an analytics firm, provides best-in-class products and solutions.It has deep analytics expertise as well as domain expertise in various industries. It's employees extremely passionate about taking on challenges that matter to the clients.")
     st.markdown("Click here to know more about [AI Variant](https://aivariant.com/)")
     st.markdown("###### Projects:")
     with st.expander("Bank Loan Analysis"):
        one, two = st.columns([1,1])
        
        with one:
           panel = st.container(height=480, border=True)
           with panel:
            st.write("Bank Loan Applications Report")
            st.image("Bank Loan Applications.png")
            st.write("""This report provides an analysis of the bank loan applications based on key metrics such as loan types, demographics, housing
            situations, employment details, education levels, and organization types. The visual analysis further highlights patterns and trends 
            across these categories.""")
 
        with two:
          panel = st.container(height=480, border=True)
          with panel:
            st.image("Bank Loan Defaulters.png")
            st.write("""This dashboard titled \"Loan Defaulters vs Repayers\" provides an in-depth analysis of loan default patterns among a total of 307,511 applicants, with 24,825 (8.07%) identified as defaulters. The visualization categorizes defaulters by gender, age, contract type, income type, education, family status, housing type, employment year, and organization type.""")
       
       
        three, four = st.columns([1,1])
        with three:
          panel = st.container(height=550, border=True)
          with panel:
            st.image("Bank Loan repayers.png")
            st.write("This dashboard titled \"Loan Defaulters vs Repayers\" provides an in-depth analysis of loan repayment patterns among a total of 307,511 applicants, with 2,82,686 (91.93%) identified as repayers. The visualization categorizes repayers by gender, age, contract type, income type, education, family status, housing type, employment year, and organization type, offering valuable insights into repayment behaviors.")
        
        with four:
          panel = st.container(height=550, border=True)
          with panel:
            st.image("Bank Loan credit, good price and income correlations.png")
            st.write("This dashboard titled \"Credit, Goods Price, and Income Correlations\" analyzes the relationships among credit amount, goods price, and income for 307,511 applicants. It highlights a strong positive correlation between credit amount and goods price, limited impact of income on credit size, and the distribution of applicants by family size (majority with 0 or 1 child). Additionally, it examines the variability of annuity amounts relative to income and employment.")

        five, six = st.columns([1,1])
        with five:
          panel = st.container(height=570, border=True)
          with panel:
            st.image("Bank Loan Comprehensive financial overview.png")
            st.write("The \"Comprehensive Financial Overview\" report examines financial patterns across 307,511 applicants, focusing on credit amount, goods price, and income distribution. It reveals cash loans as the most utilized contract type, with females receiving higher credit amounts on average than males. Credit levels peak among individuals aged 30–50, with employment durations of up to 20 years correlating with higher credit and goods prices. Repayers consistently secure higher financial benefits compared to defaulters.")
    
        with six:
          panel = st.container(height=600, border=True)
          with panel:
            st.image("Bank Loan Comprehensive financial overview2.png")
            st.write("The report reveals that credit and goods price utilization is highest among married individuals, those with secondary or higher education, and working professionals, particularly in managerial roles. Credit levels peak for applicants aged 30–50, with longer employment durations correlating with greater financial engagement. Private business entities and individuals living in houses or apartments report the highest credit and goods price activity. Minimal engagement is seen among students, unemployed individuals, and those with unknown or unstable family and housing statuses.")
        
        seven, eight = st.columns([1,1])
        with seven:
          panel = st.container(height=520, border=True)
          with panel:
            st.image("Bank Loan Privious application status based on applicants.png")
            st.write("The report highlights cash loans as the most common contract type, with repairs and electronics leading in loan purposes and purchases. Connectivity and consumer electronics dominate seller industries, while cash payments through banks are the preferred method. Middle-yield applicants and cash portfolios account for the majority of activity. Approval rates are high, but refusals and unused offers indicate potential for improvement.")
        
        st.write("---")
        st.write("If you are more intrested please hit the below links for more information:")
        st.markdown(":bank: [Bank Loan Analysis](https://github.com/SantoshRottayyanavar/Bank-Loan-Analysis---Tableau-and-Python)")
        st.markdown("[Detailed Information](https://github.com/SantoshRottayyanavar/Bank-Loan-Analysis---Tableau-and-Python/blob/main/Bank%20Loan%20Analisis%20Final%20Report.pdf)")
        st.markdown("[Dashboard(report)](https://public.tableau.com/app/profile/santosh.rottayyanavar2698/viz/BankloanAnalysisextract/BankLoanApplicantions)")
     
     with st.expander("HR Data Analysis"):
        a1,b1 = st.columns(2)
        a1.image("HRmain.jpg")
        b1.write("This image showcases an HR Data Analysis dashboard with a clean and professional layout. The title, \"HR Data Analysis,\" is prominently displayed at the top, and a \"Main Page\" button is centered for navigation. The left side lists key HR metrics, such as Employee Distribution, Monthly Hours, Turnover Rate, and Workplace Accidents. A visual illustration on the right complements the theme, enhancing its appeal.")

        one, two = st.columns([1,1])
        with one:
           panel = st.container(height=780, border=True)
           with panel:
             st.image("HR1 Employee_distribution.jpg")
             st.write("This dashboard provides an overview of employee distribution and HR metrics. Key highlights include:")
             st.write("\* Turnover and attrition rates are 31.25% and 23.81%, respectively, with a retention rate of 76.19%.")
             st.write("\* The sales department has the highest number of employees (4,140), while management has the least (630).")
             st.write("\* Most employees fall under the low to medium salary categories, with only 8.25% earning high salaries.")
             st.write("\* The distribution of projects shows the sales department leading with over 7,800 projects, followed by technical and support teams.")
             
        with two:
           panel = st.container(height=780, border=True)
           with panel:
              st.image("HR2Employee Avg Monthly Hrs and satisfaction.jpg")
              st.write("This dashboard analyzes average monthly hours and satisfaction levels:")
              st.write("\* The sales department logs the highest average monthly hours (832K) and satisfaction levels (2.54K), followed by technical and support departments.")
              st.write("\* Employees with medium salaries work the most hours (48.76%), while high salary groups show the highest satisfaction levels (47.82%).")
              st.write("\* Management and HR departments have the lowest satisfaction levels and average monthly hours.")
              st.write("\* There is a positive correlation between average monthly hours and satisfaction in departments like sales, technical, and support.")
        
        three, four = st.columns([1,1])
        with three:
           panel = st.container(height=780, border=True)
           with panel:
              st.image("HR3 Employees Precence.jpg")
              st.write("This dashboard provides an analysis of employee presence and related metrics, structured into six main sections. Key highlights include:")
              st.write("\* Employees who stayed tend to work more hours, especially in sales, technical, and support departments.")
              st.write("\* Higher satisfaction levels correlate with employee retention across all departments.")
              st.write("\* Most employees who left had low to medium salaries, whereas retention is higher among medium-salary employees.")
              st.write("\* Longer time spent in the company is linked to higher retention, especially in departments with strong workforce stability like sales and technical teams.")
        
        with four:
           panel = st.container(height=1020, border=True)
           with panel:
              st.image("HR4 Turnover Rate.jpg")
              st.write("This dashboard provides insights into employee turnover rates and related metrics. Key highlights include:")
              st.write("\* The total turnover rate is 31.25%, reflecting a significant portion of the workforce leaving.")
              st.write("\* The HR department has the highest turnover rate at 41.03%, followed by accounting (36.23%) and technical (34.45%). Management has the lowest turnover rate (16.88%), suggesting better retention strategies.")
              st.write("\* Employees with low satisfaction levels (0.31–0.4) account for the highest turnover, indicating dissatisfaction as a key driver of attrition.")
              st.write("\* Turnover is highest among employees with low salaries (42.22%), while high-salary employees experience the least turnover (7.10%)")
              st.write("\* Employees who were not promoted in the last five years show significantly higher turnover rates (83.44%), highlighting the importance of career progression.")
              st.write("\* Turnover is slightly higher among employees with no accidents (36.08%) compared to those with accidents (8.45%).")
        
        five, six = st.columns([1,1])
        with five:
           panel = st.container(height=950, border=True)
           with panel:
              st.image("HR5 Workplace Accident.jpg")
              st.write("This dashboard provides insights into workplace accidents and their impact across departments and salary levels. Key observations include:")
              st.write("\* A total of 2,169 accidents occurred, with 13,000 employees not affected and 2,000 experiencing accidents.")
              st.write("\* The sales department has the highest number of accidents (265), followed by technical (195) and support (174). Most accidents occurred among employees with low (47.95%) and medium salaries (43.2%), while high-salary employees are the least affected (8.85%).")
              st.write("\* Sales, technical, and support departments show a high correlation between workplace accidents and employee turnover.")
              st.write("\* Departments like sales and technical show higher accident counts with longer employee tenure. Shorter-tenured departments (e.g., marketing and IT) exhibit fewer accidents.")
              st.write("\* Employees involved in accidents show lower satisfaction levels compared to others.")

        with six:
           panel = st.container(height=1450, border=True)
           with panel:
              st.image("HR6 Promotion.jpg")
              st.write("This report visualizes key metrics related to employee promotions over the last five years. Here's an analysis of each section:")
              st.write("\* Only 2.13% of employees were promoted (0.32K), while 97.87% (14.68K) were not promoted.Promotions are rare, indicating either a highly selective process or limited opportunities for promotion.")
              st.write("\* Employees with medium salaries saw the highest promotion rate (56.74%, 181 employees, High-salary employees followed at 22.57% (72 employees). Employees with low salaries were least likely to be promoted (20.69%, 66 employees). This suggests a potential bias toward mid-salary employees for promotions.")
              st.write("\* Employees with higher satisfaction levels (e.g., 0.71-0.8) had higher promotion rates (59 promotions). Lower satisfaction levels (e.g., 0-0.1) corresponded to minimal promotions. Satisfaction may be a contributing factor in promotion decisions, possibly reflecting better performance or attitude.")
              st.write("\* The Sales department leads with the most promotions (100), followed by Management (69) and Marketing (43). Departments like IT (3) and Product Management (0) had very few or no promotions, indicating disparities in promotion opportunities across departments.")
              st.write("\* Most promotions (94.04%, 300 employees) were given to those who stayed with the company. Only 5.96% (19 employees) of promotions went to those who eventually left. This indicates the company prioritizes retention when promoting.")
              st.write("\* Employees without work accidents had a significantly higher promotion rate (76.18%, 243 employees). Those who had work accidents were less likely to be promoted (23.82%, 76 employees). This could indicate a preference for employees with consistent performance and no interruptions due to accidents.")

        st.markdown(":female-office-worker: [HR Data Analysis](https://github.com/SantoshRottayyanavar/HR-Data-Analysis)")

elif choice == "Resume":
    with open("Santosh Rottayyanavarmath (Resume).pdf", "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="Santosh Rottayyanavarmath (Resume).pdf",
            mime="text/pdf"
        )
    pdf_viewer("Santosh Rottayyanavarmath (Resume).pdf")

elif choice == "Contact":
    st.markdown("### :handshake: Get in Touch")
    st.write("")
    st.text("Feel free to reach out to me! trough")
    st.write("")
    
    st.markdown("santoshrottayyanavar81@gmail.com")
    social_media_links = [
        "https://www.linkedin.com/in/santosh-rottayyanavar-/",
        "https://github.com/SantoshRottayyanavar",
    ]

    social_media_icons = SocialMediaIcons(social_media_links)

    social_media_icons.render()
   
    
    st.write("---")

    #Contact form
    st.markdown("### :postbox: Message Box")
    st.write("write to me for any collaborations / Suggestions to improve")
    
     # google sheets connection
    if 'conn' not in st.session_state:
        st.session_state.conn = st.connection("gsheets", type=GSheetsConnection)

    if "Message_df" not in st.session_state:
        st.session_state.Message_df = st.session_state.conn.read(worksheet="Feedback")
      
    if "msg_df" not in st.session_state:
       st.session_state.msg_df = pd.DataFrame()

    with st.form(key="contact_form", clear_on_submit=True):
        name = st.text_input("Name")
        email = st.text_input("Email")
        text = st.text_area("Message")
        col1, col2, col3, col4 = st.columns(4)
        submit_button = col4.form_submit_button("Send")

        if submit_button:
            if (name == "") or (email == "") or (text == ""):
                st.error("Please fill all the fields")
            else:
                st.success(f"Thank you, {name}! I'll get back to you soon if any.")
                
                message = [{"Name": name,
                            "Mail ID": email,
                            "Message": text}]
                
                st.session_state.msg_df = pd.DataFrame(message)
                st.session_state.Message_df = pd.concat([st.session_state.Message_df, st.session_state.msg_df], ignore_index = True)
                st.session_state.conn.update(worksheet="Feedback", data=st.session_state.Message_df)

    