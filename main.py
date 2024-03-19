import streamlit as st,uuid
#"""ここで読み込んだりしてください"""

if len(st.session_state)==0:
  st.session_state["access"]=0
  st.session_state["data"]={}
  st.session_state["aikotoba"]={}
def save():
  return #ここに何かプログラムを入れます
st.write("""<h1>マルチデータベース</h1><h2>筆記法</h2>名前:値,名前:値...ノヨウナカタチデ記述します""",unsafe_allow_html=True)
st.header("作成")
st.info('パスワードなどはメモをしてください')
password=st.text_input("秘密パスワード(かきこみ)")
password2=st.text_input("公開用パスワード")
aikotoba=st.checkbox('あいことばをつかう')
password3=st.text_input("あいことば")
if st.button("作成"):
  key_=str(uuid.uuid4())
  try:
    st.session_state["data"][key_]=[]
    st.session_state["data"][key_+"password"]=[password,password2]
    st.success(f"キー:{key_}")
    if aikotoba:
      st.session_state["aikotoba"][password3]=[password2,key_]
  except Exception as a:
    st.warning('何らかの問題')
    print(a)
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
      if password_==st.session_state["data"][key__+"password"][0]:
        st.session_state["data"][key__].append(dictss)
        st.success('成功!')
      else:
        st.warning('キーが存在しません')
    else:
      st.warning('キーが存在しません')
  except:
    st.warning('失敗!')
st.header("復元")
st.info('合言葉に登録されている必要があります')
aikotoba2=st.text_input("合言葉")
if st.button("復元"):
  try:
    st.write(st.session_state["aikotoba"][aikotoba2])
  except:
    st.text("ないよ！")
