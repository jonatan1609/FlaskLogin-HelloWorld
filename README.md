You can run the project by `python -m HelloWorld` after you are inside HelloWorldApp directory.

Then try to browse towards http://127.0.0.1:54321/, you will get a message that says you need to log in, and it will take you to the login page.
Then you just need to add a username & a password:

http://127.0.0.1:54321/login?username=a&password=b

you will probably get a message that says that there is no such account therefore you need to browse to

http://127.0.0.1:54321/signup?username=a&password=b

to create an account. Right after you could browse to http://127.0.0.1:54321/ .

Then you can log out by http://127.0.0.1:54321/logout and then you will have to log in again in order to see the content inside http://127.0.0.1:54321/ :D
