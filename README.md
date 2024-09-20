# SpoofTalk - Anonymous Messaging Application

This project is an anonymous messaging platform built using Django, Django Channels, and WebSockets. The app allows users to send messages in real-time with features for handling server downtime and recovering undelivered messages.

## Project Structure

```
├── db.sqlite3
├── manage.py
├── messaging
│   ├── admin.py
│   ├── apps.py
│   ├── consumers.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_message_timestamp.py
│   │   ├── 0003_alter_message_timestamp.py
│   │   ├── 0004_alter_message_timestamp.py
│   │   └── __init__.py
│   ├── models.py
│   ├── routing.py
│   ├── serializers.py
│   ├── templates
│   │   ├── index.html
│   │   └── messaging.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── spooftalk
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Features

- **Anonymous Messaging**: Send and receive messages without revealing user identity.
- **Real-Time Communication**: Uses WebSockets for instant message delivery.
- **Server Downtime Handling**: Frontend waits and resends messages if the server is down.
- **Recoverability**: Messages are not lost during downtime and are sent once the server recovers.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/TheAnushervon/SpoofTalk/
   cd spooftalk
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Install and run redis-server
   ```bash
   sudo apt install redis-server
   sudo service redis-server start
   ```

3. Apply migrations and run the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

4. Access the app at `http://localhost:8000/`.

## Endpoints

```/messages/``` - chat

```/messages/count``` - count of all messages in the chat via GET request

## Acknowledgements & Sources

- [Channels Documentation](https://channels.readthedocs.io/en/latest/index.html)

- [DRF for CRUD App](https://www.youtube.com/watch?v=3tougC9VVMo&list=PL-2EBeDYMIbQ2lx2wgi9cplRAd_EEorIS&index=3)
