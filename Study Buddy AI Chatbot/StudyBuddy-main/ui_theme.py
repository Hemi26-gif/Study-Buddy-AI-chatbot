"""Colorful responsive theme + the Mimi doll mascot (pure SVG/CSS, no images needed)."""
import html

import streamlit as st


def _flat(s: str) -> str:
    """Collapse to one line so Streamlit's markdown never treats HTML as a code block."""
    return " ".join(line.strip() for line in s.strip().splitlines() if line.strip())


CSS = """
:root{color-scheme:light;}
.stApp{background:linear-gradient(135deg,#f5f7ff 0%,#edf2ff 48%,#fdf1ff 100%);background-attachment:fixed;color:#171a35;}
header[data-testid="stHeader"]{background:rgba(245,247,255,.82);}
.block-container{width:min(100% - 2rem,1180px);padding-top:1.4rem;padding-bottom:3rem;}
section[data-testid="stSidebar"]{background:linear-gradient(180deg,#eef2ff 0%,#f6edff 100%);border-right:1px solid #dce1f5;}
.stApp h1,.stApp h2,.stApp h3,.stApp h4,.stApp p,.stApp label,.stApp li{color:#171a35;}
.stApp [data-testid="stCaptionContainer"] p{color:#475079;}

.hero{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:clamp(16px,4vw,36px);
padding:clamp(18px,4vw,34px);border:1px solid rgba(255,255,255,.28);border-radius:28px;
background:linear-gradient(120deg,#172554 0%,#4c1d95 52%,#86198f 100%);
box-shadow:0 18px 48px rgba(49,46,129,.25);margin-bottom:22px;}
.doll-wrap{width:clamp(110px,16vw,170px);flex:0 0 auto;animation:float 3.2s ease-in-out infinite;filter:drop-shadow(0 10px 12px rgba(0,0,0,.25));}
.doll-svg{width:100%;height:auto;display:block;}
.hero-text{flex:1 1 320px;min-width:min(100%,240px);}
.hero-title{color:#fff;font-size:clamp(1.8rem,4vw,2.7rem);font-weight:800;line-height:1.1;}
.hero-tag{color:#f3e8ff;margin:.45rem 0 .9rem;font-size:1.05rem;}
.chips span{display:inline-block;background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.3);color:#fff;
border-radius:999px;padding:5px 12px;margin:0 6px 7px 0;font-size:.85rem;font-weight:700;}
.bubble{position:relative;background:#fff;color:#201544;border-radius:16px;padding:12px 18px;font-weight:700;
display:inline-block;max-width:100%;box-shadow:0 6px 18px rgba(0,0,0,.18);margin-top:8px;}
.bubble::before{content:"";position:absolute;left:-12px;top:50%;margin-top:-10px;border:10px solid transparent;
border-right-color:#fff;border-left:0;}

.stButton>button,.stFormSubmitButton>button,.stDownloadButton>button{background:linear-gradient(100deg,#6d28d9,#a21caf);
color:#fff;border:0;border-radius:14px;font-weight:800;padding:.58rem 1rem;box-shadow:0 6px 16px rgba(91,33,182,.24);
transition:transform .15s ease,box-shadow .15s ease;}
.stButton>button:hover,.stFormSubmitButton>button:hover,.stDownloadButton>button:hover{transform:translateY(-2px);
color:#fff;box-shadow:0 10px 22px rgba(91,33,182,.34);}
.stButton>button p,.stFormSubmitButton>button p,.stDownloadButton>button p{color:#fff;font-weight:800;}
.stButton>button:focus-visible,.stFormSubmitButton>button:focus-visible,.stDownloadButton>button:focus-visible{outline:3px solid #f59e0b;outline-offset:3px;}

.stTabs [data-baseweb="tab-list"]{gap:8px;flex-wrap:wrap;border-bottom:1px solid #d8ddf0;}
.stTabs [data-baseweb="tab"]{background:#fff;border:1px solid #dce1f2;border-radius:13px 13px 0 0;padding:10px 14px;height:auto;
box-shadow:0 3px 10px rgba(49,46,129,.08);}
.stTabs [aria-selected="true"]{background:linear-gradient(100deg,#6d28d9,#86198f);border-color:#6d28d9;}
.stTabs [aria-selected="true"] p{color:#fff; padding: 10px 14px; font-weight:700;}
.stTabs [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-border"]{display:none;}


[data-testid="stChatMessage"],div[data-testid="stForm"],[data-testid="stMetric"],[data-testid="stExpander"],
div[data-testid="stVerticalBlockBorderWrapper"]>div{background:rgba(255,255,255,.94);border:1px solid #e0e5f4;border-radius:18px;}
[data-testid="stChatMessage"]{padding:14px 18px;margin-bottom:10px;box-shadow:0 4px 14px rgba(49,46,129,.08);}
div[data-testid="stForm"]{padding:clamp(12px,2vw,22px);box-shadow:0 8px 24px rgba(49,46,129,.06);}
[data-testid="stMetric"]{padding:12px 16px;box-shadow:0 4px 14px rgba(49,46,129,.1);}
[data-testid="stMetricLabel"],[data-testid="stMetricValue"]{color:#171a35;}
[data-testid="stExpander"]{overflow:hidden;}
div[data-baseweb="input"]>div,div[data-baseweb="select"]>div,div[data-testid="stDateInput"] input,
div[data-testid="stNumberInput"] input,div[data-testid="stTextArea"] textarea{background:#fff;color:#171a35;border-color:#aab4d0;}
input::placeholder,textarea::placeholder{color:#687294!important;opacity:1;}
div[data-testid="stProgress"]>div>div{background:linear-gradient(90deg,#6d28d9,#c026d3);}

@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
@keyframes blink{0%,92%,100%{transform:scaleY(1)}96%{transform:scaleY(.1)}}
@keyframes wave{from{transform:rotate(0deg)}to{transform:rotate(-55deg)}}
@keyframes pulse{0%,100%{opacity:.25}50%{opacity:1}}
@keyframes twinkle{0%,100%{transform:scale(.7);opacity:.5}50%{transform:scale(1.2);opacity:1}}
.blink{transform-origin:100px 106px;animation:blink 4s infinite;}
.wave{transform-origin:132px 172px;animation:wave .55s ease-in-out infinite alternate;}
.d1,.d2,.d3{animation:pulse 1.2s infinite;}
.d2{animation-delay:.2s}.d3{animation-delay:.4s}
.spark{transform-box:fill-box;transform-origin:center;animation:twinkle 1s infinite;}

@media (max-width:640px){
.block-container{width:100%;padding:1rem .85rem 2rem;}
.hero{padding:18px 14px;text-align:center;gap:10px;border-radius:20px;}
.doll-wrap{width:118px;}
.hero-title{font-size:1.85rem;}
.hero-text{flex-basis:100%;}
.bubble::before{left:50%;top:-12px;margin-left:-10px;margin-top:0;border:10px solid transparent;border-bottom-color:#fff;border-top:0;}
.stTabs [data-baseweb="tab-list"]{gap:5px;}
.stTabs [data-baseweb="tab"]{padding:10px 14px;font-size:.86rem;}
div[data-testid="stForm"]{padding:10px;}
}
"""


