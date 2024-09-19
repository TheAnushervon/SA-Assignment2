# SpoofTalk

Simple anonymous chat application.

### Installation

To be able to run server locally:
1. Clone repo
2. Install redis-server, if you have not any
3. ```pip install requirements.txt```
4. ```cd spooftalk```
5. ```python manage.py runserver```

### Endpoints

```/messages/``` - chat

```/messages/count``` - count of all messages in the chat via GET request

### Acknowledgements & Sources

- [Channels Documentation](https://channels.readthedocs.io/en/latest/index.html)

- [DRF for CRUD App](https://www.youtube.com/watch?v=3tougC9VVMo&list=PL-2EBeDYMIbQ2lx2wgi9cplRAd_EEorIS&index=3)