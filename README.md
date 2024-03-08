# Notes_django_api

This git repository is hosted on Render.com ( https://notes-api-1ew6.onrender.com/ )

Steps to Run this Django App

1. Download this git repository.
2. Unzip the repository and copy it where you want to keep this project.
3. Go insite the parent folder "Notes_django_api" using command prompt/any terminal.
4. Here we have to create a environment for this django app.
5. Run the command "python -m venv django_env" or "virtualenv django_env" -- Here django_env is the name of environment.
6. Now run "django_env/Scripts/activate" -- This command will activate your django environment.
7. Go to "Notes_django_api > notes_api>" 
8. Run "pip install -r requirements.txt" -- This will install all the required packages mentioned
     in the requirements.txt file.
9. Now run "python manage.py runserver"


------------------------API Endpoints:---------------------------

/* If we run this server on our windows machine we can also use:
     "http://127.0.0.1:8000/"
     instead of
     "https://notes-api-1ew6.onrender.com".

*/
1. For user Registration
     url - https://notes-api-1ew6.onrender.com/api/signup/
     request type - POST

     body - {
     "username" : "test4",
     "email" : "test4@gmail.com",
     "password" : 12345
     }

     response: {
     "msg": "Account Created successfully",
     "username": "test4",
     "email": "test4@gmail.com"
     }


2. User Login 
     url - https://notes-api-1ew6.onrender.com/api/login/
     request type - POST
     body - {
          "username_or_email":"test4",
          "password": 12345
          }
     
     response - {
     "user": "test4",
     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5ODE5NTc3LCJpYXQiOjE3MDk4MTM1NzcsImp0aSI6IjQ5Y2Y0MmQwZWI5NzQ0MzA4OWEwN2ZlZTJlMzk5ZjlmIiwidXNlcl9pZCI6NX0.bTczjElz8YjmL5RI1FR5cR7HlljieZ4R0Xsk3WmRXW4",
     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwOTg5OTk3NywiaWF0IjoxNzA5ODEzNTc3LCJqdGkiOiI4NzBmODFmZTc3NTk0MWQ5OTYzMTEwNDdlMjJhZGU2YSIsInVzZXJfaWQiOjV9.6DqsO-JFZ80G0egB10f7sMF9KCZFtvSCQo96_AO_QJ0"
     }

3. Create a Note:
     url - https://notes-api-1ew6.onrender.com/api/notes/create/
     request type - POST

     header - {
         "Content-Type": "application/json"
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5ODExNjI3LCJpYXQiOjE3MDk4MDU2MjcsImp0aSI6IjViNTBmMzI2YTg4MTRlNmY5N2YzYmVlYzY2Zjg4MGUwIiwidXNlcl9pZCI6M30.RoAhASmqKzs9WbBAS8r-pbq7bIiVBn2eo4_n4vpWZj0"
     }

     body - {
     "note" : "this is my second note for test3"
     }

     response - {
          "success": "notes created successfully"
          }

4. Get Note By ID
     url - https://notes-api-1ew6.onrender.com/api/notes/4
     request type - GET

     header - {
         "Content-Type": "application/json"
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5ODExNjI3LCJpYXQiOjE3MDk4MDU2MjcsImp0aSI6IjViNTBmMzI2YTg4MTRlNmY5N2YzYmVlYzY2Zjg4MGUwIiwidXNlcl9pZCI6M30.RoAhASmqKzs9WbBAS8r-pbq7bIiVBn2eo4_n4vpWZj0"
     }


     response - 
               [
                    {
                    "id": 4,
                    "userId_id": 3,
                    "note": "this is my second note for test3",
                    "shared": false,
                    "versions": "[{'note': 'this is my second note for test3', 'updated_at': '2024-03-07 10:01:52'}]",
                    "created_at": "2024-03-07T10:01:52.955160Z"
                    }
               ]

5. Update any Note
     url - https://notes-api-1ew6.onrender.com/api/notes/4
     request type - POST

     header - {
         "Content-Type": "application/json"
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5ODExNjI3LCJpYXQiOjE3MDk4MDU2MjcsImp0aSI6IjViNTBmMzI2YTg4MTRlNmY5N2YzYmVlYzY2Zjg4MGUwIiwidXNlcl9pZCI6M30.RoAhASmqKzs9WbBAS8r-pbq7bIiVBn2eo4_n4vpWZj0"
     }

     body - {
          "note" : "This is updated note for ID 4"
          }

     response - {
          "success": "updated successfully"
          }

6. Share Note with other Users
     url - https://notes-api-1ew6.onrender.com/api/notes/share/
     request type - POST

     header - {
         "Content-Type": "application/json"
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5ODExNjI3LCJpYXQiOjE3MDk4MDU2MjcsImp0aSI6IjViNTBmMzI2YTg4MTRlNmY5N2YzYmVlYzY2Zjg4MGUwIiwidXNlcl9pZCI6M30.RoAhASmqKzs9WbBAS8r-pbq7bIiVBn2eo4_n4vpWZj0"
     }

     body - {
          "noteId" : 4,
          "usernames":"['test2']" //list of users whom you want 
                                        to  share the note information
          }
     response - {
          "msg": "Note infromation shared successfully",
          "note id": 4,
          "usernames": "['test2']"
          } 

7. Version History for a particular note.
     url - https://notes-api-1ew6.onrender.com/api/notes/version-history/4
     request type - GET

     header - {
         "Content-Type": "application/json"
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5ODExNjI3LCJpYXQiOjE3MDk4MDU2MjcsImp0aSI6IjViNTBmMzI2YTg4MTRlNmY5N2YzYmVlYzY2Zjg4MGUwIiwidXNlcl9pZCI6M30.RoAhASmqKzs9WbBAS8r-pbq7bIiVBn2eo4_n4vpWZj0"
     }
     
     response - [
                    {
                    "versions": "[{'note': 'This is updated note for ID 4', 'updated_at': '2024-03-08 00:12:56'}, {'note': 'this is my second note for test3', 'updated_at': '2024-03-07 10:01:52'}]"
                    }
               ]