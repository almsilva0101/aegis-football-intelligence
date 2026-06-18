import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import json
import os
import time

# =====================================================================
# 1. CONFIGURAÇÃO DE DESIGN E ESTILIZAÇÃO (CSS PREMIUM TURF)
# =====================================================================
st.set_page_config(
    page_title="AEGIS | Football Tactical Twin & Moneyball IA",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        .reportview-container .main .block-container { padding-top: 1.5rem; }
        h1, h2, h3, h4 { font-family: 'Space Grotesk', 'Segoe UI', sans-serif; font-weight: 700; color: #F8FAFC; }
        
        /* Customização dos cartões táticos de métricas futebolísticas */
        div[data-testid="stMetricValue"] { font-size: 32px !important; font-weight: 800; color: #00FF66; letter-spacing: -0.5px; }
        div[data-testid="stMetricDelta"] { font-size: 12px !important; }
        
        /* Containers de Alta Densidade (Premium Cards) */
        .card-painel {
            background-color: #0E1117;
            border: 1px solid #1E293B;
            padding: 24px;
            border-radius: 12px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        }
        
        /* Blocos explicativos obrigatórios */
        .manual-box {
            background-color: #0F172A;
            border-left: 4px solid #00FF66;
            padding: 15px;
            border-radius: 0 8px 8px 0;
            margin-bottom: 20px;
        }
        .manual-title { color: #00FF66; font-weight: bold; margin-bottom: 5px; font-size: 14px; }
        .manual-text { color: #94A3B8; font-size: 13px; line-height: 1.6; }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 2. SISTEMA DE PERSISTÊNCIA DE USUÁRIOS (JSON LOCAL)
# =====================================================================
DB_FILE = "usuarios_futebol_db.json"

def carregar_usuarios():
    if not os.path.exists(DB_FILE):
        default_db = {"cbf_director": "copa2026"}
        with open(DB_FILE, "w") as f:
            json.dump(default_db, f)
        return default_db
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return {"cbf_director": "copa2026"}

def salvar_usuario(usuario, senha):
    usuarios = carregar_usuarios()
    usuarios[usuario] = senha
    with open(DB_FILE, "w") as f:
        json.dump(usuarios, f)

if 'auth_football' not in st.session_state:
    st.session_state['auth_football'] = False

def login_cadastro_page():
    st.markdown("<h1 style='text-align: center; color: #00FF66; margin-top: 5rem; margin-bottom: 0;'>🛡️ AEGIS FOOTBALL</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748B; font-size: 15px; letter-spacing: 1px;'>Tactical Twin, Cognitive Load & Preditivo Moneyball Intelligence</p>", unsafe_allow_html=True)
    st.write("")
    
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<div class='card-painel'>", unsafe_allow_html=True)
        tab_login, tab_cadastro = st.tabs(["🔒 Acessar Vestiário", "📝 Registrar Novo Analista/Técnico"])
        
        with tab_login:
            with st.form("football_login"):
                user = st.text_input("ID do Analista / Técnico", placeholder="Ex: cbf_director").strip()
                password = st.text_input("Chave Tática de Acesso", type="password")
                if st.form_submit_button("AUTENTICAR NO CAMPUS"):
                    usuarios = carregar_usuarios()
                    if user in usuarios and usuarios[user] == password:
                        st.session_state['auth_football'] = True
                        st.rerun()
                    else:
                        st.error("❌ Credenciais táticas inválidas.")
                        
        with tab_cadastro:
            with st.form("football_register"):
                new_user = st.text_input("Novo Usuário Técnico", placeholder="Ex: guardiola_staff").strip()
                new_password = st.text_input("Senha de Acesso", type="password")
                confirm = st.text_input("Confirmar Senha", type="password")
                if st.form_submit_button("CADASTRAR NO STAFF"):
                    usuarios = carregar_usuarios()
                    if new_password != confirm: st.error("❌ As senhas não coincidem.")
                    elif new_user in usuarios: st.error("❌ Usuário já registrado no comitê.")
                    else:
                        salvar_usuario(new_user, new_password)
                        st.success("✅ Profissional cadastrado! Faça login na aba ao lado.")
        st.markdown("</div>", unsafe_allow_html=True)

def main_dashboard():
    # --- HEADER ---
    h1, h2 = st.columns([3, 1])
    with h1:
        st.markdown("<p style='color: #00FF66; font-size: 12px; font-weight: bold; letter-spacing: 2px; margin-bottom: 0;'>⚽ LIVE DATA PLATFORM // ENGINE VERSION 2.0 ACTIVE</p>", unsafe_allow_html=True)
        st.title("📊 AEGIS Football Intelligence Center")
    with h2:
        st.write("")
        if st.button("🔒 ENCERRAR SESSÃO OPERACIONAL"):
            st.session_state['auth_football'] = False
            st.rerun()
            
    st.markdown("---")

    # SIDEBAR
    st.sidebar.markdown("### 📋 Seleção de Elenco")
    atleta_ativo = st.sidebar.selectbox("Focar Monitoramento no Atleta (Abas 1 e 2):", ["Atleta 10 - Meio-Campista Armador", "Atleta 09 - Centroavante Escorador", "Atleta 04 - Zagueiro Central"])
    st.sidebar.markdown("---")
    st.sidebar.info("📡 Conexão com Coletes GPS: ATIVA (10Hz)")
    st.sidebar.success("● Motores Scouter IA: CONECTADOS")

    tab_cognitiva, tab_biomecanica, tab_espacial, tab_moneyball = st.tabs([
        "🧠 1. Fadiga Cognitiva & Decisão",
        "🦵 2. Gêmeo Biomecânico & Lesões",
        "📐 3. Ocupação Espacial & Governança",
        "💸 4. Algoritmo Moneyball & IA Scouting"
    ])

    # =====================================================================
    # ABA 1: FADIGA COGNITIVA
    # =====================================================================
    with tab_cognitiva:
        st.markdown("### 🧠 Monitoramento Preditivo de Desgaste Mental")
        st.markdown("""
        <div class='manual-box'>
            <div class='manual-title'>📘 DIRETRIZ OPERACIONAL - O QUE É, COMO FUNCIONA E PARA QUE SERVE</div>
