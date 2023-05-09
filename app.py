import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects
import base64
from streamlit_option_menu import option_menu
from PIL import Image
import webbrowser
import mysql.connector
from plotly.offline import plot
import plotly.io as pio
import ast
from babel.numbers import format_currency
from urllib.request import urlopen
import json
import plotly.graph_objects as go




                                        #DATABASE CONNECTION
mydb=mysql.connector.connect(host='localhost',user='root',password='3915')
mycurser=mydb.cursor()
mycurser.execute('use phonepepulse')


st.set_page_config(page_title='Phonepe Pulse',page_icon='./Icon/phonepeico.png',layout='wide')



# Background Image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )
add_bg_from_local('Images/bg.jpg')


head1,head2=st.columns([0.18,3])
with head1:
    image = Image.open('./Images/logo.png')
    st.image(image, width=60)
with head2:
    tit1,tit2=st.columns([0.456,2])
    with tit1:
        st.markdown("<h2 style= 'color: white;font-size: 34px;'>PhonePe Pulse  |</h2>", unsafe_allow_html=True)
    with tit2:
        st.markdown("<h2 style= 'color: #9932CC;font-weight: normal;font-size: 34px;'>The Best of Progress</h2>", unsafe_allow_html=True)
st.write('')
st.write('')
st.write('')
left,optioncontainer,right=st.columns([0.2,3,0.2])

