#Importing necessary plug-ins and modules
from collections import Counter
import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import subprocess
import os
import time as time

#Reads our CSV file and assigns its value to a variable
file = open("CleanData.csv", "r")
database = file.read()
file.close()

#Empty csv to fill with inputs from website
df = pd.read_csv('survey.csv')

#Error checking
print(df)

#Splits our dataset into a list
database = database.split("\n")
database.remove(database[0])
database.remove(database[-1])

#Empty list for our 2d list
list2d = []

#Splitting our database into a 2d list`
for key in database:
    templist = []
    key = key.split(",")
    for item in key:
        templist.append(item)
    list2d.append(templist)

#Error checking
print(list2d)


#Empty lists to get our 2d list filtered even further
gender = []
age = []
course = []
cgpa = []
depress = []
anxiety = []
panics = []

#Taking the items from our 2d list and filling lists with the same piece of information
for profile in list2d:
    gender.append(profile[0])
    age.append(profile[1])
    course.append(profile[2])
    cgpa.append(profile[3])
    depress.append(profile[4])
    anxiety.append(profile[5])
    panics.append(profile[6])

#Error checking
print(age)
print(course)
print(cgpa)
print(depress)

#Making usable/graphable data using the list course
#Empty list for the amount of different courses and splitting the courses into a list
course2 = []
course3 = []

#Error checking
print(len(course))
print(len(course2))

#getting the amount of different courses and removing duplicates
for item in course:
    item = str(item)
    tempvar = str(item)
    course2 = dict(Counter(course))
    course.remove(item)
    course.append(tempvar)

#Error checking  
print(course)
print(course2)
print(len(course))
print(len(course2))

#sorts the dictionary
course2sorted = {k: v for k, v in sorted(course2.items(), key=lambda x: x[1])}

#makes 2 lists, one for keys and one for values
coursename = list(course2sorted.keys())
courseamount = list(course2sorted.values())

#Error checking
print(courseamount)
print(coursename)

#Reverses the order of the list so that it goes from highest to lowest
coursename.reverse()
courseamount.reverse()

#Error checking
print(courseamount)
print(coursename)

#top 10 courses
top10name = coursename[:9]
top10amount = courseamount[:9]

print(top10name)
print(top10amount)
#End of usable data 1/3

#start of usable data grade-mental health

mental1 = []
mental2 = []
noyes = 0
oneyes = 0
twoyes = 0
allyes = 0

for item in database:
    item = item.split(",")
    templist = []
    templist.append(item[4])
    templist.append(item[5])
    templist.append(item[6])
    mental1.append(templist)

print(len(mental1))

for item in mental1:
    templist = []
    tempvar = 0
    templist = dict(Counter(item))
    #Error checking
    print(templist)
    if "No" in templist:
        tempvar = list(templist.values())[list(templist.keys()).index("No")]
        if tempvar == 3:
            noyes +=1
            mental2.append(0)
        elif tempvar == 2:
            oneyes +=1
            mental2.append(1)
        elif tempvar == 1:
            twoyes +=1
            mental2.append(2)
    else:
        allyes +=1
        mental2.append(3)
    
#Error checking
print(noyes)
print(oneyes)
print(twoyes)
print(allyes)
print(cgpa)
print(len(cgpa))
print(mental2)
print(len(mental2))

mentalcgpa = []
loop = 0

while loop < len(cgpa):
    templist = []
    templist.append(cgpa[loop])
    templist.append(mental2[loop])
    mentalcgpa.append(templist)
    loop +=1

#Error checking
print(mentalcgpa)

cgpa000_199 = []
cgpa200_249 = []
cgpa250_299 = []
cgpa300_349 = []
cgpa350_400 = []

for item in mentalcgpa:
    if item[0] == '0 - 1.99':
        cgpa000_199.append(item[1])
    if item[0] == '2.00 - 2.49':
        cgpa200_249.append(item[1])
    if item[0] == '2.50 - 2.99':
        cgpa250_299.append(item[1])
    if item[0] == '3.00 - 3.49':
        cgpa300_349.append(item[1])
    if item[0] == '3.50 - 4.00':
        cgpa350_400.append(item[1])

#Error checking
print(cgpa000_199)
print(cgpa200_249)
print(cgpa250_299)
print(cgpa300_349)
print(cgpa350_400)

