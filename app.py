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
            <div class='manual-text'>
                <b>O que é:</b> Um indicador proprietário que calcula a velocidade de processamento cerebral do jogador sob pressão física e tática.<br>
                <b>Como funciona:</b> Cruza o tempo de reação do passe (capturado por visão computacional) com os picos de frequência cardíaca.<br>
                <b>Para que serve:</b> Substituir atletas antes que o cansaço mental gere erros cruciais de posicionamento ou perda de posse de bola.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Eficiência de Tomada de Decisão", "84.5%", "-3.2% nos últimos 10min")
        m2.metric("Tempo Médio de Reação", "0.42s", "+0.11s de atraso", delta_color="inverse")
        m3.metric("Distância Percorrida Total", "9.42 km", "Alta Intensidade")
        m4.metric("Índice de Estresse Mental (IA)", "6.8 / 10", "Alerta Amarelo")

        minutos = np.linspace(1, 90, 90)
        eficiencia = 100 - (minutos * 0.2) - (np.random.randn(90) * 1.5)
        eficiencia[65:] -= 12 
        
        fig_cog = px.line(x=minutos, y=eficiencia, labels={'x': 'Minuto da Partida', 'y': 'Lucidez de Tomada de Decisão (%)'}, color_discrete_sequence=['#00FF66'])
        fig_cog.update_layout(paper_bgcolor='#0E1117', plot_bgcolor='#0E1117', font_color='white', height=250)
        st.plotly_chart(fig_cog, use_container_width=True)

    # =====================================================================
    # ABA 2: GÊMEO BIOMECÂNICO
    # =====================================================================
    with tab_biomecanica:
        st.markdown("### 🦵 Análise de Assimetria Cinemática e Risco de Lesão")
        st.markdown("""
        <div class='manual-box'>
            <div class='manual-title'>📘 DIRETRIZ OPERACIONAL - O QUE É, COMO FUNCIONA E PARA QUE SERVE</div>
            <div class='manual-text'>
                <b>O que é:</b> Um espelho biomecânico que monitora o balanço de forças nas articulações inferiores durante o jogo.<br>
                <b>Como funciona:</b> Sensores de aceleração nos coletes captam a força de frenagem e arranque, medindo descompensações de carga.<br>
                <b>Para que serve:</b> Prevek estiramentos e lesões de ligamento (LCA) antes que ocorram, sugerindo janelas protetivas de substituição.
            </div>
        </div>
        """, unsafe_allow_html=True)

        col_bio_esq, col_bio_dir = st.columns([1, 1])
        with col_bio_esq:
            st.markdown("#### Distribuição de Sobrecarga Articular Dinâmica")
            categorias = ['Aceleração', 'Frenagem Aguda', 'Mudança de Direção', 'Impacto de Passada', 'Estabilidade Pélvica']
            fig_radar = go.Figure()
            fig_radar.add_trace(go.Scatterpolar(r=[85, 90, 75, 80, 88], theta=categorias, fill='toself', name='Perna Direita', line=dict(color='#00FF66')))
            fig_radar.add_trace(go.Scatterpolar(r=[70, 72, 60, 82, 85], theta=categorias, fill='toself', name='Perna Esquerda (Compensando)', line=dict(color='#FF2E93')))
            fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), paper_bgcolor='#0E1117', font_color='white', height=300, margin=dict(t=30, b=30))
            st.plotly_chart(fig_radar, use_container_width=True)
            
        with col_bio_dir:
            st.markdown("#### Painel Clínico Preditivo do Gêmeo Digital")
            st.markdown("<div class='card-painel'>", unsafe_allow_html=True)
            st.error("🚨 ALERTA MÉDICO: Assimetria Crítica detectada no Isquiotibial Esquerdo (Diferença de 15% na frenagem excêntrica).")
            st.warning("⚠️ Recomendação da IA: Limite operacional de sprint atingido. Substituição preventiva urgente.")
            st.write(f"**Atleta Selecionado:** {atleta_ativo}")
            st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================================
    # ABA 3: ESPACIAL & GOVERNANÇA DE APIs
    # =====================================================================
    with tab_espacial:
        st.markdown("### 📐 Mapa de Ocupação Espacial Dinâmica e Matriz de Ingestão de Dados")
        st.markdown("""
        <div class='manual-box'>
            <div class='manual-title'>📘 DIRETRIZ OPERACIONAL - O QUE É, COMO FUNCIONA E PARA QUE SERVE</div>
            <div class='manual-text'>
                <b>O que é:</b> Um orrery tático bidimensional do campo que calcula a compactação de blocos e linhas de passes seguras.<br>
                <b>Como funciona:</b> Processa os vetores de posicionamento dos atletas em relação à bola para identificar vulnerabilidades estruturais.<br>
                <b>Para que serve:</b> Ajustar as estratégias de pressão defensiva e amplitude de ataque durante os treinos ou no intervalo da partida.
            </div>
        </div>
        """, unsafe_allow_html=True)

        col_esp_mapa, col_esp_api = st.columns([1, 1.2])
        with col_esp_mapa:
            st.markdown("#### Simulação Espacial de Compactação de Bloco")
            x_jogadores = [10, 15, 12, 25, 30, 22, 5, -5, -12, 0]
            y_jogadores = [5, -8, 12, 15, 0, -14, -2, 10, -5, 2]
            cores = ['#00FF66']*6 + ['#FF2E93']*4
            
            fig_campo = px.scatter(x=x_jogadores, y=y_jogadores, color=cores, color_discrete_map={'#00FF66':'Mandante', '#FF2E93':'Visitante'}, text=[f"P{i}" for i in range(10)])
            fig_campo.update_traces(marker=dict(size=18, line=dict(width=2, color='white')), textposition="top center")
            fig_campo.update_layout(
                paper_bgcolor='#0E1117', plot_bgcolor='#020617', font_color='white', height=300, margin=dict(t=10),
                xaxis=dict(showgrid=True, gridcolor='#1E293B', range=[-30, 40]), yaxis=dict(showgrid=True, gridcolor='#1E293B', range=[-25, 25])
            )
            st.plotly_chart(fig_campo, use_container_width=True)

        with col_esp_api:
            st.markdown("#### 🔌 Matriz de Integração de APIs de Ingestão de Dados (Data Governance)")
            api_football_data = {
                "Vetor de Informação": ["Coordenadas X, Y dos Atletas", "Frequência Cardíaca/Métrica Interna", "Histórico Clínico e Contratos", "Eventos de Jogo (Passes/Faltas)", "Mapeamento Biomecânico de Transmissão"],
                "Provedor Oficial": ["ChyronHego / TRACAB API", "Catapult Sports Cloud", "Transfermarkt / FBref Ledger", "StatsPerform / Opta API", "Second Spectrum Vision API"],
                "Endpoint Tecnológico Integrado": ["api.chyronhego.com/v2/tracking", "api.catapultsports.com/v4/metrics", "internal.aegis.football/scouting", "api.statsperform.com/v1/football", "api.secondspectrum.com/v1/vision"],
                "Protocolo / Taxa Ingestão": ["Stream Binário // 25fps", "REST JSON // 10Hz", "Batch Diário // JSON", "REST Webhook // Event-Driven", "Websocket Live // 30fps"]
            }
            st.dataframe(pd.DataFrame(api_football_data), use_container_width=True, hide_index=True)

    # =====================================================================
    # ABA 4: ALGORITMO MONEYBALL E SCOUTING IA
    # =====================================================================
    with tab_moneyball:
        st.markdown("### 💸 Algoritmo Moneyball Inteligente: Identificação de Atletas Subestimados e de Baixo Custo")
        st.markdown("""
        <div class='manual-box'>
            <div class='manual-title'>📘 DIRETRIZ OPERACIONAL - O QUE É, COMO FUNCIONA E PARA QUE SERVE</div>
            <div class='manual-text'>
                <b>O que é:</b> Um motor analítico preditivo de Machine Learning voltado para recrutamento de alta eficiência de custo.<br>
                <b>Como funciona:</b> O algoritmo varre bases de dados internacionais de ligas secundárias e calcula o <b>Score de Eficiência Estatística</b> (combinando passes progressivos, desarmes, xG e assistências) em relação ao <b>Valor de Mercado</b> do jogador.<br>
                <b>Para que serve:</b> Encontrar talentos de elite ocultos no mercado global por preços extremamente baixos, garantindo retorno esportivo e financeiro massivo para os clubes e federações.<br>
                <b>API de Integração Pública:</b> Consome metadados estruturados de mercado via <b>Wyscout Open API</b> (<code>api.wyscout.com/v3/players</code>) e históricos do <b>Transfermarkt API Gateway</b>.
            </div>
        </div>
        """, unsafe_allow_html=True)

        scouting_data = {
            "Nome do Atleta": ["Mateo Kovacevic", "Lukas Nielsen", "Gabriel Barbosa Jr.", "Amara Diallo", "Hiroshi Tanaka", "Santiago Rossi", "Alan Kardec Sol", "Viktor Ivanov"],
            "Posição": ["Volante Construtor", "Zagueiro Central", "Lateral Esquerdo", "Ponta Velocista", "Meia Central", "Centroavante", "Meia Atacante", "Volante de Contenção"],
            "Idade": [22, 23, 21, 20, 24, 22, 19, 23],
            "Liga Atual": ["2ª Divisão Croácia", "Liga Dinamarquesa", "Série B Brasileira", "Campeonato Senegalês", "J2 League (Japão)", "Liga Uruguaia", "Campeonato Paranaense", "Liga Búlgara"],
            "Score de IA (Performance)": [89.2, 85.0, 87.4, 91.1, 83.5, 86.0, 92.4, 82.1],
            "Valor de Mercado": ["€ 450K", "€ 800K", "€ 600K", "€ 200K", "€ 500K", "€ 750K", "€ 150K", "€ 300K"],
            "Status de Recomendação IA": ["🔥 Alvo Crítico (Pechincha)", "✅ Altamente Recomendado", "🔥 Alvo Crítico (Pechincha)", "💎 Joia Oculta Subestimada", "✅ Recomendado", "✅ Recomendado", "💎 Joia Oculta Subestimada", "⚠️ Avaliar Monitoramento"]
        }
        df_scouting = pd.DataFrame(scouting_data)
        
        col_filtro1, col_filtro2 = st.columns([1, 2])
        with col_filtro1:
            st.markdown("#### Filtros Estratégicos")
            filtro_posicao = st.multiselect("Filtrar por Posição:", options=list(df_scouting["Posição"].unique()), default=list(df_scouting["Posição"].unique()))
            df_filtrado = df_scouting[df_scouting["Posição"].isin(filtro_posicao)]
            
            st.markdown("<div class='card-painel'>", unsafe_allow_html=True)
            st.write("**Resumo do Algoritmo:**")
            st.write("📈 Total de Alvos Mapeados: **1.420**")
            st.write("🎯 Margem de Erro do Modelo: **± 2.4%**")
            st.write("💎 Maior ROI Identificado hoje: **Alan Kardec Sol**")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col_filtro2:
            st.markdown("#### Matriz de Custo x Performance (Anomalias de Mercado)")
            np.random.seed(42)
            n_mercado = 40
            perf_sim = np.random.uniform(50, 95, n_mercado)
            custo_sim = (perf_sim * np.random.uniform(0.1, 0.4, n_mercado)) + np.random.uniform(0.5, 12, n_mercado)
            
            perf_sim = np.append(perf_sim, [92.4, 91.1, 89.2])
            custo_sim = np.append(custo_sim, [0.15, 0.20, 0.45])
            nomes_sim = ["Outros Atletas"]*n_mercado + ["Alan Kardec Sol", "Amara Diallo", "Mateo Kovacevic"]
            
            df_chart = pd.DataFrame({"Performance (Score IA)": perf_sim, "Custo Estimado (€ Milhões)": custo_sim, "Atleta": nomes_sim})
            
            fig_money = px.scatter(df_chart, x="Custo Estimado (€ Milhões)", y="Performance (Score IA)", color="Atleta",
                                   color_discrete_map={"Outros Atletas": "#334155", "Alan Kardec Sol": "#00FF66", "Amara Diallo": "#00E5FF", "Mateo Kovacevic": "#FFD600"})
            fig_money.update_traces(marker=dict(size=14, opacity=0.85))
            fig_money.update_layout(paper_bgcolor='#0E1117', plot_bgcolor='#0E1117', font_color='white', height=300, margin=dict(t=10, b=10))
            st.plotly_chart(fig_money, use_container_width=True)

        st.markdown("#### 🎯 Alvos Identificados pelo Sistema de Recomendações")
        st.dataframe(df_filtrado, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #334155; font-size: 11px;'>SISTEMA DE INTELIGÊNCIA TÁTICA, DEFESA BIOMECÂNICA E RETORNO FINANCEIRO AEGIS FOOTBALL © 2026 // ACESSO RESTRITO</p>", unsafe_allow_html=True)

# Inicializador Root Controlado
if not st.session_state['auth_football']:
    login_cadastro_page()
else:
    main_dashboard()
