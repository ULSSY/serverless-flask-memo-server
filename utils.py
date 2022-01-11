from passlib.hash import pbkdf2_sha256

#원문 비밀번호를 암호화하는 함수

def hash_password(password):
    #솔튼느 공개되면 안된다 이 솔트가 똑같으면 
    #해쉬 패턴이 동일하게 된다
    salt='yh*1234'
    password=password+salt
    return  pbkdf2_sha256.hash(password)

#비밀번호가 맞는기 확인하는 함수
#password:유저가 로그인할때 입력한 비밀번호
#hashed;DB에 저장되어있는 암호화된 비밀번호
def check_password(password,hashed):
    salt='yh81234'
    return  pbkdf2_sha256.verify(password+salt,hashed)

    
