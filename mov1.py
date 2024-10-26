import random
user_name=input("enter the user_name:")
password=input("enter the password")
otp=random.randint(1001,9999)
print(otp)
while True:
    otp_rev=input("enter the received otp:")
    if otp_rev==str(otp):
        print("otp verified sucessfully")
        break
    else:
        print("incorect otp,please try agin")
movies=[
     {"movie_name":"Master","avaliable_ticket":"110","total_ticket":"150","cost_per_ticket":"120"},
     {"movie_name":"Vip-2","avaliable_ticket":"90","total_ticket":"130","cost_per_ticket":"100"},
     {"movie_name":"Billa","avaliable_ticket":"80","total_ticket":"100","cost_per_ticket":"90"},
     {"movie_name":"star","avaliable_ticket":"60","total_ticket":"130","cost_per_ticket":"120"}
     ]  
print("..................................................................")
print("                      WELCOME TO THEATER                          ")        
print("..................................................................")
def get_movie_list():
    print("...................Movie_List.................................")
    for elem in movies:
        print(f"movie_name:{elem['movie_name']}")
        print(f"avaliable_ticket:{elem['avaliable_ticket']}")
        print(f"cost_per_ticket:{elem['cost_per_ticket']}\n")
get_movie_list()
tic=input("enter the movie_name:")
book_1='master'
if tic == book_1:
    print("you can select for",book_1,"movie")
    date=input("which date you can see the movie")
    print("11:00am")
    print("3:00pm")
    print("6:00pm")
    print("10:00pm")      
    time=input("enter the show timing")
    bk=int(input("how many ticket you want:"))
    rs=bk*120
    print(" sucessfully booking")
    ticket=int(input("you see ticket press 1:"))
    if ticket==1:
        print(".............ticket.............")
        print("Name:",user_name)
        print("Movie_name:",book_1)
        print("Date",date)
        print("show timing",time)
        seat=random.randint(1000,999999)
        print("seat_number:",seat)
        print("total_cost:",rs)    
elif tic=="vip-2":
    book_2="vip-2"
    print("you can select for",book_2,"movie")
    date=input("which date you can see the movie")
    print("11:00am")
    print("3:00pm")
    print("6:00pm")
    print("10:00pm")      
    time=input("enter the show timing")
    bk=int(input("how many ticket you want:"))
    rs=bk*100
    print(" sucessfully booking")
    ticket=int(input("you see ticket press 1:"))
    if ticket==1:
        print(".............ticket.............")
        print("Name:",user_name)
        print("Movie_name:",book_2)
        print("Date",date)
        print("show timing",time)
        seat=random.randint(1000,999999)
        print("seat_number:",seat)
        print("total_cost:",rs)
elif tic=="Billa":
    book_3="Billa"
    print("you can select for",book_3,"movie")
    date=input("which date you can see the movie")
    print("11:00am")
    print("3:00pm")
    print("6:00pm")
    print("10:00pm")      
    time=input("enter the show timing")
    bk=int(input("how many ticket you want:"))
    rs=bk*90
    print(" sucessfully booking")
    ticket=int(input("you see ticket press 1:"))
    if ticket==1:
        print(".............ticket.............")
        print("Name:",user_name)
        print("Movie_name:",book_3)
        print("Date",date)
        print("show timing",time)
        seat=random.randint(1000,999999)
        print("seat_number:",seat)
        print("total_cost:",rs)
elif tic=="star":
    book_4="star"
    print("you can select for",book_4,"movie")
    date=input("which date you can see the movie")
    print("11:00am")
    print("3:00pm")
    print("6:00pm")
    print("10:00pm")      
    time=input("enter the show timing")
    bk=int(input("how many ticket you want:"))
    rs=bk*120
    print(" sucessfully booking")
    ticket=int(input("you see ticket press 1:"))
    if ticket==1:
        print(".............ticket.............")
        print("Name:",user_name)
        print("Movie_name:",book_4)
        print("Date",date)
        print("show timing",time)
        seat=random.randint(1000,999999)
        print("seat_number:",seat)
        print("total_cost:",rs)
else:
    print("please enter the movie_name try agin")
    
