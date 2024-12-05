import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(page_title="SantoshRottayyanavar", layout="wide", page_icon="👨🏻‍💼")

page_bg_image = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://img.freepik.com/free-vector/gradient-technological-background_23-2148884155.jpg?t=st=1733391602~exp=1733395202~hmac=c4cd328b8d7b8432c36f96c17ac394b9acd385ffa6946b2c74839a5657108ae5&w=1060");
background-size: cover; 
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

# name, first, second, third, fourth, fifth = st.columns([3,1,1,1,1,1])
# name.title("Santosh")
#   
     
if choice == "Home":    
    st.write("")
    into, image = st.columns([10,4])
    into.markdown("<H2 style = 'text-align: center;'>Hi, </h2>", unsafe_allow_html=True)
    into.markdown("<H2 style = 'text-align: center;'>I'm Santosh Rottayyanavar </h2>", unsafe_allow_html=True)
    into.markdown("<H5 style = 'text-align: center;'>Help discovering insights from data to make better and informed business decisions.</h5>", unsafe_allow_html=True)

    image.image("Santosh Photo.png")
    st.write("")
    st.write("---") 
    st.write("")

    collect, stats, process = st.columns(3)
    
    collect.markdown("#### :basket: Collect")
    collect.write("A Data Analyst collects, cleans, and organizes raw data from various sources to uncover patterns and trends. They use tools like SQL, Python, Excel, or Tableau to process and visualize data. Analysts interpret insights to support decision-making and improve business strategies. They ensure data accuracy and create reports for stakeholders.")
    
    stats.markdown("#### :1234: Stats")
    stats.write("A Data Analyst uses statistics to summarize data with measures like mean and standard deviation. They perform hypothesis testing to validate assumptions and explore relationships. Regression models are used to predict outcomes and identify key factors. Probability analysis helps estimate risks and forecast trends for decision-making.")
    
    process.markdown("#### :white_check_mark: Process")
    process.write("A Data Analyst processes raw data by collecting it from various sources and cleaning it to ensure accuracy and quality. They analyze the data using tools like SQL, Python, or Excel to uncover trends and patterns. Visualization tools like Power BI or Tableau are used to create interactive dashboards and reports. The insights are then shared with stakeholders to support data-driven decisions.")
    
    modelling, visualize = st.columns(2)
    
    modelling.markdown("#### :snowflake: Modelling")
    modelling.write("Modeling a fact and dimension involves creating a fact table that contains measurable data, such as sales revenue, along with foreign keys linking to related dimension tables. Dimension tables provide descriptive attributes, like customer information or product details, enhancing the context of the data. Relationships are established to ensure that each dimension is connected to the fact table, typically in a star or snowflake schema. This structure facilitates efficient querying and analysis of business metrics.")
    
    visualize.markdown("#### :bar_chart: Visualize")
    visualize.write("Data visualization is the graphical representation of data that helps communicate insights clearly and effectively. It includes various types, such as bar charts, line graphs, and dashboards, tailored to highlight trends and patterns. Tools like Tableau, Power BI, and Matplotlib enable the creation of interactive visuals. Effective visualizations use best practices to enhance comprehension and support data-driven decision-making.")

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
     select = st.selectbox("Internships", ["Bank Loan Analysis", "HR Analysis", "Sales Analysis"])   
     
     if select == "Bank Loan Analysis":
        one, two = st.columns([1,1])
        one.image("Bank Loan Applications.png")
        two.image("Bank Loan Defaulters.png")
        three, four = st.columns([1,1])
        three.image("Bank Loan repayers.png")
        four.image("Bank Loan credit, good price and income correlations.png")
        five, six = st.columns([1,1])
        five.image("Bank Loan Comprehensive financial overview.png")
        six.image("Bank Loan Comprehensive financial overview2.png")
        seven, eight = st.columns([1,1])
        seven.image("Bank Loan Privious application status based on applicants.png")

     elif select == "HR Analysis":
        a1,b1 = st.columns(2)
        a1.image("HRmain.jpg")

        one, two = st.columns([1,1])
        one.image("HR1 Employee_distribution.jpg")
        two.image("HR2Employee Avg Monthly Hrs and satisfaction.jpg")
        
        three, four = st.columns([1,1])
        three.image("HR3 Employees Precence.jpg")
        four.image("HR4 Turnover Rate.jpg")
        
        five, six = st.columns([1,1])
        five.image("HR5 Workplace Accident.jpg")
        six.image("HR6 Promotion.jpg")

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
    col1, col2, col3 = st.columns(3)
    col1.markdown(":email: Mail: santoshrottayyanavar81@gmail.com")
    col2.markdown(":chains: [my LinkedIn](https://www.linkedin.com/in/santosh-rottayyanavar-/)")
    col3.markdown(":smile_cat: [My Github](https://github.com/SantoshRottayyanavar)")
    st.write("---")