cgpa000_199 = dict(Counter(cgpa000_199))
cgpa200_249 = dict(Counter(cgpa200_249))
cgpa250_299 = dict(Counter(cgpa250_299))
cgpa300_349 = dict(Counter(cgpa300_349))
cgpa350_400 = dict(Counter(cgpa350_400))

#Error checking
print(cgpa000_199)
print(cgpa200_249)
print(cgpa250_299)
print(cgpa300_349)
print(cgpa350_400)

#values are taken from the terminal and hardcoded
cgpagraphdata = {
    'CGPA' : ['0.00 - 1.99', '0.00 - 1.99', '0.00 - 1.99', '0.00 - 1.99', '2.00 - 2.49', '2.00 - 2.49', '2.00 - 2.49', '2.00 - 2.49', '2.50 - 2.99', '2.50 - 2.99', '2.50 - 2.99', '2.50 - 2.99', '3.00 - 3.49', '3.00 - 3.49', '3.00 - 3.49', '3.00 - 3.49', '3.50 - 4.00', '3.50 - 4.00', '3.50 - 4.00', '3.50 - 4.00'],
    'Mental Health' : ['0 Mental health conditions', '1 Mental health conditions', '2 Mental health conditions', '3 Mental health conditions', '0 Mental health conditions', '1 Mental health conditions', '2 Mental health conditions', '3 Mental health conditions', '0 Mental health conditions', '1 Mental health conditions', '2 Mental health conditions', '3 Mental health conditions', '0 Mental health conditions', '1 Mental health conditions', '2 Mental health conditions', '3 Mental health conditions', '0 Mental health conditions', '1 Mental health conditions', '2 Mental health conditions', '3 Mental health conditions', ],
    'Number of Students' : [3, 1, 0, 0, 1, 1, 0, 0, 1, 0, 2, 1, 15, 17, 7, 4, 17, 17, 9, 5]
    }

#Usable data 2 done, mental health to cgpa
#Usable data 3 
#Mental health to gender
#checking lists
print(gender)
print(mental2)
print(len(gender))
print(len(mental2))

#while loop variable
loop = 0
gendermental = []

#making profiles
while loop <101:
    templist = []
    templist.append(gender[loop])
    templist.append(mental2[loop])
    gendermental.append(templist)
    loop +=1

#error checking
print(gendermental)

#empty lists
malemental = []
femalemental = []

#splitting profiles into men and women
for item in gendermental:
    if item[0] == 'Female':
        femalemental.append(item)
    elif item[0] == 'Male':
        malemental.append(item)
    
#error checking
print(malemental)
print(femalemental)
print(len(malemental))
print(len(femalemental))

gender2 = []
mental2 = []

for item in malemental:
    gender2.append(item[0])
    mental2.append(item[1])
for item in femalemental:
    gender2.append(item[0])
    mental2.append(item[1])
    
maleamount = len(malemental)
femaleamount = len(femalemental)
print(gender2)
print(mental2)

fig3dict = {
    'Gender' : ['Male', 'Male', 'Male', 'Male' , 'Female', 'Female', 'Female', 'Female'],
    'Number of Students' : [10, 8, 6, 1, 22, 21, 11, 10],
    'Mental Health' : ['0 Mental health conditions', '1 Mental health conditions', '2 Mental health conditions', '3 Mental health conditions', '0 Mental health conditions', '1 Mental health conditions', '2 Mental health conditions', '3 Mental health conditions'],
    }

#graphing data 1/3
#create the pi chart
fig1 = go.Figure(data=[go.Pie(labels=top10name, values=top10amount, hole=0.3)])

#customise the chart
fig1.update_layout(
    title="10 Most Popular Courses Pie Chart",
    annotations=[dict(text='Course', x=0.5, y=0.5, font_size=20, showarrow=False)],
    showlegend=True
)

#graphing data 2/3
#histogram
fig2 = px.histogram(cgpagraphdata, y="CGPA", x="Number of Students", color="Mental Health", title = 'Common Grade Point Average to Mental Health')

#graphing data 3/3
fig3 = px.bar(fig3dict, x="Gender", y="Number of Students", color="Mental Health", title = 'Gender to Mental Health')

#get thing
dfs = pd.read_csv('survey.csv')

#*****STREAMLIT*****
#Break the site into tabs
st.title("CS Project")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Data", "Courses", "CGPA", "Gender", "Reccommendations", "Form"])

