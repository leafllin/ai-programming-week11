import pandas as pd


def 정제(df):
    cleaned = df.copy()  # 원본 df를 직접 수정하지 않는다.

    cleaned = cleaned.dropna(subset=["점수"])  # 점수가 비어 있는 행을 삭제한다.
    print(len(cleaned))

    cleaned = cleaned.drop_duplicates()  # 완전히 같은 행 하나만 남긴다.
    print(len(cleaned))

    cleaned["반"] = cleaned["반"].str.strip()  # 반 앞뒤 공백을 제거한다.
    cleaned["과목"] = cleaned["과목"].str.strip()  # 과목 앞뒤 공백을 제거한다.
    print(len(cleaned))

    cleaned["점수"] = pd.to_numeric(cleaned["점수"], errors="coerce")
    cleaned = cleaned.dropna(subset=["점수"])
    cleaned = cleaned[cleaned["점수"].between(0, 100)]  # 점수 범위를 벗어난 행을 삭제한다.
    print(len(cleaned))

    return cleaned


def 반별평균(df):
    averages = df.groupby("반")["점수"].mean().round(2)  # 반별 평균을 소수 둘째 자리까지 낸다.
    return averages


if __name__ == "__main__":
    df = pd.read_csv("week12/scores_2026.csv", encoding="utf-8")
    df = 정제(df)

    math_df = df[df["과목"] == "수학"]  # 과목이 수학인 행만 남긴다.
    print(len(math_df))

    class_1_high = df[(df["반"] == "1반") & (df["점수"] >= 90)]  # 1반이면서 90점 이상인 행만 남긴다.
    print(len(class_1_high))

    print(df.groupby("반")["점수"].mean())  # 반별 점수 평균을 출력한다.
    print(df.groupby(["과목", "반"])["점수"].mean())  # 과목과 반 기준 평균을 출력한다.

    statistics = df.groupby("반")["점수"].agg(["count", "mean", "median", "max"]).round(2)
    print(statistics)
