import streamlit as st

# 4가지 MBTI별 운동 추천 데이터
exercise_recommendations = {
    'ESTP': {
        '맨몸 운동': '인터벌 훈련과 부트캠프 스타일 운동',
        '헬스장 운동': '복합운동 (케틀벨, 박스 점프 등)'
    },
    'ISTP': {
        '맨몸 운동': '칼리스테닉스 (기술 도전형 운동)',
        '헬스장 운동': '자유 웨이트와 TRX 운동'
    },
    'ISFP': {
        '맨몸 운동': '플로우 기반 운동 (바디 컴배트 등)',
        '헬스장 운동': '소도구 운동과 자유로운 환경 운동'
    },
    'ESFP': {
        '맨몸 운동': '리듬감 있는 줌바와 댄스',
        '헬스장 운동': 'HIIT + 음악, 친구와 함께하는 운동'
    },
}

st.title("MBTI 기반 운동 추천 웹앱")

mbti = st.selectbox("당신의 MBTI를 선택하세요:", options=list(exercise_recommendations.keys()))

exercise_type = st.radio("운동 종류를 선택하세요:", ('맨몸 운동', '헬스장 운동'))

if mbti and exercise_type:
    recommendation = exercise_recommendations[mbti][exercise_type]
    st.subheader(f"{mbti} 유형에게 맞는 {exercise_type} 추천:")
    st.write(recommendation)
