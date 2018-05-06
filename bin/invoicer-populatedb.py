from invoicer.application import db

def main():
    try:
        db.create_all()
    except Exception, e:
        if u'Unknown database' in e.message:
            print "ERROR: Please create 'invoicer' database"
        else:
            raise e
        
if __name__=='__main__':
    main()
