import code
from contextlib import nullcontext
from curses import flash
from dis import dis
from email import charset
from faulthandler import is_enabled
from importlib.resources import open_binary
import queue as qqq
import time
from typing import KeysView
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sn
import matplotlib.pyplot as plt
from io import BytesIO

# from lizbboo import communication 



# st.set_page_config(page_title="all_ml", layout='wide',initial_sidebar_state="collapsed")

if not "list" in st.session_state:
    # coms=communication()
    st.set_page_config(page_title="all_ml", layout='wide',initial_sidebar_state="collapsed"
        ,menu_items={'About': "fdsdfsdfds"})
    st.session_state["allkeys_1"]=None
    st.session_state["no_toggel"]=False
    st.session_state["first_dis"]=False
    st.session_state["go"]=False    
    st.session_state["data"]=None
    st.session_state["date_sel_type"]={}
    st.session_state["time_sel_type"]={}
    st.session_state["v_disable"]=True
    st.session_state["reset"]=None
    st.session_state["some_flag"]=False
    st.session_state["to_correct"]=None
    st.session_state["some_flag1"]=False
    st.session_state["time_type"]=["full","hour","minute","days","years","other"]
    st.session_state["date_type"]=["full","month","year","day","other"]
    st.session_state["ch_list"]={"nominal":[],"ordinal":[],"discret":[],"continuas": [],"date":[],"time":[],"id":[]}
    st.session_state["get_meta_data"]=False
    st.session_state["orders"]={"or3":["12","21","31"]}
    st.session_state["list"]={"nominal":[],"ordinal":['or1','or2', 'or3'],"discret":['green', 'blue'],"continuas": ['indigo', 'violet'],"date":["123","321"],"time":["qwqe1"],"id":["names","pID"]}
    # st.session_state["fo"]=None

if st.session_state["reset"] is not None:
    st.session_state["allkeys_1"]=None
    st.session_state["list"]=None
    st.session_state["first_dis"]=False
    st.session_state["data"]=None
    st.session_state["no_toggel"]=False
    st.session_state["reset"]=None
    st.session_state["date_sel_type"]={}
    st.session_state["time_sel_type"]={}
    st.session_state["to_correct"]=None
    st.session_state["some_flag"]=False
    st.session_state["some_flag1"]=False
    st.session_state["go"]=False
    st.session_state["v_disable"]=True
    st.session_state["time_type"]=["full","hour","minute","days","years","other"]
    st.session_state["date_type"]=["full","month","year","day","other"]
    st.session_state["ch_list"]={"nominal":[],"ordinal":[],"discret":[],"continuas": [],"date":[],"time":[],"id":[]}
    st.session_state["get_meta_data"]=False
    st.session_state["orders"]={"or3":["12","31","21"]}
    st.session_state["list"]={"nominal":[],"ordinal":['or1','or2', 'or3'],"discret":['green', 'blue'],"continuas": ['indigo', 'violet'],"date":["123","321"],"time":["qwqe1"],"id":["names","pID"]}

def clearr():
    st.session_state["nominal"]=[]# fromer fd
    st.session_state["ordinal"]=[]# fromer fd1
    st.session_state["discret"]=[]
    st.session_state["continuas"]=[]
    st.session_state["date"]=[]
    st.session_state["time"]=[]
    st.session_state['id']=[]

def  got_data():
    st.session_state["list"]={"nominal":[],"ordinal":['or1','or2', 'or3'],"discret":['green', 'blue'],"continuas": ['indigo', 'violet'],"date":["123","321"],"time":["qwqe1"],"id":["names","pID"]}

def project():
    st.title("all is ML")
    st.header("preprocessing data and Auto ML tool")
    menu = ["Home","About","data clean","Model selection","play ground"]
    sub_menu=["NLP","ML","EDA"]
    m=st.sidebar.selectbox("Menu",menu,key="gg")
    if m == menu[0]:
        Home()
    elif m == menu[1]:
        About()
    elif m == menu[2]:
        sm=st.sidebar.radio("Type",sub_menu)
        if sm == sub_menu[0]:
            NLP_clean()
        elif sm == sub_menu[1]:
            ML_clean()
        elif sm == sub_menu[2]:
            EDA_clean()
    elif m == menu[3]:
        sm=st.sidebar.radio("Type",sub_menu[:-1])
        if sm == sub_menu[0]:
            NLP_model_selection()
        elif sm == sub_menu[1]:
            ML_model_selection()
    elif m == menu[4]:
        playground()
    

