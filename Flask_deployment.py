#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from flask import Flask, request, render_template
from flask_ngrok import run_with_ngrok
doc_idx = 0
user_idx = 0
user_new = np.zeros((1,20))
app = Flask(__name__, template_folder= 'NLP_Recommender')
run_with_ngrok(app)


@app.route('/', methods=['GET', 'POST'])
def homepage():
  return render_template('index.html')

@app.route('/new_page', methods=['GET', 'POST'])
def new_page():
  output_new_user, user_topic_matrix1 = newUserHybridRecommender(new_user_vec, user_topic_matrix, doc_topic_matrix)
  user_new = user_topic_matrix1[-1]
  user_idx = user_topic_matrix1.shape[0]
  return render_template('index2.html',user_id = user_idx, data1 = output_new_user[0][1],data2 = output_new_user[1][1],data3 = output_new_user[2][1],data4 = output_new_user[3][1],data5 = output_new_user[4][1],data6 = output_new_user[5][1],data7 = output_new_user[6][1],data8 = output_new_user[7][1],data9 = output_new_user[8][1],data10 = output_new_user[9][1])


@app.route('/existing_headlines', methods=['GET', 'POST'])
def existing_page():
  return render_template('index_3.html') #, data=request.form['text'], response=doc)

@app.route('/existing_headlines', methods=['GET', 'POST'])
def existing_headlines():
  user_idx =int(request.form.get('text'))
  print(user_topic_matrix[user_idx-1])
  output_new_user1,kk = newUserHybridRecommender(user_topic_matrix[user_idx-1], user_topic_matrix, doc_topic_matrix)
  print(output_new_user1)
  return render_template('index_4.html', user_id = user_idx, data1 = output_new_user1[0][1],data2 = output_new_user1[1][1],data3 = output_new_user1[2][1],data4 = output_new_user1[3][1],data5 = output_new_user1[4][1],data6 = output_new_user1[5][1],data7 = output_new_user1[6][1],data8 = output_new_user1[7][1],data9 = output_new_user1[8][1],data10 = output_new_user1[9][1])



@app.route('/active_headlines', methods=['GET', 'POST'])
def existing_headlines():
  output_new_user2 = oldUserHybridRecommender(user_idx, doc_id, user_topic_matrix, doc_topic_matrix)
  print(user_topic_matrix[user_idx-1])
  print(output_new_user2)
  return render_template('index_5.html', user_id = user_idx, data1 = output_new_user2[0][1],data2 = output_new_user2[1][1],data3 = output_new_user2[2][1],data4 = output_new_user2[3][1],data5 = output_new_user2[4][1],data6 = output_new_user2[5][1],data7 = output_new_user2[6][1],data8 = output_new_user2[7][1],data9 = output_new_user2[8][1],data10 = output_new_user2[9][1])



if __name__ == '__main__':
  app.run()


# In[ ]:


from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
app = Flask(__name__, template_folder= 'NLP_Recommender')
run_with_ngrok(app)
@app.route('/')
def home():
    return render_template('index2.html')

if __name__ == '__main__':
  app.run()

