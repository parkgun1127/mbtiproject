import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="MBTI 포켓몬 매칭",
    page_icon="⚡",
    layout="centered"
)

# MBTI별 포켓몬 데이터
mbti_pokemon = {
    "INTJ": {
        "name": "뮤츠",
        "emoji": "🧠",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "description": "전략적이고 신비로운 천재! 깊은 사고력과 강한 정신력의 소유자예요.",
        "traits": ["🎯 전략가", "🔮 직관적", "💪 독립적"]
    },
    "INTP": {
        "name": "폴리곤",
        "emoji": "💻",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/137.png",
        "description": "논리적이고 분석적인 사고의 달인! 호기심 가득한 탐구자예요.",
        "traits": ["🔬 분석적", "💡 창의적", "🧩 논리적"]
    },
    "ENTJ": {
        "name": "리자몽",
        "emoji": "🔥",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
        "description": "타고난 리더십과 카리스마! 목표를 향해 불타오르는 지도자예요.",
        "traits": ["👑 리더십", "🎯 목표지향", "🔥 열정적"]
    },
    "ENTP": {
        "name": "겐가",
        "emoji": "😈",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
        "description": "장난기 가득한 발명가! 새로운 아이디어로 세상을 놀라게 해요.",
        "traits": ["💭 창의적", "🎭 재치있음", "🚀 도전적"]
    },
    "INFJ": {
        "name": "루카리오",
        "emoji": "✨",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "description": "파동을 읽는 통찰의 소유자! 깊은 공감 능력과 신념을 가진 수호자예요.",
        "traits": ["🌟 통찰력", "💖 공감능력", "🛡️ 신념"]
    },
    "INFP": {
        "name": "이브이",
        "emoji": "🌸",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "description": "무한한 가능성을 품은 몽상가! 순수하고 따뜻한 마음의 소유자예요.",
        "traits": ["💭 이상주의", "🎨 감성적", "🌱 성장형"]
    },
    "ENFJ": {
        "name": "푸린",
        "emoji": "🎤",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
        "description": "모두를 행복하게 만드는 매력덩어리! 따뜻한 카리스마의 소유자예요.",
        "traits": ["💕 따뜻함", "🎵 매력적", "🤝 사교적"]
    },
    "ENFP": {
        "name": "피카츄",
        "emoji": "⚡",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        "description": "에너지 넘치는 자유로운 영혼! 어디서든 빛나는 분위기 메이커예요.",
        "traits": ["⚡ 에너지", "🌈 자유로움", "😄 긍정적"]
    },
    "ISTJ": {
        "name": "거북왕",
        "emoji": "🛡️",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png",
        "description": "믿음직한 책임감의 화신! 듬직하고 성실한 모범생이에요.",
        "traits": ["📋 체계적", "💪 책임감", "🏛️ 신뢰성"]
    },
    "ISFJ": {
        "name": "해피너스",
        "emoji": "💝",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png",
        "description": "모두를 보살피는 따뜻한 수호천사! 헌신적이고 다정한 친구예요.",
        "traits": ["💗 헌신적", "🤗 다정함", "🌷 배려심"]
    },
    "ESTJ": {
        "name": "갸라도스",
        "emoji": "🌊",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/130.png",
        "description": "강력한 통솔력의 실행가! 목표를 향해 거침없이 나아가요.",
        "traits": ["⚔️ 결단력", "📊 조직력", "🎯 실행력"]
    },
    "ESFJ": {
        "name": "라프라스",
        "emoji": "🐉",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/131.png",
        "description": "모두를 품어주는 마음의 안식처! 친절하고 협조적인 친구예요.",
        "traits": ["🤲 친절함", "🌊 포용력", "👥 협동심"]
    },
    "ISTP": {
        "name": "스라크",
        "emoji": "🗡️",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/123.png",
        "description": "쿨하고 능숙한 만능 해결사! 위기 상황에서 빛나는 실력자예요.",
        "traits": ["🔧 손재주", "🧊 침착함", "⚡ 순발력"]
    },
    "ISFP": {
        "name": "이상해꽃",
        "emoji": "🌺",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/3.png",
        "description": "자연을 닮은 부드러운 예술가! 평화롭고 감성적인 영혼이에요.",
        "traits": ["🎨 예술적", "🍃 평화로움", "💚 감성적"]
    },
    "ESTP": {
        "name": "잠만보",
        "emoji": "💥",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png",
        "description": "현재를 즐기는 모험가! 활동적이고 거침없는 행동파예요.",
        "traits": ["🎢 모험심", "💪 활동적", "🎲 즉흥적"]
    },
    "ESFP": {
        "name": "뮤",
        "emoji": "🎉",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png",
        "description": "사랑스러운 분위기 메이커! 호기심 많고 즐거움이 넘치는 친구예요.",
        "traits": ["🎀 사랑스러움", "🌟 활발함", "🎪 유쾌함"]
    }
}