def ff():
    st.session_state["gg"]="About"

def get_main_call():
    pass

def reseet():
    st.session_state["reset"]=True
    st.experimental_memo.clear()
    # st.experimental_rerun()


def editing():
    st.session_state.edit_m = not st.session_state.edit_m


@st.experimental_memo
def file_upladed():
    return pd.read_pickle("temp.pkl")


def tranfer():
    if st.session_state["nominal"] !=[]:
        for i in st.session_state["nominal"]:
            st.session_state["list"]["nominal"].remove(i)
            st.session_state["ch_list"]["nominal"].append(i)
    if st.session_state["ordinal"] !=[]:
        for i in st.session_state["ordinal"]:
            st.session_state["list"]["ordinal"].remove(i)
            st.session_state["ch_list"]["ordinal"].append(i)
    if st.session_state["discret"] !=[]:
        for i in st.session_state["discret"]:
            st.session_state["list"]["discret"].remove(i)
            st.session_state["ch_list"]["discret"].append(i)
    if st.session_state["continuas"] !=[]:
        for i in st.session_state["continuas"]:
            st.session_state["list"]["continuas"].remove(i)
            st.session_state["ch_list"]["continuas"].append(i)
    if st.session_state["date"] !=[]:
        for i in st.session_state["date"]:
            st.session_state["list"]["date"].remove(i)
            st.session_state["ch_list"]["date"].append(i)
    if st.session_state["time"] !=[]:
        for i in st.session_state["time"]:
            st.session_state["list"]["time"].remove(i)
            st.session_state["ch_list"]["time"].append(i)
    if st.session_state["id"] !=[]:
        for i in st.session_state["id"]:
            st.session_state["list"]["id"].remove(i)
            st.session_state["ch_list"]["id"].append(i)
    
    
def change():
    allkeys=list()
    for i in st.session_state["ch_list"].values():
        allkeys.extend(i)
    for i in allkeys:
        st.session_state["list"][st.session_state[f"{i}_change"]].append(i)
    for i in ("date","time","ordinal"):
        if st.session_state["list"][i] != []:
            st.session_state["to_correct"]=True

def type_conv():
    for j in ("date","time","ordinal"):
        for i in st.session_state:
            if '_' in i:
                if i.split('_')[1] == "order" :
                    st.session_state["orders"][i.split('_')[0]]=st.session_state[i]
                if i.split('_')[0] == "date" and i.split('_')[1] not in ("sel","type") :
                    st.session_state["date_sel_type"].update({i.split('_')[1]:st.session_state[i]})
                if i.split('_')[0] == "time"and i.split('_')[1] not in ("sel","type") :
                    st.session_state["time_sel_type"].update({i.split('_')[1]:st.session_state[i]})


def go_all_to_next():
    allkeys=list()
    for i in st.session_state["ch_list"].values():
        allkeys.extend(i)
    st.session_state["allkeys_1"]=allkeys


def if_go_all_to_next(i:str):
    if st.session_state[f"{i}_change"] == None:
        if i not in st.session_state["allkeys_1"]:
            st.session_state["allkeys_1"].append(i)    
    else:
        if i in st.session_state["allkeys_1"]: 
            st.session_state["allkeys_1"].remove(i)


def go_all_2_next():
    allkeys=list()
    for j in ("date","time"):
        allkeys.extend(st.session_state["list"][j])
    st.session_state["allkeys_1"]=allkeys


def if_go_all_2_next(i:str,j:str):
    if st.session_state[f"{j}_{i}_type"] == None:
        if i not in st.session_state["allkeys_1"]:
            st.session_state["allkeys_1"].append(i)    
    else:
        if i in st.session_state["allkeys_1"]:
            st.session_state["allkeys_1"].remove(i)


