import pandas as pd

from analysis import 정제, 반별평균


scores_path = "week12/scores_2026.csv"
df = pd.read_csv(scores_path, encoding="utf-8")
cleaned_df = 정제(df)


def test_cleaned_row_count():
    assert len(cleaned_df) == 100


def test_cleaned_class_names():
    assert set(cleaned_df["반"].unique()) == {"1반", "2반"}


def test_grouped_score_sum_equals_total():
    grouped_sum = cleaned_df.groupby("반")["점수"].sum().sum()
    assert grouped_sum == cleaned_df["점수"].sum()


def test_mini_class_1_average():
    mini_df = pd.read_csv("week12/mini.csv", encoding="utf-8")
    mini_cleaned = 정제(mini_df)
    averages = 반별평균(mini_cleaned)
    assert averages["1반"] == 80.0
