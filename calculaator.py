import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")

# ---------- CSS for Windows-like look ----------
st.markdown("""
<style>
.calc {
    max-width: 360px;
    margin: auto;
}
.display {
    background: #f3f3f3;
    padding: 20px;
    font-size: 40px;
    text-align: right;
    border-radius: 8px;
    margin-bottom: 10px;
    font-weight: bold;
}
.stButton>button {
    width: 100%;
    height: 60px;
    font-size: 20px;
    border-radius: 8px;
}
.op button {
    background-color: #e6e6e6;
}
.equal button {
    background-color: #0078D4;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------- Session state ----------
if "expr" not in st.session_state:
    st.session_state.expr = ""

# ---------- Display ----------
st.markdown('<div class="calc">', unsafe_allow_html=True)
st.markdown(f'<div class="display">{st.session_state.expr or "0"}</div>', unsafe_allow_html=True)

# ---------- Button handler ----------
def press(val):
    if val == "C":
        st.session_state.expr = ""
    elif val == "=":
        try:
            st.session_state.expr = str(eval(st.session_state.expr))
        except:
            st.session_state.expr = "Error"
    else:
        st.session_state.expr += val

# ---------- Button layout ----------
buttons = [
    ["%", "C", "⌫", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["±", "0", ".", "="]
]

for row in buttons:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        with cols[i]:
            if btn == "=":
                st.button(btn, on_click=press, args=(btn,), key=btn, type="primary")
            elif btn in ["+", "-", "*", "/", "%"]:
                st.button(btn, on_click=press, args=(btn,), key=btn)
            elif btn == "⌫":
                st.button(btn, on_click=lambda: st.session_state.__setitem__(
                    "expr", st.session_state.expr[:-1]
                ))
            elif btn == "±":
                st.button(btn, on_click=lambda: st.session_state.__setitem__(
                    "expr", "-" + st.session_state.expr if not st.session_state.expr.startswith("-") else st.session_state.expr[1:]
                ))
            else:
                st.button(btn, on_click=press, args=(btn,), key=btn)

st.markdown('</div>', unsafe_allow_html=True)