def delTemp():
    for i in st.session_state:
        if '_' in i:
            if i.split('_')[1] == "order" :
                del st.session_state[i]
            if i.split('_')[0] == "date" and i.split('_')[1] not in ("sel","type") :
                del st.session_state[i]
            if i.split('_')[0] == "time"and i.split('_')[1] not in ("sel","type") :
                del st.session_state[i]
            if i.split('_')[1] == "change":
                del st.session_state[i]
    st.session_state["date_sel_type"]={}
    st.session_state["time_sel_type"]={}
    st.session_state["ch_list"]={"nominal":[],"ordinal":[],"discret":[],"continuas": [],"date":[],"time":[],"id":[]}


def f():
    return all([ True if len(st.session_state[f"{i}_order"]) == len(st.session_state["orders"][i]) else False for i in st.session_state["orders"]])


def g():
    return True if len([ True for i in st.session_state.nominal+st.session_state.ordinal+st.session_state.discret+st.session_state.continuas+st.session_state.date+st.session_state.time+st.session_state.id]) != 0 else False


def ordinal_catagories_get(das):
    # if all( True if das[ str.replace(i,'~',' ') ].nunique() < 11 else False for i in st.session_state["list"]["ordinal"]):
    st.session_state["orders"]=coms.ordinal_catagories(st.session_state["list"]["ordinal"])
    

def list_get():
    st.session_state["list"]=coms.list_colum_type()
    st.session_state["get_meta_data"]=True


def feed_back():
    coms.change_list_colum_type(st.session_state["list"])


def not_kidding():
    # get feed_back if the type_edited are compatible to the real data
    return coms.feed_back_good()

@st.experimental_memo
def submit():
    coms.generate_report()


