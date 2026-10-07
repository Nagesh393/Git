import streamlit as st


st.title("🎯 Simple Quiz Game")
score=int(st.query_params.get("score", 0))
q1 = "1 What is the capital of Nepal?"
o1= ["Pokhara", "Kathmandu", "Lalitpur", "Biratnagar"]
a1="Kathmandu"

q2= "2 What is the capital of Japan?"
o2=["Kathmandu", "Colombu", "Tokyo", "Tibet"]
a2="Tokyo"

q3= "3 What is the sum of 625+25?"
o3=[600, 650, 675, 700]
a3=650

q4= "4 Which language is used in data science?"
o4=["Java", "C++", "C", "Python"]
a4="Python"

q5="5 What is the multiple of 5?"
o5=["79", "66", "55", "4"]
a5=55

i=int(st.query_params.get("q", 1))
if i==1:
    q=globals()[f"q{i}"]
    o=globals()[f"o{i}"]
    ans= st.radio(q, o, key=f"q{i}")
elif i==2:
    q=globals()[f"q{i}"]
    o=globals()[f"o{i}"]
    ans= st.radio(q, o, key=f"q{i}")
elif i==3:
    q=globals()[f"q{i}"]
    o=globals()[f"o{i}"]
    ans= st.radio(q, o, key=f"q{i}")
elif i==4:
    q=globals()[f"q{i}"]
    o=globals()[f"o{i}"]
    ans= st.radio(q, o, key=f"q{i}")
elif i==5:
    q=globals()[f"q{i}"]
    o=globals()[f"o{i}"]
    ans= st.radio(q, o, key=f"q{i}")
    
    if st.button("Submit"):
     
       if ans==globals()[f"a{i}"]:
        st.query_params["score"]=score+1
        st.success(f"Your Score: {score}")
       else:
            st.success(f"Your Score: {score}")



if i<5:
    if st.button("Submit"):
        if ans==globals()[f"a{i}"]:
            st.query_params["score"]=score+1
        else:
            score=score
            

        st.query_params["q"]=i+1
        st.rerun()


    

