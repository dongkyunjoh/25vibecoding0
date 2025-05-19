import streamlit as st
import datetime
import random

# 1. 운동 데이터 정의 (장소 + 난이도별)
exercises = {
    "맨몸 운동": {
        "초급": [
            "푸쉬업", "스쿼트", "크런치", "워킹 런지", "점핑잭"
        ],
        "중급": [
            "플랭크", "마운틴 클라이머", "버피 테스트", "점프 스쿼트", "파이크 푸쉬업"
        ],
        "고급": [
            "핸드스탠드 푸쉬업", "플로우 버피", "플랭크 투 푸쉬업", "점프 런지", "스파이더 플랭크"
        ]
    },
    "헬스장 운동": {
        "초급": [
            "레그 프레스", "랫풀다운", "체스트 프레스", "바이셉 컬 (머신)", "시티드 레그 컬"
        ],
        "중급": [
            "벤치프레스", "스쿼트 (바벨)", "시티드 로우", "숄더 프레스", "사이클 머신"
        ],
        "고급": [
            "데드리프트", "클린 앤 저크", "바벨 스쿼트", "덤벨 스내치", "케이블 크로스오버"
        ]
    }
}

# 2. 세트/횟수 추천 함수
def get_sets_reps(level, name):
    if level == "초급":
        sets = random.randint(2, 3)
        reps = random.choice(["10~12회", "15회", "시간 기준 30초"])
    elif level == "중급":
        sets = random.randint(3, 4)
        reps = random.choice(["12~15회", "20회", "시간 기준 45초"])
    else:  # 고급
        sets = random.randint(4, 5)
        reps = random.choice(["15~20회", "25회", "시간 기준 1분"])

    return f"{sets}세트 × {reps}"

# 3. UI 구성
st.title("🏋️ 오늘의 운동 루틴 추천")

place = st.radio("운동 장소를 선택하세요:", ("맨몸 운동", "헬스장 운동"))
level = st.radio("운동 난이도를 선택하세요:", ("초급", "중급", "고급"))

# 날짜 기반 추천
today = datetime.date.today()
random.seed(today.toordinal())

# 운동 루틴 추천
exercise_names = exercises[place][level]
selected = random.sample(exercise_names, k=min(5, len(exercise_names)))

# 4. 결과 출력
st.write(f"📅 날짜: {today.strftime('%Y-%m-%d')}")
st.subheader(f"🏃 오늘의 운동 루틴 ({place}, {level})")

for i, name in enumerate(selected, 1):
    plan = get_sets_reps(level, name)
    st.markdown(f"**{i}. {name}**  \n- 권장 운동: {plan}")
