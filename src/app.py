import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.models.technical import TechnicalAnalysisRecommender
from src.data.factory import DataLoaderFactory
from src.utils import KR_TICKERS, US_TICKERS, format_currency

st.set_page_config(page_title="Stock AI Dashboard", page_icon="📈", layout="wide")

st.title("📈 AI 주식 추천 대시보드")
st.markdown("""
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

st.sidebar.header("설정 (Settings)")
market_type = st.sidebar.radio("시장 선택", ["🇰🇷 국내 주식 (KRX)", "🇺🇸 미국 주식 (US)"])

# @st.cache_resource
def get_recommender():
    return TechnicalAnalysisRecommender()

recommender = get_recommender()
loader_factory = DataLoaderFactory()

if "국내" in market_type:
    selected_tickers = KR_TICKERS
    currency_symbol = "KRW"
else:
    selected_tickers = US_TICKERS
    currency_symbol = "USD"

tab1, tab2, tab3 = st.tabs(["💡 AI 추천", "📊 시장 트렌드", "🔎 상세 분석"])

with tab1:
    st.subheader(f"오늘의 {market_type} AI 추천 Top 3")
    
    with st.spinner('AI가 종목을 분석 중입니다...'):
        df_recommend = recommender.recommend(selected_tickers)
    
    if not df_recommend.empty:
        top3 = df_recommend.head(3)
        cols = st.columns(3)
        
        for idx, row in top3.iterrows():
            with cols[idx]:
                st.metric(
                    label=f"{row['Name']} ({row['Ticker']})", # 이름 표기
                    value=format_currency(row['Close'], currency_symbol),
                    delta=f"{row['Change']}%"
                )
                st.info(f"💡 {row['Reason']} (Score: {row['Score']})")
        
        st.markdown("---")
        st.write("### 전체 분석 결과")
        # 컬럼 순서 재배치
        st.dataframe(
            df_recommend[['Name', 'Ticker', 'Close', 'Change', 'RSI', 'Score', 'Reason']], 
            use_container_width=True
        )
    else:
        st.error("데이터를 불러오는데 실패했습니다.")

with tab2:
    st.subheader("🔥 변동성 Top 5")
    if not df_recommend.empty:
        df_recommend['AbsChange'] = df_recommend['Change'].abs()
        df_volatility = df_recommend.sort_values(by='AbsChange', ascending=False).head(5)
        
        st.table(df_volatility[['Name', 'Ticker', 'Close', 'Change', 'Score']])
    else:
        st.info("데이터가 없습니다.")

with tab3:
    st.subheader("차트 및 상세 데이터")
    # 딕셔너리에서 이름만 추출하여 선택 목록 생성
    # 선택박스는 '이름 (코드)' 형식으로 표시
    options = {f"{name} ({code})": code for code, name in selected_tickers.items()}
    selected_option = st.selectbox("종목 선택", list(options.keys()))
    selected_code = options[selected_option]
    
    if st.button("차트 보기"):
        st.write(f"### {selected_option} 주가 흐름")
        loader = loader_factory.get_loader(selected_code)
        df_chart = loader.get_price_data(selected_code)
        
        if not df_chart.empty:
            fig = go.Figure(data=[go.Candlestick(
                x=df_chart.index,
                open=df_chart['Open'],
                high=df_chart['High'],
                low=df_chart['Low'],
                close=df_chart['Close']
            )])
            fig.update_layout(xaxis_rangeslider_visible=True, height=500)
            st.plotly_chart(fig, use_container_width=True)
            
            st.write("### 최근 데이터")
            st.dataframe(df_chart.tail(10))
        else:
            st.error("차트 데이터를 불러올 수 없습니다.")