def sin_dasa(datas):
    
    st.write('<p style="color:blue;font-size:30px;margin-bottom:30px">Data review</p>',unsafe_allow_html=True)
    st.table(datas.head())
    st.write('<p style="color:blue;font-size:30px;margin-bottom:30px">Corrections</p>',unsafe_allow_html=True)
    st.text("to change to other select from this and click change ")
    if st.session_state["get_meta_data"]== False:
        list_get()
    ss=st.container()
    fp=ss.empty()
    fs=ss.empty()    

    nominal,ordinal,dicret,continuas,date,time,id=fp.columns([1,1,1,1,1,1,1])
    
    with nominal:
        st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Nominal</p>',unsafe_allow_html=True)
        s="\n".join(["- "+i for i in st.session_state["list"]["nominal"]])
        st.markdown(s)
    with ordinal:
        st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Ordinal</p>',unsafe_allow_html=True)
        s="\n".join(["- "+i for i in st.session_state["list"]["ordinal"]])
        st.markdown(s)
    with dicret:
        st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Discret</p>',unsafe_allow_html=True)
        s="\n".join(["- "+i for i in st.session_state["list"]["discret"]])
        st.markdown(s)
    with continuas:
        st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Continuas</p>',unsafe_allow_html=True)
        s="\n".join(["- "+i for i in st.session_state["list"]["continuas"]])
        st.markdown(s)
    with date:
        st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Date</p>',unsafe_allow_html=True)
        s="\n".join(["- "+i for i in st.session_state["list"]["date"]])
        st.markdown(s)
        if st.session_state["date_sel_type"] != []:
            l="\n".join([f"- {i}={v}" for i,v in st.session_state["date_sel_type"].items()])
            st.markdown(l)
    with time:
        st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Time</p>',unsafe_allow_html=True)
        s="\n".join(["- "+i for i in st.session_state["list"]["time"]])
        st.markdown(s)
        if st.session_state["time_sel_type"] != []:
            l="\n".join([f"- {i}={v}" for i,v in st.session_state["time_sel_type"].items()])
            st.markdown(l)
    with id:
        st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">ID</p>',unsafe_allow_html=True)
        s="\n".join(["- "+i for i in st.session_state["list"]["id"]])
        st.markdown(s)
    
    nominal1,ordinal1,dicret1,continuas1,date1,time1,id1=fs.columns([1,1,1,1,1,1,1])

    with nominal1:
        st.multiselect(label='.',key="nominal",options=st.session_state["list"]["nominal"],disabled=st.session_state["no_toggel"],label_visibility="collapsed")
        
    with ordinal1:
        st.multiselect(label='.',key="ordinal",options=st.session_state["list"]["ordinal"],disabled=st.session_state["no_toggel"],label_visibility="collapsed")
        
    with dicret1:
        st.multiselect(label='.',key="discret",options=st.session_state["list"]["discret"],disabled=st.session_state["no_toggel"],label_visibility="collapsed")
        
    with continuas1:
        st.multiselect(label='.',key="continuas",options=st.session_state["list"]["continuas"],disabled=st.session_state["no_toggel"],label_visibility="collapsed")
        
    with date1:
        st.multiselect(label='.',key="date",options=st.session_state["list"]["date"],disabled=st.session_state["no_toggel"],label_visibility="collapsed")
        
    with time1:
        st.multiselect(label='.',key="time",options=st.session_state["list"]["time"],disabled=st.session_state["no_toggel"],label_visibility="collapsed")
    
    with id1:
        st.multiselect(label='.',key="id",options=st.session_state["list"]["id"],disabled=st.session_state["no_toggel"],label_visibility="collapsed")
    
    if g():
        st.session_state["v_disable"]=False
    v=st.button("next",disabled=st.session_state["v_disable"],on_click=tranfer)
    if v :
        st.session_state["v_disable"]=True
        st.session_state["some_flag"]=True
        st.session_state["no_toggel"]=True
        st.experimental_rerun()

    c1=st.container()
    if st.session_state["some_flag"] == True:
        with c1:
            st.write("correct the type by selecting write")
            if st.session_state["allkeys_1"] is None:
                go_all_to_next()
            for j in st.session_state["ch_list"].items():
                if j[1] != []:
                    st.write(f"from {j[0]} to ...")
                    for i in j[1]:
                        st.selectbox(i,key=f"{i}_change",options=[None]+[l for l in st.session_state['list'] if l!=j[0]],on_change=if_go_all_to_next,kwargs={"i":f"{i}"},help="change values to proceed",format_func=lambda x :'select' if x==None else x)
            
            if st.session_state["allkeys_1"] == [] and all( True if datas[ str.replace(i,'~',' ') ].nunique() < 11 else False for i in st.session_state["list"]["ordinal"]):
                v1=st.button(label="next->",on_click=change)
                if v1 :
                    st.session_state["some_flag1"]=True
                    st.session_state["some_flag"]=False
                    st.session_state["allkeys_1"]=None
                    if st.session_state["to_correct"] is None:
                        st.session_state["some_flag1"]=False
                        st.session_state["v_disable"]=False
                        ordinal_catagories_get()
                    st.experimental_rerun()

    if st.session_state["some_flag1"] == True:
        with c1:
            st.write("selct interal type")
            if st.session_state["allkeys_1"] is None:
                go_all_2_next()
            for j in ("date","time","ordinal"):
                if j == "ordinal":
                    for i in st.session_state["list"][j]:
                        st.multiselect(i,key=f"{i}_order",options=st.session_state["orders"][i],help="select all the element in order to proceed")
                else:
                    for i in st.session_state["list"][j]:
                        st.selectbox(i,key=f"{j}_{i}_type",options=[None]+st.session_state[f"{j}_type"],on_change=if_go_all_2_next,kwargs={"i":f"{i}","j":f"{j}"},help="change values to proceed",format_func=lambda x :'select' if x==None else x)
        if f() and st.session_state["allkeys_1"] == []:
            v2=st.button(label="next->>",on_click=type_conv)
            if v2 :
                st.session_state["some_flag1"]=False
                st.session_state["v_disable"]=True
                st.session_state["no_toggel"]=False
                st.session_state["to_correct"]=None
                st.session_state["allkeys_1"]=None
                delTemp()
                st.experimental_rerun()
                
    # vv=st.button("Proce")
    # if vv:
    #     st.write(st.session_state["orders"])
    p,r=st.columns([25,1])    
    r.button("reset",help="click for start fom start",on_click=reseet)
    p.button("Proceed with this data set",key="j",on_click=submit)
    if st.session_state["j"]:
        st.button("",on_click=ff)



