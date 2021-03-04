# # from flask import Flask
# # from threading import Event
# # import signal

# # from flask_kafka import FlaskKafka
# # app = Flask(__name__)

# # INTERRUPT_EVENT = Event()

# # bus = FlaskKafka(INTERRUPT_EVENT,
# #                  bootstrap_servers=",".join(["172.17.0.1:9091"])
# #                  )


# # def listen_kill_server():
# #     signal.signal(signal.SIGTERM, bus.interrupted_process)
# #     signal.signal(signal.SIGINT, bus.interrupted_process)
# #     signal.signal(signal.SIGQUIT, bus.interrupted_process)
# #     signal.signal(signal.SIGHUP, bus.interrupted_process)


# # @bus.handle('books')
# # def test_topic_handler(msg):
# #     print(msg)


# # if __name__ == '__main__':
# #     bus.run()
# #     listen_kill_server()
# #     app.run(debug=True, port=5004)
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import sqlalchemy
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine

# engine = sqlalchemy.create_engine('mysql://lab:osmentos@mysqldb:3307/sqlalchemy',echo=True)

# class User(db.Model):
#     __tablename__ = 'library'
#     book_name = db.Column(db.String(64), unique=True, index=True)
#     author_name = db.Column(db.String(64), unique=True, index=True)
#     description= db.Column(db.String(300), unique=True, index=True)
#     publish=DateField('Start Date', format='%m/%d/%Y')
#     condition=db.Column(db.String(100), unique=True, index=True)


    
# if __name__ == "__main__":
#     app.run(debug=True)