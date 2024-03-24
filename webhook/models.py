from flask_sqlalchemy import SQLAlchemy
from datetime import time

db = SQLAlchemy()

"""
class Board(db.Model) :
    __table_name__ = 'tb_board'
    # 여기서 db 모델 적용
    board_id = db.Column(db.Integer, primary_key=True)
    board_title = db.Column(db.String(300, 'utf8mb4_general_ci'), nullable=True)
    board_content = db.Column(db.String(300, 'utf8mb4_general_ci'), nullable=True)
    # board_time =


    def __init__(self, board_id, board_title, board_content):
        self.board_id = board_id
        self.board_title = board_title
        self.board_content = board_content
"""
"""
class Data(db.Model) :
    __table_name__ = 'tb_data'
    
    data_id = db.Column(db.String(100, 'utf8mb4_general_ci'), nullable=True, primary_key = True)
    data_content = db.Column(db.String(300, 'utf8mb4_general_ci'), nullable=True)
    data_heart = db.Column(db.Integer(20), nullable=True)
    data_retweet = db.Column(db.Integer(20), nullable=True)
    # data_date = 
    
    def __init__(self, data_id, data_content, data_heart, data_retweet):
        self.data_id = data_id
        self.board_title = board_title
        self.board_content = board_content
"""
# 취미 테이블
class Hobby(db.Model) :
    __tablename__ = 'tb_hobby'

    hobby_name = db.Column(db.String(100, 'utf8mb4_general_ci'), primary_key=True)
    hobby_count = db.Column(db.Integer, nullable=True)
    hobby_classification = db.Column(db.String(100, 'utf8mb4_general_ci'), nullable=True)

    def __init__(self, hobby_name, hobby_count, hobby_classification):
        self.hobby_name = hobby_name
        self.hobby_count = hobby_count
        self.hobby_classification = hobby_classification

# 룸 테이블
class Room(db.Model) :
    __tablename__ = 'tb_room'

    room_id = db.Column(db.Integer, primary_key=True)
    room_title = db.Column(db.String(300, 'utf8mb4_general_ci'), nullable=True)
    room_keyword = db.Column(db.String(300, 'utf8mb4_general_ci'), nullable=True)

    def __init__(self, room_id, room_title, room_keyword):
        self.room_id = room_id
        self.room_title = room_title
        self.room_keyword = room_keyword

"""
class User(db.Model) :
    __tablename__ = 'tb_user'

    user_id = db.Column(db.String(100, 'utf8mb4_general_ci'), primary_key=True)
    user_password = db.Column(db.String(200, 'utf8mb4_general_ci'), nullable=True)
    user_name = db.Column(db.String(200, 'utf8mb4_general_ci'), nullable=True)
    user_denHobby = db.Column(db.String(300, 'utf8mb4_general_ci'), nullable=True)
    user_prefHobby = db.Column(db.String(300, 'utf8mb4_general_ci'), nullable=True)
    user_record = db.Column(db.String(300, 'utf8mb4_general_ci'), nullable=True)

    def __init__(self, user_id, user_password, user_name, user_denHobby, user_prefHobby, user_record):
        self.user_id = user_id
        self.user_password = user_password
        self.user_name = user_name
        self.user_denHobby = user_denHobby
        self.user_prefHobby = user_prefHobby
        self.user_record = user_record
"""