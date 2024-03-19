import streamlit as st,uuid
"""ここで読み込んだりしてください"""
form multiapp import MaltiApp
if len(st.session_state)==0:
  st.session_state["access"]=0
  st.session_state["data"]={}
def save():
  return #ここに何かプログラムを入れます
st.write("""<h1>マルチデータベース</h1><h2>筆記法</h2>名前:値,名前:値...ノヨウナカタチデ記述します""",unsafe_allow_html=True)
st.header("作成")
password=st.text_input("パスワード")
if st.button("作成"):
  key_=str(uuid.uuid4())
  try:
    st.session_state["data"][key_]=[]
    st.success(f"キー:{key_}")
  except:
    
  key_=""
