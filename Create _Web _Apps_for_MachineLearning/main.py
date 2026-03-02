import streamlit as st

st.title("Hello Siddhi 👋")
st.write("My first Streamlit app!")
st.header("This is my header")
st.subheader("this is subheader")
st.text("this is text")

st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
exp = ZeroDivisionError("Trying to divide by zero")
st.exception(exp)
if st.checkbox("Show/Hide"):
    st.text("Showing the widget")

status = st.radio("Select Gender:", ("Male", "Female", "Trans", "Don't want to disclose"))    
if status == "Male":
    st.success("Male")
elif status == "Female":
    st.success("Female")  
elif status == "Trans":
    st.success("Trans")  
else:
    st.success("Don't want to disclose")        

#selection Box = uses List to store data
hobby = st.selectbox("Hobbies:", ['Dancing', 'Reading', 'Sports']) 
st.write("Your hobby is:", hobby)   

# Multiple select
hobbies = st.multiselect("Hobbies are:", ['Dancing', 'Reading', 'Sports'])
st.write("Your hobbies are:", len(hobbies),'hobbies')

#create a simple button
st.button("Click me")
if st.button("See more..."):
    st.text("Button click operation is done")