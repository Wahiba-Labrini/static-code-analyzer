from sqlalchemy import create_engine,ForeignKey, Column,Integer,String,DateTime
from sqlalchemy.orm import declarative_base,sessionmaker,relationship
from sqlalchemy.sql import func


db_url='sqlite:///database.db'
engine=create_engine(db_url)
Session=sessionmaker(bind=engine)
session=Session()
base=declarative_base()
 
class Report(base):
    __tablename__="reports"
    id=Column(Integer,primary_key=True)
    filename=Column(String(50))
    total_issue=Column(Integer)
    created_at=Column(DateTime(timezone=True),server_default=func.now())

    issue=relationship("Issue",back_populates="report")

class Issue(base):
    __tablename__="issues"
    id=Column(Integer,primary_key=True)
    rule_id=Column(String(50))
    line=Column(Integer)
    severity=Column(String(20))
    message=Column(String(200))
    
    report_id=Column(Integer,ForeignKey("reports.id"))
    report=relationship("Report",back_populates="issue")


base.metadata.create_all(engine)
"""
if __name__ == "__main__":
    report1=Report(filename="appAnalyzer.py",total_issue=6)
    issue1=Issue(rule_id="eval-exec",line=2,severity="high",message="contains a dangerous use",report_id=1)
   
    report1.issue.append(issue1)

    session.add_all((report1,issue1))
    session.commit()
    print("data saved successfully")"""