@st.experimental_memo
def loaddata():
    st.session_state["data"].seek(0)
    return pd.read_csv(st.session_state["data"])


def disabled():
    coms.input_data(pd.read_csv(st.session_state["fo"]))
    st.session_state["first_dis"]=True


def Home(i=False):

    st.radio("are you professinaly a",["DataScientist","Business Owner"],horizontal=True,key="who",disabled=st.session_state["first_dis"])
    if st.session_state["who"] ==  "DataScientist":
        
        "hard relation and with all the discriptio of the data with terminology including change the name of certain things in peoples way"
        st.radio("number of data files",["single","multi"],key="ds",horizontal=True,disabled=st.session_state["first_dis"])
        if st.session_state["ds"] ==  "single" :

            st.file_uploader("Upload Data",type=['csv','tsv'],key="fo",disabled=st.session_state["first_dis"],on_change=disabled)
            if st.session_state["fo"] is not None :
                st.session_state["data"]=st.session_state["fo"]
            if st.session_state["data"] is not None :
                sin_dasa(loaddata())
         

        elif st.session_state["ds"] ==  "multi":
            fo=st.file_uploader("upload data",type=['csv','tsv'],accept_multiple_files=True)
            data_m=None
            if len(fo) != 0 :
                for i in fo :
                    if data_m is None :
                        data_m=pd.read_csv(i)
                    else:
                        data_m=pd.concat([data_m,pd.read_csv(i)],ignore_index=True)
                    i.seek(0)
                                
                st.text(data_m.shape)        
                st.table(data_m.head())
                st.write('<p style="color:blue;text-align:center;font-size:30px;margin-bottom:30px">Corrections</p>',unsafe_allow_html=True)
                st.text("to change to other select from this and click change ")

                nominal,ordinal,dicret,continuas,date,time,id=st.columns([1,1,1,1,1,1,1])
                
                with nominal:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Nominal</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
                    
                with ordinal:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Ordinal</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd1",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
                    
                with dicret:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Discret</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd2",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
                    
                with continuas:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Continuas</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd3",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
                    
                with date:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Date</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd4",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
                    
                with time:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Time</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd5",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
                    
                with id:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">ID</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd6",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
                    
                place_hold=st.empty()
                correction=place_hold.container()
                with correction:
                    for i in st.session_state.fd+st.session_state.fd1+st.session_state.fd2+st.session_state.fd3+st.session_state.fd4+st.session_state.fd5+st.session_state.fd6:
                        st.radio(i,key=f"{i}",horizontal=True,options=["nominal","ordinal","dicret","continuas","date","time","id"])
                
                if st.button("change",on_click=clearr):
                    st.write(st.session_state)

                st.download_button(label="Download combined data as CSV",data=data_m.to_csv(),file_name='large_data.csv',mime='csv')
                
                st.button("Proceed with this data ")


    elif st.session_state["who"] ==  "Business Owner":
        "easy graphs as possible and the discription is as simple as possible including change the name of certain things in peoples way"
        ds=st.radio("number of data files",["single","multi"],horizontal=True,disabled=st.session_state.fi)
        if st.session_state["ds"] ==  "single" :
            fo=st.file_uploader("Upload Data",type=['csv','tsv'])
            if fo:
                data=pd.read_csv(fo)
                # types=find_type_of_columns(data)

                catagori,ordered,numbers,date,time,id,no_use=st.columns([1,1,1,1,1,1])
                
                with catagori:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Nominal</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
                    
                with ordered:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Ordinal</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd1",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])

                with numbers:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Discret</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd2",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])

                with date:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Discret</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd3",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
                    
                with time:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Continuas</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd4",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
                    
                with id:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Date</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd5",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
                    
                with no_use:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Time</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd6",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
                    
                    
                place_hold=st.empty()
                correction=place_hold.container()
                with correction:
                    for i in st.session_state.fd+st.session_state.fd1+st.session_state.fd2+st.session_state.fd3+st.session_state.fd4+st.session_state.fd5+st.session_state.fd6:
                        st.radio(i,key=f"{i}",horizontal=True,options=["nominal","ordinal","dicret","continuas","date","time","id"])
                
                if st.button("change",on_click=clearr):
                    st.write(st.session_state)

                st.button("Proceed with this data set")

        elif st.session_state["ds"] ==  "multi":
            fo=st.file_uploader("upload data",type=['csv','tsv'],accept_multiple_files=True)
            data_m=None
            if len(fo) != 0 :
                for i in fo :
                    if data_m is None :
                        data_m=pd.read_csv(i)
                    else:
                        data_m=pd.concat([data_m,pd.read_csv(i)],ignore_index=True)
                    i.seek(0)
                
                # types=find_type_of_columns(data_m)
                
                st.text(data_m.shape)        
                st.table(data_m.head())
                st.write('<p style="color:blue;text-align:center;font-size:30px;margin-bottom:30px">Corrections</p>',unsafe_allow_html=True)
                st.text("to change to other select from this and click change ")

                catagori,ordered,numbers,date,time,id,no_use=st.columns([1,1,1,1,1,1])
                
                with catagori:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Nominal</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
                    
                with ordered:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Ordinal</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd1",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])

                with numbers:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Discret</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd2",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])

                with date:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Discret</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd3",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
                    
                with time:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Continuas</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd4",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
                    
                with id:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Date</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd5",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
                    
                with no_use:
                    st.write('<p style="color:blue;text-align:center;font-size:25px;margin-bottom:0">Time</p>',unsafe_allow_html=True)
                    s="\n".join(["- "+i for i in x])
                    st.markdown(s)
                    st.multiselect("Nominal",key="fd6",options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
                    
                    
                place_hold=st.empty()
                correction=place_hold.container()
                with correction:
                    for i in st.session_state.fd+st.session_state.fd1+st.session_state.fd2+st.session_state.fd3+st.session_state.fd4+st.session_state.fd5+st.session_state.fd6:
                        st.radio(i,key=f"{i}",horizontal=True,options=["nominal","ordinal","dicret","continuas","date","time","id"])
                
                if st.button("change",on_click=clearr):
                    st.write(st.session_state)

                st.download_button(label="Download combined data as CSV",data=data_m.to_csv(),file_name='large_df.csv',mime='csv')
                st.button("Proceed with this data set")



    # ds=st.radio("number of data files",["single","multi"],horizontal=True)
    # if st.session_state["ds"] ==  "single" :
    #     fo=st.file_uploader("Upload Data",type=['csv','tsv'])
    #     if fo:
    #         st.table(pd.read_csv(fo).head())
    #         st.download_button(label="Download data as CSV",data=fo,file_name='large_df.csv',mime='text/csv')
    #         st.button("Proceed with this data set")



        # color = st.selectbox(
        #     "fdf",
        # # value=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
        # options=['red,dsadsa,ggg','ggg', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])

        # with st.spinner('Wait for it...'):
        #     time.sleep(5)
        #     st.success('Done!')
#         next_action = st.selectbox(
#     'How would you like to proceed?',
#     ('Stay', 'Next page', 'Previous page')
# )

# if next_action == 'Stay':
#     pass
# elif next_action == 'Next page':
#     page -= 1
#     show_images(page=page)
# elif next_action == 'Previous page':
#     page += 1
#     show_images(page=page)

        # seaborn / altair
        # plt.style.use('dark_background')
        # n_cols=3
        # cat_images=[True for _ in range(9)]
        

        # ----------------------------------
        # chart lenge usme uski prioty lagake group kaenge 
        # like for 1 use max 3 columns
        #     for 1 wala hai per uske sath koi nahi hai usko 
        #     with ratio change [4,3,3] with 2 for 3 use [5,2.5,2.5]
        #     all 2 or lower max 3 col 
        #     for 2 use max 4 isme kabhi hua without same
        #     for 3 use max 4
        # ---------------------------------------------
        # cat_images=['1.png','2.png','3.png','4.png','5.png','6.png']
    #     n_rows = 1 + len(cat_images) // int(n_cols)
    #     rows = [st.container() for _ in range(n_rows)]
    #     cols_per_row = [r.columns(n_cols) for r in rows]
    #     cols = [column for row in cols_per_row for column in row]
    #     cp=sn.color_palette('bright')
    #     for image_index, cat_image in enumerate(cat_images):
    #         # cols[image_index].image(cat_image)
    #         # fig,ax=plt.subplots(figsize=(6,3))
    #         # ax.figure()
    #         fig=px.pie(values=[20,30,50],names=["Apple","Bnana","Mango"])
    #         fig.update_traces(
    #             textinfo="percent+label",
    #         )
    #         fig.update_layout(
    #         # widht=800,
    #         height=350,
    #             title_text="Sector Tree in for hello",
    #             # title_font_family="Times New Roman",
    #             title_font_family="monospace",
    #             title_font_size=18,
    #             font_size=15,
    #             title_x=0.5,
    #             margin_b=10
    #         )
    #         cols[image_index].plotly_chart(fig,use_container_width=True)
    #         vv=cols[image_index].expander("fdsfsdf")
    #         vv.write("fdsfdsfds")

    #     tab0 ,tab1, tab2 = st.tabs(["Genral info","Main", "Missing values"])
    #     # tab1.write("this is tab 1")
    #     # tab1.metric(label="Gas price", value=4, delta=-0.5)
    #     color1 = tab2.selectbox(
    #         "select columns or column to find best relation",
    #     # value=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    #     options=['variable 1','variable 2', 'variable 3', 'variable 4', 'variable 1 and variable 2 and variable 3 and variable 4'])
    #     tab2.write("this is tab 2")
    #     tab2.metric("My metric", 42, 2)
    #     # with st.container():
    #     #     tab1.write("this is tab 1")
    #     #     tab1.metric(label="Gas price", value=4, delta=-0.5)
    #     ccc=tab2.container()
    #     if color1 == 'variable 1':
    #         with ccc:
    #             tab2.success("ndjsndjns-------------------")
    #             expander = tab2.expander("See explanation")
    #             expander.write("""
    #                 The chart above shows some numbers I picked for you.
    #                 I rolled actual dice for these, so they're *guaranteed* to
    #                 be random.
    #             """)
    #     else :
    #         with ccc:
    #             tab2.write("""<p>fdsfdfsfsdfsdf &#128516 </p>""",unsafe_allow_html=True)
    #             tab2.success("hellooooo")
    #             expander = tab2.expander("See explanation ooooooo")
    #             expander.write("""
    #                 The chart above shows some numbers I picked for you.
    #                 I rolled actual dice for these, so they're *guaranteed* to
    #                 be random.
    #             """)


    #     tab2.metric(label="Gas price", value=4, delta=-0.5)
    #     # from PIL import Image
    #     col1,col2,col3=tab1.columns([4,3,3],gap="small")
    #     with col1:
    #         st.image('1.png',use_column_width=True)
    #         # st.plotly_chart()
    #         st.image('2.png',use_column_width=True)
    #         st.image('3.png',use_column_width=True)

    #     with col2:
    #         st.image('4.png'
    #         ,use_column_width=True
    #             )
        
    #         st.image('5.png',
    #         use_column_width=True
    #         )
    #         # st.image('6.png',
    #         # use_column_width=True
    #         # )
            
    #         # st.image(image1,caption="hatt")
    #         # st.image
    #     with col3:
    #         st.image('7.png',use_column_width=True)
    #         st.image('8.png',use_column_width=True)
    #         # st.header("An owl")
    #         # st.image(image1)
    #         # st.metric("My metric", 42, 2)
    #         # st.metric(label="Gas price", value=4, delta=-0.5)

    #     # image1 = Image.open('bigdata.jpg')
    #     # col1,col2,col3=st.columns([4,3,3])
    #     # with col1:
    #     #     st.image('bigdata.jpg')

    #     # with col2:
    #     #     st.image(image1,caption="hatt")
    #     #     # st.image

    #     # with col3:
    #     #     # st.header("An owl")
    #     #     st.image(image1)
    #     #     st.metric("My metric", 42, 2)
    #     #     st.metric(label="Gas price", value=4, delta=-0.5)
        
        
        
        
    
            
    # elif st.session_state["ds"] ==  "multi":
    #     fo=st.file_uploader("upload data",type=['csv','tsv'],accept_multiple_files=True)
    #     data_m=None
    #     if len(fo) != 0 :
    #         for i in fo :
    #             if data_m is None :
    #                 data_m=pd.read_csv(i)
    #             else:
    #                 data_m=pd.concat([data_m,pd.read_csv(i)],ignore_index=True)
    #             i.seek(0)
    #         st.text(data_m.shape)        
    #         st.table(data_m.tail(14))
    #         st.download_button(label="Download data as CSV",data=data_m.to_csv(),file_name='large_df.csv',mime='csv')
    #         st.button("Proceed with this data set")


def playground():
    st.text("welcome to play graound")
    


def About():
    st.text("just data to train \n with feed back")
    st.markdown("""
    ## Funs:
       - playground (with stepby step suggestions and data cleaning with metrics showing with graphs to playgraound user)
           - all step to deal with ML or NLP problems with verity of probelm selection
       - NLP_clean
           - user give type of NLP problem to solve
           - with target variable and other things 
           - get the cleandata or transformed
           - pickel it to be downloaded
       - ML_clean
           - user give type of ML problem to solve 
           - with target variable and other things 
           - get the cleandata or transformed 
           - pickel it to be downloaded
       - EDA_clean
           - eda prelim data cleaning or transformed
           - pickel transformations or cleaning steps as pipeline 
       - ML_model_selection
           - create piplelines to deal with all the hyper perameter of all the algos
           - pickel it to be downloaded
       - NLP_model_selection
           - create piplelines to deal with all the hyper perameter of all the algos
           - pickel it to be downloaded

    ## Error handling for home:
       - file size exceed
           - alternative file input
       - out of memory error
           - divide data set with skiprows
       - encoding error
           - change encode using other method
       - to much cols
           - not to display in case if it is image data/unwanded null data
           - report error type and suggestion to solve 
       - multiple data set to stack
           - append data sets itteratively

    ## Data collect:
""")


def NLP_clean():
    pass


def ML_clean():
    pass


def EDA_clean():
    pass


def ML_model_selection():
    pass


def NLP_model_selection():
    pass


def EDA():
    pass


if __name__ == '__main__':
    project()


# datao=pd.read_csv(fo)
# data1=pd.read_csv(f1)
# datao=datao.append(data1)
# st.table(datao.head())
# st.text(type(st.file_uploader("upload data",type=['csv'],accept_multiple_files=True)))
# st.text(fo[0].name)
# data=pd.read_csv(fo[0])
# st.table(data.tail())
# for file in fo:
#     dataframe = pd.read_csv(file)
#     file.seek(0)
#     st.write(dataframe)


# funs:
#        - playground (with stepby step suggestions and data cleaning with metrics showing with graphs to playgraound user)
#            - all step to deal with ML or NLP problems with verity of probelm selection
#        - NLP_clean
#            - user give type of NLP problem to solve
#            - with target variable and other things 
#            - get the cleandata or transformed
#            - pickel it to be downloaded
#        - ML_clean
#            - user give type of ML problem to solve 
#            - with target variable and other things 
#            - get the cleandata or transformed 
#            - pickel it to be downloaded
#        - EDA_clean
#            - eda prelim data cleaning or transformed
#            - pickel transformations or cleaning steps as pipeline 
#        - ML_model_selection
#            - create piplelines to deal with all the hyper perameter of all the algos
#            - pickel it to be downloaded
#        - NLP_model_selection
#            - create piplelines to deal with all the hyper perameter of all the algos
#            - pickel it to be downloaded
# error handling for home:
#        - file size exceed
#            - alternative file input
#        - out of memory error
#            - divide data set with skiprows
#        - encoding error
#            - change encode using other method
#        - to much cols
#            - not to display in case if it is image data/unwanded null data
#            - report error type and suggestion to solve 
#        - multiple data set to stack
#            - append data sets itteratively
# data collect:
#  standard ops
#     - detect outliers and chenck for null or word "None" or "Null" according
#     - treat or impute them according
#     - special variable treatment 
#     - cleating new  and droping other non usefull
#     - outlier detection and treatment
