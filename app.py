import streamlit as st

# Title
st.title("🧠 College Helpdesk AI Chatbot")
st.write("Ask any question related to our college!")

# User input
user_input = st.text_input("You:", "type here")

# Responses dictionary
responses = {
    "hi": " Hello! How can I assist you with college-related questions?",
    "hello": " Hi there! Ask me anything about our college.",
    "hey": "Hey! I'm here to help you with your college queries.",
    "what are the college timings": " Our college runs from 9:00 AM to 4:00 PM, Monday to Saturday.",
    "who is the principal": " The principal of our college is Dr. S. Ramesh.",
    "when are the semester exams": " Semester exams usually begin in the second week of December and May.",
    "where is the office located": " The college office is on the ground floor near the main entrance.",
    "what courses are available": " We offer B.Tech, M.Tech, BBA, MBA, and Diploma courses.",
    "how to apply for leave": " Submit a leave application via the student portal or a handwritten note to your class in-charge.",
    "when is the last date for exam fee": " The last date to pay the exam fee is June 20, 2025.",
    "how to get bonafide certificate": " Visit the office and fill out a bonafide certificate request form. It will be issued in 2 days.",
    "is there a library": " Yes, the college has a well-equipped library open from 9 AM to 5 PM.",
    "how to get id card": " Submit your admission receipt to the office. The ID card will be issued within a week.",
    "who is the hod of cse department": " The HOD of the CSE department is Prof. Anitha Rao.",
    "where can i find exam timetable": " The exam timetable is available on the notice board and student portal.",
    "how to apply for scholarship": " Apply through the National Scholarship Portal or contact the office for guidance.",
    "are there any clubs or activities": " Yes, we have coding, robotics, cultural, literary, and sports clubs.",
    "how to get transfer certificate": " Submit a written request and get clearance from all departments.",
    "what is the dress code": " Students must wear formal dress and carry ID cards inside campus.",
    "is attendance mandatory": " Yes, 75% attendance is mandatory to write exams.",
    "is there a canteen": "Yes, the college canteen is open from 8 AM to 5 PM.",
    
    # Cultural/Events/Sports
    "what are the cultural events": "Vignan Mahotsav includes dance, music, drama, fashion shows, and celebrity concerts.",
    "what is vignan mahotsav": "It's our national youth festival with competitions, performances, and celebrity guests.",
    "are there tech fests": " Yes, departments host tech fests with coding, paper presentations, and workshops.",
    "what sports are available": "We offer cricket, volleyball, basketball, kabaddi, badminton, and athletics.",
    "is there a sports fest": "Yes, inter-college tournaments are held annually in various sports.",
    "what are annual day events": "Annual Day includes performances, awards, and guest lectures.",
    "are celebrities invited": "Yes! Celebrities from Tollywood and music bands attend Vignan Mahotsav.",
    "what are student clubs": " We have clubs for drama, dance, music, coding, photography, and more.",
    "how to join clubs": " Register during induction or talk to club coordinators anytime."
}

# Normalize input
normalized_input = user_input.lower().strip("?!. ")

# Get response
response = responses.get(normalized_input, "❓ I'm sorry, I don't know the answer to that. Please contact the college office.")

# Display bot response (read-only)
st.markdown(f"**Chatbot:** {response}")