def inject_css() -> None:
    st.markdown(f"<style>{_flat(CSS)}</style>", unsafe_allow_html=True)


def doll_svg(mood: str = "idle") -> str:
    """Return the Mimi doll as inline SVG. mood: idle | thinking | happy."""
    if mood == "happy":
        eyes = (
            '<path d="M72 108 Q82 96 92 108" stroke="#2d2250" stroke-width="4" fill="none" stroke-linecap="round"/>'
            '<path d="M108 108 Q118 96 128 108" stroke="#2d2250" stroke-width="4" fill="none" stroke-linecap="round"/>'
        )
        mouth = '<path d="M86 126 Q100 150 114 126 Z" fill="#d6336c"/>'
        extra = (
            '<text class="spark" x="150" y="52" font-size="20">✨</text>'
            '<text class="spark" x="18" y="70" font-size="16" style="animation-delay:.4s">⭐</text>'
        )
        arm_class = "wave"
    else:
        eyes = (
            '<g class="blink">'
            '<ellipse cx="82" cy="106" rx="7" ry="9" fill="#2d2250"/>'
            '<ellipse cx="118" cy="106" rx="7" ry="9" fill="#2d2250"/>'
            '<circle cx="84.5" cy="102" r="2.6" fill="#fff"/><circle cx="120.5" cy="102" r="2.6" fill="#fff"/>'
            "</g>"
        )
        arm_class = ""
        if mood == "thinking":
            mouth = '<ellipse cx="100" cy="131" rx="4" ry="5" fill="#d6336c"/>'
            extra = (
                '<circle class="d1" cx="152" cy="62" r="4" fill="#fff"/>'
                '<circle class="d2" cx="162" cy="48" r="6" fill="#fff"/>'
                '<circle class="d3" cx="176" cy="30" r="9" fill="#fff"/>'
            )
        else:
            mouth = '<path d="M90 127 Q100 138 110 127" stroke="#d6336c" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
            extra = ""

    return f"""
    <svg class="doll-svg" viewBox="0 0 200 255" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mimi the study doll">
      <ellipse cx="100" cy="248" rx="55" ry="6" fill="#00000026"/>
      <ellipse cx="38" cy="122" rx="20" ry="36" fill="#6b3f2a"/>
      <ellipse cx="162" cy="122" rx="20" ry="36" fill="#6b3f2a"/>
      <circle cx="48" cy="92" r="9" fill="#ff5fa2"/><circle cx="152" cy="92" r="9" fill="#ff5fa2"/>
      <path d="M70 165 Q100 150 130 165 L158 236 Q100 250 42 236 Z" fill="#ff8fc7"/>
      <path d="M82 160 L100 180 L118 160 Z" fill="#fff"/>
      <circle cx="100" cy="205" r="5" fill="#ffd93d"/><circle cx="100" cy="222" r="5" fill="#ffd93d"/>
      <ellipse cx="82" cy="243" rx="14" ry="6" fill="#7a6cff"/><ellipse cx="118" cy="243" rx="14" ry="6" fill="#7a6cff"/>
      <g><ellipse cx="62" cy="190" rx="10" ry="18" fill="#ffe3cc" transform="rotate(20 62 190)"/></g>
      <g class="{arm_class}"><ellipse cx="138" cy="190" rx="10" ry="18" fill="#ffe3cc" transform="rotate(-20 138 190)"/></g>
      <circle cx="100" cy="100" r="62" fill="#6b3f2a"/>
      <circle cx="100" cy="104" r="50" fill="#ffe3cc"/>
      <path d="M50 100 Q52 52 100 50 Q148 52 150 100 Q140 72 100 70 Q60 72 50 100 Z" fill="#6b3f2a"/>
      {eyes}
      <circle cx="68" cy="122" r="7" fill="#ff8fab" opacity=".5"/><circle cx="132" cy="122" r="7" fill="#ff8fab" opacity=".5"/>
      {mouth}
      <path d="M72 56 L72 70 Q100 84 128 70 L128 56 Z" fill="#3a2f95"/>
      <polygon points="52,54 100,32 148,54 100,76" fill="#4b3fb8"/>
      <line x1="148" y1="54" x2="154" y2="84" stroke="#ffd93d" stroke-width="3"/>
      <circle cx="154" cy="86" r="5" fill="#ffd93d"/>
      {extra}
    </svg>
    """


def hero_html(mood: str, message: str) -> str:
    return _flat(
        f"""
        <div class="hero">
          <div class="doll-wrap">{_flat(doll_svg(mood))}</div>
          <div class="hero-text">
            <div class="hero-title">🎓 StudyBuddy</div>
            <div class="hero-tag">Your AI study assistant – learn smarter, not harder!</div>
            <div class="chips"><span>📅 Schedules</span><span>🧠 Concepts</span><span>📝 MCQs</span><span>🎯 Quizzes</span></div>
            <div class="bubble">{html.escape(message)}</div>
          </div>
        </div>
        """
    )
