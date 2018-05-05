from invoicer.application import User
from invoicer.application import db

def main():
    try:
        dave = User(username='dave', email='dave@example.com')
        db.session.add(dave)
        db.session.commit()
    except Exception, e:
        if u'Unknown database' in e.message:
            print "ERROR: Please create 'invoicer' database"
        else:
            raise e
        
if __name__=='__main__':
    main()