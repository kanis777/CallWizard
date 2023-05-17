import streamlit as st

# ----------------------------------------------------------------------------------------------------------------------------------------
# About the Webpage
# ------------------
st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:65px'>About the Webpage</h1>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style=' font-size:20px'>We are living in a world where the use of mobile phones is increasing rapidly. It has become an integral part of our life. With the ever-increasing number of smartphone companies, it difficult for a user to choose the best one. To make this task easier, it is necessary to have data about the phones that can be used for comparison purposes. GSMArena is one of the biggest websites that provide information about mobile phones. It has been providing information about mobile phones for more than 10 years. This data can be used to analyze the features and prices of mobile phones </p>", unsafe_allow_html=True)


st.markdown("<br><hr>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------------------------------------------------------------------
# About the Project
# ------------------
st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:65px'>About the Project</h1>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Main Features", "Libraries", "References"])
with tab1:
   
   st.markdown("""<ul>  
                        <li>Dataset is obtained through Web Scraping</li>
                        <li>Data Cleaning</li>
                        <li>Data Wrangling</li>
                        <li>User Interface (Website)</li>                      
                        <li>Data Visualisation</li>
                        <li>Dashboard PowerBI</li>
                        <li>Predicting price of New Launch </li>    
                                                                      </ul> """, unsafe_allow_html=True) 
with tab2:
   st.markdown("""<ul>  
                        <li>Numpy</li>
                        <li>Pandas</li>
                        <li>BeautifulSoup</li>
                        <li>Requests</li>
                        <li>CSV</li>
                        <li>Streamlit</li>
                                          </ul> """, unsafe_allow_html=True) 
with tab3:
   st.markdown("""<ul>  
                        <li>GeekforGeeks</li>
                        <li>Streamlit Documentation</li>
                        <li>Towards Data Science</li>
                        <li>Freecodecamp</li>
                        <li>Bootstrap Icons</li>
                        <li>Towards Data Science</li>
                        <li>Coding is Fun - Youtube</li>
                                          </ul> """, unsafe_allow_html=True) 


st.markdown("<br><hr>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------------------------------------------------------------------
