import FinanceDataReader as fdr
import pandas as pd
from datetime import datetime, timedelta

class KrLoader:
    """
    국내 주식 데이터 로더 (FinanceDataReader 사용)
    """

    def get_price_data(self, ticker: str, start_date: str = None, end_date: str = None) -> pd.DataFrame:
        """
        지정된 기간 동안의 종목 주가 데이터를 가져옵니다.
        
        Args:
            ticker (str): 종목 코드 (예: '005930')
            start_date (str, optional): 시작일 (YYYY-MM-DD). 기본값은 1년 전.
            end_date (str, optional): 종료일 (YYYY-MM-DD). 기본값은 오늘.
            
        Returns:
            pd.DataFrame: 주가 데이터 (Date, Open, High, Low, Close, Volume, Change)
        """
        if not start_date:
            # 기본값 1년 전
            start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
        
        if not end_date:
            end_date = datetime.now().strftime('%Y-%m-%d')

        # FinanceDataReader를 통해 데이터 조회
        # KRX 종목은 기본적으로 숫자 6자리임
        try:
            df = fdr.DataReader(ticker, start_date, end_date)
            return df
        except Exception as e:
            print(f"Error fetching KR data for {ticker}: {e}")
            return pd.DataFrame()