# 타이틀
st.markdown("""
<div style='text-align: center;'>
    <h1>⚡ MBTI 포켓몬 매칭 ⚡</h1>
    <h3>🎮 너와 닮은 포켓몬은 누구일까? 🎮</h3>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# 소개
st.markdown("""
### 🌟 환영합니다, 트레이너! 🌟

당신의 MBTI를 선택하면 가장 잘 어울리는 포켓몬을 추천해드려요! 🔮✨  
어떤 포켓몬이 당신과 닮았을지 알아보러 가볼까요? 🚀
""")

st.markdown("---")

# MBTI 선택
st.markdown("### 🎯 당신의 MBTI를 선택해주세요!")

col1, col2 = st.columns(2)
with col1:
    energy = st.radio("🔋 에너지 방향", ["E (외향) 🎤", "I (내향) 📚"])
    sensing = st.radio("👀 인식 방식", ["S (감각) 🌳", "N (직관) 🔮"])
with col2:
    thinking = st.radio("🧠 판단 방식", ["T (사고) ⚖️", "F (감정) 💖"])
    judging = st.radio("📅 생활 방식", ["J (계획) 📋", "P (즉흥) 🎲"])

mbti = energy[0] + sensing[0] + thinking[0] + judging[0]

st.markdown("---")

# 결과 보기 버튼
if st.button("🎁 내 포켓몬 확인하기! 🎁", use_container_width=True):
    with st.spinner('🔮 포켓몬을 찾는 중... ✨'):
        import time
        time.sleep(1.5)
    
    pokemon = mbti_pokemon[mbti]
    
    st.balloons()
    
    st.markdown(f"""
    <div style='text-align: center; background: linear-gradient(135deg, #FFE5E5 0%, #FFF5E5 100%); 
                padding: 30px; border-radius: 20px; border: 3px dashed #FF6B6B;'>
        <h2>🎊 당신의 MBTI는 <span style='color:#FF6B6B;'>{mbti}</span> 입니다! 🎊</h2>
        <h1>{pokemon['emoji']} {pokemon['name']} {pokemon['emoji']}</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    
    # 포켓몬 이미지
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(pokemon['image'], use_container_width=True)
    
    # 설명
    st.markdown(f"""
    ### 💌 포켓몬 소개
    > {pokemon['description']}
    """)
    
    # 특성
    st.markdown("### ✨ 당신의 매력 포인트")
    cols = st.columns(3)
    for i, trait in enumerate(pokemon['traits']):
        with cols[i]:
            st.markdown(f"""
            <div style='text-align: center; background-color: #F0F8FF; 
                        padding: 15px; border-radius: 15px; border: 2px solid #87CEEB;'>
                <h4>{trait}</h4>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.success(f"🎮 {pokemon['name']}와 함께 멋진 모험을 떠나보세요! 🌈")

# 푸터
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>💖 Made with Streamlit | 🎮 Gotta Catch 'Em All! 💖</p>
</div>
""", unsafe_allow_html=True)
