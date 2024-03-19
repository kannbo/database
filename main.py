import streamlit as st,uuid
"""ここで読み込んだりしてください"""
key_value={}
if len(st.session_state)==0:
  st.session_state["access"]=0
  st.session_state["data"]={}
def save():
  return #ここに何かプログラムを入れます
st.write("""<h1>マルチデータベース</h1><h2>筆記法</h2>名前:値,名前:値...ノヨウナカタチデ記述します""",unsafe_allow_html=True)
st.header("作成")
st.info('パスワードなどはメモをしてください')
password=st.text_input("パスワード")
if st.button("作成"):
  key_=str(uuid.uuid4())
  try:
    st.session_state["data"][key_]=[]
    st.success(f"キー:{key_}")
  except:
    st.warning('何らかの問題')
  key_=""
st.header("追加")
st.info('ここではパスワードなどが必須')
key_value["key"]=st.text_input("キー")
key_value["password"]=st.text_input("パスワード")
key_value["value"]=st.text_input("追加要素")
dictss={}
if st.button("追加"):
  try:
    if key_value["key"] in st.session_state["data"]:
      #for i in key_value["value"].split(","):
      #  dictss[i.split(":")[0]]=i.split(":")[1]
      dictss=[{aaa.split(":")[0]:aaa.split(":")[1]} for aaa in key_value["value"].split(",")]
      st.session_state["data"][key_value["key"]].append(dictss)
      st.success('成功!')
    else:
      st.warning('キーが存在しません')
  except:
    st.warning('失敗!')
