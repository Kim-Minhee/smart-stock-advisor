# 기본적으로 모니터링할 인기 종목 리스트 (티커: 종목명)
KR_TICKERS = {
    '005930': '삼성전자',
    '000660': 'SK하이닉스',
    '035420': 'NAVER',
    '035720': '카카오',
    '005380': '현대차',
    '000270': '기아',
    '051910': 'LG화학',
    '006400': '삼성SDI',
    '207940': '삼성바이오로직스',
    '068270': '셀트리온'
}

US_TICKERS = {
    'AAPL': 'Apple',
    'MSFT': 'Microsoft',
    'GOOGL': 'Alphabet (Google)',
    'AMZN': 'Amazon',
    'TSLA': 'Tesla',
    'NVDA': 'NVIDIA',
    'META': 'Meta (Facebook)',
    'NFLX': 'Netflix',
    'AMD': 'AMD',
    'INTC': 'Intel',
    'QCOM': 'Qualcomm',
    'SBUX': 'Starbucks',
    'KO': 'Coca-Cola',
    'PEP': 'PepsiCo',
    'DIS': 'Disney'
}

def format_currency(value, currency="KRW"):
    """통화 포맷팅 함수"""
    if currency == "KRW":
        return f"₩{value:,.0f}"
    else:
        return f"${value:,.2f}"
