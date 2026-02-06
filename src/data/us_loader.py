import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

class UsLoader:
    """
    미국 주식 데이터 로더 (yfinance 사용)
    """

    def get_price_data(self, ticker: str, start_date: str = None, end_date: str = None) -> pd.DataFrame:
        """
        지정된 기간 동안의 종목 주가 데이터를 가져옵니다.
        
        Args:
            ticker (str): 종목 티커 (예: 'AAPL')
            start_date (str, optional): 시작일 (YYYY-MM-DD). 기본값은 1년 전.
            end_date (str, optional): 종료일 (YYYY-MM-DD). 기본값은 오늘.
            
        Returns:
            pd.DataFrame: 주가 데이터 (Open, High, Low, Close, Volume 등)
        """
        if not start_date:
            start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
        
        if not end_date:
            end_date = datetime.now().strftime('%Y-%m-%d')

        try:
            ticker_obj = yf.Ticker(ticker)
            # auto_adjust=True: 배당/분할 수정 주가 사용
            df = ticker_obj.history(start=start_date, end=end_date, auto_adjust=True)
            return df
        except Exception as e:
            print(f"Error fetching US data for {ticker}: {e}")
            return pd.DataFrame()