with optioncontainer:
    selected=option_menu(menu_title='', options=['Home','Geo','Visualization'],icons=['house','globe2','graph-up-arrow'],orientation='horizontal',styles={
            "container": { "background-color": "#480668"},
            "icon": {"color": "orange", "font-size": "18px"},
            "nav-link": {"font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "#391C59"},
            "nav-link-selected": {"background-color": "#691592"}  })
st.write('')
st.write('')
st.write('')

if selected=='Home':
    st.title('PhonePe Pulse')
    st.write('')
    st.write('')
    textcon,mid,imgcon=st.columns([4,0.4,1])
    with textcon:
        st.markdown('''<p style= 'color: white;font-size: 16px;text-align: justify;'>
        Founded in December 2015, PhonePe has become a homegrown success story, with its meteoric growth powered by India’s emerging digital ecosystem, particularly in the Unified Payments
        Interface (UPI) space. The company builds products and offerings tailored for the Indian market and has emerged as India’s largest payments app, enabling digital inclusion for consumers and merchants alike. With 380 million registered users, one in four Indians are
        now on PhonePe. The company has also successfully digitized over 30 million offline merchants spread across Tier 2,3,4 and beyond, covering 99% pin codes in the country. PhonePe is proud
        to help lead India’s country-wide digitization efforts and believes that this powerful public-private collaboration has made the Indian digital ecosystem a global exemplar. Pulse is a notel interactive
        platform that is India's go-to destination for accurate and comprehensive data on digital payment trends.</p>''', unsafe_allow_html=True)

    with imgcon:
        image=Image.open('Images/PP img.jpg')
        st.image(image,width=250)

    st.title('Data APIs')
    st.write('')
    st.write("""
    This data has been structured to provide details on data cuts of Transactions and Users on the Explore tab.
    """)
    st.write('')
    aggcol,mapcol,topcol=st.columns([1.7,1,1])
    with aggcol:
        st.subheader('Aggregated')
        st.write('')
        st.write('Aggregated values of various payment categories as shown under Categories section')
        st.write('')
    with mapcol:
        st.subheader('Map')
        st.write('')
        st.write('Total values at the State and District levels')
        st.write('')
    with topcol:
        st.subheader('Top')
        st.write('')
        st.write('Totals of top States / Districts / Pin Codes')
        st.write('')
    st.write('')
    st.title('GitHub')
    st.write('')
    st.write('A home for the data that powers the PhonePe Pulse website.')
    st.write('')
    url = 'https://github.com/PhonePe/pulse#readme'

    if st.button('GitHub'):
        webbrowser.open_new_tab(url)



                                               #GEO
if selected=='Geo':
    col1,col3, col2 = st.columns([1.8,0.22, 1])
    with col1:
        st.subheader('All India')
        st.write('')
        optcol,yearcol,qurcol,noncol=st.columns([0.5,0.2,0.2,0.1])
        with optcol:
            option=st.selectbox(label='',options=['Transaction','Users'])
        with yearcol:
            year=st.selectbox(label='',options=['2018','2019','2020','2021','2022'])
        with qurcol:
            quartile=st.selectbox(label='',options=['1','2','3','4'])
        with noncol:
            st.write('')
        if option=='Transaction':

            st.markdown("<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 48px;'><b>Transaction Map</b></h2>",unsafe_allow_html=True)

            select = 'select * from phonepepulse.Maptran where year={} and quarter={} '.format(year, quartile)
            mycurser.execute(select)
            result = mycurser.fetchall()
            maptranstate = []
            for i in (result):
                maptranstate.append(i[1:4])
            statenamelst=[]
            statecountlst=[]
            stateamountlst=[]
            for i in maptranstate:
                    statenamelst.append(i[0])
                    statecountlst.append(i[1])
                    stateamountlst.append(i[2])


            lat=[11.93499371,12.92038576,27.59998069,21.30039105,14.7504291,23.83540428,10.56257331,24.79997072,19.25023195,20.26657819,25.57049217,11.66702557,28.45000633,26.44999921,34.209515,31.51997398,26.7499809,23.80039349,19.82042971,25.78541445,8.900372741,12.57038129,30.71999697,17.123184,31.10002545,22.58039044,22.309425,27.3333303,25.6669979,23.71039899,22.09042035,34.29995933,15.491997,27.10039878,28.6699929,30.157352]
            log=[79.83000037,79.15004187,78.05000565,76.13001949,78.57002559,91.27999914,72.63686717,93.95001705,73.16017493,73.0166178,91.8800142,92.73598262,77.01999101,73.432617,77.615112,75.98000281,94.21666744,86.41998572,85.90001746,87.4799727,76.56999263,76.91999711,76.78000565,79.208824,77.16659704,88.32994665,72.136230,88.6166475,94.11657019,92.72001461,82.15998734,74.46665849,73.81800065,93.61660071,77.23000403,78.324478]

            df = pd.DataFrame({'lat':lat,'lon':log, 'statenamelst': statenamelst,'count':statecountlst,'amount':stateamountlst})
            df['count'] = df['count'].astype('int64')
            df['amount'] = df['amount'].astype('int64')
            fig = px.scatter_geo(df,size='count',lat='lat',lon='lon',color='count',hover_name='statenamelst'
                                 ,hover_data=(['count','amount']),scope='asia',size_max=20,width=800,height=800,color_continuous_scale=["orange", "yellow", "red"])
            fig.update_geos(visible=False, resolution=50, scope="asia",
                showcountries=True, countrycolor="Black",
                showsubunits=True, subunitcolor="black",fitbounds='locations',showland=True,landcolor='rgb(153,50,204)')
            fig.update_layout(
                {'plot_bgcolor': 'rgb(34,13,56)', 'paper_bgcolor': 'rgb(34,13,56)',},margin={"r":0,"t":0,"l":0,"b":0},coloraxis_colorbar=dict(
        len=0.5,
        xanchor="right", x=0.97,
        yanchor='bottom', y=0.28,
        thickness=20,
    )
            )
            fig.add_trace(go.Scattergeo(lon=df["lon"],
                                        lat=df["lat"],
                                        text=df["statenamelst"],
                                        textposition="middle center",
                                        mode='text',
                                        showlegend=False,opacity=0.6))
            fig.update_traces(marker=dict(symbol="octagon",
                                          line=dict(width=2.4,
                                                    color='black')),
                              selector=dict(mode='markers'))

            st.plotly_chart(fig)



        elif option=='Users':
            st.markdown("<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 48px;'><b>Users Map</b></h2>",unsafe_allow_html=True)

            select = 'select * from phonepepulse.mapuser where year={} and quarter={} '.format(year, quartile)
            mycurser.execute(select)
            result = mycurser.fetchall()
            mapuserstate = []
            mapuserstatenamelst=[]
            mapuserregistelst=[]
            mapuserappopenlst=[]
            for i in (result):
                mapuserstate.append(i[1:4])
            for i in mapuserstate:
                mapuserstatenamelst.append(i[0])
                mapuserregistelst.append(i[1])
                mapuserappopenlst.append(i[2])

            lat = [11.93499371, 12.92038576, 27.59998069, 21.30039105, 14.7504291, 23.83540428, 10.56257331,
                   24.79997072, 19.25023195, 20.26657819, 25.57049217, 11.66702557, 28.45000633, 26.44999921, 34.209515,
                   31.51997398, 26.7499809, 23.80039349, 19.82042971, 25.78541445, 8.900372741, 12.57038129,
                   30.71999697, 17.123184, 31.10002545, 22.58039044, 22.309425, 27.3333303, 25.6669979, 23.71039899,
                   22.09042035, 34.29995933, 15.491997, 27.10039878, 28.6699929, 30.157352]
            log = [79.83000037, 79.15004187, 78.05000565, 76.13001949, 78.57002559, 91.27999914, 72.63686717,
                   93.95001705, 73.16017493, 73.0166178, 91.8800142, 92.73598262, 77.01999101, 73.432617, 77.615112,
                   75.98000281, 94.21666744, 86.41998572, 85.90001746, 87.4799727, 76.56999263, 76.91999711,
                   76.78000565, 79.208824, 77.16659704, 88.32994665, 72.136230, 88.6166475, 94.11657019, 92.72001461,
                   82.15998734, 74.46665849, 73.81800065, 93.61660071, 77.23000403, 78.324478]

            df = pd.DataFrame({'lat': lat, 'lon': log, 'statenamelst': mapuserstatenamelst, 'registered': mapuserregistelst,'appopens':mapuserappopenlst})
            df['lat']=df['lat'].astype('float')
            df['lon'] = df['lon'].astype('float')
            df['registered'] = df['registered'].astype('int64')
            df['appopens']=df['appopens'].astype('int64')

            fig = px.scatter_geo(df, size='registered', lat='lat', lon='lon', color='registered', hover_name='statenamelst'
                                 ,hover_data=(['registered','appopens']),scope='asia', size_max=20, width=800, height=800,
                                 color_continuous_scale=["orange", "yellow", "red"],opacity=0.79)

            fig.update_geos(visible=False, resolution=50, scope="asia",
                            showcountries=True, countrycolor="Black",
                            showsubunits=True, subunitcolor="black", fitbounds='locations', showland=True,
                            landcolor='rgb(153,50,204)')
            fig.update_layout(
                {'plot_bgcolor': 'rgb(34,13,56)', 'paper_bgcolor': 'rgb(34,13,56)', },
                margin={"r": 0, "t": 0, "l": 0, "b": 0},coloraxis_colorbar=dict(
        len=0.5,
        xanchor="right", x=0.97,
        yanchor='bottom', y=0.28,
        thickness=20,
    )
            )
            fig.add_trace(go.Scattergeo(lon=df["lon"],
                                        lat=df["lat"],
                                        text=df["statenamelst"],
                                        textposition="middle center",
                                        mode='text',
                                        showlegend=False, opacity=0.6))

            fig.update_traces(marker=dict(symbol="octagon",
                                          line=dict(width=2.4,
                                                    color='black')),
                              selector=dict(mode='markers'))

            st.plotly_chart(fig)

    with col2:
        if option=='Transaction':
            qurt = quartile
            select = 'select * from phonepepulse.Aggtran where year={} and quartile={}'.format(year, qurt)
            mycurser.execute(select)
            result = mycurser.fetchall()
            allpptran = 0
            total = 0
            catekey=[]
            cateval=[]
            for i in result:
                allpptran += i[2]
                total += int(i[3])
                catekey.append(i[1])
                cateval.append((i[2]))
            avg =int(total/allpptran)

            st.markdown("<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 38px;'><b>Transaction</b></h2>",unsafe_allow_html=True)
            st.write('')
            st.markdown("<h2 style= 'color: white;font-weight: normal;font-size: 18px;'><b>All PhonePe Transaction(UPI+Cards+Wallets)</b></h2>",unsafe_allow_html=True)
            amount=format_currency(allpptran, 'INR', locale='en_IN')[:-3]
            tot=format_currency(total, 'INR', locale='en_IN')[:-3]
            average=format_currency(avg, 'INR', locale='en_IN')[:-3]
            st.markdown(r"<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 40px;'><b>{}</b></h2>".format(amount),unsafe_allow_html=True)
            st.write('')
            totcol,avgcol=st.columns([1.5,1])
            with totcol:
                st.markdown("<h2 style= 'color: white;font-weight: normal;font-size: 18px;'><b>Total payment value</b></h2>",unsafe_allow_html=True)
                st.markdown(r"<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 24px;'><b>{} Cr</b></h2>".format(tot),unsafe_allow_html=True)
            with avgcol:
                st.markdown("<h2 style= 'color: white;font-weight: normal;font-size: 18px;'><b>Avg. transaction value</b></h2>",unsafe_allow_html=True)
                st.markdown(r"<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 24px;'><b>{}</b></h2>".format(average), unsafe_allow_html=True)
            st.write('')
            st.subheader('Categories')
            st.write('')
            keycate,valcate=st.columns([1.5,1])
            with keycate:
                for i in range(5):
                    st.markdown(
                        "<h2 style= 'color: white;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(catekey[i]),
                        unsafe_allow_html=True)
            st.write('')
            with valcate:
                for i in range(5):
                    st.markdown(
                        "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(format_currency(cateval[i], 'INR', locale='en_IN')[1:-3]),
                        unsafe_allow_html=True)
            st.write('#')
            #selecttop = st.selectbox(label='Top 10 Records ', options=['States', 'Districts', 'Pincodes'])
            selecttop=option_menu(menu_title='' ,icons=['bar-chart-line','bar-chart','bar-chart-line-fill'], options=['States','Districts','Pincodes'],orientation='horizontal',styles={
            "container": { "background-color": "#480668"},
            "icon": {"color": "orange", "font-size": "18px"},
            "nav-link": {"font-size": "12px", "text-align": "left", "margin":"0px", "--hover-color": "#391C59"},
            "nav-link-selected": {"background-color": "#691592"}  })
            st.write('')
            select = 'select * from phonepepulse.toptran where year={} and quartile={} '.format(year, quartile)
            mycurser.execute(select)
            result = mycurser.fetchall()
            totlst = []
            topstateamount = []
            topdistamount = []
            toppinamount = []
            for i in result:
                totlst.append(i[1:5])
            for i in totlst:
                if 'state' in i:
                    topstateamount.append(i)
                elif 'district' in i:
                    topdistamount.append(i)
                elif 'pincode' in i:
                    toppinamount.append(i)
            if selecttop == 'States':
                st.subheader('Top 10 States')
                st.write('')
                statekey,stateval=st.columns([1,1])
                with statekey:
                    for i in range(0,10):
                        st.markdown(
                            "<h2 style= 'color: white;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(topstateamount[i][0].title()),
                            unsafe_allow_html=True)
                with stateval:
                    for i in range(0,10):
                        st.markdown(
                            "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(format_currency(topstateamount[i][1].title(), 'INR', locale='en_IN')[1:-3]),
                            unsafe_allow_html=True)
            elif selecttop == 'Districts':
                st.subheader('Top 10 Districts')
                st.write('')
                diskey,disval=st.columns([1,1])
                with diskey:
                    for i in range(0,10):
                        st.markdown(
                            "<h2 style= 'color: white;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(topdistamount[i][0].title()),
                            unsafe_allow_html=True)
                with disval:
                    for i in range(0,10):
                        st.markdown(
                            "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(format_currency(topdistamount[i][1].title(), 'INR', locale='en_IN')[1:-3]),
                            unsafe_allow_html=True)
            else:
                st.subheader('Top 10 Pincodes')
                st.write('')
                pinkey,pinval=st.columns([1,1])
                with pinkey:
                    for i in range(0,10):
                        st.markdown(
                            "<h2 style= 'color: white;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(toppinamount[i][0].title()),
                            unsafe_allow_html=True)
                with pinval:
                    for i in range(0,10):
                        st.markdown(
                            "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(format_currency(toppinamount[i][1].title(), 'INR', locale='en_IN')[1:-3]),
                            unsafe_allow_html=True)

        else:
            st.markdown("<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 38px;'><b>Users</b></h2>",unsafe_allow_html=True)

            select = 'select * from phonepepulse.Agguser where year={} and quartile={}'.format(year, quartile)
            mycurser.execute(select)
            result = mycurser.fetchall()
            for i in result:
                registereduser=i[1]
                appopen=i[2]
            #st.write(f'Registered PhonePe users till Q{quartile} {year}'.format(quartile,year))
            st.markdown("<h2 style= 'color: white;font-weight: normal;font-size: 18px;'><b>Registered PhonePe users till Q{} {}</b></h2>".format(quartile,year),unsafe_allow_html=True)
            st.markdown(r"<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 40px;'><b>{}</b></h2>".format(format_currency(registereduser,'INR', locale='en_IN')[1:-3]),unsafe_allow_html=True)
            st.markdown("<h2 style= 'color: white;font-weight: normal;font-size: 18px;'><b>PhonePe app opens in Q{} {}</b></h2>".format(quartile,year),unsafe_allow_html=True)
            if appopen!='0':
                st.markdown(r"<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 40px;'><b>{}</b></h2>".format(format_currency(appopen,'INR', locale='en_IN')[1:-3]),unsafe_allow_html=True)
                st.write('')
            elif appopen=='0':
                st.markdown(r"<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 40px;'><b>Unavailable</b></h2>", unsafe_allow_html=True)
            st.write('#')

            #selecttop=st.selectbox(label='Top 10 Records',options=['States','Districts','Pincodes'])
            selecttop = option_menu(menu_title='',icons=['bar-chart-line','bar-chart','bar-chart-line-fill'], options=['States', 'Districts', 'Pincodes'],
                                    orientation='horizontal', styles={
                    "container": {"background-color": "#480668"},
                    "icon": {"color": "orange", "font-size": "18px"},
                    "nav-link": {"font-size": "12px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "#391C59"},
                    "nav-link-selected": {"background-color": "#691592"}})
            select = 'select * from phonepepulse.topuser where year={} and quartile={}'.format(year, quartile)
            mycurser.execute(select)
            result = mycurser.fetchall()
            userlst = []
            userstateamount = []
            userdistamount = []
            userpinamount = []
            for i in result:
                userlst.append(i[1:5])
            for i in userlst:
                if 'state' in i:
                    userstateamount.append(i)
                elif 'district' in i:
                    userdistamount.append(i)
                elif 'pincode' in i:
                    userpinamount.append(i)

            if selecttop=='States':
                st.subheader('Top 10 States')
                st.write('')
                stateusekey,stateuseval=st.columns([1,1])
                with stateusekey:
                    for i in range(0, 10):
                        st.markdown(
                            "<h2 style= 'color: white;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                                userstateamount[i][0].title()),
                            unsafe_allow_html=True)
                with stateuseval:
                    for i in range(0, 10):
                        st.markdown(
                            "<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                                format_currency(userstateamount[i][1].title(), 'INR', locale='en_IN')[1:-3]),
                            unsafe_allow_html=True)


            elif selecttop=='Districts':
                st.subheader('Top 10 Districts')
                st.write('')
                disusekey,disuseval=st.columns([1,1])
                with disusekey:
                    for i in range(0,10):
                        st.markdown(
                            "<h2 style= 'color: white;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                                userdistamount[i][0].title()),
                            unsafe_allow_html=True)
                with disuseval:
                    for i in range(0,10):
                        st.markdown(
                            "<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                                format_currency(userdistamount[i][1].title(), 'INR', locale='en_IN')[1:-3]),
                            unsafe_allow_html=True)

            else:
                st.subheader('Top 10 Pincodes')
                st.write('')
                pinuserkey,pinuserval=st.columns([1,1])
                with pinuserkey:
                    for i in range(0,10):
                        st.markdown(
                            "<h2 style= 'color: white;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                                userpinamount[i][0].title()),
                            unsafe_allow_html=True)
                with pinuserval:
                    for i in range(0,10):
                        st.markdown(
                            "<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 18px;'><b>{}</b></h2>".format(
                                format_currency(userpinamount[i][1].title(), 'INR', locale='en_IN')[1:-3]),
                            unsafe_allow_html=True)




                                                    #DASHBOARD
if selected=='Visualization':
    sel1,sel2,sel3=st.columns([1,3,1])
    with sel1:
        st.write('')
    with sel2:
        titleft, titmid, titrgt = st.columns([1.8, 3, 1])
        with titmid:
            st.subheader('Select Your Choice')
        #visselection=st.selectbox('',['Transaction','Users','Top 10 ( State ,District ,Pincode )','Mobile Brand'])
        visselection=option_menu(menu_title='',icons=['send','people-fill','sort-numeric-up','phone-fill'], options=['Transaction', 'Users', 'Top 10','Mobile Brand'],
                                    orientation='horizontal', styles={
                    "container": {"background-color": "#480668"},
                    "icon": {"color": "orange", "font-size": "18px"},
                    "nav-link": {"font-size": "12px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "#391C59"},
                    "nav-link-selected": {"background-color": "#691592"}})
    with sel3:
        st.write('')
    st.write('')
    st.write('')
    rightcon,midcol,leftcon=st.columns([2,0.5,1.3])
    st.write('')
    with rightcon:
        if visselection=='Transaction':
            st.markdown(
                "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 48px;'><b>Transaction</b></h2>",
                unsafe_allow_html=True)
            st.write('')
            leftcon1,leftcon2=st.columns([2,1])
            with leftcon1:
                transelect=st.selectbox('',['All PhonePe Transaction','Total Payment','Average Transaction'])
            with leftcon2:
                selectedyear = st.selectbox('', ['2018', '2019', '2020', '2021', '2022'])

            def fetchalltransaction(tranyear):
                alltranlst = []
                totalamtlst=[]
                paymentmethod=[]
                totaltran = 0
                totalamt=0
                for i in range(1, 5):
                    select1 = 'select * from phonepepulse.Aggtran where year={} and quartile={}'.format(tranyear, i)
                    mycurser.execute(select1)
                    result = mycurser.fetchall()
                    for i in result:
                        totaltran += i[2]
                        totalamt+=int(i[3])
                        paymentmethod.append(i[1:])
                    alltranlst.append(totaltran)
                    totalamtlst.append(totalamt)
                    totaltran = 0
                    totalamt=0
                return alltranlst,totalamtlst,paymentmethod

            if transelect=='All PhonePe Transaction':
                Alltransaction,tot,paymenttype1=fetchalltransaction(selectedyear)
                Alltransactionqrt=['Q1','Q2','Q3','Q4']
                Alltransactionamt={Alltransaction[0],Alltransaction[1],Alltransaction[2],Alltransaction[3]}
                trandf=pd.DataFrame([Alltransactionqrt,Alltransactionamt],index=['Quarter','All Transaction']).T
                st.write('')
                st.write('')
                st.write('')
                st.markdown(
                    "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 38px;'><b>All PhonePe Transaction</b></h2>",
                    unsafe_allow_html=True)
                st.write('')
                fig=px.funnel(trandf,x='Quarter',y='All Transaction',color='Quarter',height=500)
                fig.update_traces( textposition='outside')
                fig.update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                )
                st.plotly_chart(fig)
                ptq1 = []
                ptq2 = []
                ptq3 = []
                ptq4 = []
                ptq5 = []
                for i in paymenttype1:
                    if 1 in i:
                        ptq1.append(i)
                    elif 2 in i:
                        ptq2.append(i)
                    elif 3 in i:
                        ptq3.append(i)
                    elif 4 in i:
                        ptq4.append(i)
                    elif 5 in i:
                        ptq5.append(i)
                ptname1 = []
                ptcount1 = []
                ptname2 = []
                ptcount2 = []
                ptname3 = []
                ptcount3 = []
                ptname4 = []
                ptcount4 = []
                pq1 = []
                pq2 = []
                pq3 = []
                pq4 = []
                for i in range(5):
                    ptname1.append(ptq1[i][0])
                    ptcount1.append(ptq1[i][1])
                    pq1.append(ptq1[i][-1])
                for i in range(5):
                    ptname2.append(ptq2[i][0])
                    ptcount2.append(ptq2[i][1])
                    pq2.append(ptq2[i][-1])
                for i in range(5):
                    ptname3.append(ptq3[i][0])
                    ptcount3.append(ptq3[i][1])
                    pq3.append(ptq3[i][-1])
                for i in range(5):
                    ptname4.append(ptq4[i][0])
                    ptcount4.append(ptq4[i][1])
                    pq4.append(ptq4[i][-1])
                dicq1 = {'Type': ptname1, 'Count': ptcount1, 'Quartile': pq1}
                dicq2 = {'Type': ptname2, 'Count': ptcount2, 'Quartile': pq2}
                dicq3 = {'Type': ptname3, 'Count': ptcount3, 'Quartile': pq3}
                dicq4 = {'Type': ptname4, 'Count': ptcount4, 'Quartile': pq4}
                df1 = pd.DataFrame(dicq1)
                df2 = pd.DataFrame(dicq2)
                df3 = pd.DataFrame(dicq3)
                df4 = pd.DataFrame(dicq4)
                pie1, pie2 = st.columns([1, 1])
                with pie1:
                    st.markdown(
                        "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 32px;'><b>1st Quarter</b></h2>",
                        unsafe_allow_html=True)
                    fig1 = px.pie(df1, values='Count', names='Type', labels='Type', hole=.4, height=500, width=400)
                    fig1.update_layout(
                        {'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',}
                    )
                    st.plotly_chart(fig1)
                    st.markdown(
                        "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 32px;'><b>3rd Quarter</b></h2>",
                        unsafe_allow_html=True)
                    fig2 = px.pie(df3, values='Count', names='Type', labels='Type', hole=.4, height=500, width=400)
                    fig2.update_layout(
                        {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                    )
                    st.plotly_chart(fig2)

                with pie2:
                    st.markdown(
                        "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 32px;'><b>2nd Quarter</b></h2>",
                        unsafe_allow_html=True)
                    fig1 = px.pie(df2, values='Count', names='Type', labels='Type', hole=.4, height=500, width=400)
                    fig1.update_layout(
                        {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                    )
                    st.plotly_chart(fig1)
                    st.markdown(
                        "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 32px;'><b>4th Quarter</b></h2>",
                        unsafe_allow_html=True)
                    fig2 = px.pie(df4, values='Count', names='Type', labels='Type', hole=.4, height=500, width=400)
                    fig2.update_layout(
                        {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                    )
                    st.plotly_chart(fig2)

            elif transelect=='Total Payment':
                Alltran,totalpayment,paymenttype2=fetchalltransaction(selectedyear)
                totaltranqrt = ['Q1', 'Q2', 'Q3', 'Q4']
                Alltransactionamt = {totalpayment[0], totalpayment[1], totalpayment[2], totalpayment[3]}
                trandf = pd.DataFrame([totaltranqrt, Alltransactionamt], index=['Quarter', 'Total Payments']).T
                st.write('')
                st.write('')
                st.write('')
                st.markdown(
                    "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 38px;'><b>Total Payment</b></h2>",
                    unsafe_allow_html=True)

                st.write('')
                fig = px.funnel(trandf, x='Quarter', y='Total Payments',color='Quarter')
                fig.update_traces( textposition='outside')
                fig.update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                )
                st.plotly_chart(fig)

            elif transelect=='Average Transaction':
                avgtran,avgpay,paymenttype3=fetchalltransaction(selectedyear)
                avglst=[]
                for i in range(4):
                    avglst.append(avgpay[i]/avgtran[i])
                avgqrt = ['Q1', 'Q2', 'Q3', 'Q4']
                trandf = pd.DataFrame([avgqrt, avglst], index=['Quarter', 'Average Transaction']).T
                st.write('')
                st.write('')
                st.write('')
                st.markdown(
                    "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 38px;'><b>Average Transaction</b></h2>",
                    unsafe_allow_html=True)
                st.write('')
                fig = px.bar(trandf, x='Quarter', y='Average Transaction',text='Average Transaction',color='Quarter')
                fig.update_traces(textposition='outside')
                fig.update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                )
                st.plotly_chart(fig)

        elif visselection=='Users':
            st.markdown(
                "<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 48px;'><b>Users</b></h2>",
                unsafe_allow_html=True)

            def fetchregistereduser(useryear,userqrt):
                mapuserstate = []
                select = 'select * from phonepepulse.mapuser where year={} and quarter={} '.format(useryear,userqrt )
                mycurser.execute(select)
                result = mycurser.fetchall()
                for i in (result):
                    mapuserstate.append(i)
                return mapuserstate

            leftcon1,leftcon2, leftcon3 = st.columns([2, 1,1])
            with leftcon1:
                userselect=st.selectbox('',['Registered Phonepe','App Opens'])
            with leftcon2:
                selectedyear = st.selectbox('', ['2018', '2019', '2020', '2021', '2022'])
            with leftcon3:
                selectedqrt= st.selectbox('',['1','2','3','4'])

            if userselect=='Registered Phonepe':
                st.write('')
                st.write('')
                st.write('')
                st.markdown(
                    "<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 38px;'><b>Registered Phonepe</b></h2>",
                    unsafe_allow_html=True)
                st.write('')
                val=fetchregistereduser(selectedyear,selectedqrt)
                state=[]
                count=[]
                qrt=[]
                year=[]
                for i in val:
                    state.append(i[1].title())
                    count.append(i[2])
                    qrt.append(i[-1])
                    year.append(str(i[-2]))
                userdic={'State':state,'Count':count,'Quartile':qrt,'Year':year}
                df=pd.DataFrame(userdic)

                fig=px.bar(df,x='State',y='Count',color='State',width=900,height=900)
                #fig.update_traces( textposition='outside')

                fig.update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                                )
                st.plotly_chart(fig)

            elif userselect=='App Opens':
                st.write('')
                st.write('')
                st.write('')
                st.markdown(
                    "<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 38px;'><b>App Opens</b></h2>",
                    unsafe_allow_html=True)
                st.write('')
                val = fetchregistereduser(selectedyear, selectedqrt)
                state = []
                Open = []
                qrt = []
                year = []
                for i in val:
                    print(i)
                    state.append(i[1].title())
                    Open.append(i[3])
                    qrt.append(i[-1])
                    year.append(str(i[-2]))
                userdic = {'State': state, 'AppOpens': Open, 'Quartile': qrt, 'Year': year}
                df = pd.DataFrame(userdic)
                fig = px.bar(df, x='State', y='AppOpens',color='State')
                #fig.update_traces( textposition='outside')
                fig.update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                )
                st.plotly_chart(fig)


        elif visselection=='Top 10':
            st.markdown("<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 48px;'><b>Top 10 - State , District , Pincode</b></h2>",unsafe_allow_html=True)
            topselect=st.selectbox('',['State','District','Pincode'])
            def fetchtopten(topyear,topqrt):
                select = 'select * from phonepepulse.topuser where year={} and quartile={}'.format(topyear, topqrt)
                mycurser.execute(select)
                result = mycurser.fetchall()
                userlst = []
                userstateamount = []
                userdistamount = []
                userpinamount = []
                for i in result:
                    userlst.append(i[1:])
                for i in userlst:
                    if 'state' in i:
                        userstateamount.append(i)
                    elif 'district' in i:
                        userdistamount.append(i)
                    elif 'pincode' in i:
                        userpinamount.append(i)
                topdic={'State':userstateamount,'District':userdistamount,'Pincode':userpinamount}
                return  topdic

            if topselect=='State':
                topstateright,topstateleft=st.columns([1,1])
                with topstateright:
                    topstatyear=st.selectbox('', ['2018', '2019', '2020', '2021', '2022'])
                with topstateleft:
                    topstatqrt=st.selectbox('', ['1', '2', '3', '4'])

                state=fetchtopten(topstatyear,topstatqrt)
                df=pd.DataFrame(state['State'],columns=['State','Amount','Entity','Year','Quartile'])
                df['State']=df['State'].str.title()
                df['Year']=df['Year'].astype('str')
                #st.dataframe(df)
                st.write('')
                st.write('')
                st.write('')
                st.markdown(
                    "<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 38px;'><b>Top 10 State</b></h2>",
                    unsafe_allow_html=True)

                st.write('')
                fig=px.area(df,x='State',y='Amount',text='Amount',color='State',width=810,height=600)
                #fig.update_traces(textposition='outside')
                fig.update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                )
                st.plotly_chart(fig)

            elif topselect=='District':
                topcounright,topcounleft=st.columns([1,1])
                with topcounright:
                    topcounyear=st.selectbox('', ['2018', '2019', '2020', '2021', '2022'])
                with topcounleft:
                    topcounqrt=st.selectbox('', ['1', '2', '3', '4'])

                district = fetchtopten(topcounyear, topcounqrt)
                df = pd.DataFrame(district['District'], columns=['District', 'Amount', 'Entity', 'Year', 'Quartile'])
                df['District'] = df['District'].str.title()
                df['Year'] = df['Year'].astype('str')
                # st.dataframe(df)
                st.write('')
                st.write('')
                st.write('')
                st.markdown(
                    "<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 38px;'><b>Top 10 District</b></h2>",
                    unsafe_allow_html=True)
                st.write('')
                fig = px.area(df, x='District', y='Amount',text='Amount',color='District',width=810,height=600)
                #fig.update_traces( textposition='outside')
                fig.update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                )
                st.plotly_chart(fig)

            elif topselect=='Pincode':
                toppinright,toppinleft=st.columns([1,1])
                with toppinright:
                    toppinyear=st.selectbox('', ['2018', '2019', '2020', '2021', '2022'])
                with toppinleft:
                    toppinqrt=st.selectbox('', ['1', '2', '3', '4'])

                pincode = fetchtopten(toppinyear, toppinqrt)
                df = pd.DataFrame(pincode['Pincode'], columns=['Pincode', 'Amount', 'Entity', 'Year', 'Quartile'])
                df['Pincode']=df['Pincode'].astype('str')
                df['Year'] = df['Year'].astype('str')
                #st.dataframe(df)
                st.write('')
                st.write('')
                st.write('')
                st.markdown(
                    "<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 38px;'><b>Top 10 Pincode</b></h2>",
                    unsafe_allow_html=True)
                st.write('')
                fig = px.bar(df, x='Pincode', y='Amount',text='Amount',color='Pincode',width=810,height=600)
                fig.update_traces(textposition='outside')
                fig.update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                )
                st.plotly_chart(fig)

        elif visselection=='Mobile Brand':
            try:
                st.markdown(
                    "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 48px;'><b>Mobile Brand</b></h2>",
                    unsafe_allow_html=True)


                def fetchmobiledet(mobyear,mobqrt):
                    df = pd.read_csv(r'E:\Datascience Projects\Phonepe Pulse Visualization\csv\mobile.csv')
                    df['Count']=df['Count'].astype('str')
                    df['Percentile'] = df['Percentile'].astype('str')
                    df.fillna('Missing',inplace=True)
                    df.replace('nan','Missing',inplace=True)
                    #st.dataframe(df)
                    newdf=df[(df['Year']==int(mobyear)) & (df['Quarter']==int(mobqrt))]
                    brand=(newdf['Brand'].values)
                    brandcount=newdf['Count'].values
                    brandpercent=newdf['Percentile'].values
                    brandlst=(ast.literal_eval(brand[0]))
                    brandcountlst=ast.literal_eval(brandcount[0])
                    brandpercentlst=ast.literal_eval(brandpercent[0])
                    return brandlst,brandcountlst,brandpercentlst

                mobleft,mobmid,mobright=st.columns([3,1,1])
                with mobleft:
                    mobselect=st.selectbox('',['Brand Count','Brand Percentile'])
                with mobmid:
                    branyear = st.selectbox('', ['2018', '2019', '2020', '2021', '2022'])
                with mobright:
                    branqrt = st.selectbox('', ['1', '2', '3', '4'])
                if mobselect=='Brand Count':
                    brand,brandcount,brandpercent=fetchmobiledet(branyear,branqrt)
                    brandcountdic={'Brand':brand,'Count':brandcount,'Percentile':brandpercent}
                    df=pd.DataFrame(brandcountdic)
                    st.write('')
                    st.write('')
                    st.write('')
                    st.markdown(
                        "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 38px;'><b>Mobile Brand Count</b></h2>",
                        unsafe_allow_html=True)
                    st.write('')
                    fig=px.bar(df,x='Brand',y='Count',color='Percentile')
                    fig.update_layout(
                        {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                    )
                    st.plotly_chart(fig)

                elif mobselect=='Brand Percentile':
                    brand, brandcount, brandpercent = fetchmobiledet(branyear, branqrt)
                    brandcountdic = {'Brand': brand, 'Count': brandcount, 'Percentile': brandpercent}
                    df = pd.DataFrame(brandcountdic)
                    st.write('')
                    st.write('')
                    st.write('')
                    st.markdown(
                        "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 38px;'><b>Mobile Brand Percentile</b></h2>",
                        unsafe_allow_html=True)
                    st.write('')
                    fig = px.pie(df, values='Percentile',names='Brand')
                    fig.update_layout(
                        {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', }
                    )
                    st.plotly_chart(fig)
            except:
                ncol1,ncol2,ncol3=st.columns([1,1,1])
                with ncol2:
                    st.write('#')
                    st.write('#')
                    st.write('#')
                    st.write('#')
                    st.markdown(
                        "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 28px;'><b>No Data</b></h2>",
                        unsafe_allow_html=True)
    with leftcon:
        if visselection=='Transaction':
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.write('#')
            st.markdown("<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 38px;'><b>Transaction Data</b></h2>",unsafe_allow_html=True)
            st.write('')
            if transelect=='All PhonePe Transaction':
                rtcol1,rtcol2, rtcol3 = st.columns([0.5,1,0.5])
                with rtcol1:
                    st.subheader('Quarter')
                    for i in range(4):
                        st.write(trandf['Quarter'][i])
                with rtcol2:
                    st.subheader('All Transaction')
                    for i in range(4):
                        st.write(str(trandf['All Transaction'][i]))
                with rtcol3:
                    st.subheader('Year')
                    for i in range(4):
                        st.write(str(selectedyear))

            elif transelect=='Total Payment':
                rtcol1, rtcol2, rtcol3 = st.columns([0.5, 1, 0.5])
                with rtcol1:
                    st.subheader('Quarter')
                    for i in range(4):
                        st.write(trandf['Quarter'][i])
                with rtcol2:
                    st.subheader('Total Payments')
                    for i in range(4):
                        st.write(str(trandf['Total Payments'][i]))
                with rtcol3:
                    st.subheader('Year')
                    for i in range(4):
                        st.write(str(selectedyear))
            elif transelect=='Average Transaction':
                rtcol1, rtcol2, rtcol3 = st.columns([0.5, 1, 0.5])
                with rtcol1:
                    st.subheader('Quarter')
                    for i in range(4):
                        st.write(trandf['Quarter'][i])
                with rtcol2:
                    st.subheader('Avg Transaction')
                    for i in range(4):
                        st.write(str(trandf['Average Transaction'][i]))
                with rtcol3:
                    st.subheader('Year')
                    for i in range(4):
                        st.write(str(selectedyear))


        elif visselection=='Users':
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.write('')
            st.write('')
            st.markdown("<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 38px;'><b>Users Data</b></h2>",unsafe_allow_html=True)

            st.write('')
            if userselect=='Registered Phonepe':
                rtcol1, rtcol2, rtcol3 = st.columns([2.3, 1, 0.5])
                with rtcol1:
                    st.subheader('State')
                    for i in range(36):
                        st.write(df['State'][i])
                with rtcol2:
                    st.subheader('Count')
                    for i in range(36):
                        st.write(str(df['Count'][i]))
                with rtcol3:
                    st.subheader('Year')
                    for i in range(36):
                        st.write(str(selectedyear))
            elif userselect=='App Opens':
                rtcol1, rtcol2, rtcol3 = st.columns([2.3, 1, 0.5])
                with rtcol1:
                    st.subheader('State')
                    for i in range(36):
                        st.write(df['State'][i])
                with rtcol2:
                    st.subheader('AppOpens')
                    for i in range(36):
                        st.write(str(df['AppOpens'][i]))
                with rtcol3:
                    st.subheader('Year')
                    for i in range(36):
                        st.write(str(selectedyear))


        elif visselection=='Top 10':
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.write('')
            st.markdown("<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 38px;'><b>Top 10 Data</b></h2>",unsafe_allow_html=True)

            st.write('')
            if topselect=='State':
                rtcol1, rtcol2, rtcol3 = st.columns([1.5, 1, 0.5])
                with rtcol1:
                    st.subheader('State')
                    for i in range(10):
                        st.write(df['State'][i])
                with rtcol2:
                    st.subheader('Amount')
                    for i in range(10):
                        st.write(str(df['Amount'][i]))
                with rtcol3:
                    st.subheader('Year')
                    for i in range(10):
                        st.write(str(topstatyear))

            elif topselect=='District':
                rtcol1, rtcol2, rtcol3 = st.columns([1.5, 1, 0.5])
                with rtcol1:
                    st.subheader('District')
                    for i in range(10):
                        st.write(df['District'][i])
                with rtcol2:
                    st.subheader('Amount')
                    for i in range(10):
                        st.write(str(df['Amount'][i]))
                with rtcol3:
                    st.subheader('Year')
                    for i in range(10):
                        st.write(str(topcounyear))

            elif topselect=='Pincode':
                rtcol1, rtcol2, rtcol3 = st.columns([1,1,1])
                with rtcol1:
                    st.subheader('Pincode')
                    for i in range(10):
                        st.write(df['Pincode'][i])
                with rtcol2:
                    st.subheader('Amount')
                    for i in range(10):
                        st.write(str(df['Amount'][i]))
                with rtcol3:
                    st.subheader('Year')
                    for i in range(10):
                        st.write(str(toppinyear))


        elif visselection=='Mobile Brand':
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown('##')
            st.markdown("<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 38px;'><b>Mobile Brand Data</b></h2>",unsafe_allow_html=True)

            st.write('')
            if mobselect=='Brand Count':
                try:
                    rtcol1, rtcol2, rtcol3 = st.columns([1, 1, 1])
                    with rtcol1:
                        st.subheader('Brand')
                        for i in range(10):
                            st.write(df['Brand'][i])
                    with rtcol2:
                        st.subheader('Count')
                        for i in range(10):
                            st.write(str(df['Count'][i]))
                    with rtcol3:
                        st.subheader('Year')
                        for i in range(10):
                            st.write(str(branyear))
                except:

                    ncol1, ncol2, ncol3 = st.columns([1, 1, 1])
                    with ncol2:

                        st.write('#')
                        st.markdown(
                            "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 28px;'><b>No Data</b></h2>",
                            unsafe_allow_html=True)

            elif mobselect=='Brand Percentile':
                try:
                    rtcol1, rtcol2, rtcol3 = st.columns([1, 2, 1])
                    with rtcol1:
                        st.subheader('Brand')
                        for i in range(10):
                            st.write(df['Brand'][i])
                    with rtcol2:
                        st.subheader('Percentile')
                        for i in range(10):
                            st.write(str(df['Percentile'][i]))
                    with rtcol3:
                        st.subheader('Year')
                        for i in range(10):
                            st.write(str(branyear))
                except:
                    ncol1, ncol2, ncol3 = st.columns([1, 1, 1])
                    with ncol2:

                        st.write('#')
                        st.markdown(
                            "<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 28px;'><b>No Data</b></h2>",
                            unsafe_allow_html=True)


