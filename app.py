import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Mini Image Editor",
    page_icon="🖼️",
    layout="wide"
)

# ─────────────────────────────────────────────
# STYLE
# ─────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #0f172a, #020617);
        color: #e2e8f0;
    }

    h1 {
        font-size: 2.2rem !important;
        font-weight: 700;
        color: white;
    }

    .subtitle {
        color: #94a3b8;
        font-size: 0.9rem;
        margin-bottom: 1.5rem;
    }

    .card {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 1rem;
        margin-bottom: 1rem;
    }

    .metric-box {
        background: rgba(99,102,241,0.1);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
    }

    .metric-title {
        font-size: 0.75rem;
        color: #94a3b8;
    }

    .metric-value {
        font-size: 1.4rem;
        font-weight: bold;
        color: #818cf8;
    }

    .stDownloadButton button {
        background: linear-gradient(90deg, #6366f1, #8b5cf6) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 0.6rem !important;
        width: 100% !important;
    }

    .stDownloadButton button:hover {
        background: linear-gradient(90deg, #4f46e5, #7c3aed) !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# FUNCTIONS
# ─────────────────────────────────────────────

def pil_to_cv2(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

def cv2_to_pil(image):
    return Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

def adjust_brightness(image, value):
    return cv2.convertScaleAbs(image, alpha=1.0, beta=value)

def upscale_image(image, scale):
    if scale == 1:
        return image
    h, w = image.shape[:2]
    return cv2.resize(image, (w*scale, h*scale), interpolation=cv2.INTER_CUBIC)

def image_to_bytes(image, fmt="PNG"):
    pil_img = cv2_to_pil(image)
    buf = io.BytesIO()
    pil_img.save(buf, format=fmt)
    return buf.getvalue()

def get_image_stats(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return {
        "mean": float(np.mean(gray)),
        "std": float(np.std(gray)),
        "min": int(np.min(gray)),
        "max": int(np.max(gray)),
    }

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.markdown("# 🖼️ Mini Image Editor")
st.markdown('<div class="subtitle">Brightness Adjustment + Upscale (HD Effect)</div>', unsafe_allow_html=True)
st.markdown("---")

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.header("📁 Upload")
    uploaded_file = st.file_uploader("Upload gambar", type=["jpg", "png", "jpeg"])

    st.header("⚙️ Pengaturan")

    brightness_val = st.slider("Brightness", -100, 150, 40)

    upscale_val = st.slider(
        "Kualitas (Upscale / HD Effect)",
        1, 4, 1,
        help="Memperbesar resolusi gambar"
    )

    st.info("""
💡 Tips:
- Brightness untuk pencahayaan
- Upscale untuk efek HD (lebih besar & halus)
""")

# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
if uploaded_file is None:
    st.info("Upload gambar untuk mulai editing")
else:
    pil_image = Image.open(uploaded_file).convert("RGB")
    original = pil_to_cv2(pil_image)

    # PROCESS
    result = original.copy()
    result = adjust_brightness(result, brightness_val)
    result = upscale_image(result, upscale_val)

    label = f"Brightness ({brightness_val}) + Upscale x{upscale_val}"

    # ───────── IMAGE VIEW ─────────
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("**📷 Gambar Asli**")
        st.image(cv2_to_pil(original), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(f"**✨ Hasil Edit — {label}**")
        st.image(cv2_to_pil(result), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ───────── STATS ─────────
    st.markdown("### 📊 Statistik Citra")

    stats_ori = get_image_stats(original)
    stats_res = get_image_stats(result)

    col1, col2, col3, col4 = st.columns(4)

    def metric(title, val1, val2):
        return f"""
        <div class="metric-box">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{val2}</div>
            <div style="font-size:0.7rem;color:#94a3b8;">Asli: {val1}</div>
        </div>
        """

    with col1:
        st.markdown(metric("Mean", stats_ori['mean'], stats_res['mean']), unsafe_allow_html=True)
    with col2:
        st.markdown(metric("Std Dev", stats_ori['std'], stats_res['std']), unsafe_allow_html=True)
    with col3:
        st.markdown(metric("Min", stats_ori['min'], stats_res['min']), unsafe_allow_html=True)
    with col4:
        st.markdown(metric("Max", stats_ori['max'], stats_res['max']), unsafe_allow_html=True)

    # ───────── DOWNLOAD ─────────
    st.markdown("---")
    st.markdown("### 💾 Download Hasil")

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            "⬇️ Download PNG",
            data=image_to_bytes(result, "PNG"),
            file_name="hasil.png"
        )

    with col2:
        st.download_button(
            "⬇️ Download JPG",
            data=image_to_bytes(result, "JPEG"),
            file_name="hasil.jpg"
        )

