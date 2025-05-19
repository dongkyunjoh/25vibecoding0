import streamlit as st
import datetime
import random

# 1. 운동 데이터 (이름 + 유튜브 링크)
exercise_data = {
    "맨몸 운동": {
        "초급": [
            {"name": "푸쉬업", "video": "https://www.youtube.com/watch?v=IODxDxX7oi4"},
            {"name": "스쿼트", "video": "https://www.youtube.com/watch?v=aclHkVaku9U"},
            {"name": "크런치", "video": "https://www.youtube.com/watch?v=Xyd_fa5zoEU"},
            {"name": "워킹 런지", "video": "https://www.youtube.com/watch?v=QOVaHwm-Q6U"},
            {"name": "점핑잭", "video": "https://www.youtube.com/watch?v=c4DAnQ6DtF8"},
        ],
        "중급": [
            {"name": "플랭크", "video": "https://www.youtube.com/watch?v=pSHjTRCQxIw"},
            {"name": "마운틴 클라이머", "video": "https://www.youtube.com/watch?v=nmwgirgXLYM"},
            {"name": "버피 테스트", "video": "https://www.youtube.com/watch?v=TU8QYVW0gDU"},
            {"name": "점프 스쿼트", "video": "https://www.youtube.com/watch?v=U4s4mEQ5VqU"},
            {"name": "파이크 푸쉬업", "video": "https://www.youtube.com/watch?v=3fTgR2WBM7Q"},
        ],
        "고급": [
            {"name": "핸드스탠드 푸쉬업", "video": "https://www.youtube.com/watch?v=Uw3h3WFaNGI"},
            {"name": "플로우 버피", "video": "https://www.youtube.com/watch?v=GWecqQzG2gI"},
            {"name": "플랭크 투 푸쉬업", "video": "https://www.youtube.com/watch?v=tUGUz9N1tzY"},
            {"name": "점프 런지", "video": "https://www.youtube.com/watch?v=1ZuAA2s1JXY"},
            {"name": "스파이더 플랭크", "video": "https://www.youtube.com/watch?v=IHj2vGkT0bM"},
        ],
    }
}

# 2. 세트/횟수 설정 함수
def get_sets_reps(level):
    if level == "초급":
        return f"{random.randint(2, 3)}세트 × {random.choice(['10~12회', '15회', '30초'])}"
    elif level == "중급":
        return f"{random.randint(3, 4)}세트 × {random.choice(['12~15회', '20회', '45초'])}"
    else:
        return f"{random.randint(4, 5)}세트 × {random.choice(['15~20회', '25회', '1분'])}"

# 3. UI 구성
st.title("🏋️ 오늘의 운동 루틴 추천")

place = st.radio("운동 장소를 선택하세요:", list(exercise_data.keys()))
level = st.radio("운동 난이도를 선택하세요:", list(exercise_data[place].keys()))

# 날짜 기반 추천
today = datetime.date.today()
random.seed(today.toordinal())

routines = random.sample(exercise_data[place][level], k=min(5, len(exercise_data[place][level])))

st.write(f"📅 날짜: {today.strftime('%Y-%m-%d')}")
st.subheader(f"📌 오늘의 운동 루틴 ({place}, {level})")

# 운동 추천 출력
for i, ex in enumerate(routines, 1):
    plan = get_sets_reps(level)
    st.markdown(f"### {i}. {ex['name']}")
    st.markdown(f"**권장 운동**: {plan}")
    st.video(ex["video"])
    st.markdown("---")
