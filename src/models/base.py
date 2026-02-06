from abc import ABC, abstractmethod
import pandas as pd

class StockRecommender(ABC):
    """
    주식 추천 전략을 위한 추상 기본 클래스 (Strategy Pattern)
    """

    @abstractmethod
    def recommend(self, ticker_list: list) -> pd.DataFrame:
        """
        주어진 티커 리스트 중에서 추천 종목을 선별하여 반환합니다.
        
        Args:
            ticker_list (list): 분석할 종목 코드 리스트
            
        Returns:
            pd.DataFrame: 추천 종목 및 분석 결과 (Rank, Score 등 포함)
        """
        pass
