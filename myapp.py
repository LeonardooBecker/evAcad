import streamlit as st
import pandas as pd
from datetime import date

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)

partes=["inferiores","quadriceps","panturrilha","costas", "biceps", "peito", "triceps", "ombro"]

escolha=st.multiselect("Treino",partes)


# Inferiores : Leg press, agachamento, cadeira flexora, mesa flexora, stiff, panturrilha sentado, panturrilha smith.
# Quadríceps: Leg press, agachamento, hack, cadeira extensora, afundo, panturrilha sentado, panturrilha smith
# Costas: Barra, Puxada aberta, Puxada triângulo, remada baixa, cavalinho, remada curvada, terra, pull down
# Bíceps: Rosca alternada, rosca alternada 45º, rosca direta, rosca martelo, rosca invertida, rosca concetrada.
# Peito: reto barra, reto halter, inclinado barra, inclinado halter, crucifixo reto, crucifixo inclinado, paralela, cross over alto, cross over baixo
# Triceps: Triceps testa, triceps corda, frances.
# Ombro: dev barra, dev halter, elevação lateral, elevação frontal, crucifixo invertido.

inferiores=["cadeira flexora", "mesa flexora", "stiff"]
quadriceps=["leg press", "agachamento", "hack", "cadeira extensora", "afundo"]
panturrilha=["panturrilha sentado","panturrilha smith"]
costas=["barra", "puxada aberta", "puxada triângulo", "remada baixa", "cavalinho", "remada curvada", "terra", "pull down"]
biceps=["alternada", "alternada 45º", "direta", "martelo", "invertida", "rosca"]
peito=["reto barra", "reto halter", "inclinado barra", "inclinado halter", "crucifixo reto", "crucifixo inclinado", "paralela", "cross over alto", "cross over baixo"]
triceps=["triceps testa", "triceps corda", "frances"]
ombro=["dev barra", "dev halter", "elevação lateral", "elevação frontal", "crucifixo invertido"]

treinos=[]
treinos.append(inferiores)
treinos.append(quadriceps)
treinos.append(costas)
treinos.append(biceps)
treinos.append(peito)
treinos.append(triceps)
treinos.append(ombro)


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


st.write(exercicios)

tam=[]
number=[10]

tamanho=len(exercicios)

tam=st.columns(tamanho)

for i in range(tamanho):
    with tam[i]:
        st.write(exercicios[i])
        number=st.number_input("digite numero", key=i)

current_time=date.today()




col1, col2, col3, col4= st.columns(4)

with col1:
    st.write("oi")