with tab1:
    st.header("My Data")
    with st.container(border = True):
        st.write("This data is a survey of college students on their mental health. This topic is very important for people like myself who plan on attending college. It helps make us aware of the effects that college can have on our mental health. We surveyed students on their Gender, course and if they have depression, anxiety or panic attacks. By using a real survey, we get a better idea of the reality of college and how strenuous and distressing it can be. I believe that this data can help normalise seeking help from mental health professionals by showing that most people around you in college are also struggling with their mental health. I believe that this idea can help people who are struggling with mental health in college, which often goes overlooked. ")
    
with tab2:
    st.header("Courses")
    with st.container(border = True):
        st.write("This survey was performed on students from many different courses. This is a pie chart of the top 10 most popular courses. By hovering your mouse over the different sections of the pie chart, you can see the amount of students that were surveyed from each course. ")
        st.plotly_chart(fig1)
    
with tab3:
    st.header("Common Grade Point Average compared to Mental health conditions.")
    with st.container(border = True):
        st.write("This histogram represents the Mental health conditions that students have,  This graph shows the amount of students that have 0, 1, 2 or 3 of these mental health conditions and what their common grade point average (CGPA) is. This can help show us the effects that a larger workload can have on students and what kind of academic performance the surveyed students have.")
        st.plotly_chart(fig2)
    
with tab4:
    st.header("Gender compared to Mental health")
    with st.container(border = True):
        st.write("These bar charts represent the mental health conditions of male and female students. This can help us see if there is a difference in the mental health conditions of men and women. From this graph, we can see that the percentages of individuals with mental health difficulties are similar between men and women, but there were a lot more women surveyed than men. ")
        st.plotly_chart(fig3)
        
with tab5:
    st.header("Reccommendations based on my Data")
    with st.container(border = True):
        with st.container(border = True):
            st.header("Courses")
            st.write("We can see from our courses tab that business and engineering make up over half of the students in the top 10 most popular courses. This shows us that business and engineering are much more popular than any other course at this college. My recommendation based on this data is that if you are interested in business or engineering courses, be prepared for a lot of competition and study hard to score high in your tests.")
        with st.container(border = True):
            st.header("CGPA")
            st.write("We see from the graph in our CGPA tab that the vast majority of students surveyed achieved over a 3.0 CGPA, an impressive grade. This shows us that this is a very high end college. From this graph, we also see that the majority of students in each grade bracket above 2.5 CGPA have at least one mental health condition, showing that there is a lot of stress on these students. My recommendations based on this data would be to be more open about your own mental health, as the majority of your peers are going through the same struggle as you.")
        with st.container(border = True):
            st.header("Gender")
            st.write("We can see from the graph in our Gender tab that the ratio of mental health conditions between men are roughly similar. The main difference is that there were many more women surveyed than men, showing that men are less likely to talk about their mental health. The recommendation I'd make based on this data is that if you are a man, you should be more open about your mental health struggles. ")
    
with tab6:
    st.header("Form")
    st.write("Please fill out our form")
    form1 = st.form("User Form")
    email = form1.text_input("Email: ")
    pnumber = form1.text_input("Phone Number: ")
    mailing = form1.checkbox("Receive email updates?")
    submit = form1.form_submit_button("Submit", on_click=None)    
        
            
        # Perform validation again on the server-side (optional, as it was validated on client-side)
    def validate_email(email):
        if '@' in email and '.com' in email:
            return True
        return False

    def validate_phone_number(pnumber):
        if pnumber.isdigit() and 9 <= len(pnumber) <= 11:
            return True
        return False
    
if submit:
    if not validate_email(email):
        st.components.v1.html( '''
            <script>
                alert('Please enter a valid email address');
            </script>''')
        time.sleep(0.1)
        st.rerun()
    elif not validate_phone_number(pnumber):
        st.components.v1.html( '''
            <script>
                alert('Please enter a valid phone number');
            </script>''')
        time.sleep(0.1)
        st.rerun()
    else:
        # Collect survey data
        survey_data = {'Email': [email], 'Phone Number': [str(pnumber)], 'Mailing List': [mailing]}
        dfi = pd.DataFrame(survey_data)

        # Append the new data to the existing dataframe
        df1 = pd.concat([dfs, dfi], ignore_index=True)

        # Save the updated dataframe to CSV
        df1.to_csv('survey.csv', index=False)
        st.write(df1)

        st.components.v1.html( '''
            <script>
                alert('Answers submitted successfully.');
            </script>''')

        

#to run the program properly, open the system shell terminal and input the following code
#cd "#File Location#"
#python -m streamlit run CSProjectGraph.py