## 1. Lists ##

row_2=['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3=['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

## 2. Indexing ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
ratings_1=row_1[3]
ratings_2=row_2[3]
ratings_3=row_3[3]
total=ratings_1+ratings_2+ratings_3
average=total/3

## 3. Negative Indexing ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
rating_1=row_1[-1]
rating_2=row_2[-1]
rating_3=row_3[-1]
total_rating=rating_1+rating_2+rating_3
average_rating=total_rating/3

## 4. Retrieving Multiple List Elements ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
fb_rating_data=[row_1[0],row_1[3],row_1[4]]
insta_rating_data=[row_2[0],row_2[3],row_2[4]]
pandora_rating_data=[row_5[0],row_5[3],row_5[4]]
total=(fb_rating_data[2]+insta_rating_data[2]+pandora_rating_data[2])
avg_rating=total//3

## 5. List Slicing ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
first_4_fb=row_1[0:4]
last_3_fb=row_1[-3:]
pandora_3_4=[row_5[-3],row_5[-2]]



## 6. List of Lists ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
app_data_set=[row_1,row_2,row_3,row_4,row_5]
sum=0.0
for i in app_data_set:
    sum=sum+i[4]
avg_rating=sum/5
    

## 7. Opening a File ##

from csv import reader
opened_file=open("AppleStore.csv")
read_file=reader(opened_file)
apps_data=list(read_file)
print(len(apps_data))
print(apps_data[0])
print(apps_data[2:4])


## 8. Repetitive Processes ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]
for i in app_data_set:
   print(i)

## 9. For Loops ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]
rating_sum=0
rating=0
for i in app_data_set:
    rating=rating+1
    rating_sum=rating_sum+i[4]
avg_rating=rating_sum/rating

    

## 10. The Average App Rating ##

from csv import reader
opened_file=open("AppleStore.csv")
read_file=reader(opened_file)
apps_data=list(read_file)
rating_sum=0
rating=0
for i in apps_data[1:]:
    rating=rating+1
    rating_sum=rating_sum+float(i[7])
avg_rating=rating_sum/rating    

## 11. Alternative Way to Compute an Average ##

from csv import reader
opened_file=open("AppleStore.csv")
read_file=reader(opened_file)
apps_data=list(read_file)
all_ratings = []
for i in apps_data[1:]:
    all_ratings.append(float(i[7]))
avg_rating=sum(all_ratings)/len(all_ratings)    