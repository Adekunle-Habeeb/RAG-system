data = [
    {'Question': 'Who is Habeeb Adekunle?',
     'Answer': 'Habeeb Adekunle is an AI engineer with 2 years of experience and expertise in backend development, data science, and machine learning. He is proficient in Python for data science and machine learning, as well as in JavaScript and TypeScript for backend development. Habeeb enjoys writing code and exploring various fields in the tech space. When not writing code, Habeeb engages in outdoor activities like swimming and playing football.'},
    {'Question': 'What is Habeeb educational background?',
     'Answer': 'Habeeb Adekunle is currently pursuing his degree in Marine Science at the University of Lagos, Nigeria. He aims to leverage his knowledge of data science and machine learning to advance the field of marine science. Habeeb has already developed a temperature prediction app that forecasts the temperature of a city based on various factors. In the future, he aims to provide viable solutions to the problems of climate change with the help of AI.'},
    {'Question': 'What is Habeeb work experience?',
     'Answer': 'Habeeb Adekunle has diverse experience in backend development and machine learning. As a Freelance Backend Software Engineer, he led the development of a Project Management Software that integrated Kanban methodology, Gantt charts, and automated invoicing/budgeting, boosting software functionality by 30%. At NITDA IT Hub, he optimized a chat application for ISL Unilag, increasing user engagement by 15%. and reducing latency by 10%. He is also part of the NITDA IT Hub AI research team, where he collaborates on developing a food price prediction model for prices in Nigeria. During his internship at Intrapair, Habeeb was involved in the Flip Educational Assessment Platform, benefiting over 500 secondary school students. Currently, he holds the position of Backend Engineer and Machine Learning Engineer at Peerhub Ltd, a company based in Canada.'},
    {'Question': 'What technologies are Habeeb proficient in?',
     'Answer': 'Habeeb is proficient in several technologies, including HTML/CSS/JS for web development, Node.js/Express.js and NestJS for backend development, MongoDB, MySQL, and PostgreSQL for databases, Git/GitHub for version control, AWS and GCP for deployment. In the field of AI, he is skilled in Python and uses SQL, Pandas, Matplotlib, NumPy, and Seaborn for data analysis. For model building, he utilizes TensorFlow and Keras. Langchain, Huggingface, Streamlit, google palm and gpt models'},
    {'Question': 'What are Habeeb Projects in machine learning?',
     'Answer': 'Habeeb has worked on several projects in machine learning. In addition to building a temperature prediction app, he developed a model that classifies images of tech giants (Elon Musk, Jeff Bezos, Mark Zuckerberg, Jack Ma, and Larry Page). He also created a potato disease classification app. Additionally, he built a RAG system capable of engaging in conversation with users.'},
    {'Question': 'What languages can Habeeb Adekunle speak?', 'Answer': 'Habeeb Adekunle speaks English and Arabic.'},
    {'Question': 'What certifications does Habeeb Adekunle hold?',
     'Answer': 'Habeeb holds certifications in AWS with JavaScript and Node.js from Udemy, and in Data Science and Machine Learning from Udemy.'},
    {'Question': 'What soft skills does Habeeb Adekunle possess?',
     'Answer': 'Communication, Attention details and time management'},
    {'Question': 'What are the main features of the temperature prediction model built by Habeeb?',
     'Answer': 'The temperature prediction model predicts temperature for global cities according to month and year, using embeddings for city names stored in a columns.json file. Habeeb optimized it using GridSearchCV to find the best model, achieving a score of 97% accuracy with a decision tree model. The model utilizes historical temperature data from global cities spanning from 1850 to 2013, enabling accurate predictions based on specific months and years.'},

]

import csv

filename = "about_habeeb.csv"

fields = ["Question", "Answer"]

with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerows(data)
