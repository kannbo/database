import streamlit as st,uuid
#"""ここで読み込んだりしてください"""

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
    st.session_state["data"][key_+"password"]=password
    st.success(f"キー:{key_}")
  except:
    st.warning('何らかの問題')
  key_=""
st.header("追加")
st.info('ここではパスワードなどが必須')
key_value={"key":"","password":"","value":""}
key__=st.text_input("キー")
password_=st.text_input("パスワード  ")
value_=st.text_input("追加要素")
dictss={}
if st.button("追加"):
  try:
    if key__ in st.session_state["data"]:
      #for i in key_value["value"].split(","):
      #  dictss[i.split(":")[0]]=i.split(":")[1]
      dictss=[{aaa.split(":")[0]:aaa.split(":")[1]} for aaa in value_.split(",")]
      if password_==st.session_state["data"][key__+"password"]:
        st.session_state["data"][key__].append(dictss)
        st.success('成功!')
      else:
        st.warning('謎のエラー')
    else:
      st.warning('キーが存在しません')
  except:
    st.warning('失敗!')
