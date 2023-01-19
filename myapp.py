import streamlit as st
import pandas as pd
from datetime import date
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import style

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)


current_time=date.today()

dfAux=pd.read_csv("treinos.csv",sep=",")

if len(dfAux)>0:
    dd=str((dfAux.loc[(len(dfAux)-1)])["dia"])
# if(dd==str(current_time)):


partes=["inferiores","quadriceps","panturrilha","costas", "biceps", "peito", "triceps", "ombro"]

escolha=st.multiselect("Treino",partes)

inferiores=["cadeira flexora", "mesa flexora", "stiff"]
quadriceps=["leg press", "agachamento", "hack", "cadeira extensora", "afundo"]
panturrilha=["panturrilha sentado","panturrilha smith"]
costas=["barra", "puxada aberta", "puxada triângulo", "remada baixa", "cavalinho", "remada curvada", "terra", "pull down"]
biceps=["alternada", "alternada 45", "direta", "martelo", "invertida", "rosca"]
peito=["reto barra", "reto halter", "inclinado barra", "inclinado halter", "crucifixo reto", "crucifixo inclinado", "paralela", "cross over alto", "cross over baixo"]
triceps=["triceps testa", "triceps corda", "frances"]
ombro=["dev barra", "dev halter", "elevação lateral", "elevação frontal", "crucifixo invertido"]

treinos=[]
treinos.append(["inferiores",inferiores])
treinos.append(["quadriceps",quadriceps])
treinos.append(["costas",costas])
treinos.append(["biceps",biceps])
treinos.append(["peito",peito])
treinos.append(["triceps",triceps])
treinos.append(["ombro",ombro])


exercicios=[]
for i in escolha:
    if (i=="inferiores"):
        exercicios.extend(inferiores)
    if(i=="quadriceps"):
        exercicios.extend(quadriceps)
    if(i=="panturrilha"):
        exercicios.extend(panturrilha)
    if(i=="costas"):
        exercicios.extend(costas)
    if(i=="biceps"):
        exercicios.extend(biceps)
    if(i=="peito"):
        exercicios.extend(peito)
    if(i=="triceps"):
        exercicios.extend(triceps)
    if(i=="ombro"):
        exercicios.extend(ombro)

tam=[]
number=[]

tamanho=len(exercicios)

if tamanho>0:   
    with st.form(key="form1"):
        tam=st.columns(tamanho+1)
        tam[tamanho]=st.date_input("insira data")
        for i in range(tamanho):
            with tam[i]:
                st.write(exercicios[i])
                valor=st.number_input("Digite o valor", key=i)
                number.append([valor,exercicios[i]])
        if (st.form_submit_button()):
            st.experimental_rerun()

df=pd.read_csv("treinos.csv",sep=",")

dfInsert=pd.DataFrame()

for i in number:
    if(i[0]!=0):
        dfInsert[(i[1])]=[(i[0])]

treino=""
if escolha is not None:
    escolha.sort()
    for i in escolha:
        if(treino==""):
            treino=str(i)
        else:
            treino=treino+' + '+str(i)
dfInsert["treino"]=treino
if tamanho>0:
    dfInsert["dia"]=tam[tamanho]


dfResul=pd.concat([df,dfInsert],ignore_index=True)
dfResul.to_csv("treinos.csv",index=False)

qnt_treinos=len(dfResul)
st.write(f"No total foram realizados {qnt_treinos} treinos")
all_treinos=pd.Series.unique(dfResul["treino"])
all_treinos.tolist()
cont_treinos=[]

for i in all_treinos:
    dfCorte=dfResul[dfResul["treino"]==i]
    cont_treinos.append([i,len(dfCorte)])

for i in cont_treinos:
    st.write(f"{i[1]} treinos de {i[0]}")

style.use('fivethirtyeight')


colunas=st.columns(len(treinos))

cont=0
for treino in treinos:
    df_graph=pd.DataFrame()
    for i in treino[1]:
        df_graph[i]=(dfResul[i])
    df_graph["dia"]=dfResul["dia"]
    df_graph=df_graph.set_index("dia")

    keys=df_graph.keys()

    for j in range (len(keys)):
        for i in range (len(df_graph)):
            valor=df_graph.iloc[i,j]
            if(math.isnan(valor)):
                if(i>0):
                    df_graph.iloc[i,j]=df_graph.iloc[(i-1),j]
                else:
                    df_graph.iloc[i,j]=0
    with colunas[cont]:
        st.title(treino[0])
        plt.plot(df_graph)
        st.pyplot(plt)
        plt.clf()
    cont+=1

# dias=[]
# for i in range(len(dfResul)):
#     dias.append(i)
# st.write(dias)

# plt.stackplot(dias,(vet[0].tolist()),(vet[2].tolist()))
# plt.tight_layout()
# plt.show()