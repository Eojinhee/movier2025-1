import pandas as pd
from click.testing import Result


def random_items():
    movies_df = pd.read_csv("data/movies_final.csv")
    movies_df = movies_df.fillna('')
    result_items = movies_df.sample(n=10).to_dict("records")
    return result_items

def random_genres_items(genre):
    movies_df = pd.read_csv("data/movies_final.csv")
    genre_df = movies_df[ movies_df['genres'].apply(lambda  x: genre in x.lower())]
    genre_df = genre_df.fill('')
    # Todo 선택한 장르의 갯수가 5보다 작은 경우 처리 해야함
    result_items = genre_df.sample(n=5).to_dict("recodes")
    return result_items

# Todo1 지정된 장르를 포함한 영화중 평점이 높은 5개의 영화를 추천함
# 단 추천인수가 5명 이상
def random_genres_items_best(genre):
    movies_df = pd.read_csv("data/movies_final.csv")
    genre_df = movies_df[ movies_df['genres'].apply(lambda  x: genre in x.lower())]
    genre_df = genre_df.fill('')
    # Todo2 선택한 장르의 갯수가 5보다 작은 경우 처리 해야함
    result_items = genre_df.query('rcount >= 5').sort_values(by='rmean',ascending=False).head(5).to_dict("recodes")
    return result_items