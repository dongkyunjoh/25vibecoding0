import streamlit as st
import random

# 🎨 페이지 기본 설정
st.set_page_config(
    page_title="✨ MBTI 진로 추천 마법상자 ✨",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="auto"
)

# 💜 예쁜 타이틀
st.markdown("<h1 style='text-align: center; color: hotpink;'>🌟 MBTI 유형별 진로 추천 🎯</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: mediumvioletred;'>🧠 나의 성격에 딱 맞는 멋진 직업을 찾아보자! 🚀</h3>", unsafe_allow_html=True)

# 🎭 MBTI 유형 및 추천 직업 데이터
mbti_jobs = {
    "INTJ": {
        "desc": "💡 전략적인 사색가! 창의적이고 논리적이야!",
        "jobs": ["🔬 데이터 과학자", "📊 전략 컨설턴트", "🧪 연구원"]
    },
    "INFP": {
        "desc": "🎨 감성적인 중재자! 따뜻한 마음과 상상력이 풍부해!",
        "jobs": ["✍️ 작가", "🎭 예술가", "🫂 상담가"]
    },
    "ESTJ": {
        "desc": "📋 믿음직한 관리자! 체계적이고 현실적이야!",
        "jobs": ["🏢 경영 관리자", "📈 프로젝트 매니저", "💼 세무사"]
    },
    "ESFP": {
        "desc": "🎉 사교적인 연예인! 에너지 넘치고 모두를 즐겁게 해!",
        "jobs": ["🎤 가수", "🎨 디자이너", "🎬 방송인"]
    },
    "ENTP": {
        "desc": "🧠 창의적인 발명가! 토론을 좋아하고 아이디어가 넘쳐!",
        "jobs": ["💻 스타트업 창업가", "🎙️ 방송 토론자", "🔧 제품 개발자"]
    },
    "ISFJ": {
        "desc": "🛡️ 헌신적인 수호자! 따뜻하고 꼼꼼한 스타일!",
        "jobs": ["👩‍⚕️ 간호사", "👩‍🏫 교사", "📚 사서"]
    }
    # 원하는 MBTI 계속 추가 가능!
}

# 🧩 MBTI 선택 UI
st.markdown("### 👉 아래에서 당신의 MBTI를 골라보세요!")
selected_mbti = st.selectbox("🌈 MBTI를 선택하세요", list(mbti_jobs.keys()))

# 🎁 결과 출력
if selected_mbti:
    mbti_info = mbti_jobs[selected_mbti]
    
    st.markdown(f"<h2 style='color: deepskyblue;'>🔍 {selected_mbti} 유형</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 18px; color: mediumblue;'>{mbti_info['desc']}</p>", unsafe_allow_html=True)

    st.markdown("#### 🎯 어울리는 직업 추천!")
    for job in mbti_info["jobs"]:
        st.markdown(f"- {job} 🌟")

    # 🎉 랜덤 응원 메시지
    cheer_msgs = [
        "🌟 너는 어떤 일이든 잘 해낼 수 있어!",
        "🚀 세상은 너의 재능을 기다리고 있어!",
        "💖 너만의 길을 멋지게 걸어가자!",
        "🎈 꿈을 향해 힘차게 출발~!"
    ]
    st.markdown(f"<h4 style='color: hotpink; text-align: center;'>{random.choice(cheer_msgs)}</h4>", unsafe_allow_html=True)

# 👣 푸터
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>Made with 💖 by 선생님과 AI</p>", unsafe_allow_html=True)
