### importing python libraries #####################
import random
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity



###########  user defined functions ###############
def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]
##################################################




from tkinter import *
top=Tk()


###read csv for title column
df=pd.read_csv("movie_dataset.csv")  # csv file having movie dataset
title_col=df["title"]



###code to make GUI for Selection or Main window
top.title("movie recommender")
top.geometry("821x650")


### movieCallBack() function will finds out movies similar to a movie selected by user
def movieCallBack(film):
    
    ### Select Features
    features=['keywords','cast','genres','director']

    for feature in features:
        df[feature]=df[feature].fillna('')


    ### we have to create a new column in DataFrame which would combine all the above selected features
    def combine_features(row):
        try:
            return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
        except:
            print("Error",row)

    df["combined_features"]=df.apply(combine_features,axis=1)


    ### Creating count matrix from this new combined column
    cv=CountVectorizer()
    count_matrix=cv.fit_transform(df["combined_features"])
    


    ### Compute the Cosine Similarity based on the count_matrix
    cosine_sim=cosine_similarity(count_matrix)
    movie_user_likes = film       # name of selected movie is given here 
    

    ### Get index of this movie from its title
    movie_index=get_index_from_title(movie_user_likes)
    similar_movies=list(enumerate(cosine_sim[movie_index]))
    


    ### Get a list of similar movies in descending order of similarity score
    sorted_similar_movies=sorted(similar_movies,key=lambda x:x[1],reverse=True)
    


    ### Storing most similar first five movies in a list
    i=0
    film_list2=[]
    for movie in sorted_similar_movies:
        film_list2.append(get_title_from_index(movie[0]))
        i=i+1
        if i>5:
            break
    
    
    ### code to make GUI for recommendation window
    tp=Tk()
    tp.title("recommendations")
    tp.geometry("815x380")


    
    l1=Label(tp, text = "You previously selected",pady=10) 
    l1.grid(row = 1, column = 0, sticky = W)
    
    
    
    box4=Button(tp,text=film,width=15,height=1,border=7,bg='lime',relief='flat')
    box4.grid(row = 2, column = 0, sticky = W, padx = 4)

    box5=Button(tp,text=" Recommended Movies",width=20,height=1,border=7,bg='mediumturquoise',relief='flat')
    box5.grid(row = 3, column = 2, sticky = W, padx = 4)

    b1=Button(tp,text=film_list2[1],width=20,height=15,border=3,bg='turquoise',relief='flat',command=lambda:movieCallBack(film_list2[1]))  
    b2=Button(tp,text=film_list2[2],width=20,height=15,border=5,bg='mediumturquoise',relief='flat',command=lambda:movieCallBack(film_list2[2]))
    b3=Button(tp,text=film_list2[3],width=20,height=15,border=7,bg='lightseagreen',relief='flat',command=lambda:movieCallBack(film_list2[3]))
    b4=Button(tp,text=film_list2[4],width=20,height=15,border=5,bg='mediumturquoise',relief='flat',command=lambda:movieCallBack(film_list2[4]))
    b5=Button(tp,text=film_list2[5],width=20,height=15,border=3,bg='turquoise',relief='flat',command=lambda:movieCallBack(film_list2[5]))


    b1.grid(row = 4, column = 0, sticky = W, padx = 4,pady=10) 
    b2.grid(row = 4, column = 1, sticky = W, padx = 4) 
    b3.grid(row = 4, column = 2, sticky = W, padx = 4) 
    b4.grid(row = 4, column = 3, sticky = W, padx = 4) 
    b5.grid(row = 4, column = 4, sticky = W, padx = 4)

    tp.mainloop()
    




l1=Label(top, text = " ",pady=10) 
l1.grid(row = 0, column = 0, sticky = W) 


box1=Button(top,text=" Click on any ",width=20,height=2,bg='lime',relief='flat')
box1.grid(row = 1, column = 1, sticky = W, padx = 4)
box2=Button(top,text=" Movie Button to ",width=20,height=2,border=5,bg='turquoise',relief='flat')
box2.grid(row = 1, column = 2, sticky = W, padx = 4)
box3=Button(top,text=" get similar movies ",width=20,height=2,bg='lime',relief='flat')
box3.grid(row = 1, column = 3, sticky = W, padx = 8)

l2=Label(top, text = " ",pady=10) 
l2.grid(row = 2, column = 0, sticky = W)


# by using random.choice() function a random movie would be displayed on Movie Selection window
# everytime the program is run
film_list1=[]
for i in range(10):
    film_list1.append(random.choice(title_col))


# creating buttons for the selection of a particular movie by user
b1=Button(top,text=film_list1[0],command=lambda:movieCallBack(film_list1[0]),width=20,height=15,border=5,bg='lime',relief='flat')
b2=Button(top,text=film_list1[1],command=lambda:movieCallBack(film_list1[1]),width=20,height=15,border=3,bg='turquoise',relief='flat')
b3=Button(top,text=film_list1[2],command=lambda:movieCallBack(film_list1[2]),width=20,height=15,border=5,bg='lime',relief='flat')
b4=Button(top,text=film_list1[3],command=lambda:movieCallBack(film_list1[3]),width=20,height=15,border=3,bg='turquoise',relief='flat')
b5=Button(top,text=film_list1[4],command=lambda:movieCallBack(film_list1[4]),width=20,height=15,border=5,bg='lime',relief='flat')

b1.grid(row = 3, column = 0, sticky = W, padx = 4) 
b2.grid(row = 3, column = 1, sticky = W, padx = 4) 
b3.grid(row = 3, column = 2, sticky = W, padx = 4) 
b4.grid(row = 3, column = 3, sticky = W, padx = 4) 
b5.grid(row = 3, column = 4, sticky = W, padx = 4) 

b6=Button(top,text=film_list1[6],command=lambda:movieCallBack(film_list1[6]),width=20,height=15,border=3,bg='turquoise',relief='flat')
b7=Button(top,text=film_list1[5],command=lambda:movieCallBack(film_list1[5]),width=20,height=15,border=5,bg='lime',relief='flat')  
b8=Button(top,text=film_list1[8],command=lambda:movieCallBack(film_list1[8]),width=20,height=15,border=3,bg='turquoise',relief='flat')
b9=Button(top,text=film_list1[7],command=lambda:movieCallBack(film_list1[7]),width=20,height=15,border=5,bg='lime',relief='flat')
b10=Button(top,text=film_list1[9],command=lambda:movieCallBack(film_list1[9]),width=20,height=15,border=5,bg='turquoise',relief='flat')

b6.grid(row = 4, column = 0, sticky = W, padx = 4,pady=4) 
b7.grid(row = 4, column = 1, sticky = W, padx = 4,pady=4) 
b8.grid(row = 4, column = 2, sticky = W, padx = 4,pady=4) 
b9.grid(row = 4, column = 3, sticky = W, padx = 4,pady=4) 
b10.grid(row = 4, column = 4, sticky = W, padx = 4,pady=4) 


top.mainloop()

### end of program
