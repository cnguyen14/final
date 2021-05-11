Chien Nguyen
IS-439
Professor Kevin Trainor
REQUIREMENT
1. Virtual Environment: e4_ezu, I am using same virtual environment as EZU project.
2. The application is an small online store for selling phone.
What function does it have?
It has Add to Cart, Register, Log In, Check Out, Check Order from customer. I do not have much 
time to open more extension for it, so It has some limit currently.
How to use it ?
Add to Cart:
When you add any item to cart, the cart will show up how many items that you already take.Check Out: At the checkout Page, It will show up what you take, and calculate the total amount you need to 
pay. You can adjust the quantity, the total will multiply the price and quantity then so up total of 
all item on the top. After you decide to take it click on check out then it will move to next
shipping and take payment page.At the shipping page. There are 2 options, 
First check out if you have account:
You do not need to have Name and Email to complete the form, It will take your name and email 
automatically in your account.
Second, check out if you don’t have account (check out as guess):
You will need to fill in the form Name and Email, It will show up when you are not logging in.
It is using cookie to store what you take. And after you finish payment, cookie will clear and start 
a new order.A small notification will pop up to let you know your order has been taken care of. You don’t
need to do anything after that.There is a order list button on the Nav bar, when you click on it, it will show up all the order that 
customer already took.If you click on the number order, you will be directed to a new page with a full detail of the 
customer order. 
About Admin Panel:
You can add more product by click on the product tab -> add. Fill up the product with Name, 
Price, Digital – Yes if your product is digital, you do not need to ship it if product is digital. For 
Example, You sell a software, keygen, or any kind of digital stuff, then the system will take the payment only and send product directly to customer via email. You can also upload the image of 
the product.
In User:
I created 3 more accounts.
Customer account is using for testing. When customer log in, they can see there order status. 
Unfortunately, I have not done it yet and I do not have enough time to finish it so it is missing 
that function.About Authentication and Permission:
I already created the chain and permission, but like I said about, I have not done the permission 
for my site yet so It is missing that function, but the database is good at the moment.3. How can you use my application?
First, You need to clone it to your machine. You can using git clone to clone my project to your 
computer.
The link of my project is: 
https://github.com/cnguyen14/final.git or https://github.com/cnguyen14/final
It is using the same ezu environment so it should be good with your machine. Python 3.8 is 
required. Additional requirements need to install:
asgiref==3.3.1
certifi==2020.12.5
Django==3.1.7
Pillow==8.2.0
pytz==2021.1
sqlparse==0.4.1
wincertstore==0.2
start project by run manage.py > runserver. No need to migrate any database or collect static.
4. Account you can use to test?
For check out as guess, you do not need to use any account to check out.
For check out if you already have account, you can use anyone of these to test.
- Username: tester/manager/customer/shipper
- Password: (secret)If you do not like any of these, you can click on register to create new account.
To sum up, If I have more times to do, I want to add more features for this project such as, customer can
view order detail only, manager can edit or remove the order for customer, shipper can view shipping 
and order detail, create a category for products, and some more view detail for products, front end for 
manager and shipper to limit them log in to admin panel