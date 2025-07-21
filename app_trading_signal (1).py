
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Análisis de Gráfico OTC", layout="centered")
st.title("📈 Señal de Trading desde Imagen OTC (PocketOption)")

uploaded_file = st.file_uploader("📸 Sube una imagen del gráfico OTC (1M)", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gráfico cargado", use_column_width=True)

    st.markdown("## 📊 Resultado del análisis simulado")
    st.success("📉 **Señal generada: VENTA**")
    st.markdown("""
- ✅ **Tendencia**: Bajista
- ✅ **EMA50 < EMA200**
- ✅ **MACD bajista**
- ⚠️ **RSI bajo (posible rebote)**

**🕐 Temporalidad recomendada**: 1 minuto  
**⏱️ Expiración sugerida**: 2 minutos
""")
else:
    st.info("Por favor, sube una imagen para generar la señal.")
