import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import streamlit as slt
icon = Image.open("icon2.png")
slt.set_page_config(page_title = "EDA",page_icon = icon, layout = "wide")
slt.caption("Praneethvasa")
slt.title("Exploratory Data Analysis -- On any DataSet")
m = True
#m = False
if m:
    imag = Image.open("mn.png")
    slt.image(imag,use_column_width = True)
    slt.title("Sorry, the web app is currently under maintenance. Please try again Later😶‍🌫️")
else:
    file1 = slt.file_uploader("Upload a DataSet in (.csv Form)")
    if file1 is not None:
        data = pd.read_csv(file1)
        slt.write("Preview : ")
        slt.dataframe(data.head(10))
        if slt.checkbox("How many rows and columns in the DataSet?"):
            slt.write("Number of rows : ",len(data))
            slt.write("Number Of Columns : ",len(data.columns))
            if slt.button('Click Here to get Code',key = '1'):
                slt.code("""slt.write("Number of rows : ",len(data))\nslt.write("Number Of Columns : ",len(data.columns))""")
        if slt.checkbox("Display the dimension and Shape of DataSet"):
            slt.write("Dimension : ",data.ndim)
            slt.write("Shape : ",data.shape)
            if slt.button('Click Here to get Code',key = '2'):
                slt.code("""slt.write("Dimension : ",data.ndim)\nslt.write("Shape : ",data.shape)""")
        if slt.checkbox("List the name of Attributes/columns in dataset"):
            slt.write("Columns : ")
            slt.write(pd.DataFrame(data.columns,columns = ["Attribute Names"]))
            if slt.button('Click Here to get Code',key = '3'):
                slt.code(""" slt.write("Columns : ")\nslt.write(pd.DataFrame(data.columns,columns = ["Attribute Names"]))""")
        if slt.checkbox("Display the count of Non - Null values in dataset"):
            slt.write(data.count())
            if slt.button('Click Here to get Code',key = '4'):
                slt.code("""slt.write(data.count())""")
        if slt.checkbox("Display the count of Null values in dataset"):
            slt.write(data.isna().sum())
            if slt.button('Click Here to get Code',key = '5'):
                slt.code("""slt.write(data.isna().sum())""")
        if slt.checkbox("Display the Data types of each columns"):
            slt.write(pd.DataFrame(data.dtypes,columns = ["data type"]))
            if slt.button('Click Here to get Code',key = '50'):
                slt.code("""slt.write(pd.DataFrame(data.dtypes,columns = ["data type"]))""")
        num_data = data.select_dtypes(exclude = ["object","bool"])
        obj_data = data.select_dtypes(include = "object")
        if slt.checkbox("Display the Data of Numeric columns "):
            slt.dataframe(num_data)
            if slt.button('Click Here to get Code',key = 'a'):
                slt.code("""num_data = data.select_dtypes(exclude = ["object","bool"])\nslt.dataframe(num_data)""")
        if slt.checkbox("Display the Data of Object Columns"):
            slt.write(obj_data)
            if slt.button('Click Here to get Code',key = 'd'):
                slt.code("""obj_data = data.select_dtypes(include = "object")\nslt.write(obj_data)""")
        for i in obj_data:
            if slt.checkbox(f"Display the Unique Values of '{i}' Column"):
                slt.write(data[i].unique())
                if slt.button('Click Here to get Code',key = i):
                    slt.code(f"slt.write(data['{i}'].unique())")
        slt.title("STATISTICS")
        for i in num_data:
            if slt.checkbox(f"Display the Basic Statistics of '{i}' Column"):
                slt.write(data[i].describe())
                if slt.button('Click Here to get Code',key = i):
                    slt.code(f"slt.write(data['{i}'].describe())")
        for i in obj_data:
            if slt.checkbox(f"Display the Mode of '{i}' Column"):
                slt.write(data[i].mode(dropna = False))
                if slt.button('Click Here to get Code',key = i+' '):
                    slt.code(f"slt.write(data['{i}'].mode(dropna = False))")
        if slt.checkbox("Display the statistics of Numeric data in dataset"):
            slt.write(data.describe())
            if slt.button('Click Here to get Code',key = 'g'):
                slt.code("slt.write(data.describe())")
        slt.title("VISUALIZATION")
        ty = slt.selectbox("select Type ",['Distribution','Correlation'])
        x_l = slt.selectbox("On X - AXIS " ,list(data.columns))
        if ty == 'Correlation':
            y_l = slt.selectbox("On Y - AXIS ",list(data.columns))
        if slt.button("Plot Graph",key='fd'):
            fig,ax = plt.subplots()
            if ty == 'Distribution':
                plt.title(f"The {ty} of {x_l}")
                sns.histplot(x = x_l,data = data,kde = True,ax=ax)
                plt.xticks(rotation = 'vertical')
                slt.pyplot(fig)
            else:
                plt.title(f"The {ty} of {x_l} and {y_l}")
                sns.scatterplot(x = x_l,y = y_l,data = data,ax=ax)
                plt.xticks(rotation = 'vertical')
                slt.pyplot(fig) 
        if slt.button('Click Here to get Code',key = 'fhd'):
            if ty == 'Distribution':
                slt.code(f"""fig,ax = plt.subplots()\nplt.title("The {ty} of {x_l}")\nsns.histplot(x = '{x_l}',data = data,kde = True,ax=ax)\nplt.xticks(rotation = 'vertical')\nslt.pyplot(fig)""")
            else:
                slt.code(f"""fig,ax = plt.subplots()\nplt.title("The {ty} of {x_l} and {y_l}")\nsns.scatterplot(x = '{x_l}', y = '{y_l}',data = data,kde = True,ax=ax)\nplt.xticks(rotation = 'vertical')\nslt.pyplot(fig)""")

    
            
                                                       
