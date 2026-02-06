# 주식 추천 대시보드 (Stock Recommendation Dashboard)

## 📌 프로젝트 소개
**Live Demo:** [👉 https://mini-stock-advisor.streamlit.app/](https://mini-stock-advisor.streamlit.app/)

이 프로젝트는 **국내 주식(KRX)**과 **미국 주식(US)**의 시세를 한눈에 확인하고, AI/알고리즘 기반으로 매일 유망한 종목을 추천해주는 **웹 대시보드**입니다.
주식 초보자부터 전문가까지 가볍게 시장 흐름을 파악하고 투자 아이디어를 얻을 수 있도록 돕습니다.

## 🚀 주요 기능
- **통합 대시보드**: 국내/미국 시장의 주요 지수 및 관심 종목 시세 확인
- **AI 종목 추천**: 기술적 분석(RSI, 이동평균 등) 기반의 "오늘의 Top 3" 종목 추천
- **인기 급등주**: 실시간 변동성이 크거나 거래량이 급증하는 시장 주도주 포착
- **상세 차트 분석**: 인터랙티브 차트를 통한 주가 흐름 및 보조지표 확인

## 🛠 기술 스택
- **Language**: Python 3.10+
- **Web Framework**: Streamlit
- **Data Source**: 
  - 🇰🇷 국내: FinanceDataReader (Naver Finance)
  - 🇺🇸 미국: yfinance (Yahoo Finance)
- **Charting**: Plotly
- **Analysis**: Pandas, TA-Lib (Technical Analysis Library)

## 📂 프로젝트 구조
```bash
stock/
├── .streamlit/          # Streamlit 설정 파일
├── src/                 # 소스 코드 디렉토리
│   ├── app.py           # 메인 애플리케이션 진입점
│   ├── data/            # 데이터 수집 (Data Loader) 모듈
│   ├── models/          # 추천 알고리즘 및 AI 모델
│   └── utils.py         # 유틸리티 함수
├── requirements.txt     # 의존성 패키지 목록
└── README.md            # 프로젝트 설명서
```

## ⚡ 시작하기 (Getting Started)

### 1. 환경 설정
```bash
# 가상환경 생성 (선택사항)
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 2. 패키지 설치
```bash
pip install -r requirements.txt
```

### 3. 실행
```bash
streamlit run src/app.py
```
